class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        five=0
        ten=0
        for i in bills:
            if i==5:
                five+=1
                continue
            elif i==10:
                ten+=1
                five-=1
            elif i==20:
                if ten>0 and five>0:
                    ten-=1
                    five-=1
                elif five>=3:
                    five-=3
                else:
                    return False
            if five<0 or ten<0:
                return False

        return True
