monkeys = [] # of [0:op,1:arg,2:div,3:throw_t,4:throw_f,5:items,6:counter]
modulus = 1
for l in open("input.txt","rt"):
  l = l.strip()
  if l.startswith("Monkey"):
    assert int(l[7])==len(monkeys)
  elif l.startswith("Start"):
    items = [int(x) for x in l[16:].split(", ")]
  elif l.startswith("Operation"):
    if "old * old" in l: op = lambda x,n: x*x; arg = 0
    elif "old *" in l:   op = lambda x,n: x*n; arg = int(l[23:])
    elif "old +" in l:   op = lambda x,n: x+n; arg = int(l[23:])
  elif l.startswith("Test"):
    div = int(l[19:])
    modulus *= div
  elif "true:" in l:
    throw_t = int(l[25:])
  elif "false:" in l:
    throw_f = int(l[26:])
    monkeys.append([op,arg,div,throw_t,throw_f,items,0])

def round(div=True):
  for m in monkeys:
    while len(m[5])>0:
      m[6] += 1
      item = m[5].pop(0)
      w = m[0](item,m[1])
      if div: w = w//3
      else: w = w % modulus
      if w%m[2]==0:
        monkeys[m[3]][5].append(w)
      else:
        monkeys[m[4]][5].append(w)

save = [m[:] for m in monkeys]
for i,m in enumerate(monkeys): save[i][5] = m[5][:]

for rnd in range(20):
  round()

mb = sorted(m[6] for m in monkeys)
print(mb[-1]*mb[-2])

monkeys = save

for rnd in range(10000):
  round(div=False)

mb = sorted(m[6] for m in monkeys)
print(mb[-1]*mb[-2])