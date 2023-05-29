""" # User Choices
PAPER = 0
ROCK = 1
SCISSORS = 2
QUIT = 3
INVALID_CHOICE = -1 """
from enum import Enum
class UserChoice(Enum):
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
            
        return True
def read_user_choice():
    """
        Lee una seleccio del usuario (piedra, papel, tijera o salir)
        y la devuelve
    """
    user_choice = UserChoice.INVALID
    while user_choice == UserChoice.INVALID:
        
        print("Select one number: ")
        print(f"{UserChoice.PAPER.value}. Paper")
        print(f"{UserChoice.ROCK.value}.Rock")
        print(f"{UserChoice.SCISSORS.value}.Scissors")
        print(f"---------------------")
        print(f"{UserChoice.QUIT.value}. QUIT the game")
        
        try:
            user_choice = int(input("Enter your user choice: "))
        except ValueError:
            user_choice = UserChoice.INVALID
            
        # valido lo que me ha dicho
        if user_choice !=  UserChoice.INVALID:
            break # ok, nos vamos
        else:
            user_choice = UserChoice.INVALID # antes te cansas
    
    
    return user_choice

def is_exit(user_choise):
    """
    Predicado que devuelve True si el usuario ha decidido parar 
    y False si quiere seguir jugando
    """
    return True

def generate_computer_choice():
    """
    genera y devuelve una jugada al azar
    """
    return None

def evaluate_move(user_choice, comp_choice):
    """
        compara las dos jugadas y devuelve un texto con el resultado
    """
    return True
def print_move():
    """
    """
    return None
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