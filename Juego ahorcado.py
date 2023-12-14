import random

def choose_word():
    words = ['python', 'programacion', 'computadora', 'algoritmo', 'inteligencia']
    return random.choice(words)

def display_word(word, guessed_letters):
    displayed_word = ''
    for letter in word:
        if letter in guessed_letters:
            displayed_word += letter + ' '
        else:
            displayed_word += '_ '
    return displayed_word.strip()

def get_guess(guessed_letters):
    while True:
        guess = input('Ingresa una letra: ').lower()
        if len(guess) != 1:
            print('Por favor, ingresa una sola letra.')
        elif guess in guessed_letters:
            print('Ya has intentado con esa letra. Prueba con otra.')
        elif not guess.isalpha():
            print('Ingresa una letra válida.')
        else:
            return guess

def play():
    word_to_guess = choose_word()
    guessed = []
    attempts = 3

    print('¡Bienvenido al Juego del Ahorcado!')
    print(display_word(word_to_guess, guessed))

    while attempts > 0:
        guess = get_guess(guessed)
        guessed.append(guess)

        if guess not in word_to_guess:
            attempts -= 1
            print(f'¡Incorrecto! Te quedan {attempts} intentos.')
        else:
            print('¡Correcto!')

        displayed = display_word(word_to_guess, guessed)
        print(displayed)

        if '_' not in displayed:
            print('¡Felicidades! Has adivinado la palabra.')
            break

    if attempts == 0:
        print(f'¡Oh no! Se acabaron tus intentos. La palabra era: {word_to_guess}')

if __name__ == "__main__":
    play()

