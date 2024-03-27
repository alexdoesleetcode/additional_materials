'''
Trie implementation.

See https://leetcode.com/problems/longest-common-suffix-queries/ for example usage
'''

class Trie:
    def __init__(self):
        self.items = []
        self.children = defaultdict(Trie)

    # Insert an item into a Trie.
    # Key is used to determine where the item is placed, usually key == item
    # Since item is stored in every single Trie node, you can save space by
    # making key and item different. For instance, if you have a list of words
    #
    # to insert, key can be the word and item can be the index it occurs in
    # the original list. This way you can look up the word without incurring
    # the cost of storing it.
    def insert(self, key: str, item=None, exact=False):
        if item == None:
            item = key
        if len(key) == 0 or not exact:
            self.items.append(item)
        if len(key) > 0:
            initial = key[0]
            self.children[initial].insert(key[1:], item, exact)
        else:
            return self

    # Look for a previously stored key and return its items.
    #
    # exact=True: Return [] unless the exact match is found
    # exact=False: Return the longest match with the key
    def find(self, query):
        if len(query) == 0:
            return self.items
        else:
            initial = query[0]
            if initial in self.children:
                return self.children[initial].find(query[1:])
            else:
                return self.items

    # toString is a helper function for __repr__
    def toString(self, indent="  "):
        s = [str(self.items)]
        for key, child in self.children.items():
            s.append(indent + f"'{key}'-> " + child.toString(indent=indent+"  "))
        return "\n".join(s)
    def __repr__(self):
        return self.toString()
