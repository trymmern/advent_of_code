from collections import deque
import sys

f = open("input.txt", "r")

queue = deque([""]*4) 
for x in f:
    for i in range(0, len(x)):
        queue.pop();
        queue.appendleft(x[i]);
        print(queue)
        print(len(set(queue)), len(queue))
        if (len(queue) == len(set(queue)) and '' not in queue):
            print(i + 1)
            sys.exit()