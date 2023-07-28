import re
import sys

prefix = "x"
suffix = 1
loopList = []


def isConst(x):
    if type(x) is not list:
        if x[0].isupper():
            return True
        return False
    return True


def FETCHMATCH(Rules, Facts, goal, flag):
    if flag == 0 and goal['Pred'] in Facts:
        return (0, Facts[goal['Pred']])
    elif flag <= 1 and goal['Pred'] in Rules:
        return (1, Rules[goal['Pred']])
    else:
        return (2, [])


def Standardize(rule):
    global prefix, suffix
    newRule = {}
    equiv = {}
    argUnion = list(set(rule['Conclusion']['Args']))
    for every in rule['Premises']:
        argUnion = list(set(argUnion) | set(every['Args']))
    for every in argUnion:
        if not isConst(every):
            string = str(prefix+str(suffix))
            equiv[every] = string
            suffix += 1
    newRule['Conclusion'] = {}
    arglc = []
    for a in rule['Conclusion']['Args']:
        if not isConst(a):
            arglc.append(equiv[a])
        else:
            arglc.append(a)
    newRule['Conclusion']['Pred'] = rule['Conclusion']['Pred']
    newRule['Conclusion']['Args'] = arglc
    newRule['Premises'] = []
    ctr = 0
    for a in rule['Premises']:
        arglp = []
        for b in a['Args']:
            if not isConst(b):
                arglp.append(equiv[b])
            else:
                arglp.append(b)
        newRule['Premises'].append({'Pred': a['Pred'], 'Args': arglp})
        ctr += 1
    return newRule


def checkConsts(a, b):
    for each in b:
        if isConst(each) and isConst(a[b.index(each)]):
            if not each == a[b.index(each)]:
                return False
    return True


def UNIFY_VAR(var, x, s):
    if var in s.keys():
        # print("Unifying ",s[var]," with ",x)
        return UNIFY(s[var], x, s)
    elif x in s.keys():
        # print("Unifying ",var," with ",s[x])
        return UNIFY(var, s[x], s)
    else:
        # print("Adding substitution for ",var)
        s[var] = x
        # print("New substitution:",s)
        return s


def UNIFY(rhs, goal, s):
    global loopList
    if type(rhs) is list and len(rhs) == 1:
        rhs = rhs[0]
    if type(goal) is list and len(goal) == 1:
        goal = goal[0]
    # print("In unify of ",rhs," and ",goal,". And subst. is: ",s)
    if s == False:
        # print("Supposed failure")
        return False
    elif rhs == goal:
        # print("Direct unif.")
        return s
    elif not isConst(rhs):
        # print("RHS is not const")
        return UNIFY_VAR(rhs, goal, s)
    elif not isConst(goal):
        # print("Goal is not const")
        return UNIFY_VAR(goal, rhs, s)
    elif type(rhs) == list and type(goal) == list:
        # print("Both lists")
        x = checkConsts(rhs, goal)
        if x == False:
            return x
        else:
            return UNIFY(rhs[1:], goal[1:], UNIFY(rhs[0], goal[0], s))
    else:
        return False


def Substitute(s, f):
    global loopList
    fin = []
    args = f['Args']
    for ea in args:
        if ea in s.keys():
            fin.append(s[ea])
        else:
            fin.append(ea)
    res = {'Pred': f['Pred'], 'Args': fin}
    # print("Substituted: ",res)
    return res


def BW_AND(Rules, Facts, goals, subList):
    global loopList
    # print("In BW_AND for:",goals)
    if subList == False:
        # print("Supposed failure")
        return
    elif len(goals) == 0:
        # print("Fact")
        yield subList
    else:
        first, rest = goals[0], goals[1:]
        # print("First of Premises: ",first)
        for eachS in BW_OR(Rules, Facts, Substitute(subList, first), subList):
            # print("EachS:",eachS)
            for eachSD in BW_AND(Rules, Facts, rest, eachS):
                # print("Subst. for each AND:",eachSD)
                # print("Before pop in AND:",loopList)
                loopList.pop()
                yield eachSD
            # print("EachS:",eachS)
        # print("Before pop in AND:",loopList)
        loopList.pop()


def BW_OR(Rules, Facts, goal, subList):
    global loopList
    # print("In BW_OR of:", goal)
    if goal in loopList:
        # print("Found loop", goal,loopList)
        subList = False
        yield False
    # loopList.append(goal)
    # print("LL after:",loopList)
    ind, match = FETCHMATCH(Rules, Facts, goal, 0)
    print("I", ind)
    ind2 = 0
    if ind == 0:
        ind2, match2 = FETCHMATCH(Rules, Facts, goal, 1)
    # print("The matching rules:",match)
    if ind != 2:
        for eachRule in match:
            loopList.append(goal)
            # print("LL after:",loopList)
            # print("each:",eachRule)
            if not subList is False:
                currSubList = subList.copy()
            else:
                currSubList = False
            if ind == 1:
                eachRule = Standardize(eachRule)
                # print("Standardized rule:",eachRule)
                s2 = UNIFY(eachRule['Conclusion']['Args'],
                           goal['Args'], subList)
                for eachS in BW_AND(Rules, Facts, eachRule['Premises'], s2):
                    # print("Subst. for each OR:",eachS)
                    yield eachS
            else:
                s2 = UNIFY(eachRule['Args'], goal['Args'], subList)
                for eachS in BW_AND(Rules, Facts, [], s2):
                    # print("Subst. for each OR:",eachS)
                    yield eachS
            # print("Curr rule",eachRule)
            if not currSubList is False:
                subList = currSubList.copy()
            else:
                subList = False

        if ind2 == 0:
            yield False
        elif ind2 == 1:
            for eachRule in match2:
                loopList.append(goal)
                # print("LL after:",loopList)
                # print(eachRule)
                if not subList is False:
                    currSubList = subList.copy()
                else:
                    currSubList = False
                eachRule = Standardize(eachRule)
                # print("Standardized rule:",eachRule)
                s2 = UNIFY(eachRule['Conclusion']['Args'],
                           goal['Args'], subList)
                for eachS in BW_AND(Rules, Facts, eachRule['Premises'], s2):
                    # print("Subst. for each OR:",eachS)
                    yield eachS
                # print("currSub",currSubList)
                if not currSubList is False:
                    subList = currSubList.copy()
                else:
                    subList = False
            yield False
        else:
            yield False
    else:
        # print("No match found!")
        return False


def BWChain(Rules, Facts, query):
    global loopList, suffix
    # print("In BWChain")
    for x in BW_OR(Rules, Facts, query, {}):
        print("ANS: ", x)
        if x is not False:
            # print("True")
            writeOutput.write("TRUE\n")
            if query['Pred'] not in Facts:
                Facts[query['Pred']] = []
            Facts[query['Pred']].append(
                {'Pred': query['Pred'], 'Args': query['Args']})
            # print(Facts[query['Pred']])
            return
        else:
            # print("False")
            writeOutput.write("FALSE\n")
            return


Rules = {}
Facts = {}
Queries = []
# readInput=open(str(sys.argv[2]),'r').readlines()
readInput = open("input_5.txt", 'r').readlines()
writeOutput = open("output.txt", 'w')
i = 0
for e in readInput:
    readInput[i] = e.strip()
    i += 1
numOfQueries = int(readInput[0])
queries = []
rules = []
for e in range(1, numOfQueries+1):
    queries.append(readInput[e])
numOfRules = int(readInput[numOfQueries+1])
for e in range(numOfQueries+2, numOfQueries+numOfRules+2):
    rules.append(readInput[e])
for each in rules:
    ruleInd = each.split(' ')
    flag = 0
    if "=>" in ruleInd:  # can check if ruleind is of size 1 also
        flag = 0
    else:
        flag = 1
    elem = ruleInd.pop()
    splitElem = re.findall(r"[\w']+", elem)
    add = ""
    if elem[0] == '~':
        add = "~"
    Cpred = add+splitElem[0]
    Cargs = splitElem[1:]
    if flag == 1:
        if Cpred not in Facts:
            Facts[Cpred] = []
        Facts[Cpred].append({'Pred': Cpred, 'Args': Cargs})
        continue
    if Cpred not in Rules:
        Rules[Cpred] = []
    Rules[Cpred].append(
        {'Conclusion': {'Pred': Cpred, 'Args': Cargs}, 'Premises': []})
    currRInd = len(Rules[Cpred])-1
    for eachR in ruleInd:
        if eachR == "^" or eachR == "=>":
            continue
        splitEach = re.findall(r"[\w']+", eachR)
        pred = splitEach[0]
        args = splitEach[1:]
        Rules[Cpred][currRInd]['Premises'].append({'Pred': pred, 'Args': args})
for each in queries:
    splitElem = re.findall(r"[\w']+", each)
    add = ""
    if each[0] == '~':
        add = "~"
    Cpred = add+splitElem[0]
    Cargs = splitElem[1:]
    Queries.append({'Pred': Cpred, 'Args': Cargs})
for query in Queries:
    print("Q:", query)
    loopList = []
    suffix = 1
    BWChain(Rules, Facts, query)
writeOutput.close()
