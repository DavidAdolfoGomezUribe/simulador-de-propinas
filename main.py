from menu.principalMenu import desingMenuPrincipal
from menu.menuOptOne import desingMenuOptOne
from menu.menuOptTwo import desingMenuOptTwo
from menu.menuDataOne import desingDataOne
print("Simulador de propinas")


while True:
    awnser = desingMenuPrincipal()
    if awnser == 1:
        desingMenuOptOne()
        
    if awnser == 2:
        desingMenuOptTwo()
        
    if awnser == 3:
        desingDataOne()
        
    
    if awnser == 4:
        print("ok")
        break
     
    
    