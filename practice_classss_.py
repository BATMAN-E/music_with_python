#jam = [1,2,3,4,5]
#print(jam[2])

#fruit1 = ['apple','banana','mango','orange']
#fruit1.insert(1,'grapes')
#print(fruit1)

'''fruit1 = ['apple','banana','mango','orange']
fruit1.append('grapes')
print(fruit1)
'''
'''color = ['red','black','white','orange']
del color [1]
print(color)'''

'''color = ['red','black','white','orange']
color_1 =  color.pop(1)
print(color)
print(color_1)'''

'''color = ['red','black','white','orange']
color.remove('black')
print(color)'''

''' items = 'IamsocutethatIwilldie'
lcount = items.count('l')
print(lcount) '''

'''thistuple = ( 'apple', 'banana', 'orange', True , False)
print(thistuple[2])

thistuple1 = ( 1, 33, 4,5, 6,7,12,45)
print(max(thistuple1))
print(min(thistuple1))

thistuple2 = ( 1, 33.5, 4.5, 6.7,12,45)
for i in range(len(thistuple2)):
    print(thistuple2[i])'''

'''thistuple3 = ( 1, 33.5, 4.5)
total = 0
for num in thistuple3:
    total += num
print(total)'''''

'''set1 = {1,2,3,4}
set2 = {4,5,6,7}

x = set1.add(10)
print(set1)

x1 = set1.remove(1)
print(set1)

x1 = set1.pop()
print(set1)

set3 = set1 | set2
print(set3)

if set3.intersection({2}):
    print('2 was in set3')
    '''''

'''def myclass(a,b):
    return a+b
c = int(input("Enter the numbers: "))
d = int(input("Enter the numbers: "))
print(myclass(c,d))
'''

'''def myclass():
    return "Hello World"
x = myclass()
print(x)
'''

'''def myclass(name):
    return f"Hello {name}"
x = input("Enter Your name: ")
y = myclass(x)
print(y)'''''

'''def myclass(a):
    return a**2
x = int(input("Enter the number: "))
y = myclass(x)
print(y)'''

'''def evenandodd(a):
    if a%2 == 0:
        print("Even")
    else:
        print("Odd")
x = int(input("Enter the number: "))
evenandodd(x)'''


'''add  = lambda a: a+10

x = int(input("Enter the number: "))
y = add(x)
print(y)'''

''' [1,2,3,4]
sq = list(map(lambda x: x**2 , l))
print(sq)
even = list(filter(lambda x: x%2 == 0 , l))
print(even)'''

'''x = [(2,3),(2,4),(1,2),(1,3),(3,4)]
s = sorted(x ,key =lambda l: l[1])
print(s)'''

'''mul = lambda a,b: a*b
m = int(input())
y = int(input())
z = mul(m,y)
print(z)'''



