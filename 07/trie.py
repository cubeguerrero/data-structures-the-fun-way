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




if __name__ == '__main__':
    t = Trie()
    t.add('add')
    print(t.search('ad'))