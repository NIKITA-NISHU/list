print(''' 1) Square 2) Triangle 3) circle 4) Rectangle 5) Right Triangle 6) trapezoid 7) parallelogram 8) Arc 9)Cube 10) Cuboid 11. Cylinder 12. Cone 13. Sphere 14.Trapezium ''') 
shape= input('enter your choise :') 
if shape == '1': 
    a = int(input('\t enter the length of the square value of the A =:')) 
    print(''' 1) area 2) perimeter 3) Diagonal 4) Side''') 
    choise = input('\t enter your choise :') 
    d=a*0.5*2 
    if choise =='1': 
        res=a*2 
    elif choise == '2': 
        res=4*a 
    elif choise =='3': 
        res=d 
    elif choise =='4': 
        res=d/2*0.5*2 
    else: res = 'you enter something wrong :' 
elif shape == '2': 
    print(''' 1) area 2) perimeter ''') 
    choise = input('\t enter your choise :') 
    h = int(input('\t enter the hight of the Triangle value of the H =:')) 
    b = int(input('\t enter the base of the Triangle value of the B =:')) 
    c=int(input('\t enter the base of the Triangle value of the C =:')) 
    if choise== '1': 
        res =0.5*h*b 
    elif choise=='2': 
        res=h+b+c 
    else: res='you enter something wrong :' 
elif shape =='3': 
    print(''' 1) area 2) Circumference 3) diameter ''') 
    choise = input('\t enter your choise :') 
    if choise == '1': 
        PI = 3.14 
        r = float(input("Enter the radius of a circle:")) 
        area = PI * r * r 
        res='Area of a circle = ' ,area 
    elif choise =='2': 
        r = float(input('Enter Radius of Circle: ')) 
        c = 3.14*r*r 
        res = 'Circumference = ', c 
    elif choise =='3': 
        PI = 3.14 
        radius = float(input(' Please Enter the radius of a circle: ')) 
        res =" \nDiameter Of a Circle = ", 2 * radius 
    else: res ='you enter something wrong :' 
elif shape =='4': 
    print(''' 1) Perimeter 2) Area 3) Diagonal ''') 
    choise =input('\t enter your choise :') 
    l= int(input("enter the 'l' = length of a rectangle :")) 
    w= int(input("enter the 'w' = width of a rectangle :")) 
    if choise == '1': 
        res ='Perimeter', 2(l + w) 
    elif choise == '2': 
        res ='Area', l*w 
    elif choise == '3': 
        res='Diagonal',0.5*(l*2+w*2) 
    else: 
        res='you enter something wrong :' 
elif shape =='5': 
    a=int(input('altitude of a Right triangle :')) 
    b = int(input('base of a Right triangle :')) 
    c=int(input('hypotenuse of a triangle :')) 
    print(''' 1) Perimeter 2) Area ''') 
    choise = input('enter your choise :') 
    if choise == '1': 
        res=(a + b )+ 0.5*(a*2+b*2) 
    elif choise == '2': 
        res= 1/2*a*b 
    else: 
        res='you enter something wrong :'