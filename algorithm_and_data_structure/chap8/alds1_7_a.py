tree = list()
deep = list()


class Node:
    def __init__(self, parent, left, right):
        self.parent = parent
        self.left   = left
        self.right  = right

def get_node_type(node):
    if node.parent == -1:
        return "root"
    elif node.left == None:
        return "leaf"
    else:
        return "internal node"

def get_child_list(node):
    child_list = ''
    child = node.left
    flag = False
    while child != None:
        if flag:
            child_list += ', '
        child_list += str(child)
        child = tree[child].right
        flag = True
    return child_list

def print_tree():
    for index, (node, d) in enumerate(zip(tree, deep)):
        node_type = get_node_type(node)
        child_list = get_child_list(node)
        print(f"node {index}: parent = {node.parent}, depth = {d}, {node_type}, [{child_list}]")


def rec(u, p):
    deep[u] = p
    if (tree[u].right != None):
        rec(tree[u].right, p)
    if (tree[u].left != None):
        rec(tree[u].left, p + 1)


def main():
    n = int(input())
    tree = [Node(None,None,None) for _ in range(n)]
    deep = [None for _ in range(n)]

    root_num = -1
    for _ in range(n):
        data = list(map(int, input().split(' ')))
        node_num  = data.pop(0)
        child_num = data.pop(0)
        left = None
        for i in range(child_num):
            child_node_num = data.pop(0)
            if i == 0:
                tree[node_num].left = child_node_num
            else:
                tree[left].right = child_node_num
            left = child_node_num
            tree[child_node_num].parent = node_num
    
    for i in range(n):
        if tree[i].parent == None:
            root_num = i
            tree[root_num].parent = -1
            break

    rec(root_num, 0)

    print_tree()



if __name__ == '__main__':
    main()
