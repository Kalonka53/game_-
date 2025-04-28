



import random
import time
print('Привет, давай сыграем в игру числовую угадайку')


def is_valid(n, low, hight):
    return low <= n <= hight


def choose_difficulty():
    while True:
        choise = input('Выбери уровень сложности: \n1: Easy \n2: Medium \n3: Hard \nВаш выбор: ')
        if choise == '1':
            return {'low': 1, 'hight': 50, 'max_attempts': 15}
        elif choise == '2':
            return {'low': 1, 'hight': 100, 'max_attempts': 10}
        elif choise == '3':
            return {'low': 1, 'hight': 200, 'max_attempts': 5}
        else:
            print('Неправильный выбор. Выберите уровень сложности 1, 2 или 3')

def play_game(low, hight, max_attempts):
    random_number = random.randint(low, hight)
    attempts = 0
    dimin_attempts = max_attempts
    start_time = time.time()
    print(f'Выбери число от {low} до {hight} у тебя {max_attempts} попыток')

    while dimin_attempts > 0:
        try:    
            n = int(input(f'твоя догадка [№{dimin_attempts}] попытка: '))
            attempts += 1
            dimin_attempts -= 1
            if not is_valid(n, low, hight):
                print(f'Выбери число в диапозоне от {low} до {hight}')
                continue
            responce_time = time.time() - start_time
            if responce_time >= 10:
                print('Долго думаешь, быстрее!')
            if n < random_number:
                print('Больше')
            elif n > random_number:
                print('Меньше')
            else:
                print(f'Поздравляю! Вы угадали число {random_number} за {attempts} попытки и {responce_time:.2f} времени')
                break
        except ValueError:
            print("Вводите только числа !")

continue_game = True
while continue_game:
    settings = choose_difficulty()
    play_game(**settings)
    more_time = input('Желаете продолжить ?\nДа\Нет: ').strip().lower()
    if more_time != 'да':
        continue_game = False
        print('Спасибо за игру, хорошего дня!')


