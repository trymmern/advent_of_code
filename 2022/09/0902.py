from typing import NamedTuple

f = open("input.txt", "r")

class Pos(NamedTuple):
    x: int
    y: int

def main():
    h_pos = Pos(x = 0, y = 0)
    t_pos = h_pos

    points: list[Pos] = [h_pos]*9
    visited: list(Pos) = [t_pos]
    for l in f:
        cmd = l.strip().split(" ")
        
        for _ in range(int(cmd[1])):
            match cmd[0]:
                case 'U':
                    h_pos = Pos(h_pos.x, h_pos.y+1)
                case 'D':
                    h_pos = Pos(h_pos.x, h_pos.y-1)
                case 'R':
                    h_pos = Pos(h_pos.x+1, h_pos.y)
                case 'L':
                    h_pos = Pos(h_pos.x-1, h_pos.y)

            h_new = h_pos

            for i in range(len(points)):
                t_pos = move(h_new, points[i].x, points[i].y)
                points[i] = t_pos
                h_new = points[i]

            if points[-1] not in visited:
                visited.append(points[-1])
        
    print(len(visited))

def move(h_pos: Pos, t_pos_x: int, t_pos_y: int) -> Pos:
    move_x = abs(h_pos.x - t_pos_x) > 1 or abs(h_pos.x - t_pos_x) >= 1 and abs(h_pos.y - t_pos_y) > 1
    move_y = abs(h_pos.y - t_pos_y) > 1 or abs(h_pos.y - t_pos_y) >= 1 and abs(h_pos.x - t_pos_x) > 1

    if move_x and h_pos.x > t_pos_x:
        t_pos_x += 1
    if move_x and h_pos.x < t_pos_x:
        t_pos_x -= 1
    if move_y and h_pos.y > t_pos_y:
        t_pos_y += 1
    if move_y and h_pos.y < t_pos_y:
        t_pos_y -= 1
    
    return Pos(t_pos_x, t_pos_y)

main()