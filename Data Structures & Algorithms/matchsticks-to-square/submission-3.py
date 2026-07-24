class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        # This is a bucket assignment backtracking problem
        # Each stick has 4 choices, not 2.
        if sum(matchsticks)%4!=0:
            return False
        # optimise solution by sorting in descending order- if largest stick>length it will immediately return false
        matchsticks.sort(reverse=True)
        length= sum(matchsticks)//4
        sides= [0]*4
        
        def backtracking(i):
            if i==len(matchsticks):
                return True
            for side in range(4): #checks which side the current matchstick should be assigned to
                if sides[side]+matchsticks[i]<=length:
                    sides[side]+=matchsticks[i]
                    if backtracking(i+1):
                        return True
                    sides[side]-=matchsticks[i]
                # another optimisation
                if sides[side] == 0: #skips duplicate empty states- Trying another empty side produces exactly the same search tree.
                    break
            return False

        return backtracking(0)