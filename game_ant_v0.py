from itertools import count
import numpy as np

def nonrandom_predict(number:int=1) -> int:
    """Угадываем число с помощью деления отрезка попалам

    Args:
        number (int, optional): Число для угадывания. Defaults to 1.

    Returns:
        int: Количество шагов для угадывания
    """
    count = 0
    step = 50
    predict_number = 50
    while True:
        count += 1
        step = round(step / 2)
        if number == predict_number:
            break # выход из цикла, если угадали
        else:
            if predict_number > number:
                predict_number = predict_number - step
            elif predict_number < number:
                predict_number = predict_number + step
        

                    
    return(count)


def score_game(nonrandom_predict) -> int:
    """За какое количество попыток в среднем из 1000 подходов угадывает наш алгоритм

    Args:
        random_predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """

    count_ls = [] # список для сохранения количества попыток
    np.random.seed(1) # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(1000)) # загадали список чисел

    for number in random_array:
        count_ls.append(nonrandom_predict(number))

    score = int(np.mean(count_ls)) # находим среднее количество попыток

    print(f'Ваш алгоритм угадывает число в среднем за: {score} попыток')
    return(score)

# RUN
if __name__ == '__main__':
    score_game(nonrandom_predict)