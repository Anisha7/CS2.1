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
        

if __name__ == '__main__':
    # content= ['hello', 'lone', 'hen', 'hear']
    # file = open('/usr/share/dict/words','r')
    file = open('scrabbleWords.txt','r')
    content = list(file)
    # print('')
    trie = DictTrie(content)
    result = trie.findWordsWithPrefix('a')
    # print(result)

    letters = ['a', 'p', 'm', 'o', 'n', 'l', 'e']
    result = trie.scrabbleWordFinder('ap', letters)
    # print(result)

