import numpy as np
import string
from collections import deque

f = open("input.txt", "r")

class Node:
    def __init__(self, x: int, y: int, parent=None):
        self.x: int = x
        self.y: int = y
        self.parent: Node = parent

    def __repr__(self):
        return str((self.x, self.y))

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

move_x = [-1, 0, 0, 1]
move_y = [0, -1, 1, 0]

def main():
    (m, start, end) = fill_matrix()
    path = find_path(m, start.x, start.y, end)
    print(start, end)
    print(path)

# Matrix and start postion in the matrix
def find_path(m: np.ndarray, x: int, y: int, end: Node):
    # N x N
    len_x = len(m[0])
    len_y = len(m)
    print("dimensions: ", [len_y, len_x])
    # add start to queue
    start = Node(x, y)
    q = deque()
    q.append(start)

    # Keep track of visited nodes
    visited = set()
    index = (start.x, start.y)
    visited.add(index)
    while q:
        curr: Node = q.popleft()

        #print(curr, curr.parent)
        if curr.x == end.x and curr.y == end.y:
            path = []
            get_path(curr, path)
            return path

        val = m[curr.y][curr.x]

        for k in range(len(move_x)):
            x = curr.x + move_x[k]
            y = curr.y + move_y[k]

            if is_valid(m, x, y, val):
                print("valid: ", val, m[y][x], f"({x}, {y})")
                next = Node(x, y, curr)
                index = (next.x, next.y)
                
                if index not in visited:
                    q.append(next)
                    visited.add(index)

    return

def get_path(node: Node, path=[]):
    if node:
        get_path(node.parent, path)
        path.append(node)

def is_valid(m: np.ndarray, x: int, y: int, val: int) -> bool:
    is_within = -1 < x < len(m[0]) and -1 < y < len(m)
    if not is_within:
        return False
    
    is_allowed = m[y][x]-1 <= val <= m[y][x]
    return is_allowed

def fill_matrix() -> tuple:
    m = np.array([])
    lc = dict()

    # map letters to numbers
    for index, letter in enumerate(string.ascii_lowercase, 0):
        lc[letter] = index
    # Loop trhough chars in line and add the correlating number to matrix
    # and find start and end indexes
    for y, l in enumerate(f):
        row = []
        for x, c in enumerate(l.strip()):
            if c == 'S':
                row.append(lc['a'])
                start = Node(x, y)
            elif c == 'E':
                row.append(lc['z'])
                end = Node(x, y)
            else:
                row.append(lc[c])
        if len(m) < 1:
            m = np.array([row])
        else:
            m = np.append(m, [row], axis=0)
    return (m, start, end)

main()