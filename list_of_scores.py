n = input('Enter size of scores:').strip()
scores =list(())
i = 0
while i < int(n):
  score = input('Enter score' + str(i) + ':').strip()
  scores.append(score)
  i += 1
print(scores)
input()

