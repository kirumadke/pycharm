#name = input("Give me your name: ")
#print("Your name is " + name)
#age=15
#if age > 17:
#    print("can see a rated R movie")
#elif age < 17 and age > 12:
 #   print("can see a rated PG-13 movie")
#else:
 #   print("can only see rated PG movies")
"""
name = raw_input("What's your name? ")
print("Nice to meet you " + name + "!")
age = raw_input("Your age? ")
print("So, you are already " + age + " years old, " + name + "!")
"""
#while True:
   # s = raw_input('Enter something : ')
   # if s == 'quit':
   #     break
   # print('Length of the string is', len(s))
#print('Done')
#
"""
myList=[1,2,3,4,5]
print type(myList)
myList.append(6)
myList.append(6)
print myList.count(6)
newList = ['foo','zoo']
myList.extend(newList)
print myList.index('foo')
myList.insert(0,'done')
myList.remove('zoo')
myList.reverse()
print myList
"""
##
a = [5, 10, 15, 20, 25]
def Function (x):

    e=[]
    e.append(x[0])
    e.append(x[-1])

    return e

print (Function(a))

rangers=[]
number = int(input("enter a number "))
for ranger in range ((number-(number-2)), (number -1)):
    if number%ranger ==0:
        Vlu= int(number/ranger)
        rangers.append(Vlu)
print (rangers)
