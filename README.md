### 

[TOC]

El proyecto **Simulador de Propina** es una aplicación simple de consola que permite calcular la cantidad de propina que debe dejarse en un restaurante, basada en el monto total de la cuenta y el porcentaje de propina seleccionado por el usuario. Además, el programa puede mostrar el total a pagar (con la propina incluida) y distribuir el pago entre un número de personas si el usuario lo desea.

# Problema

Cuando vamos a un restaurante, a menudo se nos presenta la necesidad de calcular la propina que dejamos a los camareros. Aunque algunas veces los restaurantes incluyen automáticamente la propina en la cuenta, en muchos casos el cliente tiene que calcularla por su cuenta. Además, la cantidad de propina puede variar dependiendo del servicio recibido (por ejemplo, 10%, 15%, o 20%). Este proyecto tiene como objetivo facilitar ese cálculo y ayudar a los usuarios a determinar el monto de la propina, el total a pagar y cómo dividirlo entre varios comensales.



# Funciones principales:

1. **Ingreso del monto total de la cuenta:**
   - El programa debe permitir al usuario ingresar el monto total de la cuenta del restaurante.
2. **Selección del porcentaje de propina:**
   - El usuario debe poder seleccionar el porcentaje de propina que desea dejar (por ejemplo, 10%, 15%, 20%). También se puede agregar la opción de ingresar un porcentaje personalizado.
3. **Cálculo de la propina:**
   - Con el monto total y el porcentaje seleccionado, el programa debe calcular el valor de la propina.
4. **Cálculo del total a pagar:**
   - El programa debe sumar el monto de la propina al total de la cuenta para mostrar el total que el usuario debe pagar.
5. **División del total entre varias personas (opcional):**
   - El programa debe permitir al usuario ingresar la cantidad de personas que van a pagar la cuenta, y dividir el total (incluyendo propina) entre ellas, calculando cuánto le corresponde a cada persona.
6. **Mostrar resultados:**
   - El programa debe mostrar:
     - La cantidad de propina calculada.
     - El total con la propina incluida.
     - Si es necesario, el monto que le corresponde pagar a cada persona.

**Ejemplo de flujo:**

1. El usuario ingresa el monto de la cuenta (por ejemplo, $50).
2. Elige el porcentaje de propina (por ejemplo, 15%).
3. El programa calcula la propina (en este caso, $7.50) y el total a pagar (en este caso, $57.50).
4. Si el usuario desea dividir la cuenta entre varias personas (por ejemplo, 4 personas), el programa muestra que cada persona debe pagar $14.38.
   

# Funciones específicas:

1. **`calcular_propina(total, porcentaje)`**:
   - Entrada: monto total de la cuenta y porcentaje de propina.
   - Salida: monto de la propina.
2. **`calcular_total_con_propina(total, propina)`**:
   - Entrada: monto total de la cuenta y monto de la propina.
   - Salida: total a pagar (con la propina incluida).
3. **`dividir_total(total, personas)`**:
   - Entrada: monto total (con propina) y número de personas.
   - Salida: monto que le corresponde a cada persona.
4. **`mostrar_resultados(propina, total, total_persona)`**:
   - Entrada: monto de la propina, total a pagar y monto por persona (si es aplicable).
   - Salida: visualización de los resultados.



# Menú Principal Simulador de Propina

```bash
=============================================
  SIMULADOR DE PROPINA
=============================================
1. Calcular propina y total a pagar
2. Calcular total a pagar divido entre varias personas
3. Salir
=============================================
Por favor, elige una opción (1-3):
```

------

## **Si el usuario elige la opción 1:**

```bash
=============================================
  Cálculo de Propina
=============================================
Ingrese el monto total de la cuenta: $____
Ingrese el porcentaje de propina (por ejemplo: 15): ___ %
=============================================
La propina calculada es: $___
El total a pagar es: $___
=============================================
¿Deseas calcular nuevamente? (S/N)
```

------

## **Si el usuario elige la opción 2:**

```bash
=============================================
  Dividir Cuenta entre Varias Personas
=============================================
Ingrese el monto total de la cuenta: $____
Ingrese el porcentaje de propina (por ejemplo: 15): ___ %
Ingrese el número de personas: __
=============================================
La propina calculada es: $___
El total a pagar es: $___
Monto por persona: $___
=============================================
¿Deseas calcular nuevamente? (S/N)
```

------

## **Si el usuario elige la opción 3:**

```bash
=============================================
¡Gracias por usar el Simulador de Propina!
=============================================
```

------

# **Flujo del Menú:**

1. **Menú Principal**: El usuario puede elegir entre las tres opciones:
   - Opción 1: Calcular la propina y el total a pagar.
   - Opción 2: Calcular la propina y dividir la cuenta entre varias personas.
   - Opción 3: Salir del programa.
2. **Submenú de Cálculo de Propina**: Si elige la opción 1, el programa le pedirá ingresar el monto total de la cuenta y el porcentaje de propina. Luego, muestra el cálculo de la propina y el total a pagar.
3. **Submenú de División de Cuenta**: Si elige la opción 2, se le solicitará el monto total de la cuenta, el porcentaje de propina y el número de personas. Luego, el programa mostrará cuánto le corresponde pagar a cada persona.
4. **Salir**: Si elige la opción 3, el programa termina.


