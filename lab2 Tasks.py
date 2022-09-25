//Activity 1//
myList1=[]
print("Enter objects of first List...")
for i in range(5):
    val=input("Enter a value:")
    n=int(val)
    myList1.append(n)
myList2=[]
print("Enter objects of secind line...")
for i in range(5):
    val=input("Enter a value:")
    n=int(val)
    myList2.append(n)
List3=myList1+myList2;
print(List3)

//Activity 2//
def isPalindrome(word):
    temp=word[: :-1]
    if temp.capitalize()==word.capitalize():
        return True
    else:
        return False
print(isPalindrome("deed"))
//Activity 3//
a=[[1,0,0] , [0,1,0],[0,0,1]]
b=[[1,2,3],[4,5,6],[7,8,9]]
c=[]

for indrow in range (3):
    c.append ([])
    for indcol in range(3):
        c[indrow].append (0)
        for indaux in range (3):

            c[indrow][indcol] += a[indrow][indaux] * b[indcol][indaux]
print (c)

//Activity 4//
def perimeter(listing):
    leng = len(listing)
    perimeter=0;
    for i in range(0,leng-1):
        dist = (((listing[i][0]-listing[i+1][0])**2)+
                ((listing[i][1]-listing[i+1][1])**2))**0.5
        perimeter = perimeter +dist
    perimeter=perimeter + (((listing[0][0]-listing[leng-1][0])**2)
                           +((listing[0][1]-listing[leng-1][1])**2))**0.5
    return perimeter
L=[(1,3),(2,7),(3,9) , (-1,8)]
print(perimeter(L))

//Activity 5//
def symmDiff(a,b):
    e=set()
    for i in a :
        if i not in b:
            e.add(i)
    for i in b:
        if i not in a:
            e.add(i)
    return e
set1={0,1,2,3,4,5}
set2={4,5,7,8,9}
print(symmDiff(set1,set2))
print(set1.symmetric_difference(set2))
print(set2.symmetric_difference(set1))
print(set1^set2)
print(set2^set1)

//Activity 6//

sample={("sohaib","ali") :"037564856874648364",("aib" ,"li") : "0475648658747",("sib" ,"ai"):"85765986743754",}
firstName = input("enter first name")
lastName=input("enetr last name")

searchTuple = (firstName , lastName)
if searchTuple in sample:
    print(sample[searchTuple])
else:
    print("name not found")


                //LAB TASKS//

//TASK1//


listOne=[]
listTwo=[]
print("Enter 6 elements for the First List : ")
for i in range (6):
    listOne.append(input())
print("\nEnter 6 element for the second List : " )
for i in range(6):
    listTwo.append(input())

listThree=[]
for i in range(6):
    listThree.append(listOne[i])
for i in range(6):
    listThree.append(listTwo[i])
listThree.sort()
print("Sorted list is:",listThree)

//TASK2//

largest = listThree[0]
lowest = listThree[0]
largest2 = None
lowest2 = None
for item in listThree[1:]:
    if item > largest:
        largest2 = largest
        largest = item
    elif largest2 is None or largest2 < item:
        largest2 = item
    if item < lowest:
        lowest2 = lowest
        lowest = item
    elif lowest2 is None or lowest2 > item:
        lowest2 = item
             
print("Largest element is:", largest)
print("Smallest element is:", lowest)

//TASK3//
from math import *
x=float(input("enter x"))
h=float(input("enter h"))
m=(sin(x+h) - sin(x))/h
n=cos(x)
print(m)
print(n)
if(m==n):
    print("equal")
else:
    print("not equal")


//TASK4//

if __name__ == '__main__':

    birthdays = {
        'Kim Namjoon': '09/12/1994',
        'Cristiano Ronaldo': '02/05/1985',
        'Lionel Messi': '06/24/1987',
        'Donald Trump': '06/14/1946',
        'Rowan Atkinson': '01/6/1955',
        'Mohammad Hasnain' : '04/05/2000',
        'Kim Taehyung': '12/30/1995'}

    print('Welcome to the birthday dictionary. We know the birthdays of:')
    for name in birthdays:
        print(name)

    print('Who\'s birthday do you want to look up?')
    name = input()
    if name in birthdays:
        print('{}\'s birthday is {}.'.format(name, birthdays[name]))
    else:
        print('Sadly, we don\'t have {}\'s birthday.'.format(name))

//TASK5//

sample_dict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"
}

keys = ["name", "salary"]
new_dict = {}

for key in keys:
    new_dict[key] = sample_dict[key]

print(new_dict)



