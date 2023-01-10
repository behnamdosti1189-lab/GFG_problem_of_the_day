    def toSumTree(self, root) :
        #code here
        if(root==None):
            return 0
        
        tmp = root.data
        
        leftSum = self.toSumTree(root.left)
        rightSum = self.toSumTree(root.right)
        root.data = leftSum+rightSum
        
        return root.data + tmp
