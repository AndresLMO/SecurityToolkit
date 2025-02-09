import PortScanner


salir= False
while salir==False:
    try:
        menu=input("\n**********MENU DE SISTEMA**********"+
                   "\n\n1. Modulo de Profesores"+
                   "\n2. Modulo de Estudiantes"+
                   "\n3. Modulo de Cursos"+
                   "\n4. Modulo de grupos"+
                   "\n5. Modulo clases"+
                   "\n6. Modulo inscripcion a Grupos"+
                   "\n7. Salir"+
                   "\n\nIngrese la opcion que desea realizar: "
                   )
        
        
        
        
        if menu=="1":
            
#****************************************************MODULO PROFESORES***********************************************************************************

            newPortScanner=PortScanner()
            soli=input("Ingrese la IP que desea analizar: ")
                
                
                
        elif menu =="7":
            salir= True
            print("Saliendo del sistema")
            
        else:
            print("\nHa ocurrido un error. Intente de nuevo.")
    except:
        print("Ha ocurrido un error. Intente de nuevo.")
            
              
