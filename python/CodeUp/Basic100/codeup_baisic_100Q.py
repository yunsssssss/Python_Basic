#6001
print("Hello")
#6002
print("Hello World")
#6003
print("Hello\nWorld")
#6004
print("'Hello'")
#6005
print("\"Hello World\"")
#6006
print("\"!@#$%^&*()\'")
#6007
print("\"C:\Download\'hello'.py\"")
#6008
print("print(\"Hello\\nWorld\")")
#6009
a=input()
print(a)
#6010
a=int(input())
print(a)
#6011
f=float(input())
print(f)
#6012
a,b=map(int,input().split())
print(a);print(b)
"or"
a=int(input())
b=int(input())
print(a);print(b)
#6013
a,b=input().split()
print(b);print(a)
"or"
a=input()
b=input()
print(b);print(a)
#6014
f=input()
print(f);print(f);print(f)
#6015
a,b=map(int,input().split())
print(a);print(b)
#6016
m,n=input().split()
print(n,m)
#6017
a=input()
print(a,a,a,sep=" ")
#6018
a,b=input().split(":")
print(a,b,sep=":")
#6019
y,m,d=input().split(".")
print(d,m,y,sep="-")
#6020
a,b=input().split("-")
print(a,b,sep='')
#6021
a=input()
for i in a :
    print(i)
" or "
print(a[0]); print(a[1]);print(a[2]);print(a[3]);print(a[4])
#6022
a=input()
print(a[0:2],a[2:4],a[4:6])
#6023
h,m,s=input().split(':')
print(m)
#6024
a,b=input().split(' ')
c=a+b
print(c)
#6025
a,b=map(int,input().split())
print(a+b)
#6026
a=float(input())
b=float(input())
print(a+b)
#6027
a=int(input())
print('%x'%a)
#6028
a=int(input())
print('%X'%a)
#6029
a=input() #16진수 입력 받기
n=int(a,16) #16진수를 10진수로 변환
print('%o'%n) #10진수를 8진수로 변환
#6030
a=ord(input())
print(a)
#6031
a=int(input())
print(chr(a))
#6032
a=int(input())
print(-a)
#6033
i=ord(input())
print(chr(i+1))
#6034
a,b=map(int,input().split())
print(a-b)
#6035
a,b=map(float,input().split())
print(a*b)
#6036
a,b=input().split()
print(a*int(b))
#6037
n=int(input())
s=input()
print(n*s)
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
f1,f2=map(float,input().split())
a=f1/f2
print(format(a,".3f"))
"or"
print(round(a,3))
#6044
a,b=map(int,input().split())
print(a+b);print(a-b);print(a*b);print(a//b);print(a%b);print(round(a/b,2))
#6045
a,b,c=map(int,input().split())
s=a+b+c
m=(a+b+c)/3
print(a,format(b,".2f"),sep=' ')
#6046
a=int(input())
print(a*2)
#6047
a,b=map(int,input().split())
print(a*(2**b))
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
print(b>a)
#6051
a,b=map(int,input().split())
if a!=b:
	print("True")
else :
	print("False")
#6052
n=int(input())
if n==0 :
	print("False")
else :
	print("True")
#6053
n=int(input())
print(not bool(n))
#6054
a,b=map(int,input().split())
print(bool(a) and bool(b))
#6055
a,b=map(int,input().split())
print(bool(a) or bool(b))
#6056
a,b=map(int,input().split())
print(bool(a)!=bool(b))
#6057
a,b=map(int,input().split())
print(bool(a)==bool(b))
#6058
a,b=map(int,input().split())
print(not bool(a) and not bool(b))
#6059
a=int(input())
print(~a)
#6060
a,b=map(int,input().split())
print(a&b)
#6061
a,b=map(int,input().split())
print(a|b)
#6062
a,b=map(int,input().split())
print(a^b)
#6063
a,b=map(int,input().split())
print(a if (a>b) else b)
#6064
a,b,c=map(int,input().split())
d=a if a<b else b
e=d if d<c else c
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
#6067
a=int(input())
if a<0 :
    if a%2==0 :
        print("A")
    else :
        print("B")
else :
    if a%2==0:
        print("C")
    else :
        print("D")
#6068
s=int(input())
if 90<=s<=100 :
    print("A")
elif 70<=s<=89 :
    print("B")
elif 40<=s<=69 :
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
n=1
while n!=0 :
    n=int(input())
    if n!=0 :
        print(n)
"or"
while True :
    a=int(input())
    if a==0 :
        break
    else :
        print(a)
#6072
n=5
while n!=0 :
    print(n)
    n=n-1
    if n==5 :
        break
"or"
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
    if a==0:
        break
#6074
c=ord(input())
t=ord('a')
while t<=c :
    print(chr(t),end=' ')
    t+=1
#6075
a=int(input())
s=0
while True :
    print(s,end=' ')
    if s==a :
        break
    s+=1
"or"
a=int(input())
i=0
while i<=a :
    print(i)
    i+=1
#6076
n=int(input())
for i in range(n+1) :
    print(i)
#6077
a=int(input())
s=0
for i in range(1,a+1):
    if i%2==0 :
        s+=i
    else:
        continue
print(s)
#6078
while True :
    n=input()
    print(n)
    if n=='q' :
        break
#6079
n=int(input())
s=0
t=0
while s<n :
    t=t+1
    s=s+t
print(t)
#6080
n,m=map(int,input().split())
for i in range(1,n+1) :
    for j in range(1,m+1):
        print(i,j)
#6081
n=int(input(),16)
for i in range(1,16):
    print('%X*%X=%X'%(n,i,n*i))
#6082
a=int(input())
for i in range(1,a+1) :
    if (i%10==3 or i%10==6 or i%10==9):
        print('X',end=' ')
    else :
        print(i,end=' ')
#6083
r,g,b=map(int,input().split())
count=0
for i in range(r):
    for j in range(g):
        for k in range(b):
            print('%d %d %d'%(i,j,k))
print(r*g*b)
#6084
h,b,c,s=map(int,input().split())
t=h*b*c*s
tbite=t/8
tkb=tbite/1024
tmb=tkb/1024
print("%0.1f MB" % tmb) #소수점 첫째자리까지 출력:0.1
#6085
w,h,b=map(int,input().split())
t=w*h*b
tbite=t/8
tkb=tbite/1024
tmb=tkb/1024
print("%0.2f MB" % tmb) #소수점 둘째자리까지 출력:0.2
#6086
a=int(input())
s=0
c=0
while True :
    s+=c
    c+=1
    if s>=a :
        break
print(s)
#6087
a=int(input())
for i in range(1,a+1) :
    if i%3==0 :
        continue
    print(i, end=' ')
#6088
a, d, n = map(int, input().split())
for i in range(2, n + 1):
    a += d
print(a)
#6089
a,r,n=map(int,input().split())

for i in range(1,n) :
    a=a*r
print(a)
#6090
a,m,d,n=map(int,input().split())
for i in range(1,n) :
    a=a*m+d
print(a)
#6091
a,b,c=map(int,input().split())
d=1
while d%a!=0 or d%b!=0 or d%c!=0 :
    d+=1
print(d)
#6092
n=출석 번호를 부른 횟수
a=무작위로 부른 n개의 번호
n=int(input())
a=input().split()

for i in range(n):
    a[i]=int(a[i])

d=[]
for i in range(24):
    d.append(0)

for i in range(n):
    d[a[i]]+=1

for i in range(1,24):
    print(d[i],end=' ')
#6093
n=int(input())
k=input().split()
k.reverse()

for i in range(n):
    k[i]=int(k[i])

for i in range(0,n):
    print(k[i],end=' ')
#6094
n=int(input())
k=map(int,input().split())
a=min(k)
print(a)

