# 개표

n = int(input())
vote = input()
vote = list(vote)
a, b = 0, 0

for i in vote:
  if i == 'A':
    a += 1
  elif i == 'B':
    b += 1

if a > b:
  print('A')
elif a < b:
  print('B')
else:
  print("Tie")