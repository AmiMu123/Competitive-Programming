class Trie:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.trie = Node()

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        currNode = self.trie
        for char in word:
            index = ord(char) - ord('a')
            if not currNode.children[index]:
                currNode.children[index] = Node(char)
            currNode = currNode.children[index]
        currNode.end = True

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        currNode = self.trie
        for char in word:
            index = ord(char) - ord('a')
            if not currNode.children[index]:
                return False
            currNode = currNode.children[index]

        if currNode.end:
            return True
        return False

    def startsWith(self, prefix: str) -> bool:
        currNode = self.trie
        for char in prefix:
            index = ord(char) - ord('a')
            if not currNode.children[index]:
                return False
            currNode = currNode.children[index]

        return True
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """


class Node:
    def __init__(self, char=None):
        self.children = [None] * 26
        self.end = False
        self.val = char


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
