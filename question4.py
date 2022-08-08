# a=[4,5,6,[2,3,4],4,2,3]
a=['12','23','34']
i=0
sum=0
while i<len(a):
    # if type (a[i])==list:
        j=0
        while j<len(a[i]):
            sum=sum+int(a[i][j])
            j+=1
        # i+=1
        print(sum)
        i+=1
#     else:
#         sum=sum+int(a[i])
#     i+=1
# print(sum)