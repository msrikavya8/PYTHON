#print("hello world")

#addition
''' a=10
 b=20
c=a+b
print(c)
 '''
#input addition
'''a=int(input("enter a value")) #by default input takes sring,so then keep int befor input
b=int(input("enter b value"))
c=a+b
print(c)'''

#string concatination
'''first_name=input("enter your fist name")
last_name=input("enter your last name")
name=first_name+last_name
print(name)'''

#typecheck
'''a=10
print(type(a))'''

#typecasting
'''a=10
b=float(a)
print(b)'''

#user input details
'''name=input("your name")
father_name=input("enter your father name")
mother_name=input("enter yout mother name")
your_education=input("enter your degree name")'''

#user input operators
'''a=int(input("enter a value"))
b=int(input("enter b value"))
#arithmatic
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a%b)
print(a//b)
print(a**b)
#assignment
a+=3
print(a)
b-=10
print(b)
a*=5
print(a)
a/=2
print(a)
a%=2
print(a)
#comparision
print(a==b)
print(a!=b)
print(a>=b)
print(a<=b)
#LOGICOL
if a>5 and b<10:
    print("both conditions are true")
else:
    print("atleast one condition is false")

if a>5 or b<10:
    print(" atleast one conditions is true")
else:
    print("condition is false")

print(not(a>5))

#membership op
name="srikavya"
print('s' in name)

name="srikavya"
print('s' not in name)'''

#finding distance:
'''import math
x1=int(input("enter x1 value"))
x2=int(input("enter x2 value"))
y1=int(input("enter y1 value"))
y2=int(input("enter y2 value"))
distance=math.sqrt((x2-x1)**2 + (y1-y2)**2)
print(distance)'''

#swaping two numbers with temp value:
'''a=int(input("enter a:"))
b=int(input("enter b:"))
temp=a
a=b
b=temp
print(a,b)'''
#without temp value:
'''a=int(input("enter a:"))
b=int(input("enter b:"))
a=a+b
b=a-b
a=a-b
print(a,b)'''
#(a+b)**2 & (a-b)**2
'''a=int(input("enter a:"))
b=int(input("enter b:"))
c=(a**2+2*a*b+b**2)
d=(a**2-2*a*b+b**2)
print(c,d)'''
#student marks:(conditional statements...)
'''marks=int(input("enter your marks"))
if(marks>0 and marks<=100):
    if(marks>=90 and marks<=100):#90<=marks<=100 without using and operator
       print("grade A")
    elif(marks>=80 and marks<=89):#80<=marks<=89
       print("grade B")
    elif(marks>=70 and marks<=79):#70<=marks<=79
       print("grade C")
    elif(marks>=60 and marks<=69):
       print("grade D")
    elif(marks>=50 and marks<=59):
       print("grade E")
    else:
       print("fail")
else:
   print("invalid marks")'''
#weekday:
'''weekday=int(input("enter the weekday"))
if(weekday>=0 and weekday<=1):
    if(weekday==1):
        print("sunday")
    elif(weekday==2):
        print("monday")
    elif(weekday==3):
        print("tuesday")
    elif(weekday==4):
        print("wednesday")
    elif(weekday==5):
        print("thursady")
    elif(weekday==6):
        print("friday")
    else:
        print("saturday")
else:
    print("invalid weekand")'''
 #ticket price/fare
'''name=input("enter your name")
gender=(input("enter you gender"))
age=int(input("enter your age"))
ticket_price=int(input("enter you ticketprice"))
if(age>60 and gender=="female"):
    final_price=ticket_price*0.5
    print("you ticket price is ", final_price)
elif(age<60 and gender=="female"):
    final_price=ticket_price*0.7
    print("you ticket price is ",final_price)
elif(age>=60 and gender=="male"):
    final_price=ticket_price*0.7
    print("you ticket price is ",final_price)
else:
    print("you ticket price is ",final_price)'''

#student loan
'''name=input("enter your name")
age=int(input("enter you age"))
percentage=float(input("enter your percentage"))
if(age>=18 and age<=21):      #if(18<=age<=21 and percentage>=80)
    if(percentage>=80.0):
        print("eligible for student loan")
    else:
        print("not eligible")
else:
    print("not eligible for student loan")'''

#ELECTRICITY BILL
'''units=int(input("enter your units"))
if(units>0 and units<=100):
    bill=units*5
elif(units>=101 and units<=200):
    bill=(100*5)+(units-100)*10
elif(units>=201 and units<=300):
    bill=(100*5)+(100*10)+(units-200)*15
elif(units>=301 and units<=400):
    bill=(100*5)+(100*10)+(100*15)+(units-300)*18
print("your electricity bill is",bill)'''

#armstrong number
'''num=int(input("enter a number"))
length=len(str(num))
x=num
sum=0
while(x>0):
    digit=x%10
    sum+=digit**length
    x//=10
if(sum==num):
    print(num,"armstrong number")
else:
    print(num,"not a armstrong number")'''

#harshad number
'''num=int(input("enter a number"))
x=num
sum=0
while(x>0):
    remainder=x%10
    sum=sum+remainder
    x//=10
if(num%sum==0):
    print(num,"harshad num") 
else:
    print(num,"not harshad num")'''       
    
#palindrome number
'''num=int(input("enter anumber"))
x=num
rev=0
while(num>0):
    r=num%10
    rev=(rev*10)+r
    num//=10
if(x==rev):
    print(x,"palinrome")
else:
    print(x,"not palindrome")'''

#perfect number[the sum of the factors of a number except that number itself is equal to the actual number.. 
'''num=int(input("enter anumber"))
sum=0
for i in range(1,num):
    if(num%i==0):
        sum+=i
if(sum==num):
    print(num,"perfect number")
else:
    print(num,"not perfect number")'''
        
#deficient number[it should be lessthan the actual number]
'''num=int(input("enter anumber"))
sum=0
for i in range(1,num):
    if(num%i==0):
        sum+=i
if(sum<num):
    print(num,"deficient number")
else:
    print(num,"not deficient number")'''

#abundent number[it should be greater than the actual number]
'''num=int(input("enter anumber"))
sum=0
for i in range(1,num):
    if(num%i==0):
        sum+=i
if(sum>num):
    print(num,"abundent number")
else:
    print(num,"not abundent number")'''
        
#STRONG NUMBER
'''n=int(input("enter a numer"))
temp=n
sum=0
while(n>0):
    digit=n%10
    fact=1
    for i in range(1,digit+1):
        fact=fact*i
    sum=sum+fact
    n=n//10
if(sum==temp):
    print(temp,"is strong number")
else:
    print(temp,"is not strong number")'''

      
#STRINGS
'''str="AShoka"  #str=input("enter a sring")
print(str.capitalize())

str="Ashoka Womens Engineering College"
for ch in str:
    print(ch.isupper())

str="Ashoka Womens Engineering College"
for ch in str:
    print(ch.islower())

str="AShoka"
print(str.upper())

str="AShoka"
print(str.lower())

str="AShoka"
print(str.istitle())

str="12345" #12a456 is not a digit it return false...
print(str.isdigit())#12345 it is digit return true....

str=["Ashoka","Womens","Engineering","College"]
a="-".join(str)
print(a)

str="Ashoka Womens Engineering College"
a="-".join(str)
print(a)

str="Ashoka Womens Engineering College"
a=str.split()
print(a)

str="   Ashoka Womens Engineering College"
a=str.lstrip()
print(a)

str="Ashoka Womens Engineering College   "
a=str.rstrip()
print(a)

str=["Ashoka","Womens","Engineering","College"]
print(str.index("College"))

str="AShokaa"
print(str.count("a"))

str="Ashoka"
length=len(str)
print(length)

str1="sree "
str2="kavya"
str=str1+str2
print(str)

str="AShokaa"
print(max(str))

str="AShokaa"
print(min(str))

str="Ashoka Womens Engineering College"
for ch in str:
    print(ch.isspace())

str="AShokaa"
print(str.find("a"))

str="AShokaa"
print(str.replace("AShokaa","kavya"))

str="kavya ashoka"
sub=str[6:]
print(sub)'''

#counting no.uppercase and lowercase:
'''str=input("enter a string")
upper_count=0
lower_count=0
for ch in str:
    if(ch.isupper()):
        upper_count+=1
    else:
        lower_count+=1
print("uppercase:",upper_count)
print("lowercase:",lower_count)'''

#counting no.vowels and consonents:
'''str=input("enter your string")
vowels_count=0
consonents_count=0
for ch in str:
    if(ch=="A" or ch=="E" or ch=="I" or ch=="O" or ch=="U" or ch=="a" or ch=="e" or ch=="i" or ch=="o" or ch=="u"):
        vowels_count+=1
    else:
        consonents_count+=1
print("vowels:" ,vowels_count)
print("consonents:", consonents_count)'''

#palindrome
'''str=input("enter a string")
palindrome=(str[::-1])
if(palindrome==str):
    print(palindrome," is palindrome")
else:
    print(palindrome,"not a palindrome")'''

#sum of digit in letter
'''s=input("enter a string with number")
sum=0
for i in s:
    if(i.isdigit()==True):
        sum=sum+int(i)
print("sum of digit is",sum)'''


#list:
'''list=[10,20,30,18,14,17,80,100,19]
print(list)
list.sort()
print(list)

list=[10,20,30,18,14,17,80,100,19]
print(list)
list.sort(reverse=True)#TO PRINT DESENDING ORDER
print(list)

list=[10,20,30,18,14,17,80,100,19]
print(list)
list.insert(2,15)
print(list)

list=[10,20,30,18,14,17,80,100,19]
print(list)
list.append(200)
print(list)

list=[10,20,30,18,14,17,80,100,19]
print(list)
list.pop()
print(list)

list=[10,20,30,18,14,17,80,100,19]
print(list)
list.remove(100)
print(list)

list=[10,20,30,18,14,17,80,100,19]
print(list)
minimum=min(list)
print(minimum)

list=[10,20,30,18,14,17,80,100,19]
print(list)
maximum=max(list)
print(maximum)

list=[10,20,30,18,14,17,80,100,19]
print(list)
length=len(list)
print(length)

list=[10,20,30,18,14,17,80,100,19]
print(list)
i=list.index(18)
print("index of 18",i)

list=[10,100,20,30,18,14,17,100,80,100,19]
print(list)
c=list.count(100)
print("count of 100 is:",c)

list=[10,20,30,18,14,17,80,100,19]
print(list)
list.clear()
print(list)'''

#TAKING A LIST OF ELEMENT FROM THE USER AS INPUT:
'''list1=list(map(int,input().split()))
print(list1)'''

#TAKING A LIST OF ELEMENT IN PARTICULAR OR FIXED SIZE:
'''n=int(input("enter list size"))
list=[]
for i in range(1,n+1):
    list.append(input())
print(list)'''
 
#TUPLE

'''tuple1=(10,20,30,18,14,17,80,100,19)
print(tuple1)
minimum=min(tuple1)
print(minimum)

tuple1=(10,20,30,18,14,17,80,100,19)
print(tuple1)
maximum=max(tuple1)
print(maximum)


tuple1=(10,20,30,18,14,17,80,100,19)
print(tuple1)
i=tuple1.index(18)
print("index of 18",i)

tuple1=(10,20,30,18,14,17,80,100,19)
print(tuple1)
i=tuple1.count(18)
print(i)

tuple1=(10,20,30,18,14,17,80,100,19)
print(tuple1)
length=len(tuple1)
print(length)
   
tuple1=(10,20,30,18,14,17,80,100,19)
print(tuple1)
s=sorted(tuple1)
print(s)'''

#TAKING A TUPLE OF ELEMENT FROM THE USER AS INPUT:
'''tuple1=tuple(map(int,input().split()))
print(tuple1)'''

#TAKING A tuple OF ELEMENT IN PARTICULAR OR FIXED SIZE:
'''n=int(input("enter list size"))
tuple=[]
for i in range(1,n+1):
    tuple1.append(input())
print(tuple(tuple1))'''

#longest word in the list
'''n=int(input("enter list size"))
heros=[]
for i in range(1,n+1):
      heros.append(input())
for hero in heros:
    longest=heros[0]
for hero in heros:
    if(len(hero)>len(longest)):
        longest=hero
print("longest hero is",longest)'''
          
#all zeros print at right side of the list

'''list1=list(map(int,input().split()))
zeros_count=0
list2=[]
for num in list1:
    if(num==0):
        zeros_count+=1
    else:
        list2.append(num)
result=list2+[0]*zeros_count
print(result)'''

#print second largest and second largest:
'''list1=list(map(int,input().split()))
list1.sort()
print(sort[-2])
list1.sort(reverse=True)
print(list1[-2])'''

#list comprehenssion
'''n=int(input("enter a number"))
squares=[x**2 for x in range(1,n+1)]
print(squares)'''

#SETS:
'''set1={1,2,3,4,5,6,'kavya','sree'}
print(set1)
set1.add('sri')
print(set1)

set1={1,2,3,4,5,6,'kavya','sree','sri'}
print(set1)
set1.remove('sri')
print(set1)

set1={1,2,3,4,5,6,'kavya','sree'}
print(set1)
set1.clear()
print(set1)

set1={1,2,3,4,5,6,'kavya','sree'}
print(set1)
set1.discard('sri')
print(set1)

set1={1,2,3,4,5,6,'kavya','sree'}
set2={8,9,10,4,5,6,'kavya'}
set3=set1.union(set2)   #set2=set2.union(set2)
print(set3)               print(set2)

set1={1,2,3,4,5,6,'kavya','sree'}
set2={7,8,9,10,'sri'}
set1.update(set2)
print(set1)

set1={1,2,3,4,5,6,'kavya','sree'}
print(set1)
set2=set1.copy()
print(set2)

set1={1,2,3,4,5,6,'kavya','sree'}
set2={8,9,10,4,5,6,'kavya'}
set3=set1.intersection(set2)
print(set3)

set1={1,2,3,4,5,6,'kavya','sree'}
set2={8,9,10,4,5,6,'kavya'}
set3=set1.difference(set2) #set1 lo vundi set2 lo lenivi printing
print(set3)

set1={1,2,3,4,5,6,'kavya','sree'}
set2={8,9,10,4,5,6,'kavya'}
set3=set1.symmetric_difference(set2) #it print which are not common in 2 sets
print(set3)

set1={1,2,3,4,5,6,'kavya','sree'}
set2={'kavya'} #it check set2 is subset of set1,return true or false
print(set2.issubset(set1))

set1={1,2,3,4,5,6,'kavya','sree'}
set2={'kavya'} 
print(set1.issuperset(set2))

set1={1,2,3,4,5,6,'kavya','sree'}
set2={'kavya'} 
print(set1.isdisjoint(set2))'''#in this disjoint both set elements should be different

#TAKING USER INPUT SET OF ELEMENTS
'''set1=set(map(int,input().split()))
print(set1)

#TAKING USER ELEMENTS FIXED SIZE AND DIFFERENT DATA ELEMENTS:
n=int(input("enter size of set"))
set1=set()
for i in range(1,n+1):
    element=(input("enter set elements"))
    set1.add(element)
print(set1)'''



#DICTIONARIES
'''student={
    'name':'kavya',
    'roll no':'b8',
    'class':3
    }
print(student)

student=dict({'name':'kavya','roll no':'b8'}) #using dict funtion to store elemnts in dictionary,it can use or not use (optional)
print(student)'''

#operations of dictionaries: get, get_keys, get_values, get_items, update, pop 
'''student={
    'name':'kavya',
    'roll no':'b8',
    'class':3
    }
print(student.get('name'))


student={
    'name':'kavya',
    'roll no':'b8',
    'class':3
    }
print(student.keys())                

                 
student={
    'name':'kavya',
    'roll no':'b8',
    'class':3
    }
print(student.values()) 


student={
    'name':'kavya',
    'roll no':'b8',
    'class':3
    }
print(student.items())


student={
    'name':'kavya',
    'roll no':'b8',
    'class':3
    }
student.update({'name':'sree'})
print(student)


student={
    'name':'kavya',
    'roll no':'b8',
    'class':3
    }
student.pop('name')
print(student)'''

#TAKING USER INPUT DICTIONARY OF ELEMENTS:
'''n=int(input("enter dictionary size"))
my_dict=dict({})
for i in range(1,n+1):
    keys=input("enter key")
    values=input("enter values")
    my_dict[keys]=values
print("final dictionary:",my_dict)'''

#number with square:
'''n1=int(input("enter a n1:"))#lower range
n2=int(input("enter a n2:"))#upper range
squares=[(x,x**2) for x in range(n1,n2+1)]
print(squares)'''

#the product of the numbers:
'''n=list(map(int,input().split()))
product=1
for i in n:
    product=product*i
print(tuple(n))
print(product)'''

#FUNCTION
'''def greet():  #simple function
    print("hi kavya")
    print("gd mrg")
greet()

def add(a,b): #adding with function
    c=a+b
    print(c)
add(10,20)'''

#functin with types of arguments:  #positional arg...
'''def perfect(num): 
    sum=0
    for i in range(1,num):
        if(num%i==0):
            sum+=i
    if(sum==num):
        print(num,"perfect number")
    else:
        print(num,"not perfect number")
    num=int(input("enter a number"))
perfect(28)

def armstrong(num):
    length=len(str(num))
    x=num
    sum=0
    while(x>0):
        digit=x%10
        sum+=digit**length
        x//=10
    if(sum==num):
        print(num,"armstrong number")
    else:
        print(num,"not a armstrong number")
armstrong(153)

def harshad(num):
    x=num
    sum=0
    while(x>0):
        remainder=x%10
        sum=sum+remainder
        x//=10
    if(num%sum==0):
        print(num,"harshad num")
    else:
        print(num,"not harshad num")
num=int(input("enter a number"))
harshad(num)


def palindrome(num):
    x=num
    rev=0
    while(num>0):
        r=num%10
        rev=(rev*10)+r
        num//=10
    if(x==rev):
        print(x,"palinrome")
    else:
        print(x,"not palindrome")
palindrome(128)

def strong_num(n):
    temp=n
    sum=0
    while(n>0):
        digit=n%10
        fact=1
        for i in range(1,digit+1):
            fact=fact*i
        sum=sum+fact
        n=n//10
    if(sum==temp):
        print(temp,"is strong number")
    else:
        print(temp,"is not strong number")
strong_num(146)'''

#DEFAULT ARGUMENTS
'''def perfect(num=28): 
    sum=0
    for i in range(1,num):
        if(num%i==0):
            sum+=i
    if(sum==num):
        print(num,"perfect number")
    else:
        print(num,"not perfect number")
perfect()

def armstrong(num=153):
    length=len(str(num))
    x=num
    sum=0
    while(x>0):
        digit=x%10
        sum+=digit**length
        x//=10
    if(sum==num):
        print(num,"armstrong number")
    else:
        print(num,"not a armstrong number")
armstrong()

def harshad(num=121):
    x=num
    sum=0
    while(x>0):
        remainder=x%10
        sum=sum+remainder
        x//=10
    if(num%sum==0):
        print(num,"harshad num")
    else:
        print(num,"not harshad num")
harshad()


def palindrome(num=121):
    x=num
    rev=0
    while(num>0):
        r=num%10
        rev=(rev*10)+r
        num//=10
    if(x==rev):
        print(x,"palinrome")
    else:
        print(x,"not palindrome")
palindrome()

def strong_num(n=145):
    temp=n
    sum=0
    while(n>0):
        digit=n%10
        fact=1
        for i in range(1,digit+1):
            fact=fact*i
        sum=sum+fact
        n=n//10
    if(sum==temp):
        print(temp,"is strong number")
    else:
        print(temp,"is not strong number")
strong_num()'''

#LIST OF ARGUMENTS
'''def perfect(*numbers):
    for num in numbers:
        sum=0
        for i in range(1,num):
            if(num%i==0):
                sum+=i
        if(sum==num):
            print(num,"perfect number")
        else:
            print(num,"not perfect number")
perfect(28,30,38,)

def armstrong(*numbers):
    for num in numbers:
        length=len(str(num))
        x=num
        sum=0
        while(x>0):
            digit=x%10
            sum+=digit**length
            x//=10
        if(sum==num):
            print(num,"armstrong number")
        else:
            print(num,"not a armstrong number")
armstrong(153,143,123)

def harshad(*number):
    for num in number:
        x=num
        sum=0
        while(x>0):
            remainder=x%10
            sum=sum+remainder
            x//=10
        if(num%sum==0):
            print(num,"harshad num")
        else:
            print(num,"not harshad num")
harshad(18,20,19,8)


def palindrome(*number):
    for num in number:
        x=num
        rev=0
        while(num>0):
            r=num%10
            rev=(rev*10)+r
            num//=10
        if(x==rev):
            print(x,"palinrome")
        else:
            print(x,"not palindrome")
palindrome(121,131,151)

def strong_num(*number):
    for n in number:
        temp=n
        sum=0
        while(n>0):
            digit=n%10
            fact=1
            for i in range(1,digit+1):
                fact=fact*i
            sum=sum+fact
            n=n//10
        if(sum==temp):
            print(temp,"is strong number")
        else:
            print(temp,"is not strong number")
strong_num(145,156,178)'''

#KEYWORD ARGUMENTS:

'''def details(name,age,grade):
    print('my name is',name,'age is',age,'my grade is',grade)
details(age=19,name='kavya',grade='A')
details('kavya',19,'A')
details(19,'kavya','A')'''

#ARBITARY ARGUMENTS/DICTIONARY ARGUMENTS:

'''def details(**info):#this is used to when we dont know the no.of arguments to give
    print(info)
details(name='kavya',age=19,classs='3year')'''


#LAMBDA:it is anonymoues function 
'''numbers=list(map(int,input().split()))
squares=list(map(lambda x:x**2,numbers)) #map()
print(squares)

even_num=list(filter(lambda x:x%2==0,numbers)) #filter
print(even_num)'''

#RECURSION (factorial)
'''def factorial(n):
    if n==1:
        return 1
    return n*factorial(n-1)
print(factorial(5))'''

#OOPS CONCEPT:.........

'''class student:
    def __init__(self,name):#constructor
        self.name=name
    def greet(self):#instance method
        print("hello,i am",self.name)
#create objects
s1=student("kavya")
s1.greet()
s1=student("sree")
s1.greet()'''

        
'''class Car:
    def __init__(self,brand,color,cost,model):
        self.brand=brand
        self.color=color
        self.cost=cost
        self.model=model
    def show(self):
        print("brand:",self.brand,"color:",self.color,"cost:",self.cost,"model:",self.model)
car1=Car("kia","black",10000000,2022)
car2=Car("audi","blue",1000000000,2023)
car3=Car("rolls royale","gold",200000000,2024)
car4=Car("bmw","black",25000000000,2015)
car1.show()
car2.show()
car3.show()
car4.show()'''
    

#SINGLE INHERITENCE:
'''class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def info(self):
        print("name:",self.name,"age:",self.age)
class Teacher(person):
    def subject(self,sub):
        print(self.name,"teaches",sub)
t1=Teacher("mr sharkar yadav",27)
t1.info()
t1.subject("python")

t2=Teacher("mr ravi",27)
t2.info()
t2.subject("java")'''

#MULTIPLE INHERITENCE:
'''class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
        
    def info(self):
        print("name:",self.name,"age:",self.age)
        
class sports:
    def sport(self,game):
        print("plays",game)

class student(person,sports):
    def grade(self,g):
        print(self.name,"is in grade",g)

s1=student("saikumar",15)
s1.info()
s1.grade("10")
s1.sport("foot ball")'''

#MULTI LEVEL INHERITENCE
     
'''class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
        
    def info(self):
        print("name:",self.name,"age:",self.age)
        
class Teacher(person):
    def subject(self,sub):
        print(self.name,"teaches",sub)

class principal(Teacher):
    def manage_school(self):
        print("pincipal",self.name,"manages the school")

p1=principal("vardhan",50)
p1.info()
p1.subject("social")
p1.manage_school()'''


#HIERARCHICAL INHERITENCE:

'''class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def info(self):
        print("name: ",self.name,"age: ",self.age)

class Teacher(Person):
    def subject(self, sub):
        print(self.name,"teaches",sub)

class Student(Person):
    def grade(self,g):
        print(self.name,"is in grade",g)

t1=Teacher("Raju",35)
t1.info()
t1.subject("emglish")

s1= Student("aman",14)
s1.info()
s1.grade(8)'''


#HYBRID(multiple + multi level):

'''class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def info(self):
        print("name: ",self.name, "age: ",self.age)
        
class Sports:
    def sport(self,game):
        print("playes",game)

class Teacher(Person):
    def subject(self, sub):
        print(self.name,"teaches",sub)

class Student(Teacher,Sports):
    def grade(self,g):
        print(self.name,"goes to grade",g)

s1=Student("priya",29)
s1.info()
s1.subject("pysics")
s1.sport("basketball")
s1.grade(10)'''


'''class Dog:
    def speak(self):
        return "woof"
class Cat:
    def speak(self):
        return "meow"'''
#polymorphism in action
'''for animal in [Dog(), Cat()]:
    print(animal.speak())'''
      

      
