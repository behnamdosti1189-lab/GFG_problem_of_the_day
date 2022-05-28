# Shortest Path between Cities 

# https://practice.geeksforgeeks.org/viewSol.php?subId=e9e5d69027f4cc897811632ff9858002&pid=705791&user=dharmeshpoladiya75

class Solution:
    def shortestPath(self, x, y): 
       # code here
       path=0
       while x!=y:
           if x<y:
               y=y//2
           else:
               x=x//2
           path+=1
       return path