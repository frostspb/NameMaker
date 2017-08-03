x = [('a1', 'b1', 'c1'), ('a1', 'b1', 'c2')]
z = [[a for a in i] for i in x]


def ddd(c):
    x = (''.join(c))
    print (x)
    return (x,)

b = [i + (''.join(i),) for i in x]

print(b)

def spl(a):

        a.append(''.join(a))

c = [i for i in z]

#for d in x:
#    spl(d)


print(c)