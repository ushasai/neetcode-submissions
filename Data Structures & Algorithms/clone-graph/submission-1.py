class Solution:
    def cloneGraph(self, node):
        copies = {}

        def dfs(node):
            if node in copies:          # already copied
                return copies[node]
            new = Node(node.val)                   # make the copy
            copies[node] = new           # store it BEFORE the neighbors
            for nb in node.neighbors:
                new.neighbors.append(dfs(nb))
            return new

        if not node:
            return None
        return dfs(node)