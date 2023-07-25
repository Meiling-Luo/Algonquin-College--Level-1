def f(a,b):
    a = 2*b
    return a
x = 12
y = 24
a = f(x,y)
print(a,x,y)

x = f(0,0)
print(x,y)

def g(a=0,b=0):
    a += b +2
    return a

x = 12
y = 24
print(g())
print(g(b=3,a=2))
print(g(x,y))


def h(x,y):
    x *= 2
    y *= 2
    z = x + y
    return z

x = 12
y = 24
print(h(12,24))
print(h(x,y))
print(h(y=10,x=20))


c = 10
d = -8
if c==d:
    print("Branch 1")
elif c > 0 and d < 0:
    print("Branch 2")
else:
    print("Branch3")

c = 'a'
d = 'a'
if c==d:
    print("Branch 1")
elif c > 0 and d < 0:
    print("Branch 2")
else:
    print("Branch3")


i = 0
j = 1
while i < 10:
    j += i * 2
    i = i + 2
print(i,j)

i = 0
while i < 4:
    i=i+1
print(i)

l=[6,5,4,3,2,1]
for el in l:
    print(el)
