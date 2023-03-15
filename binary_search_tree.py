from queue_array import Queue


class TreeNode:
    def __init__(self, key, data, left=None, right=None):
        self.key = key
        self.data = data
        self.left = left
        self.right = right


class BinarySearchTree:

    def __init__(self):
        self.root = None

    def is_empty(self):
        return self.root is None

    def search(self, key):
        return self.search_helper(key, self.root)

    def search_helper(self, key, n):
        if n is not None:
            if n.right is None and n.left is None and not n.key == key:
                return False
            elif n.key == key:
                return True
            else:
                if key < n.key and n.left is not None:
                    return self.search_helper(key, n.left)
                elif n.right is not None:
                    return self.search_helper(key, n.right)

    def insert(self, key, data=None):
        n = TreeNode(key, data)
        if self.root is None:
            self.root = n
        self.insert_helper(n, self.root)

    def insert_helper(self, new_n, current_n):
        if new_n.key < current_n.key and current_n.left is not None:
            self.insert_helper(new_n, current_n.left)
        elif new_n.key > current_n.key and current_n.right is not None:
            self.insert_helper(new_n, current_n.right)
        elif new_n.key < current_n.key and current_n.left is None:
            current_n.left = new_n
        elif new_n.key > current_n.key and current_n.right is None:
            current_n.right = new_n
        else:
            current_n.data = new_n.data

    def find_min(self):
        if self.is_empty():
            return None
        return self.find_min_helper(self.root)

    def find_min_helper(self, n):
        if n.left is not None:
            return self.find_min_helper(n.left)
        else:
            return n.key, n.data

    def find_max(self):
        if self.is_empty():
            return None
        return self.find_max_helper(self.root)

    def find_max_helper(self, n):
        if n.right is not None:
            return self.find_max_helper(n.right)
        else:
            return n.key, n.data

    def tree_height(self):
        if self.is_empty():
            return None
        return self.tree_height_helper(self.root)

    def tree_height_helper(self, n):
        if n is None:
            return -1
        else:
            height_left = self.tree_height_helper(n.left)
            height_right = self.tree_height_helper(n.right)
            if height_left > height_right:
                return 1 + self.tree_height_helper(n.left)
            else:
                return 1 + self.tree_height_helper(n.right)

    def inorder_list(self):
        return self.inorder_list_helper(self.root)

    def inorder_list_helper(self, n):
        if n is not None:
            if n.left is not None and n.right is not None:
                return self.inorder_list_helper(n.left) + [n.key] + self.inorder_list_helper(n.right)
            if n.left is None and n.right is not None:
                return [n.key] + self.inorder_list_helper(n.right)
            if n.left is None and n.right is None:
                return [n.key]
            if n.left is not None and n.right is None:
                return self.inorder_list_helper(n.left) + [n.key]
        else:
            return []

    def preorder_list(self):
        return self.preorder_list_helper(self.root)

    def preorder_list_helper(self, n):
        if n is not None:
            if n.left is None and n.right is None:
                return [n.key]
            elif n.left is not None and n.right is None:
                return [n.key] + self.preorder_list_helper(n.left)
            elif n.left is None and n.right is not None:
                return [n.key] + self.preorder_list_helper(n.right)
            else:
                return [n.key] + self.preorder_list_helper(n.left) + self.preorder_list_helper(n.right)
        else:
            return []

    def level_order_list(self):
        q = Queue(25000)  # Don't change this!
        lst = []
        q.enqueue(self.root)
        while not q.is_empty():
            n = q.dequeue()
            lst.append(n.key)
            if n.left is not None:
                q.enqueue(n.left)
            if n.right is not None:
                q.enqueue(n.right)
        return lst
