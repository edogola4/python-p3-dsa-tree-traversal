class Tree:
    def __init__(self, root=None):
        self.root = root

    def get_element_by_id(self, id):
        return self._dfs(self.root, id)

    def _dfs(self, node, id):
        if node is None:
            return None
        if node.get('id') == id:
            return node
        for child in node.get('children', []):
            result = self._dfs(child, id)
            if result is not None:
                return result
        return None
