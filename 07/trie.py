class Trie:
    def __init__(self):
        self.root = TrieNode(value='*')

    def search(self, target):
        return TrieNode.search(self.root, target, 0)

    def add(self, new_word):
        return TrieNode.add(self.root, new_word, 0)

    def delete(self, word):
        return TrieNode.delete(self.root, word, 0)


class TrieNode:
    def __init__(self, value, is_word = False):
        self.value = value
        self.children = {}
        self.is_entry = False

    def __str__(self):
        return f'TrieNode({self.value}, {self.children}, {self.is_entry})'

    def search(current, target, index):
        if index == len(target):
            if current.is_entry:
                return current
            else:
                return None

        next_letter = target[index]
        next_child = current.children.get(next_letter)
        if next_child:
            return TrieNode.search(next_child, target, index+1)
        else:
            return None

    def add(current, new_word, index):
        if index == len(new_word):
            current.is_entry = True
        else:
            next_letter = new_word[index]
            next_child = current.children.get(next_letter)
            if next_child:
                TrieNode.add(next_child, new_word, index+1)
            else:
                current.children[next_letter] = TrieNode(value=next_letter)
                TrieNode.add(current.children[next_letter], new_word, index + 1)

    def delete(current, target, index):
        if index == len(target):
            if current.is_entry:
                current.is_entry = False
        else:
            next_letter = target[index]
            next_child = current.children[next_letter]
            if next_child:
                if TrieNode.delete(next_child, target, index + 1):
                    current.children[next_letter] = None

        if current.is_entry:
            return False

        for c in current.children:
            if current.children[c]:
                return False


if __name__ == '__main__':
    t = Trie()
    t.add('eek')
    t.add('egads')
    t.add('yikes')
    t.add('yippee')
    t.add('zonk')
    t.add('zounds')
    print(t.search('yippee'))
    print(t.search('yike'))
    t.delete('yippee')
    print(t.search('yippee'))
    