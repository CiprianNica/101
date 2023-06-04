""" # User Choices
PAPER = 0
ROCK = 1
SCISSORS = 2
QUIT = 3
INVALID_CHOICE = -1 """
from enum import Enum

class GameChoice(Enum):
    PAPER = 0
    ROCK = 1
    SCISSORS = 2
    QUIT = 3
    INVALID= -1
    

def game_loop():
    """Arranca el bucle principal del juego
    """
    while True:
        # leo la seleccion del usuario (piedra, papel, tijera o parar el juego)
        user_choice = read_user_choice()
        #siempre y cuando no quiera parar
        if not is_exit(user_choice):
            # genero una jugada del ordenador
            comp_choice = generate_computer_choice()
            # evaluo la jugada
            result = evaluate_move(user_choice, comp_choice)
            # muestro el ganador en pantalla y vuelta al principio
            print_result(result)
        else:
            # el humano es un gallina: salgo
            break
            
        
def read_user_choice():
    """
        Lee una seleccio del usuario (piedra, papel, tijera o salir)
        y la devuelve
    """
    user_choice = GameChoice.INVALID
    while user_choice == GameChoice.INVALID:
        
        print("Select one number: ")
        print(f"{GameChoice.PAPER.value}. Paper")
        print(f"{GameChoice.ROCK.value}.Rock")
        print(f"{GameChoice.SCISSORS.value}.Scissors")
        print(f"---------------------")
        print(f"{GameChoice.QUIT.value}. QUIT the game")
        
        try:
            user_choice = GameChoice(int(input("Enter your user choice: ")))
        except ValueError:
            user_choice = GameChoice.INVALID
            
        # valido lo que me ha dicho
        #if user_choice !=  UserChoice.INVALID:
        #    break # ok, nos vamos
        #else:
        #    user_choice = UserChoice.INVALID # antes te cansas
    
    # devuelve un tipo que hemos creado
    return user_choice

def is_exit(user_choice):
    """
    Predicado que devuelve True si el usuario ha decidido parar 
    y False si quiere seguir jugando
    """
    return user_choice == GameChoice.QUIT

def generate_computer_choice():
    """
    genera y devuelve una jugada al azar
    """
    from random import choice
    
    return choice([GameChoice.PAPER, GameChoice.ROCK, GameChoice.SCISSORS])

def evaluate_move(user_choice, comp_choice):
    """
        compara las dos jugadas y devuelve un texto con el resultado
    """
    assert user_choice != GameChoice.INVALID and user_choice != GameChoice.QUIT
    assert comp_choice != GameChoice.INVALID and user_choice != GameChoice.QUIT
    
    result = ''
    if user_choice == GameChoice.PAPER:
        if comp_choice == GameChoice.PAPER:
            result = "It`s a tie!"
        elif comp_choice == GameChoice.ROCK:
            result = "You win! paper cover rock."
        else:
            result = "I win ! Scissors cut paper."
    elif user_choice == GameChoice.ROCK:
        if comp_choice == GameChoice.ROCK:
            result = "It`s a tie!"
        elif comp_choice == GameChoice.PAPER:
            result = "You win! paper cover rock."
        else:
            result = "You win! Rock smashes scissors"
    else:
        #scissors
        if comp_choice == GameChoice.SCISSORS:
            result = "It`s a tier!"
        elif comp_choice == GameChoice.PAPER:
            result = "You win! Scissor cut paper."
        else:
            #rock
            result = "I win ! Rock smashes scissors."
    
    
    return result
    
def print_result(result):
    """
    imprime en bonito el resultado
    """
    print('\n\n----------------------------------------')
    print("Game Over")
    print(result)
    print('\n\n----------------------------------------')
    
def log_error(error):
    """
    gusarda el error en crashlytics
    """
    print(error)

if __name__ == "__main__":
    try:
        game_loop()
    except Exception as error:
        log_error(error)
else:
    print("Si llego aqui, es que me estan importando")