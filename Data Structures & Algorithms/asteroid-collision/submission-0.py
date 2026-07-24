class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack=[]
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

        
