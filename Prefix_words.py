# Creating a Trie for storing the node labels
class TrieNode :

    def __init__(self,c='root') :
        self.ch=c
        self.children=dict()
        self.leaf=False

    def isLeaf(self) :
        return self.leaf

    def makeLeaf(self) :
        self.leaf=True

prefix_words=[]

class Trie :

    def __init__(self) :
        self.root=TrieNode()

    def addWord(self,word) :

        trav=self.root

        for char in word :
            if char in trav.children :
                trav=trav.children[char]
            else :
                node=TrieNode(char)
                trav.children=node
                trav=node

        trav.makeLeaf()


    def bfs_words(self,children,prefix) :

        if len(children)==0 : return

        for child in children :
            if child.isLeaf() :
               prefix_words.append(prefix+child.c)
            else :
               self.bfs_words(child.children,prefix+c)





    def getPrefixWords(self,prefix) :


        trav=self.root

        for ch in prefix :
            if ch in trav.children :
                trav=trav.children[ch]
            else :
                return []

        # Now,a BFS should be done to get all the words which have the prefix

        children=trav.children

        self.bfs_words(children,prefix)


        return prefix_words


trie=TrieNode()

trie.addWord('abishek')
trie.addWord('abiram')
trie.addWord('abinov')
trie.addWord('anvesh')
trie.addWord('abhish')

print trie.getPrefixWords('ab')
