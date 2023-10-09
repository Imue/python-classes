# Multiples of any no btw 0-100

n = input ('Enter any number').strip()
n_int = int(n)

i = 1
while i <= 12:
    j = i * n_int
    print(n, "x", i, "=", j)
    i += 1
  
input()  
