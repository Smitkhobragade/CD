class Tree:
    def __init__(self, root, left=None, right=None):
        self.root = root
        self.left = left
        self.right = right
        self.label = None

    def __str__(self):
        return f"{self.root=} | {self.left=} | {self.right=} | {self.label=}"


def get_node(value, left=None, right=None):
    root = Tree(value, left, right)
    return root


def inorder(root):
    if root is None:
        return
    inorder(root.left)
    print(root)
    inorder(root.right)


def create_label(root, label=None):
    if root.left is None and root.right is None:
        root.label = label
        return label
    left = create_label(root.left, 1)
    right = create_label(root.right, 0)
    if left == right:
        root.label = left + 1
    else:
        root.label = max(
            left if left is not None else -1, right if right is not None else -1
        )
    return root.label


arr = []


def return_opname(value):
    match value:
        case "+":
            return "ADD"
        case "-":
            return "SUB"
        case "*":
            return "MUL"
        case "/":
            return "DIV"
        case _:
            return "Invalid"


def gen_code(root, rstack):
    if root is None:
        return

    if root.left is None and root.right is None:
        if root.label == 1:
            print(f"MOV {root.root}, {rstack[-1]}")
        return

    if root.right and root.right.label == 0:
        name = root.right.root
        gen_code(root.left, rstack)
        print(f"{return_opname(root.root)} {name}, {rstack[-1]}")

    elif root.right.label > root.left.label and root.left.label < root.label:
        rstack[0], rstack[1] = rstack[1], rstack[0]
        gen_code(root.right, rstack)
        r = rstack[-1]
        rstack.pop()
        gen_code(root.left, rstack)
        rstack.append(r)
        rstack[0], rstack[1] = rstack[1], rstack[0]
        print(f"{return_opname(root.root)}, {r}, {rstack[-1]}")

    elif root.right.label <= root.left.label and root.right.label < root.label:
        gen_code(root.left, rstack)
        r = rstack.pop()
        gen_code(root.right, rstack)
        print(f"{return_opname(root.root)}, {rstack[-1]}, {r}")
        rstack.append(r)


root = get_node("-")
t1 = get_node("+")
t3 = get_node("-")
a = get_node("a")
b = get_node("b")
t2 = get_node("+")
e = get_node("e")
c = get_node("c")
d = get_node("d")
t1.left = a
t1.right = b
root.left = t1
t3.left = e
t2.left = c
t2.right = d
t3.right = t2
root.right = t3
create_label(root)
inorder(root)

rstack = ["R1", "R0"]
gen_code(root, rstack)
