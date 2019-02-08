import sys

class DictTrie(object):
    def __init__(self, words=[]):
        self.d = dict()
        for word in words:
            word = word.strip('\n')
            word = word.strip('\r\n')
            self.add(word.strip('\n').lower())

    def add(self, word):
        curr = self.d
        for i in range(len(word)):
            curr = self.addLetter(word[i], curr)
            if 'isWord' not in curr.keys():
                curr['isWord'] = False
        curr['isWord'] = True
        

    # returns the key dict the added letter points to
    # or if it already exists, returns the dict it points to
    def addLetter(self, letter, d):
        if letter in d.keys():
            return d[letter]
        else:
            d[letter] = dict()
            return d[letter]

    # finds the dictionary that the last letter of the prefix points to
    def findNode(self, prefix, node):
        if (len(prefix) <= 0):
            return node

        for key in node.keys():
            if key == prefix[0]:
                return self.findNode(prefix[1:], node[key])
        return None

    def findWordsHelper(self, prefix, node, result):
        if (node['isWord'] == True):
            result.append(prefix)
        
        for key in node.keys():
            if (key != 'isWord'):
                self.findWordsHelper(prefix+key, node[key], result)
        
        return

    def findWordsWithPrefix(self, prefix):
        node = self.findNode(prefix, self.d)
        if (node == None):
            return None
        
        result = []
        self.findWordsHelper(prefix, node, result)
        return result

    def remove(self, word):
        node = self.findNode(word, self.d)
        if (node != None):
            node['isWord'] = False
        return
    
    def scrabbleHelper(self, prefix, letters, result, node):
        if (len(letters) <= 0):
            return
        
        if ('isWord' in node.keys() and node['isWord'] == True):
            result.append(prefix)
        
        for i in range(len(letters)):
            l = letters[i]
            if l in node.keys():
                self.scrabbleHelper(prefix + l, letters[:i]+letters[i+1:], result, node[l])
        return

    # given a prefix and a list of letters that can be used, give all possible words
    def scrabbleWordFinder(self, prefix, letters):
        node = self.findNode(prefix, self.d)
        if (node == None):
            return None
        
        result = []
        self.scrabbleHelper(prefix, letters, result, self.d)
        return result

def gameLoop(trie):
    gameLoop = True
    while gameLoop == True:
        print('Type "auto" if you would like to try the autocomplete program.\n Type "scrabble" if you would like scrabble words.\nType "q" if you would like to quit')
        gameType = raw_input('Type here: ')
            
        if gameType.lower() == "auto":
            prefix = raw_input("Give me a prefix: ")
            result = trie.findWordsWithPrefix(prefix)
            print(result)
            print(" ")

        if gameType.lower() == "scrabble":
            print("Give me all the letters in your hand, separated by spaces: ")
            letters = raw_input("Type here: ")
            letters = letters.split(' ')
            prefix = raw_input("Give me a prefix: ")
            result = trie.scrabbleWordFinder(prefix, letters)
            print(result)
            print(" ")
        
        if gameType.lower() == 'q':
            gameLoop = False
            print(" ")
            print("Thanks, b-bye!")
        

if __name__ == '__main__':
    # content= ['hello', 'lone', 'hen', 'hear']
    # file = open('/usr/share/dict/words','r')
    file = open('scrabbleWords.txt','r')
    content = list(file)
    # print('')
    trie = DictTrie(content)
    
    gameLoop(trie)
        


