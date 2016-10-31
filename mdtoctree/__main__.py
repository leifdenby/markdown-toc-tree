import tree_text
import operator
import sys

class Node:
    def __init__(self, parent, value):
        self.children = []
        self.parent = parent
        self.value = value

    @property
    def depth(self):
        if not self.parent is None:
            return 1 + self.parent.depth
        else:
            return 1

    @property
    def index(self):
        if self.parent is None:
            return ''
        else:
            return self.parent.index + '%d' % (self.parent.children.index(self) + 1)

    def tolist(self):
        if len(self.children) > 0:
            return (self.value, [c.tolist() for c in self.children])
        else:
            return self.value

if __name__ == "__main__":
    current_node = Node(parent=None, value='')
    root_node = current_node

    for line in sys.stdin:
        if line.startswith('#'):
            d = sum([s == '#' for s in line])

            title = line[d+1:].strip()

            while d != current_node.depth:
                if d > current_node.depth:
                    parent_node = current_node
                    current_node = Node(parent=parent_node, value=title)
                    parent_node.children.append(current_node)
                else:
                    current_node = current_node.parent

            parent_node = current_node
            current_node = Node(parent=parent_node, value=title)
            parent_node.children.append(current_node)


    print tree_text.format_tree(root_node, format_node=lambda n: '%s. %s' % (n.index, n.value), get_children=lambda n: n.children)
