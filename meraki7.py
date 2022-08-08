# number=[50,40,23,70,56,12,5,10,7]
# index=0
# min=number[0]
# while index<len(number):
#     if number[index] <min:
#         min=number[index]
#     index=index+1
# print(min)


# number=[50,40,23,70,56,12,5,10,7]
# index=0
# max=number[0]
# while index<len(number):
#     if number[index]>max:
#         max=number[index]
#     index=index+1
# print(max)



n=[50,40,23,70,56,12,5,10,7]
index=0
second_max=n[0]
while index<len(n):
    if n[index]>second_max:
        second_max=second_max[index]
    index=index+1
print(second_max)
