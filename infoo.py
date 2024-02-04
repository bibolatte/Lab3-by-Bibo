# def sum_range(a,b):
#     cnt = 0
#     if a>b:
#         for i in range(b,a+1):
#             cnt=cnt +i
#     else:
#         for i in range(a, b+1):
#             cnt = cnt +i
#     return cnt
# print(sum_range(3,4))            

# def func(a):
#     for i in range(0,len(a)):
#         if a[i] == 0 and  a[i+1]==0:
#             return "bar"
#     return "zhok"
# a =[1,3,4,6,0,2,0,0]
# print(func(a))        


# def ailar(a):
#     if a==12 or a==1 or a==2:
#         print("kys")
#     elif a==3 or a==4 or a==5:
#         print("koktem")
#     elif a==6 or a==7 or a==8:
#         print("zhaz")
#     elif a==9 or a==10 or a==11:
#         print("kuz")

# ailar(9)        

# def ks(a):
#     for i in range(0, len(a)):
#         if a[i]==0:
#             a[i]=a[i-1]+ a[i-2]
#     print(a)
# a=[2,4,0,5,4,8]      
# ks(a)      

# def prime_number(a):
#     for i in range(2,a):
#         if a % i ==0:
#             return "kurama"
#     return "zhai"

# print(prime_number(7))

# def bl(a,b,c):
#     if c=="+":
#         print(a+b)
#     elif c=="-":
#         print(a-b)
#     elif c=="*":
#         print(a*b)
#     elif c=="/":
#         print((a)/(b))

# bl(3,5,"*")   




