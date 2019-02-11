class Node(object):
    def __init__(self, data = None, isWord = False):
        self.data = data
        self.isWord = isWord
        self.children = []
        self.count = 0


class Trie(object):
    def __init__(self, words = []):
        self.head = Node('')
        for word in words:
            self.add(word)
    
    def findNode(self, word, node):
        if (len(word) <= 0):
            return node
        if (node == None):
            return None

        for child in node.children:
            if (child.data == word[0]):
                return self.findNode(word[1:], child)
        
        return None

    # add one letter 
    def addLetter(self, letter, node):
        for child in node.children:
            if (child.data == letter):
                return child
        newNode = Node(letter)
        node.children.append(newNode)
        return newNode

    # add word to trie
    def add(self, word):
        node = self.findNode(word, self.head)
        if (node != None):
            node.isWord = True
            return
        
        node = self.head
        i = 0
        while (i < len(word)):
            node = self.addLetter(word[i], node)
            i += 1

        node.isWord = True
        return

    # find if a word exists in trie
    def find(self, word):
        node = self.findNode(word, self.head)
        if (node.isWord == True):
            return True
        return False

    # finds all words and append to result array
    def findWordsWithPrefixHelper(self, result, node, prefix):
        if (node.isWord == True):
            result.append(prefix)

        for child in node.children:
            self.findWordsWithPrefixHelper(result, child, prefix+child.data)
        
        return
        
    # find all words with the given prefix
    def findWordsWithPrefix(self, prefix):
        node = self.findNode(prefix, self.head)
        if (node == None):
            return []
        result = []
        self.findWordsWithPrefixHelper(result, node, prefix)
        return result

        