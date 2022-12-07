from anytree import Node, RenderTree
import re

f = open("input.txt", "r")

def main():
    score: int = 0
    root: Node = Node(name="root", size = 0)
    parent: Node
    smallest_possible = 30000000
    for l in f:
        l = l.strip()
        cmd = list[str]
        if l[0:1] == "$":
            cmd = l[2:].split(" ")

            if cmd[0] == "cd": # changing dir
                if cmd[1] == "/":
                    parent = root
                elif cmd[1] == "..": # moving up
                    for child in parent.children:
                        parent.size += child.size
                    if parent.size <= 100000: 
                        score += parent.size
                    if parent.size >= 572957 and parent.size < smallest_possible:
                        smallest_possible = parent.size
                    parent = parent.parent
                else: # moving down
                    parent = Node(cmd[1], parent, size = 0)
            elif cmd[0] == "ls":
                continue
        else:
            create_leaf_node(l, parent)

    for child in root.children:
        root.size += child.size
    

    for pre, fill, node in RenderTree(root):
        print("%s%s (%s)" % (pre, node.name, node.size))
    
    unused_space = 70000000-root.size
    delete = 30000000-unused_space
    print(f"Unused space: 70000000 - {root.size} = {unused_space}")
    print(f"Need to delete: 30000000 - {unused_space} = {delete}")
    print(smallest_possible)
    print(score)

def create_leaf_node(l: str, parent: Node) -> Node:
    name = l.split(" ")[1]
    numbers = re.findall('[0-9]+', l)
    size = 0
    if len(numbers) > 0:
        size = int(numbers[0])
        Node(name, parent, None, size = size)

main()