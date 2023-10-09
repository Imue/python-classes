# Multiples of 12

n = input ('Enter any number').strip()
n_int = int(n)
i = 0
while i <= 100:
 if i % n_int == 0:
  print(i)
  i += 12
input()  
