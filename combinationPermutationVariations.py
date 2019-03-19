input1 = [1,2,3,4,8]
target1 = 8
def simpleCombination(candidates, leng):
    candidates.sort()
    print('Combination(order matters), No repick candidate, dedupelicated result, length:' + str(leng))
    def dfs(candidates, chosen, res, leng):
        if leng == len(chosen): 
	    #### easy but slow dedupe
            if chosen[:] not in res:
                res.append(chosen[:]) 
                return
        else:
            #### order doesn't matters, so iterate from 0
            for i in range(0, len(candidates)):
                curr = candidates[i]
	        chosen.append(curr)
                #### no repick candidate
		#### can either control by triming candidates or using index
                dfs(candidates[:i] + candidates[i + 1:], chosen, res, leng)
                chosen.pop()
    res = []
    dfs(candidates, [], res, leng)
    res.sort()
    print res
def simplePermutation(candidates, leng):
    candidates.sort()
    print('Permutation(order doesnt matter), No repick candidate, deduplicated result, length:' + str(leng))
    def dfs(candidates, toBePickedPt, chosen, res, leng):
        if leng == len(chosen): 
            if chosen[:] not in res:
	        res.append(chosen[:]) 
                return
        else:
            #### order matters, so iterate from the controlled pointer
            for i in range(toBePickedPt, len(candidates)):
                chosen.append(candidates[i])
                #### i + 1 ==>> no repick candidate 
		#### can either control by triming candidates or using index
                #### one trap here is to make sure recusrive calls from i + 1 but not toBePickedPt
                dfs(candidates, i + 1, chosen, res, leng)
                chosen.pop()
    res = []
    dfs(candidates, 0, [], res, leng)
    res.sort()
    print res
def hitATargetNoRepick(candidates, leng, target):
    candidates.sort()
    print('HIT a target, no repick candidate, deduplicated result, length:' + str(leng))
    def dfs(candidates, toBePickedPt, chosen, res, leng):
        if len(chosen) == leng and sum(chosen) == target and sorted(chosen[:]) not in res:
            res.append(chosen[:])
            return
        else:
            for i in range(toBePickedPt, len(candidates)):
                chosen.append(candidates[i])
                dfs(candidates, i + 1, chosen, res, leng)
                chosen.pop()
    res = []
    dfs(candidates, 0, [], res, leng)
    res.sort()
    print res

def hitATargetRepick(candidates, leng, target):
    candidates.sort()
    print('HIT a target, repick candidate, deduplicated result, length:' + str(leng))
    def dfs(candidates, toBePickedPt, chosen, res, leng):
        if len(chosen) == leng and sum(chosen) == target and sorted(chosen[:]) not in res:
            res.append(chosen[:])
            return
        else:
            for i in range(0, len(candidates)):
                chosen.append(candidates[i])
                if sum(chosen) > target:
                    chosen.pop()
                    continue
                dfs(candidates, i, chosen, res, leng)
                chosen.pop()
    res = []
    dfs(candidates, 0, [], res, leng)
    res.sort()
    print res
print("input:" + str(input1))
print("target:" + str(target1))
for i in range(2,5):
    print
    simpleCombination(input1, i)
    simplePermutation(input1, i)
    print
    hitATargetNoRepick(input1, i, target1)
    hitATargetRepick(input1, i, target1)
