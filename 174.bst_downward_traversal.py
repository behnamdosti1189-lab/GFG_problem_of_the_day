class Solution:
    def __init__(self):
        self.flag = False
        self.ans = 0
        self.g = 0
        self.start = None

    def dfs(self, root, trt, gg):
        if root is None:
            return
        if root.data == trt and not self.flag:
            self.g = gg
            self.start = root
            return
        self.dfs(root.left, trt, gg - 1)
        self.dfs(root.right, trt, gg + 1)
        if self.flag:
            if self.g == gg:
                self.ans += root.data

    def verticallyDownBST(self, root, target):
        self.dfs(root, target, 0)
        self.flag = True
        if self.start is None:
            return -1
        self.dfs(self.start, target, self.g)
        return self.ans - self.start.data
