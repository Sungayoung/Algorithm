# 연결리스트 방식으로 트리 클래스 구현

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.value)


class Tree:
    def __init__(self):
        self.root = None

    # 항상 부모노드의 왼쪽부터 값을 채워넣음
    def make_node(self, parent_node, child_node):

        # 현재 트리에 같은 value값을 가진 노드가 있는지 먼저 탐색
        tmp_node = self.find_node(parent_node.value)

        if not self.root:
            self.root = parent_node
        elif tmp_node:
            parent_node = tmp_node

        if not parent_node.left:
            parent_node.left = child_node
        elif not parent_node.right:
            parent_node.right = child_node
        else:
            return "Full"

    def find_node(self, value):
        if not self.root:
            return None
        node = self.root
        stack = [node]
        while stack:
            cur_node = stack.pop()
            if cur_node.value == value:
                return cur_node

            if cur_node.left:
                stack.append(cur_node.left)
            if cur_node.right:
                stack.append(cur_node.right)


def preorder(node):
    global cnt
    cnt += 1
    print(node.value)
    if node.left:
        preorder(node.left)
    if node.right:
        preorder(node.right)


for tc in range(int(input())):
    E, N = map(int, input().split())
    node_list = list(map(int, input().split()))
    cnt = 0
    tree = Tree()
    for i in range(E):
        parent = Node(node_list[i * 2])
        child = Node(node_list[i * 2 + 1])
        tree.make_node(parent, child)
    new_root = tree.find_node(N)
    preorder(new_root)
    print("#{} {}".format(tc + 1, cnt))
