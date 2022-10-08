from random import randint
from typing import List


def user_interface(options: List[str]) -> int:
    '''
    Представить пользователю интерфейс.
    '''
    for index, option in enumerate(options):
        print(f'{index} = {option}')
    try:
        user_input: int = int(input('Что выбираете?\n'))
        return user_input
    except ValueError:
        print('Ошибка! Невозможно преобразовать переменную в тип int')
    except Exception:
        print('Неизвестная ошибка!')


def computer_choice(options: List[str]) -> int:
    '''
    Генерировать выбор компьютера.
    '''
    return randint(0, len(options) - 1)


def check_results(options: List[str], player: int, computer: int) -> str:
    '''
    Проверять результат.
    '''
    if player == computer:
        return 'Ничья'
    elif (player == len(options) - 1 and computer == 0):
        return 'Вы выиграли! Спок испарил камень'
    elif (player == len(options) - 1 and computer == 1):
        return 'Вы выиграли! Спок сломал ножницы'
    elif (player == 3 and computer == 2):
        return 'Вы выиграли! Ящерица съела бумагу'
    elif (player == 3 and computer == 4):
        return 'Вы выиграли! Ящерица отравила спока'
    elif (player == 2 and computer == 0):
        return 'Вы выиграли! Бумага покрыла камень'
    elif (player == 2 and computer == 4):
        return 'Вы выиграли! Бумага подставила спока'
    elif (player == 1 and computer == 2):
        return 'Вы выиграли! Ножницы разрезали бумагу'
    elif (player == 1 and computer == 3):
        return 'Вы выиграли! Ножницы обезглавили ящерицу'
    elif (player == 0 and computer == 1):
        return 'Вы выиграли! Камень разбил ножницы'
    elif (player == 0 and computer == 3):
        return 'Вы выиграли! Камень раздавил ящерицу'
    else:
        return f'Вы проиграли! {options[computer]} сильнее {options[player]}'


def play() -> None:
    '''
    Играть.
    '''
    print('''
    ---------------------------------
    Камень, ножницы, бумага, ящерица, спок!
    Сделай свой выбор:
    ''')
    options_list: List[str] = [
        'Камень', 'Ножницы', 'Бумага', 'Ящерица', 'Спок',
    ]
    player_result: int = user_interface(options_list)
    computer_result: int = computer_choice(options_list)
    if (player_result < 0 or player_result > len(options_list) - 1):
        raise IndexError('Выбранное число должно быть от 0 до 4')
    print(f'Выбор игрока: {options_list[player_result]}')
    print(f'Выбор компьютера: {options_list[computer_result]}')
    results: str = check_results(options_list, player_result, computer_result)
    print(f'\n{results}')


def main():
    '''
    Главная функция.
    '''
    play_again: str = ''
    while play_again.lower() != 'n':
        play()
        print('Хотите сыграть снова?')
        play_again = input('Если да нажмите любую кнопку, если нет \'n\': ')


main()
