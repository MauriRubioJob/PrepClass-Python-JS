'''
https://www.w3resource.com/python-exercises/python-basic-exercises.php
'''
def Exercise_1():
    print("Twinkle, twinkle, little star,\n\tHow I wonder what you are!\n\t\tUp above the world so high,\n\t\tLike a diamond in the sky.\nTwinkle, twinkle, little star,\n\tHow I wonder what you are")

def Exercise_2():
    from sys import version
    print(version)

def Exercise_3():
    # Display Date and Time
    import datetime
    now=datetime.datetime.now()
    print("Current Date and Time is :")
    print(now.strftime("%Y-%m-%d %H:%M:%S"))

def Exercise_4():
    from math import pi
    radius=float(input("Insert radius in cm of the circle : "))
    area=pi*radius**2
    print("The Area of the circle is: "+str(area))

def Exercise_5():
    nombre = input("Introduce tu nombre: ")
    apellido = input("Introduce tu apellido: ")
    print(f"{apellido} {nombre}")

def Exercise_6():
    # STRING METHOD SPLIT

    values = input("introduce numeros separados por comas: ")
    lista = values.split(",")
    tupla = tuple(lista)
    print(f"Mi lista es: {lista}")
    print(f"Mi tupla es: {tupla}")
    
def Exercise_7():
    filename = input("Insert the filename: ")
    file = filename.split(".")
    print(f"file extension is {file [1]}")

def Exercise_8():
    color_list = ["Red","Green","White" ,"Black"]
    print(f"first color is {color_list[0]} and last one is {color_list[-1]}")
    
def Exercise_9():
    exam_st_date = (11, 12, 2014)
    print(f"The exam is the {exam_st_date[0]}/{exam_st_date[1]}/{exam_st_date[2]}")

def Exercise_10():
    n = input("Insert and n value: ")
    print(f"The result of the operation n+nn+nnn {int(n)+int(n+n)+int(n+n+n)}")

def Exercise_11():
    # Write a Python program to print the documents (syntax, description etc.) of Python built-in function(s). 
    print(abs.__doc__)

def Exercise_12():
    # Write a Python program to print the calendar of a given month and year.
    import calendar
    print(calendar.month(2020,8))

def Exercise_13():
    print('''a string that you "don't" have to escape
    This
    is a ....... multi-line
    heredoc string --------> example''')
    
def Exercise_14():
    from datetime import date
    date1 = date(2014,7,2)
    date2 = date(2013,8,5)
    days = date1-date2
    print(days)

def Exercise_15():
    # Sphere volume
    from math import pi
    Radius = 6
    Volume = (4/3)*pi*Radius**3
    print(f"El volumen de una esfera de radio 6 es: {Volume}")

def Exercise_16():
    given_num = int(input("Introduce your number: "))
    if(given_num>17):
        print(f"Difference is: {abs(17-given_num)*2}")
    else:
        print(f"Difference is: {(17-given_num)}")

def Exercise_17():
    # using operators to check something
    number = int(input("Introduce the number you'd like to be checked: "))
    print(abs(1000-number)<=1000 or abs(2000-number)<=2000)

def Exercise_18():
    number1 = int(input("Introduce el primer número: "))
    number2 = int(input("Introduce el segundo número: "))
    number3 = int(input("Introduce el tercer número: "))
    if(number1==number2 and number2==number3):
        print(f"Los 3 son iguales {number1**3}")
    else:
        print(f"La suma es: {number1+number2+number3}")

def Exercise_19():
    My_string = input("Introduce la string: ")
    if(My_string.startswith("Is")):
        print("Unchanged")
    else: 
        My_string = "Is "+My_string
        print(My_string)

def Exercise_20():
    n = 3
    My_string = "Hola"
    Result = ""
    for i in range(n):
        Result += My_string
    print(Result)

def Exercise_21():
    Given_num = int(input("Introduce el número: "))
    if(Given_num%2 == 0):
        print("It's even")
    else: 
        print("It's odd")

def Exercise_22():
    Lista = [2,3,5,6,4,43,45,632,2,4,4,5,2,34,4]
    Count = 0
    for x in Lista:
        if x == 4:
            Count += 1
    print(f"Number 4 is {Count} times in the List")

def Exercise_23():
    My_string = input("Introduce la string: ")
    if(len(My_string)<=2):
        print(My_string*2)
    else:
        print(My_string[0:2]*2)

def Exercise_24():
    letter = input("Introduce a letter: ")
    if letter in ('a','e','i','o','u'):
        print("It's a vowel")
    else:
        print("It's not a vowel")
def Exercise_25():
    values = input("Introduce values separated by commas: ")
    lista = values.split(",")
    if "3" in lista:
        print("True")
    else:
        print("False")
def Exercise_26():
    Lista = [2,3,4,2,5]
    for x in Lista:
        print("*"*x)
    
def Exercise_27():
    lista = ["a","b","ho","g"]
    s = ""
    for x in lista:
        s += x
    print(s)
def Exercise_28():
    numbers = [386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345, 
    399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217, 
    815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 742, 717, 
    958,743, 527
    ]
    lista_even = []
    for x in numbers:
        if x%2 == 0 and x<237:
            lista_even.append(x)
    print(lista_even)

def Exercise_29():
    color_list_1 = set(["White", "Black", "Red"])
    color_list_2 = set(["Red", "Green"])
    for x in color_list_1:
        if x not in color_list_2:
            print(x)

def Exercise_30():
    base = int(input("Introduce the base of the triangle: "))
    height = int(input("Introduce the height of the triangle: "))
    print(f"the area is {base*height/2}")

def Exercise_31():
    # obtener el máximo comun divisor
    def MCD(x,y):
        mcd = 1
        if x%y == 0:
            return y
        for i in range(int(y/2),0,-1):
            if x%i == 0 and y%i ==0:
                mcd = i
                return mcd
    
    print(MCD(9,18))

def Exercise_33():
    num1 = 3
    num2 = 2
    num3 = 24
    
    if(num1==num2 or num3==num2 or num1==num3):
        print("Result = 0")
    else:
        print(num1+num2+num3)
def Exercise_34():
    num1 = 5
    num2 = 10
    Result = num1+num2
    if(Result>=15 and Result<=20):
        print("Resultado es 20")
    else:
        print(Result)

def Exercise_35():
    num1 = 5
    num2 = 6
    print(num1 == num2 or num1+num2 == 5 or abs(num1-num2)==5)

def Exercise_36():
    obj1 = 2
    obj2 = 2
    if(type(obj1) == int and type(obj2) == int):
        print("The sum is", obj1+obj2)
    else:
        print("One or both of them are not integers")

def Exercise_37():
    print(f"name\nage\naddress")

def Exercise_38():
    x = 4
    y = 3
    print(f"{x}+{y}*({x}+{y}) = {(x + y) * (x + y)}")

def Exercise_39():
    amt = 10000
    inte = 3.5
    years = 7

    future_value  = amt*((1+(0.01*inte)) ** years)
    print(round(future_value,2))

def Exercise_40():
    from math import sqrt
    from math import pow
    p1 = (5,8)
    p2 = (17,20)
    distance = sqrt(pow(p2[0]-p1[0],2)+pow(p2[1]-p1[1],2))
    print(distance)

def Exercise_41():
    #  Write a Python program to check whether a file exists.
    import os.path
    open('abc.txt', 'w')
    print(os.path.isfile('abc.txt'))

def Exercise_42():
    #  Write a Python program to determine if a Python shell is executing in 32bit or 64bit mode on OS.
    import struct
    print(struct.calcsize("P")*8)

def Exercise_43():
    import platform
    import os
    print(os.name)
    print(platform.system())
    print(platform.release())

def Exercise_44():
    pass

def Exercise_45():
    pass

def Exercise_46():
    pass

def Exercise_47():
    pass

def Exercise_48():
    pass

def Exercise_49():
    pass

def Exercise_50():
    pass

    
Exercise_15()