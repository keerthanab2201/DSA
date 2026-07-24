class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack=[] #stores indices
        res= [0]*len(temperatures)
        for i in range(len(temperatures)-1, -1, -1):
            while stack and temperatures[stack[-1]]<=temperatures[i]:
            # stack shouldnt be empty and TOS is lesser than current-> pop-> new recorded highest temp
                stack.pop()
            if stack: # if current is lesser than TOS -> calculate no of days between them
                res[i]= stack[-1]-i
            stack.append(i) #IMP- append each temp after calculation
        return res

            



