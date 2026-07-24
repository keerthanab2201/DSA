class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack=[]
        # use a flag (alive) to indicate whether current asteroid survived or not
        # append when signs are same (and) tos is negative while incoming is positive (they move away from e/o)
        # collision occurs only when incoming is negative and tos is positive 
        for i in asteroids:
            alive=True
            while alive and stack and stack[-1]>0 and i<0:
                if stack[-1]<-i:
                    stack.pop()
                elif stack[-1]==-i:
                    stack.pop()
                    alive=False
                else:
                    alive=False
            if alive:
                stack.append(i)
        return stack
