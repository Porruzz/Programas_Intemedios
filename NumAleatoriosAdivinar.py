import random

def run():
    numero_aleatorio = random.randint(1, 100)
    numero_elegido = int(input("Elige un numero del 1 al 100: "))
    while numero_elegido != numero_aleatorio:
        if numero_elegido <  numero_aleatorio:
            print("Busca un numero más Grande")
        else:
            print("Busca un numero más Pequeño")
        numero_elegido = int(input("Elige Otro Numero: "))
    print("Ganaste! El número era", numero_aleatorio)
    
if __name__ == "__main__":
    run()