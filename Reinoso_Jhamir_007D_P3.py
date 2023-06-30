import Funciones as fn

while True:
    fn.mostrar_menu()
    opcion = fn.validar_opcion()
    if opcion ==1:
        fn.grabar()
    elif opcion==2:
        fn.buscar()
    elif opcion==3:
        pass
    else:
        print("Gracias por confiar en nosotros")
        break
