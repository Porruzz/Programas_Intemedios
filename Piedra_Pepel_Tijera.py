import random

def rock_paper_scissors():
    choices = ["piedra", "papel", "tijera"]
    computer_choice = random.choice(choices)
    user_choice = input("Elige entre piedra, papel o tijera: ").lower()

    print(f"\nTu elección: {user_choice}")
    print(f"Elección de la computadora: {computer_choice}\n")

    if user_choice == computer_choice:
        print("Empate")
    elif (user_choice == "piedra" and computer_choice == "tijera") or \
         (user_choice == "tijera" and computer_choice == "papel") or \
         (user_choice == "papel" and computer_choice == "piedra"):
        print("¡Ganaste!")
    else:
        print("¡Perdiste!")

rock_paper_scissors()