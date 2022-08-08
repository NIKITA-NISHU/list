# a=[50,40,23,70,56,12,5,10,7]
# count=0
# while a[count:]:
#     count=count+1
# print(count)


def n():
    n=[1,0,0,1,1,0,1,1]
    i=len(n)-1
    c=1
    decimal=1
    while i>=0:
    # c=c/2
        decimal=decimal+n[i]/c
        c=c/2
        i-=1
    print(decimal)
    n()
    i-=1
n()
