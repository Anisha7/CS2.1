class Node(object):
    def __init__(self, data = None, isWord = False):
        self.data = data
        self.isWord = isWord
        self.children = None


class Trie(object):
    def __init__(self):