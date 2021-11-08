print("Hello")
print("World")
print("Hello world")
print("'Hello'")
print('"Hello World"')
print("\"!@#$%^&*()\'")
print("\"C:\Download\\'hello'.py\"")
print("Hello|n|World")
print("Hello\\nWorld") #6008
a=input()
print(a)
#a,b=map(int,input().split()) 에서 map의 활용
##############################################################################
#6020
a,b=input().split("-")
print(a+b)
#6021
s=input()
for i in s :
    print(i)
#6022
a=input()
print(a[0:2],a[2:4],a[4:6])
#6023
a,b,c=input().split(":")
print(b)
#6024
a,b=input().split()
print(a+b)
#6025
a,b=map(int,input().split())
print(a+b) #just a+b는 웨 오류뜨는걸까요 ..?
#6026
a=input()
b=input()
a=float(a)
b=float(b)
c=a+b
print(c)  #더 짧은 풀이는 없는것인가,,,,
#6032
a=int(input())
print(-a)
#6033
n=ord(input())
print(chr(n+1))
#6034
a,b=map(int,input().split())
c=a-b
print(c)
#6035
a,b=map(float,input().split())
c=a*b
print(c)
#6036
w,n=input().split()
print(w*int(n))
#6037
w=input()
s=input()
print(int(w)*s)
#6038
a,b=map(int,input().split())
print(a**b)
#6039
f1,f2=map(float,input().split())
print(f1**f2)
#6040
a,b=map(int,input().split())
print(a//b)
#6041
a,b=map(int,input().split())
print(a%b)
#6042
a=float(input())
print(format(a,".2f"))
#6043
a,b=map(float,input().split())
c=a/b
print(format(c,".3f"))
#6044
a,b=map(int,input().split())
print(a+b)
print(a-b)
print(a*b)
print(a//b)
print(a%b)
print(format((a/b),".2f"))
#6045
a,b,c=map(int,input().split())
print(a+b+c)
print(format(((a+b+c)/3),".2f"))
#6046
a=int(input())
print(a<<1)
#예시_비트 시프트 연산 표현 e.g) n = 10
#print(n<<1)  #10을 2배 한 값인 20 이 출력된다.
#print(n>>1)  #10을 반으로 나눈 값인 5 가 출력된다.
#print(n<<2)  #10을 4배 한 값인 40 이 출력된다.
#print(n>>2)  #10을 반으로 나눈 후 다시 반으로 나눈 값인 2 가 출력된다.
#6047
#6048
a,b=map(int,input().split())
if a<b :
    print("True")
else :
    print("False")
#6049
a,b=map(int,input().split())
if a==b :
    print("True")
else :
    print("False")
#6050
a,b=map(int,input().split())
if a<=b :
    print("True")
else :
    print("False")
#6051
a,b=map(int,input().split())
if a != b :
    print("True")
else :
    print("False")
#6052
a=int(input())
print(bool(a))
#6053
a=bool(int(input()))
print(not a)
#6054
a,b=map(int,input().split())
print(bool(a) and bool(b))
#6055
a,b=map(int,input().split())
print(bool(a) or bool(b))
#6056
#6057
a,b=map(int,input().split())
print((bool(a) and bool(b)) or (not bool(a) and not bool(b)))
#6058
a,b=map(int,input().split())
print(not bool(a) and not bool(b))
#6063
a,b=map(int,input().split())
if a>b :
    print(a)
else :
    print(b)
#6064
a,b,c=map(int,input().split())
d= a if a<b else b
e= d if d<c else c
print(e)
#6065
a,b,c=map(int,input().split())
if a%2==0 :
    print(a)
if b%2==0 :
    print(b)
if c%2==0 :
    print(c)
#6066
a, b, c = map(int, input().split())
if a % 2 == 0:
    print("even")
else:
    print("odd")

if b % 2 == 0:
    print("even")
else:
    print("odd")

if c % 2 == 0:
    print("even")
else:
    print("odd")
#6067_내풀이
a=int(input())
if a<0 and a%2==0 :
    print("A")
elif a<0 and a%2!=0 :
    print("B")
elif a>0 and a%2==0 :
    print("C")
else :
    print("D")
#6067_모범답안
a=int(input())
if a<0 :
    if a%2==0 :
        print("A")
    else :
        print("B")
else :
    if a%2==0 :
        print("C")
    else :
        print("D")
#6068
a=int(input())
if a>=90 :
    print("A")
elif 90>a>=70 :
    print("B")
elif 70>a>=40:
    print("C")
else :
    print("D")
#6069
s=input()
if s=="A" :
    print("best!!!")
elif s=="B" :
    print("good!!")
elif s=="C" :
    print("run!")
elif s=="D" :
    print("slowly~")
else :
    print("what?")
#6070
m=int(input())
if (m==12 or m==1 or m==2) :
    print("winter")
elif (m==3 or m==4 or m==5):
    print("spring")
elif (m==6 or m==7 or m==8):
    print("summer")
else :
    print("fall")
#6071
while True :
    a=int(input())
    if a==0 :
        break
    print(a)
#6072
a=int(input())
while True :
    print(a)
    a=a-1
    if a==0 :
        break
#6073
a=int(input())
while True :
    a=a-1
    print(a)
    if a==0 :
        break
#6074
a=input()
start=ord('a')
while True :
    print(chr(start), end=' ')
    if chr(start)==a :
        break
    start+=1
#6075
a=int(input())
s=0
while True :
    print(s,end=' ')
    if s==a :
        break
    s+=1
#6076
a=int(input())
for i in range(a+1):
    print(i)
#6077

