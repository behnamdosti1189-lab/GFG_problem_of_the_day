class Solution:
    def endPoints(self, mat, R, C):
        #code here
        left = 0
        right = 1
        up=0
        down=0
        i = 0
        j = 0
        
        while(True):
            if(mat[i][j]==0):
                if(right):
                    j+=1
                elif(down):
                    i+=1
                elif(left):
                    j-=1
                else:
                    i-=1
            else:
                mat[i][j]=0
                if(right):
                    right = 0
                    down = 1
                    i+=1
                elif(down):
                    down = 0
                    left = 1
                    j-=1
                elif(left):
                    left = 0
                    up = 1
                    i-=1
                else:
                    up = 0
                    right = 1
                    j+=1
                    
            if(i>=R):
                return [i-1,j]
            elif(i<0):
                return [i+1,j]
            elif(j>=C):
                return [i,j-1]
            elif(j<0):
                return [i,j+1]
