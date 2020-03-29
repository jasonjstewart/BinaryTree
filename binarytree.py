#!/usr/bin/env python3
from collections import deque

class BinaryTree(object):
    '''
    A binary tree.
    '''
    def __init__(self):
        self.root = None


    def __repr__(self):
        return repr(self.root)


    def set(self, key, value):
        '''
        Adds the given key=value pair to the tree.
        '''

        def setNode(self, node, newNode):
            if self.root is None:
                self.root=newNode
            else:
                if node.key >= newNode.key:
                    if node.left is None:
                        node.left=newNode
                        newNode.parent=node
                    else:
                        setNode(self, node.left,newNode)

                elif node.key < newNode.key:
                    if node.right is None:
                        node.right = newNode
                        newNode.parent=node
                    else:
                        setNode(self, node.right,newNode)


        node=self.root
        newNode=Node(None,key,value)
        setNode(self, node, newNode)

        print(key)

    def get(self, key):
        '''
        Retrieves the value under the given key.
        Returns None if the key does not exist.
        '''
        def getNode(node, key):
            if node is None:
                return None
                exit
            elif node.key == key:
                return node
                exit
            else: 
                if node.key < key:
                    return getNode(node.right,key)
                elif node.key > key:
                    return getNode(node.left,key)


        node=self.root
        node = getNode(node,key)
        return node.value if node is not None else None
        
        
        


    def remove(self, key):
        '''
        Removes the given key from the tree.
        Returns silently if the key does not exist.
        no child: just remove the node
        one child: move items up
        two children: go to left one node, then as far right as you can until node.right=None, deleted item run the rules
        '''
        def getN(key):
            '''
            Retrieves the value under the given key.
            Returns None if the key does not exist.
            '''
            def getNode(node, key):
                if node is None:
                    return None
                    exit
                elif node.key == key:
                    return node
                    exit
                else: 
                    if node.key < key:
                        return getNode(node.right,key)
                    elif node.key > key:
                        return getNode(node.left,key)


            node=self.root
            node = getNode(node,key)
            return node if node is not None else None

        def far_right(node):
            if node.right:
                return far_right(node.right)
            else:
                return node

        #TODO
        node = getN(key)
        if node.left==None and node.right==None:
            if node.parent.left==node:
                node.parent.left=None
            if node.parent.right==node:
                node.parent.right=None
        elif node.left and node.right:
            newNode=far_right(node.left)
            changeNode=getN(newNode.key)
            changeNode.parent.right=None
            newNode.left=node.left
            newNode.right=node.right
            newNode.parent=node.parent
            node=None

        elif node.left or node.right:
            #if node.left:
            if node.parent.right==node:
                node.parent.right=node.right
                node.right.parent=node.parent.right
                node=None
            elif node.parent.left==node:
                node.parent.left=node.left
                node.left.parent=node.parent.left
                node=None





    def walk_dfs_inorder(self):
        '''
        An iterator that walks the tree in DFS fashion.
        Yields (key, value) for each node in the tree.
        walk(left), print, walk(right)

        walk_dfs_inorder(node)
        '''
        #TODO
        # "yield (key, value)" for current node
        # "yield from walk_*()" when recursing
        currentnode=self.root
        def traverse_nodes_dfs_inorder(node):
            if node.left is not None:
                yield from traverse_nodes_dfs_inorder(node.left)
            yield (node.key, node.value)
            if node.right is not None:
                yield from traverse_nodes_dfs_inorder(node.right)


        return traverse_nodes_dfs_inorder(currentnode)


    def walk_dfs_preorder(self, node=None, level=0):
        '''
        An iterator that walks the tree in preorder DFS fashion.
        Yields (key, value) for each node in the tree.
        print, walk(left), walk(right)
        '''
        #TODO
        # "yield (key, value)" for current node
        # "yield from walk_*()" when recursing
        currentnode=self.root
        def traverse_nodes_dfs_preorder(node):
            yield (node.key, node.value)
            if node.left is not None:
                yield from traverse_nodes_dfs_preorder(node.left)
            if node.right is not None:
                yield from traverse_nodes_dfs_preorder(node.right)


        return traverse_nodes_dfs_preorder(currentnode)


    def walk_dfs_postorder(self, node=None, level=0):
        '''
        An iterator that walks the tree in inorder DFS fashion.
        Yields (key, value) for each node in the tree.
        walk(left),walk(right),print
        '''
        #TODO
        # "yield (key, value)" for current node
        # "yield from walk_*()" when recursing
        currentnode=self.root
        def traverse_nodes_dfs_postorder(node):
            if node.left is not None:
                yield from traverse_nodes_dfs_postorder(node.left)
            if node.right is not None:
                yield from traverse_nodes_dfs_postorder(node.right)
            yield (node.key, node.value)


        return traverse_nodes_dfs_postorder(currentnode)


    def walk_bfs(self):
        '''
        An iterator that walks the tree in BFS fashion.
        Yields (key, value) for each node in the tree.

        '''
        #TODO
        results = []
        q = []
        output = []
        q.append(self.root)
        node = self.root
        output.append((self.root.key, self.root.value))
        def bfs(q):
            for node in q:
                if node.left:
                    results.append(node.left)
                    output.append((node.left.key, node.left.value))
                if node.right:
                    results.append(node.right)
                    output.append((node.right.key, node.right.value))
            array = []
            for item in results:
                array.append(item)
            results.clear()
            if len(array)>0:
                bfs(array)
            else:
                return None
            # else:
            #     return
        bfs(q)
        return output


        
    ##################################################
    ###   Helper methods


    def _replace_node(self, oldnode, newnode):
        '''
        Internal method to remove a node from its parent
        '''
        #TODO: feel free to use or remove this method


    def _find(self, key):
        '''
        Internal method to find a node by key.
        Returns (parent, node).
        '''
        #TODO: feel free to use or remove this method
        currentNode=self.root
        def _get(self, key, currentNode):
            if not currentNode:
                return None
            elif currentNode.key == key:
                return currentNode
            elif key < currentNode.key:
                return self._get(key,currentNode.leftChild)
            else:
                return self._get(key,currentNode.rightChild)

        _get(key,currentNode)



class Node(object):
    '''
    A node in a binary tree.
    '''
    def __init__(self, parent, key, value):
        '''Creates a linked list.'''
        self.key = key
        self.value = value
        self.parent = parent
        self.left = None
        self.right = None

    def __repr__(self):
        result = []
        def recurse(node, prefix1, side, prefix2):
            if node is None:
                return
            result.append(prefix1 + node.key + side)
            if node.right is not None:
                recurse(node.left, prefix2 + '\u251c\u2500\u2500 ', ' \u2c96', prefix2 + '\u2502   ')
            else:
                recurse(node.left, prefix2 + '\u2514\u2500\u2500 ', ' \u2c96', prefix2 + '    ')
            recurse(node.right, prefix2 + '\u2514\u2500\u2500 ', ' \u1fe5', prefix2 + '    ')
        recurse(self, '', '', '')
        return '\n'.join(result)
