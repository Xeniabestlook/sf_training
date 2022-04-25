"""Game gess the number"""

import numpy as np

number = np.random.randint(1, 11) # загадываем число

# количество попыток
count = 0

while count < 5:
    count += 1
    predict_number = int(input("Угадай число от 1 до 10"))

    if predict_number > number:
        print("Число должно быть меньше")

    elif predict_number < number:
        print("Число должно быть больше")
    
    else:
        print("Вы угадали!")
        break
