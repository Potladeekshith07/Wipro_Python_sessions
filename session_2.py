# # slicing

nums =[10,20,30,40]
print(nums[])

nums =[10,20,30,40]
print(nums)

s = 'DataScienceIsAwesome12345'
first = s[4:11]
print(first)

third = s[::2]
print(third)

fourth = s[:-5]
print(fourth)

second = s[0:13] + s[13:20][::-1] + s[20:25]
print(second)

fifth = s[0:4][::-1] + s[4:21] + s[21:25][::-1]
print(fifth)


name = input("enter the student name: ")
age = int(input("enter age: "))
marks = list(map(int , input('enter marks: ').split()))
subjects = input('enter subjects: ').split()



total = sum(marks)
average = total/len(marks)

if average >= 75:
    result = "Distinction"
elif average >= 50 and average < 75:
    result = 'pass'
else:
    result = 'fail'

print(total)
print(average)
print(result)


a = 5
b= 3
print( a & b)
print( a | b)
print( a ^ b)
print( a << 1)
print( a >> 1)


num = int(input("enter a number: "))
if num%2==0:
    print("even")
else:
    print("odd")



a = int(input("enter 1st number : "))
b = int(input("enter 2nd number : "))
c = int(input("enter 3rd number : "))
if a>=b and a>=c:
    print(a)
elif b>=a and b>=c:
    print(b)
else:
    print(c)



    marks=int(input("enter your marks : "))
if marks >= 75:
    print("distinction")
elif marks>=50 and marks<75:
    print("pass")
else:
    print("fail")




for i in range(1 , 11):
    print(i)





number = int(input("enter number : "))
sum = 0
i=1

while i<=number:
    sum+=i
    print(sum)



for i in range (1,21):
    if i%3==0:
        continue
    print(i)



nums = [5,10,15,-2,20]

for n in nums:
    if i<0:
        break
    print(num)


number = int(input("enter number : "))
for i in range(1,11):
    print(number * i)



number = int(input("enter number : "))
if number>1:
    prime =True

    for i in range(2,number):
        if num%i==0:
            prime = False
            break
        if prime :
            print("yeah it a prime")
        else:
            print("its not a prime")
else:
    print("its not a prime")




for i in range(1,6):
    for j in range(i):
        print("*", end="")
    print()










def welcome():
    print("Welcome to python")
welcome()



marks = [80,70,90]
def get_total(marks):
    return sum(marks)
print(get_total(marks))




def greet(name="Guest"):
    return f"hello {name}"
print(greet())
print(greet("Abhi"))




def calculator(marks):
    total = sum(marks)
    avg = total / len(marks)
    return total , avg

total , avg = calculator(marks)
print(total)
print(avg)



def total_marks(*marks):
    return sum(marks)

print(total_marks(80,80,90))



def student_info(**data):
    return data
print(student_info(name="deekshith",age=21,course="python"))



square = lambda x:x*x
for i in marks:
    print(square(i))




def factorial(n):
    if n==1:
        return 1
    return n*factorial(n-1)
print(factorial(5))




def modify_list(list):
    list.append(100)

numbers = [10,20,30]
modify_list(numbers)
print(numbers)


def modify_num(x):
    x=x+10
    return x
num = 5
new_num = modify_num(num)
print(num)
print(new_num)



name = input("enter name : ")
marks = list(map(int , input("enter marks : ").split()))
print(name)
print(marks)

import math
print(math.sqrt(100))