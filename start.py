from math import *
i=3
print(i)
for i in range(1,10,1)
  print(i*(-1))

print('!')

z= [0, 1, 2, 3, 4]
print(sin(z))
print('cos(',z,')=',cos(z))


matrix = [[a, b, c, d],[e, f, g, h], [m, n, l, k]]
[[row[i] for row in matrix] for i in range(4)]


sentence = ['Mary', 'had', 'a', 'little', 'lamb', '...' ,'ohh', 'no....', 'there is no more this lamb =))', 'because it was eaten xD']
for i in range(len(sentence)):
  print(i, sentence[i])


for n in range(2, 10):
  for x in range(2, n):
    if n % x == 0:
      print(n, 'equals', x, '*', n//x)
      break
else:
  print(n, 'is a prime number')
  pass
