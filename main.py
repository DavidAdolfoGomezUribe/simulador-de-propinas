from menu.principalMenu import desingMenuPrincipal
from menu.menuOptOne import desingMenuOptOne
from menu.menuOptTwo import desingMenuOptTwo
from menu.menuDataOne import desingDataOne

import time
print("Simulador de propinas")


while True:
    try:
        awnser = desingMenuPrincipal()
        
        if awnser == 1:
            desingMenuOptOne()
            
        elif awnser == 2:
            desingMenuOptTwo()
            
        elif awnser == 3:
            desingDataOne()
            
        
        elif awnser == 4:
            print("")
            break
        else :
            print("\n    No es un numero valido\n")
            time.sleep(1) 
        
    except ValueError:
        print("")
    except KeyboardInterrupt:
        time.sleep(1) 
        print("\n    Ctrl + c detectado , ingrese los datos correctos\n")