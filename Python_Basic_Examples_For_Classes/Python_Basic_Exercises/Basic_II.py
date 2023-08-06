'''
https://www.w3resource.com/python-exercises/basic/
'''

def Exercise_1():
    lista_num = [1,2,2,4,5,6]
    ant = lista_num[0]

    for x in lista_num[1:]:
        if(x==ant):
            print("IGUALES")
        ant = x

def Exercise_2():
    from random import shuffle
    lista_vo = ['a','e','i','o','u']
    shuffle(lista_vo)
    print(lista_vo)

def Exercise_3():
    Lista = [2,3,4,52,24,5,6,765,53,2,4,2,4,3,53,2,5]
    count = 2
    while (len(Lista)>0):
        print(Lista)
        Lista.pop(count)
        if(count+3<len(Lista)):
            count += 3
        else:
            count = count-len(Lista)
    
def Exercise_4():
    Lista = [2,42,1,35,6,3,14,6,-24,-12,4,-10]
    found = False
    for x in Lista:
        for y in Lista:
            for z in Lista:
                if x!=y and y!=z and x!=z and x+y+z==0:
                    print(f"Los valores son {x,y,z}")
                    found = True
    
    if found == False:
        print("There are no values which")

def Exercise_5():
    num1 = "2";num2 = "6";num3 = "8"
    Lista = []
    Lista.append(num1);Lista.append(num2);Lista.append(num3)
    for x in range(len(Lista)):
        for y in range(len(Lista)):
            for z in range(len(Lista)):
                if y != x and z!=x and z!=y:
                    print(int(Lista[x]+Lista[y]+Lista[z]))

def Exercise_6():
    pass

def Exercise_7():
    pass

def Exercise_8():
    pass

def Exercise_9():
    pass

def Exercise_10():
    pass


Exercise_5()