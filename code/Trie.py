# optimize using [None]*26, and use chr/ord functions to find/set indices (0-25) = to a letter

class Node(object):
    def __init__(self, data = None, isWord = False):
        self.data = data
        self.isWord = isWord
        self.children = []
        self.count = 0


class Trie(object):
    def __init__(self, words = []):
        self.head = Node('')
        # add all words to trie
        for word in words:
            word = word.strip('\n')
            # remove grammar/symbols
            word = word.strip('\r\n').strip("'s").strip(',').strip('.').strip(':').strip(';')
            self.add(word)
    
    # find the node at the end of the word
    # used to find a prefix
    def findNode(self, word, node, i=0):
        # if checked all letters, node is found
        if (i >= len(word)):
            return node
        # if node is none, word doesn't exist
        if (node == None):
            return None

        # check each child for curr letter (word[i])
        for child in node.children:
            if (child.data == word[i]):
                # recursive call to deal with next letter
                return self.findNode(word, child, i+1)
        
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
            node.count += 1
            node.isWord = True
            return
        
        node = self.head
        i = 0
        while (i < len(word)):
            node = self.addLetter(word[i], node)
            i += 1

        # set word to true at last node
        node.isWord = True
        node.count += 1
        return

    def remove(self, word):
        node = self.findNode(word, self.d)
        if (node != None):
            node['isWord'] = False
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

    def search(self, prefix):
        return self.findWordsWithPrefix(prefix)

    # finds all words, counts and append to result array
    def findWordsWithPrefixCountsHelper(self, result, node, prefix):
        if (node.isWord == True):
            result.append((prefix, node.count))

        for child in node.children:
            self.findWordsWithPrefixCountsHelper(result, child, prefix+child.data)
        
        return

    # find all words with the given prefix
    def findWordsWithPrefixCounts(self, prefix):
        node = self.findNode(prefix, self.head)
        if (node == None):
            return []
        result = []
        self.findWordsWithPrefixCountsHelper(result, node, prefix)
        return result


    


def gameLoop(trie):
    gameLoop = True
    while gameLoop == True:
        print('Type "p" to play and "q" if you would like to quit')
        gameType = raw_input('Type here: ')
            
        if gameType.lower() == "p":
            prefix = raw_input("Give me a prefix: ")
            result = trie.findWordsWithPrefix(prefix)
            print(result)
            print(trie.findWordsWithPrefixCounts(prefix))
            print(" ")
        
        if gameType.lower() == 'q':
            gameLoop = False
            print(" ")
            print("Thanks, b-bye!")

if __name__ == '__main__':
    # content= ['hello', 'lone', 'hen', 'hear']
    file = open('/usr/share/dict/words','r')
    # file = open('scrabbleWords.txt','r')
    content = list(file)
    # print('')
    trie = Trie(content)
    # result = trie.findWordsWithPrefix('apple')
    # print(result)
    gameLoop(trie)