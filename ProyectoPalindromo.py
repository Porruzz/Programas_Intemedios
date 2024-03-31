def palindromo(palabra):
    palabra = palabra.replace(" ", "").lower()
    palabra_invertida = palabra[::-1]
    if palabra_invertida == palabra:
        return True
    else:
        return False

def run():
    palabra = input("Escribe Una Palabra: ")
    es_palindromo = palindromo(palabra)
    if es_palindromo == True:
        print("Es Palindromo")
    else:
        print("No Es Palindromo")

if __name__ == "__main__":
    run()