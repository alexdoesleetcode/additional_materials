class Trie:
    def __init__(self):
        self.items = []
        self.children = defaultdict(Trie)

    # Insert an item into a Trie.
    def insert(self, word: str, idx: int):
        self.items.append(idx)
        if len(word) > 0:
            first = word[0]
            self.children[first].insert(word[1:], idx)

    # Look for a previously stored key and return its items.
    def find(self, query):
        if len(query) > 0:
            first = query[0]
            if first in self.children:
                return self.children[first].find(query[1:])
            else:
                return self.items
        else:
            return self.items

    # toString is a helper function for __repr__
    def toString(self, indent="  "):
        s = [str(self.items)]
        for key, child in self.children.items():
            s.append(indent + f"'{key}'-> " + child.toString(indent=indent + "  "))
        return "\n".join(s)
    def __repr__(self):
        return self.toString()


class Solution:
    def stringIndices(
        self, wordsContainer: List[str], wordsQuery: List[str]) -> List[int]:
        wordsContainer = [w[::-1] for w in wordsContainer]
        wordsQuery = [w[::-1] for w in wordsQuery]
        tree = Trie()
        for idx, word in enumerate(wordsContainer):
            tree.insert(word, idx)
        ans = []
        for query in wordsQuery:
            idxs = tree.find(query)
            shortest_l = inf
            shortest = -1
            for i in idxs:
                if len(wordsContainer[i]) < shortest_l:
                    shortest_l = len(wordsContainer[i])
                    shortest = i
            ans.append(shortest)
        return ans
