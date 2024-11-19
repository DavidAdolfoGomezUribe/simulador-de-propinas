from logica.formulas import calcular_propina,calcular_total_con_propina
import os
import requests
import json
import time
import keyboard

def desingMenuOptOne():
    while True:
        id_actual = 0
        url =  f'https://6734e08c5995834c8a9133af.mockapi.io/propina/'
        responseid = requests.get(url)
        
        if responseid.status_code == 200:
            data = responseid.json()  # Obtener el JSON de la respuesta
            if data:
                
                id_actual = int(data[-1]['id'])  # Acceder al ulrimo elemento y obtener el 'id'
                                
                if id_actual > 0:
                    id_pos = id_actual + 1
                
            else:
                id_pos = 1               
                
        else:
            print('Error al obtener los datos.')

        print(f"""
    =============================================
                Cálculo de Propina 
    =============================================      
               Factura # {id_pos} Prop Norm
              """)

        try:
            
            total = float(input(f"    Ingrese el monto total de la cuenta: $"))
            
            if total < 0:
                raise ValueError("    El monto no puede ser negativo.")
            #--------------------
            porcentaje = int(input("    Ingrese el porcentaje de propina (por ejemplo: 10%, 15%, 20 %): "))
                 
            if porcentaje < 0:
                raise ValueError("    El monto no puede ser negativo.")
            #--------------------
           
            propina = calcular_propina(total, porcentaje)
            total_con_propina = calcular_total_con_propina(total, propina)


            # Hacer la solicitud put
            headers = {"Content-Type": "application/json"}
            data ={
                
                "monto": total,
                "porcentaje" : porcentaje,
                "propina" : propina ,
                "totalMasPropina" : total_con_propina

                }

            

            url =  f'https://6734e08c5995834c8a9133af.mockapi.io/propina/'
            response = requests.post(url , headers=headers,json=data)
            
            print(f"""      
    =============================================
    La propina calculada es: ${propina}
    El total a pagar es: ${total_con_propina}
    =============================================
    
    Respuesta del servidor """)
            time.sleep(1)
            print("\n    ")
            # Comprobar el estado de la respuesta
            if response.status_code == 200 or response.status_code == 201 :
                print('    Factura subida con exito\n')
            else:
                print(f'    Error al actualizar los datos de la factura: {response.status_code}\n')
            
            options = str(input("    ¿Deseas calcular nuevamente? (S/N): "))
            
            if options.lower() == "s":
                # Limpiar la pantalla (compatible con Windows y Unix)
                os.system("cls" if os.name == "nt" else "clear")
            else:
                os.system("cls" if os.name == "nt" else "clear")
                break

        
        except ValueError as e:
            print(f"Error: {e}. Datos no válidos.")
        except KeyboardInterrupt:
            print("\n    Porfavor entre un valor correcto para las opciones\n")
            time.sleep(1)
            