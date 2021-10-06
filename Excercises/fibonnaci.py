def fibonnaci(num):
  if num == 0:
    return 0

  if num == 1:
    return 1

  for i in range(num):
    return fibonnaci(num-1) + fibonnaci(num-2)

def fib(num):#fibonnaci up to and including num
  a = 0
  b = 1

  for i in range(num+1):
    yield a
    tmp = a
    a = b
    b += tmp

print(fibonnaci(14),end = '\n\n')

for x in fib(14):
  print(x)