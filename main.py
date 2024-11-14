from menu.principalMenu import desingMenuPrincipal
from menu.menuOptOne import desingMenuOptOne


print("Simulador de propinas")


while True:
    awnser = desingMenuPrincipal()
    if awnser == 1:
        desingMenuOptOne()
        
    if awnser == 2:
        print("ok")
        break
    
    if awnser == 3:
        print("ok")
        break
    
    