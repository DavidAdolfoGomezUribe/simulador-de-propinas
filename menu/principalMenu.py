import time


def desingMenuPrincipal():
    while True:
        print(f"""          
                   )
                      (
                         )
                 ,.----------.
                ((|          |
               .--\          /--.
              '._  '========'  _.' 
                 ``````````````
    =============================================
                SIMULADOR DE PROPINA
    =============================================
    1. Calcular propina y total a pagar
    2. Calcular total a pagar divido entre varias personas
    3. Acceder al registro de datos
    4. Salir
    =============================================    
    """)
        try:
            options = int(input("    Por favor, elige una opción (1-4): " ))
            return options
        
        except ValueError:
            print("\n    Porfavor entre un valor correcto para las opciones\n")
            time.sleep(1)
        
