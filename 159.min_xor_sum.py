class Solution:
    def minVal(self, a, b):
        def countSetBits(N):
        	count = 0
        	for i in range(4*8):
        		if(N & (1 << i)):
        			count += 1
        	return count

        x=countSetBits(a)
        y=countSetBits(b)
        diff=abs(x-y)
        if x==y:
            return a
        elif x>y:
            while diff:
                a=a&(a-1)
                diff-=1
        else:
            while diff:
                a=a|(a+1)
                diff-=1
        return a
