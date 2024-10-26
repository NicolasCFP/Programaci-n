#Cuestion 1- Nicolas Luciano Ficau

#Inicio
#Definimos el codigo del menu para utilizarlo mas adelante
def menu():
    print("Seleccione lo que quiere hacer: ")
    print("1 - Cuadrado")
    print("2 - Rectángulo")
    print("3 - Salir")
    
#Definimos el código para calcular el cuadrado para utilizarlo cuando se seleccione el numero 1
def cuadrado():
    for i in range (lado):#Para i que es un valor, en el rango de lado, haremos que se multiplique mediante asteriscos los lados e imprimiremos los lados.
        print('*' * lado)
    area = lado * lado #Calculamos el area
    perimetro = 4 * lado #Calculamos el perimetro
    print(f"Área = {area}")#Imprimimos el area
    print(f"Perímetro = {perimetro}")#Imprimimos el perimetro
    
#Definimos el código para calcular el rectanulo para utilizarlo cuando se seleccione el numero 2. 
def rectangulo():
    for i in range (altura): #Para i que es un valor, en el rango de la altura, haremos que se multiplique mediante asteriscos la base y la altura y lo imprimiremos.
        print('*' * base)
    area = base * altura #Calculamos el area
    perimetro = 2 * (base + altura) #Calculamos el perimetro
    print(f"Área = {area}") #Imprimimos el area
    print(f"Perímetro = {perimetro}") #Imprimimos el perimetro

#Mientras este funcionando, mostraremos el menu 
while True: #Mientras el comando siga funcionando
    menu()
    opcion = input("Ingrese una opción (1, 2 o 3): ")
#Si es 1 ejecutaremos la función del cuadrado
    if opcion == "1":
        lado = int(input("Introduce el valor del lado = "))
        cuadrado()
#Si es 2 ejecutaremos la función del rectangulo
    elif opcion == "2":
        base = int(input("Introduce el valor de la base = "))
        altura = int(input("Introduce el valor de la altura = "))
        rectangulo()
#En el caso de que el usuario escriba 3, terminaremos el proceso con un mensaje final.
    elif opcion == "3":
        print("Adiós!")
        break
    else:
        print("Opción no válida, por favor intentelo de nuevo.")
#Cuestion 2- Nicolas Luciano Ficau
import random #Escribimos esto para que mas adelante nos permita generar una numero aleatorrio de una lista que escribiremos.
def piedra_papel_tijera(): #Definimos el código delo juego
    victorias_usuario = 0 #Definimos las victorias del usuario
    victorias_maquina = 0 #Definimos las victorias de la maquina
    
    while victorias_usuario < 3 and victorias_maquina < 3: #Haremos que mientras las victorias del usuario o de la maquina sean menores de 3, el programa siga funcionando
        seleccion_usuario = int(input("Seleccione una opción: 1 - Piedra, 2 - Papel, 3 - Tijera:", )) #le pondremos las opciones y le leeremos lo que ha elegido
        if seleccion_usuario == 1:
            print ("Has seleccionado Piedra")
        if seleccion_usuario == 2:
            print ("Has seleccionado Papel")
        if seleccion_usuario == 3:
            print ("Has seleccionado Tijera")
        
        seleccion_maquina = random.randint(1, 3) #Le pondremos una lista random para que la maquina seleccione un numero de forma aleatoria y leeremos lo que ha elegido la maquina
        if seleccion_maquina == 1:
            print ("La maquina ha seleccionado Piedra")
        if seleccion_maquina == 2:
            print ("La maquina ha seleccionado Papel")
        if seleccion_maquina == 3:
            print ("La maquina ha seleccionado Tijera")
    
        if seleccion_usuario == seleccion_maquina: # Si tanto la maquina como el usuario han elegido lo mismo, sera un empate
            print ("Empate")
        #Estableceremos las situaciones en las que gane el usuario y en las que gane la maquina, basandonos en las reglas del juego Piedra, papel y tijera.
        elif (seleccion_usuario == 1 and seleccion_maquina == 3) or \
        (seleccion_usuario == 1 and seleccion_maquina == 3) or \
        (seleccion_usuario == 1 and seleccion_maquina == 3):
            print ("¡HAS GANADO!")#Si dichas reglas se cumplen, escribiremos que el usuario ha ganado
            victorias_usuario = victorias_usuario + 1 # y le sumaremos 1 numero a las victorias del usuario
        else:
            print ("HAS PERDIDO...") #En caso contrario, escribiremos que ha ganado la maquina
            victorias_maquina = victorias_maquina + 1 # Y le sumaremos 1 numero a las victorias del usuario

        print (f"Usuario:", {victorias_usuario}, "Maquina:", {victorias_maquina}) #Un comando para escrbir el marcador de la partida
        if victorias_usuario == 3: #Si el usuario llega a 3 victorias la partida terminara
            print ("¡HAS GANADO LA PARTIDA!") # Y escribiremos un mensaje comunicando al jugador de que ha ganado
        elif victorias_maquina == 3: #En cambio, si la maquina consigue 3 victorias la partidad terminara pero
            print("HAS PERDIDO LA PARTIDA...") #Escribiremos un mensaje comunicando al usuario de que ha perdido la partida
        
piedra_papel_tijera() #Ejecutaremos el programa

#Cuestion 3- Nicolas Luciano Ficau

def cuenta_bancaria(): #Definimos el codigo de la cuenta bancaria 
    saldo = 0.0 #Variables
    ingresos = 0.0 #Variables
    retiradas = 0.0 #Variables
    cantidad_ingresada = 0.0 #Variables
    cantidad_retirada = 0.0 #Variables
    
    saldo_inicial = float(input("Ingrese el saldo inicial que desea tener:")) #Solicitaremos el saldo con el que el usuario desea comenzar
    while saldo_inicial < 0: # Si el saldo inical es menor que cero, lo remediaremos con un texto indicando que no es posible comenzar con ese saldo y repetiremos el proceso
        print("El saldo inicial no puede ser un numero negativo, porfavor, intentelo de nuevo")
        saldo_inicial = float(input("Ingrese el saldo inicial de la cuenta:"))
    saldo = saldo_inicial #Le añadiremos el saldo que el usuario ha puesto la variable de saldo
    
    while True: #Mientras que el programa siga activo, haremos lo siguiente, ejecutaremos un menu que nos permita realizar difertentes acciones
        print("Seleccione una acción:")
        print("1 - Ingresar dinero")
        print("2 - Retirar dinero")
        print("3 - Mostrar saldo")
        print("4 - Estadísticas")
        print("5 - Salir")
        
        acción = int(input("acción:"))
        while acción < 1 or acción > 5: #Si la accion no esta entre las 5 posibles, lo remediaremos con un texto y repetiremos el proceso
            print("No has seleccionado ninguna acción. Porfavor, seleccione una:")
            acción = int(input("acción:"))
        
        if acción == 1: #Si el usuario ha seleccionado 1 
            cantidad_ingresar = float(input("Ingrese la cantidad que desee ingresar:")) #Le solicitaremos la cantidad que desea ingresar
            if cantidad_ingresar > 0: # Si es mayor que 0
                saldo = saldo + cantidad_ingresar # Aumentaremos el saldo que teniamos con lo que hemos ingresado
                cantidad_ingresada = cantidad_ingresada + cantidad_ingresar #Aumentaremos la variable de dinero que hemos ingresado
                ingresos = ingresos + 1 #Y le sumaremos 1 a la cantidad de ingrresos que hemos realizado
            else:
                print("No se pueden ingresar una cantidad negativa") # Sino, pondremos un mensaje diciendo que la cantidad no puede ser negativa y volveremos al menu            
        
        elif acción == 2: #Si el usuario ha seleccionado 2
            cantidad_retirar = float(input("Ingrese la cantidad que desee retirar:")) #Le solicitaremos la cantidad que desea retirar
            if cantidad_retirar > 0 and cantidad_retirar <= saldo: # Si al cantidad retirada es mayor que 0 y es menor del saldo que tenemos
                saldo = saldo - cantidad_retirar #Le restaremos al saldo la cantidad que queremos retirar
                retiradas= retiradas + 1  # Le sumaremos 1 al numero de veces que hemos retirado
                cantidad_retirada = cantidad_retirada + cantidad_retirar # Y sumaremos el dinero que hemos retirado a la cantidad retirada
            else:
                print("Cantidad no válida o saldo insuficiente") # Sino, escribiremos que la cantidad no es suficiente o que no disponemos del suficiente dinero como para retirar dicha cantidad
        
        elif acción == 3: #Si el usuario ha seleccionado la tercera accion
            print("Tu saldo actual es:", saldo) #Le mostraremos cual es su saldo actual
        elif acción == 4: # Si el usuario ha seleccionado la cuarta opcion 
           print("Estadísticas:") #Le mostraremos un menu de estadisticas
           print(f"Total de ingresos realizados: {ingresos}") #Los ingresos que ha realizado
           print(f"Total de retiradas realizadas: {retiradas}") #Las retiradas que ha realizado
           print(f"Cantidad total ingresada: {cantidad_ingresada}") #La cantidad ingresada
           print(f"Cantidad total retirada: {cantidad_retirada}") #La cantidad retirrada
        
        elif acción == 5: # Si el usuario ha seleccionado la accion 5
            print ("Adios!") # el programa se terminara despidiendo al usuario con un mensaje 
            break

cuenta_bancaria()#Ejecutamos el código