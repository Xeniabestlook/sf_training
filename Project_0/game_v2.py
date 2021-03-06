"""компьютер сам загадывает и узадывает числа"""
from itertools import count
import numpy as np

def random_predict(number:int=1) -> int:
    """рандомно угадываем число

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    i = 1 # начало набора чисел для рандомной выборки
    j = 101 # конец набора чисел для рандомной выборки
    count = 0
    
    while True:
        count += 1
        predict_number = np.random.randint(i, j) # предполагаемое число
        if number == predict_number:
            break # выход из цикла, если угадали
        elif number > predict_number:
            i = predict_number + 1 # сужаем область рандомной выборки снизу
        elif number < predict_number:
            j = predict_number # сужаем область рандомной выборки сверху
    return(count)

print(f'Количество попыток: {random_predict()}')

def score_game(random_predict) -> int:
    """За какое количество попыток в среднем из 1000 подходов угадывает наш алгоритм

    Args:
        random_predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """

    count_ls = [] # список для сохранения количества попыток
    np.random.seed(10) # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(1000)) # загадали список чисел

    for number in random_array:
        count_ls.append(random_predict(number))

    score = int(np.mean(count_ls)) # находим среднее количество попыток

    print(f'Ваш алгоритм угадывает число в среднем за: {score} попыток')
    return(score)

# RUN
if __name__ == '__main__':
    score_game(random_predict)