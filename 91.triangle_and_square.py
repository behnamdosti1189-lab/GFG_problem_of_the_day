'''
Triangle and Square 

Geek has a ticket to the Geek Summer Carnival. The ticket has a positive integer B written on it. B denotes the base of a right-angled isosceles triangle. 
Geek can avail discounts on X courses in the carnival.

X is the maximum number of squares of size 2x2 units that can fit in the given right-angled isosceles triangle. 
Find X. 

https://practice.geeksforgeeks.org/problems/3f48d387900a38bd9fd0594b93f9f4f97f5ada8a1644/1#
'''

#User function Template for python3
#consider this triangle as a full square.
#now the number of square present in the square (formed by joining two triangles) is = B/2 X B/2
#because formula of area of square is length * length similarly if one square is 2*2 then new length will be B/2
#AREA = B/2 * B/2
#now again break the square in triangle by dividing the area by 2
#Area of individual triangle = AREA/2
#now remove the half mini square area from the triangle 
#Area of individual triangle - half mini square = A - B/4

class Solution:
    def countShare(self,B):
        #code here
        if(B<=2):
            return 0
        tmp = (B//2)*(B//2)
        tmp //=2
        tmp -=B//4
        return tmp
        

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__=="__main__":
    for _ in range(int(input())):
        b=int(input().strip())
        obj=Solution()
        print(obj.countShare(b))
        
# } Driver Code Ends