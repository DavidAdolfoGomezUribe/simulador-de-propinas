import time
import requests
import pandas as pd

import json

def desingDataOne():
    
        while True:
            print(f"""  
                    
                ▐▓█▀▀▀▀▀▀▀▀▀█▓▌░█▄▄▄█░
                ▐▓█░░░░░░░░░█▓▌░█▄▄▄█░
                ▐▓█░░░░░░░░░█▓▌░█▄▄▄█░
                ▐▓█▄▄▄▄▄▄▄▄▄█▓▌░█████░
                ░░░░▄▄███▄▄░░░░░█████░
    =============================================
                Bases De Datos
    =============================================
    1. Base de datos Propina Normal
    2. Base de datos Propina Dividida
    3. Regresar al menu anterior
    =============================================    """)
            try:
                options = int(input("    Por favor, elige una opción (1-3): " ))
                
                
                #listar, actualizar , buscar por id ,eliminar 
                
                
                if options == 1:
                    while True:                 
                        try:
                            print(f"""  
    =============================================
            Bases De Datos Propina Normal
    =============================================
    1. Listar datos
    2. Actualizar datos
    3. Bucar por id (Numero de factura)
    4. Eliminar
    5. Regresar al menu anterior                             
    =============================================    """)
                            awnser = int(input("    Por favor, elige una opción (1-5): " ))
                            print("")

                            if awnser <=0 :
                                print("        Numeros negativos no son validos")
                                raise ValueError

                            if awnser == 1:
                                url =  f'https://6734e08c5995834c8a9133af.mockapi.io/propina/'
                                response = requests.get(url)
                                data = response.json()
                                df = pd.DataFrame(data)
                                
                                                
                                print(f"    \n{df}\n")

                        
                            if awnser == 2:
                                while True:
                                    manual_id = int(input("    Coloque el id (numero de factura) que desee editar: "))
                                    
                                    url =  f'https://6734e08c5995834c8a9133af.mockapi.io/propina/{manual_id}'
                                    response = requests.get(url)
                                    data= response.json()
                                    df = pd.DataFrame([data])

                                    print(f"    \n{df}\n")

                                    variable = int(input(f"""    Este es el dato que quieres editar? 
        1) si 2) no    """))
                                    if variable == 1:
                                        total = int(input("    Total :"))
                                        porcentaje = int(input("    Porcentaje :"))
                                        propina = int(input("    Propina :"))
                                        total_con_propina = int(input("    Total mas propina :"))
                                                    

                                        headers = {"Content-Type": "application/json"}
                                        data ={
                                            
                                            "monto": total,
                                            "porcentaje" : porcentaje,
                                            "propina" : propina ,
                                            "totalMasPropina" : total_con_propina

                                            }
                                        
                                        
                                        url =  f'https://6734e08c5995834c8a9133af.mockapi.io/propina/{manual_id}'
                                        

                                        response = requests.put(url , headers=headers,json=data)

                                        print("    Datos actualizados con exito")
                                        break
                                    else:
                                        pass


                            if awnser == 3:
                                while True:    
                                    manual_id = int(input("    Coloque el id (numero de factura) que desee consultar: "))
                                        
                                    url =  f'https://6734e08c5995834c8a9133af.mockapi.io/propina/{manual_id}'
                                    response = requests.get(url)
                                    data = response.json()
                                    df = pd.DataFrame([data])

                                    print(f"\n{df}\n")

                                    
                                    variable = int(input(f"""    Desea consultar otra factura? 
        1) si 2) no    """))
                                    if variable == 1:
                                        pass
                                    else:
                                        break
                            
                            if awnser == 4:
                                while True:
                                    manual_id = int(input("    Coloque el id (numero de factura) que desee eliminar: "))
                                    url =  f'https://6734e08c5995834c8a9133af.mockapi.io/propina/{manual_id}'
                                    
                                    response = requests.get(url)
                                    data = response.json()
                                    df = pd.DataFrame([data])

                                    print(f"\n{df}\n")

                                    
                                    variable = int(input(f"""    Desea eliminar esta factura? 
        1) si 2) no (1-2):   """))
                                    if variable == 1:
                                        response = requests.delete(url)
                                        break
                                    else:
                                        break
                
                            if awnser == 5 :
                                break

                        except ValueError:
                            print("\n    Porfavor entre un valor correcto para las opciones\n")
                            time.sleep(1)

                        except KeyboardInterrupt:
                            print("\n    Porfavor entre un valor correcto para las opciones\n")
                            time.sleep(1)
            
                
                elif options == 2:
                    while True:
                        try:                     
                            print(f"""  
    =============================================
            Bases De Datos Propina Normal
    =============================================
    1. Listar datos
    2. Actualizar datos
    3. Bucar por id (Numero de factura)
    4. Eliminar
    5. Regresar al menu anterior   
    =============================================    """)
                            awnser = int(input("    Por favor, elige una opción (1-5): " ))
                            print("")
                           
                            if awnser <=0 :
                                print("        Numeros negativos no son validos")
                                raise ValueError

                            if awnser == 1:
                                url =  f'https://6734e08c5995834c8a9133af.mockapi.io/propinaD/'
                                response = requests.get(url)
                                data = response.json()
                                df = pd.DataFrame(data)

                                    
                                                
                                print(f"\n{df}\n")

                            
                            if awnser == 2:
                                while True:
                                    manual_id = int(input("    Coloque el id (numero de factura) que desee editar: "))
                                    
                                    url =  f'https://6734e08c5995834c8a9133af.mockapi.io/propinaD/{manual_id}'
                                    response = requests.get(url)
                                    data = response.json()
                                    df = pd.DataFrame([data])

                                    print(f"\n{df}\n")


                                    variable = int(input(f"""    Este es el dato que quieres editar? 
        1) si 2) no    """))
                                    if variable == 1:
                                        total = int(input("    Total :"))
                                        porcentaje = int(input("    Porcentaje :"))
                                        personas = int(input("    Personas :"))
                                        propina = int(input("    Propina :"))
                                        totalPorPersona = int(input("    Total mas propina :"))
                                                    

                                        headers = {"Content-Type": "application/json"}
                                        data ={
                                            
                                            "monto": total,
                                            "porcentaje" : porcentaje,
                                            "personas":personas,
                                            "propina" : propina ,
                                            "totalPorPersona" : totalPorPersona

                                            }
                                        url =  f'https://6734e08c5995834c8a9133af.mockapi.io/propinaD/{manual_id}'
                                        
                                        response = requests.put(url , headers=headers,json=data)

                                        break
                                    else:
                                        pass

                            
                            if awnser == 3:
                                while True:    
                                    manual_id = int(input("    Coloque el id (numero de factura) que desee consultar: "))
                                        
                                    url =  f'https://6734e08c5995834c8a9133af.mockapi.io/propinaD/{manual_id}'
                                    response = requests.get(url)
                                    data = response.json()
                                    df = pd.DataFrame([data])

                                    print(f"\n{df}\n")



                                    
                                    variable = int(input(f"""    Desea consultar otra factura? 
        1) si 2) no    """))
                                    if variable == 1:
                                        pass
                                    else:
                                        break                    

                            if awnser == 4:
                                while True:
                                    manual_id = int(input("    Coloque el id (numero de factura) que desee eliminar: "))
                                    url =  f'https://6734e08c5995834c8a9133af.mockapi.io/propinaD/{manual_id}'
                                    
                                    response = requests.get(url)
                                    data = response.json()
                                    df = pd.DataFrame([data])

                                    print(f"\n{df}\n")

                                    
                                    variable = int(input(f"""    Desea eliminar esta factura? 
    1) si 2) no (1-2)    """))
                                    if variable == 1:
                                        response = requests.delete(url)
                                        break
                                    else:
                                        break                

                            if awnser == 5:
                                break
                
                        except ValueError:
                            print("\n    Porfavor entre un valor correcto para las opciones\n")
                            time.sleep(1)

                        except KeyboardInterrupt:
                            print("\n    Porfavor entre un valor correcto para las opciones\n")
                            time.sleep(1)


                    if options == 3:
                        break

                elif options == 3:
                    break    
                else :
                    print("\n    No es un numero valido\n")
                    time.sleep(1) 
            
            except ValueError:
                print("\n    Porfavor entre un valor correcto para las opciones\n")
                time.sleep(1)
            
            except KeyboardInterrupt:
                print("\n    Porfavor entre un valor correcto para las opciones\n")
                time.sleep(1)
            