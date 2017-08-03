import itertools

a1= 'A1'
b1= 'B1'
c1='C1'
a2='A2'
b2='B2'
c2='C2'
a3='A3'
b3='B3'
c3='C3'
x = [(a1, a2, a3), (b1, b2, b3), (c1, c2, c3)]

x_per = list(itertools.permutations(x))
x_pro = list(itertools.product(*x))
print(len(x_per))

for i in x_per:
    print(i)
print (len(x_pro))
for i in x_pro:
    print(i)