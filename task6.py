# even or odd
num=int(input("enter a number:"))
if num % 2==0:
 print("even")
else:
 print("odd")
# print lagest number
a=int(input("enter first number:"))
b=int(input("enter second number:"))
c=int(input("enter third number"))
if a>=b and a>=c:
 print("largest number is:",a)
elif b>=a and b>=c:
 print("largest  number is:",b)
else:
 print("largest number is:",c)


#  mutliplication table
num= int(input("enter a  number: "))
for i in range(1,11):
 print(num,"x",i,"=",num*i)

#  sum of numbers
n=int(input("enter a number:"))
total=0
for i in range(i,n+1):
 total+=i
 print("sum=",total)

#  count even or odd numbers
n=int(input("how many number you want to enter?"))

even=0
odd=0

for i in range(n):
  num=int(input("enter a number:"))
if num % 2==0:
 even +=1
else:
 odd+=1
 print("even numbers:",even)
 print("odd number:",odd)
 