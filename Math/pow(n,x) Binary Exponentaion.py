class Power:
    def bianryExponentaion(self,base : float,exponent: int):
        ans = 1
        # Handling -ve exponent
        base = float(base)
        if exponent < 0:
            base = 1/base
            exponent = -exponent
        while exponent > 0:
            if exponent & 1:
                ans = ans * base
            base = base * base
            exponent = exponent // 2
        return ans
p = Power()
x, n = 2, 4
print(p.bianryExponentaion(x,n))
p1 = Power().bianryExponentaion(2,-3)
print(p1)