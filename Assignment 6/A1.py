for i in range(20):
    if i%2==0:
        print(i,"is even")
    else:
        print(i,"is odd")

year=int(input("enter a year: "))
if year%4==0:
    print(year,"is leep year")
else:
    print(year,"is not leep year")

(a,b,c)=map(int,input("enter angle of trangle:").split(' '))
if a+b+c==180:
    print("is a valid trangle")
else:
    print("is not  a valid trangle")  

a=int(input('enter the cost :'))
b=int(input('enter the selling prise :'))
if a<b:
    print("you have profite of ",b-a)
else:
    print("you have loss of ",a-b)


numb=int(input('enter your number :'))
temp=numb
total=0
while temp>0:
    i=temp%10
    total+=i**3
    temp //= 10
if total==numb:
    print(numb," is a armstrong number")
else:
    print(numb," is not a armstrong number")

i=int(input("enter a number :"))
if i<0:
    print("number is negative")
elif i>0:
    print("number is positive")
else:
    print("number is zero")


if int(input('enter your age:'))<18:
    print("you are not eligible")
else:
    print("yyou are eligible")


print(max(int(input("enter first number:")),int(input("enter second number:")),int(input("enter third number:"))),"is greater")

hight=float(input('enter your hight :'))
if hight>=165:
    print("Tall")
elif hight<150:
    print("dwarf")
else:
    print('avarage')

x=int(input('enter x:'))
y=int(input('enter y:'))

if x<0 and y<0:
    print('Q1')
elif x<0 and y>0:
     print('Q2')
elif x>0 and y>0:
     print('Q3')
elif x>0 and y<0:
     print('Q4')

s=input("enter ")
if s.isdigit():
    print('is digit')
else:
    print('is alphabate')
    print(s.upper())
    print(s.lower())

s=input("enter a character: ")
if s=="a" or s=="e" or s=="i" or s=="o" or s=="u":
    print("is vowel")
else :
    print("is constant")

mon=int(input("enter number of month :"))
numof=[31,28,31,30,31,30,31,31,30,31,30,31]
print(numof[mon-1]," daye's")


from cmath import pi
print("find area of-","square","rectangle","circle","trangle","exit",sep='\n')
while True:
 match input('enter name of sape :'):
    case "square":
        print(float(input("enter side -"))*4,)
    case "rectangle":
        print(float(input("enter hight  -"))*float(input("enter width - ")))
    case "trangle":
        print(0.5*(float(input("enter base -"))*float(input("enter hight -"))))
    case "circle":
        r=float(input("enter radius -"))
        print(pi*(r*r))
    case "exit":
        break
    case _:
        print("Enter valid number ")

name=input("enter your name:")
m=input("are you marred Y/N:")
print("miss"if m=='y' else "mrs",name,sep='.')
