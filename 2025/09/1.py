f = open("input.txt", "r")

points = [(int(x), int(y)) for x, y in (line.strip().split(",") for line in f)]

def get_area(p1, p2):
  width = abs(p2[0] - p1[0]) + 1
  height = abs(p2[1] - p1[1]) + 1
  return width * height

max_area = 0
for i in range(len(points)):
  for j in range(i+1, len(points)):
    area = get_area(points[i], points[j])
    if area > max_area:
      max_area = area

print("Result:", max_area)