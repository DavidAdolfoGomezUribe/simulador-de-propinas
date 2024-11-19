from logica.formulas import   calcular_propina, calcular_total_con_propina,dividir_total_personas

import os
import requests
import time
import keyboard

def desingMenuOptTwo():
    while True:
        try:
            id_actual = 0
            url =  f'https://6734e08c5995834c8a9133af.mockapi.io/propinaD'
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
        Dividir Cuenta entre Varias Personas
    =============================================
            Factura # {id_pos} Prop Div
            """)
            try:
                total = float(input("    Ingrese el monto total de la cuenta: $"))

                if total < 0: 
                    raise ValueError("    El monto no puede ser negativo.")

                #---------------
                porcentaje = int(input("    Ingrese el porcentaje de propina (por ejemplo: 15): "))

                if porcentaje < 0: 
                    raise ValueError("    El monto no puede ser negativo.")
                #---------------

                persona =  int(input("    Ingrese el número de personas: "))

                if persona < 1: 
                    raise ValueError("    El monto no puede ser menor a 1.")

                
                propina = calcular_propina(total, porcentaje)


                totalMasPropina = calcular_total_con_propina(total,propina)
                
                totalPorPersona = dividir_total_personas(total,persona) + (propina/persona)


                # Hacer la solicitud put
                headers = {"Content-Type": "application/json"}
                data ={
                    
                    "monto": total,
                    "porcentaje" : porcentaje,
                    "personas" : persona ,
                    "propina" : propina,
                    "totalPorPersona": totalPorPersona
                    }

                

                url =  f'https://6734e08c5995834c8a9133af.mockapi.io/propinaD'
                response = requests.post(url , headers=headers,json=data)


                print(f"""             
    =============================================
    La propina calculada es: ${propina}
    El total a pagar es: $___{totalMasPropina}
    Monto por persona: $___{totalPorPersona}
    =============================================
                """)

                time.sleep(1)
                print("\n    ",)
                # Comprobar el estado de la respuesta
                if response.status_code == 200 or response.status_code == 201 :
                    print('    Factura subida con exito\n')
                else:
                    print(f'    Error al actualizar los datos de la factura: {response.status_code}\n')

                options = str(input("    ¿Deseas calcular nuevamente? (S/N)"))

                if options.lower == "s" :
                    os.system("cls" if os.name == "nt" else "clear")
                else:
                    os.system("cls" if os.name == "nt" else "clear")
                    break    
            except ValueError as e:
                print(f"    Error: {e}. Datos no válidos.")
            except KeyboardInterrupt:
                print("\n    Porfavor entre un valor correcto para las opciones\n")
                time.sleep(1)
                
        except ValueError as e:
            print(f"    Error: {e}. Datos no válidos.")
        except KeyboardInterrupt:
            print("\n    Porfavor entre un valor correcto para las opciones\n")
            time.sleep(1)
            
