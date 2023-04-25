a=100
b=100.234
c="Hello, Emaya"
d=False
print(type(a))
print(type(b))
print(type(c))
print(type(d))
print('%i,%.2f,%s.%s' %(a,b,c,d))
s='{0}: {1:d}\t{2}\t{3}\t{4}'.format(d,d,a,b,c)
print(s)
print('%s %s' %(True,False))
print('%i %i' %(True,False))
print()
t=f'{a}{b:,.2f}\n{c[:5]}\n{d}'
print(t)
----
values = [ 3, 53, 19, -5, 60, 41, "test", 5, 22, 9, 22]
for i in values:
  if i==9:
    break
  elif isinstance(i, str):
    continue
  else:
    print(i)
    
total = 0 
loop = 0
while total < 200:
    if isinstance(values[loop], str):
        loop += 1
        continue
    elif values[loop]>0:
        total += values[loop]
    else:
        print(f'skipping{values[loop]}')
              
    if loop == len(values)-1:
              break
    loop+=1
              
print(f'sum:{total},loop:{loop}')
------
import copy
a = [[1,1,1,1], [2,2,2,2], [3,3,3,3]]
shallow_a = copy.copy(a)
deep_a = copy.deepcopy(a)
shallow_a[1][0]= 0
deep_a[1][0] = 99
print(f'original: {a}')
print(f'shallow: {shallow_a}')
print(f'deep: {deep_a}')
print(id(a[1]))
print(id(shallow_a[1]))
print(id(deep_a[1]))
----
def to_str_fill(i):
    t = str(i).zfill(8)
    return t
s=[x**2 for x in range(10)]
s=[x for x in s if x % 3 == 0]
s2=[to_str_fill(x) for x in s]
[print(x) for x in s2]

---
import numpy as np
def print_var(n,x):
    print(f'{n}:{x}{type(x)}')
    
x=2**99
print_var('x',x)
y = np.int64(2**33)
print_var('y',y)
z = np.float64(387438.238454274876754)
print_var('z',z)
y2=y.astype(np.int32)
print_var('y2',y2)
y3 = np.int32(np.int64(2**31))
print_var('y3',y3)
z2 = np.float32(z)
print_var('z2',z2)

-----
g_x = 2.5
def f1(x):
    global g_x
    y=6
    g_x =x*y
    return g_x
#print(y)
print(f'f1(5):{f1(5)}')
print(f'g_x: {g_x}')

print(f'f1(g_x):{f1(g_x)}')
print(f'g_x: {g_x}')

--
def fn(*args,**kwargs):
    total = sum(args)
    retval=f'sum of args: {total}\n'
    for k, v in kwargs.items():
        retval+= f'{k}={v}\n'
    return retval
s = fn(1,2,3, test=5, p='Hello, World!')
print (s)
t = fn(4, 5, 6,greeting = 'Hello' , recipient = 'World')
print(t)
--
def fn_next(begin):
    current=begin  
    def fn_inc():
        current +=1
        return current
    return fn_inc

get_next = fn_next(100)
print(get_next())
print(get_next())
print(get_next())
print(get_next())
print(get_next())
print(get_next())
print(get_next())
