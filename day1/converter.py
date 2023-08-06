
#Conditional check, 

# a = int(input("enter a weight "))
# b = input("k for kg and l for pounds ").lower()

# if(b == "k"):
#     print("Weight in kg is ", a/2.2)
# elif(b == 'l'):
#     print("Weight in pound is", a*2.2)



#Range Example
a = []
for number in range(0,5):
    a.append(number)
a.append(5)
print(min(a))

oddarr = [1,3,5,7,9]
newarr = []
for i in range(0, len(oddarr)):
    newarr.append(i)
    
print(newarr)

newoddarr = []
for i in range(0, 20):
    if(i%2==1):
        newoddarr.append(i) 

print(newoddarr)


def isDivisibleByThree(num):
    return num%3 == 0

result = list(filter(isDivisibleByThree, newoddarr))
print(result)


def squareNumber(num):
    return num*num
sqaredResult = list(map(squareNumber, result))
print(sqaredResult)

array = [1,2,3,4,5,6]

arrayOfNames = ["Bishal", "Bikram", "Hari", "Shyam"]
for i, name in enumerate(arrayOfNames):
    print({i: name})

firstArray = [1,2,3,2,6]
secondArray = [4,5,6,7,6,7,8,8]
for f,s in zip(firstArray, secondArray):
    print(f,s)
    
print()

def sum(a,b):
    return a+b

# tuples example, immutable, cannot change value during runtime

tupleExample = (7, "hello", "world")
print(tupleExample)

print(tuple(filter(lambda x: x%2==1, range(0,20))))
