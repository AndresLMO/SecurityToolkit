from PortScanner import PortScanner


salir= False
while salir==False:
    try:
        menu=input("\n**********MENU DE SISTEMA**********"+
                   "\n\n1. Escaneo de Puertos"+
                   "\n7. Salir"+
                   "\n\nIngrese la opcion que desea realizar: "
                   )
        
        
        
        
        if menu=="1":
            
#****************************************************MODULO PROFESORES***********************************************************************************

            newPortScanner=PortScanner()
            ip=input("Ingrese la IP que desea analizar: ")
            ports = [22, 80, 443, 3389, 8080]
            newPortScanner.scan(ip,ports)
                
                
                
        elif menu =="7":
            salir= True
            print("Saliendo del sistema")
            
        else:
            print("\nHa ocurrido un error. Intente de nuevo.")
    except:
        print("Ha ocurrido un error. Intente de nuevo.")
            
              
