def add_prod (inv):
    nom = input('Ingrese el nombre del producto que desea agregar: ').lower()
    
    for x in inv:
        if (x == nom):
            print (x)
            op = int(input('El producto se encuentra en la lista, desea actualizarlo? 1- Si  2- No \n Eleccion: '))
            if (op == 1):
                act = int(input('Ingrese la cantidad a la que desea cambiar el stock del producto: '))
                inv [x] = act
                break
            elif (op == 2):
                break
    else:
        cant = int(input('Ingrese la cantidad inicial del producto: '))
        inv [nom] = cant


def delete_prod (inv):
    nom = input('Ingrese el nombre del producto que desea eliminar: ')
    for x in inv:
        if nom == x:
            inv.pop(x)
            break

def show_inv (inv):
    print ('Marca   |   Stock')
    print (inv)

inv = {}
print ('Ingrese que tipo de accion desea realizar')
op = int(input('1- Agregar un producto \n 2- Eliminar un producto \n 3- Mostrar los productos y el stock \n 4- Salir \n Eleccion: '))
while (op != 4):
    if (op == 1):
        add_prod(inv)
    elif (op == 2):
        delete_prod(inv)
    elif (op == 3):
        show_inv(inv)
    print ('Ingrese que tipo de accion desea realizar')
    op = int(input(' 1 - Agregar un producto \n 2 - Eliminar un producto \n 3 - Mostrar los productos y el stock \n 4 - Salir \n Eleccion: '))

print ('Gracias por utilizar nuestros servicios :D')