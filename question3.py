
# a=int(input("enter the number="))

# index=1
# while index<=a:
#     c=[]
#     if index%2==0:
#         print(index,"odd")
#     else:
#         print(index,"even")
#     index=index+1
#     c.append(a)
# print(a)

# b=int(input('enter the number='))
c=[]
a=0
while a<=10:
    b=int(input('enter the number='))
    if a%2==0:
        print("odd") 
        a+=1
        # c.append(a)
    else:
        print("even")
        c.append(a)
        # a+=1
    print(c)