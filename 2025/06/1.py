f = open("input.txt", "r")

def parse_input(file):
  lines = []
  problems = []
  for (i, val) in enumerate(file):
    line = [x.strip() for x in val.split(" ") if x != "" and x != "\n"]
    lines.append(line)
  
  for i in range(len(lines[0])):
    problems.append([lines[j][i] for j in range(len(lines))])

  return problems

problems = parse_input(f)

total = 0
for problem in problems:
  result = 0
  if problem[4] == "+":
    result = int(problem[0]) + int(problem[1]) + int(problem[2]) + int(problem[3])
  elif problem[4] == "*":
    result = int(problem[0]) * int(problem[1]) * int(problem[2]) * int(problem[3])
  print("Solving problem:", problem, "Result:", result)
  total += result

print("Total of all problems:", total)