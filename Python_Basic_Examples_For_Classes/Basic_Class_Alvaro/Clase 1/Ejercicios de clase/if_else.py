edad = 18
edad_2 = 25

if edad == edad_2:
    print('Son diferentes')
    print('Si son diferentes')
    print(edad)
    print(edad_2)
elif edad_2 > edad:
    print('entre en el elif')
else:
    print('entre en el else')
print('Hola')


print('#########################')
nombre_1 = 'juan'
nombre_2 = 'pedro'
edad_1 = 20
edad_2 = 30
sueldo_1 = 1800
sueldo_2 = 1800

if nombre_1 != nombre_2:
    print('No se llaman igual')

if edad_1 >= edad_2:
    if edad_1 == edad_2:
        print('Tiene la misma edad')
    elif edad_1 > edad_2:
        print(f'{edad_1} es mayor')

if sueldo_1 - sueldo_1 * 0.19 < sueldo_2 - sueldo_2 * 0.15:
    print(f'{sueldo_2 - sueldo_2 * 1.15} es mayor')