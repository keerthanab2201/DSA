class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # first sort by position
        cars= sorted(zip(position,speed))
        p1, s1 = cars[-1]
        stack = [(target - p1) / s1]
        # process from car closest to target backwards 
        # front car cant be affected by any but the cars behind can catch upto it
        for i in range(len(cars) - 2, -1, -1):
            p,s= cars[i]
            arrivaltime= (target-p)/s
            if stack and arrivaltime>stack[-1]:
                stack.append(arrivaltime)
        return len(stack)
        

        # compute arrival time of each = (distance/speed) = (target-position)/speed

        