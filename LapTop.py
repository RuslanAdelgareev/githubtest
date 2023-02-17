def chocolate(name):
    global sklad
    if name == "Кофе":
        if sklad[0] >= 1 and sklad[1] >= 1 and sklad[2] >= 1:
            sklad[0] = sklad[0] - 1
            sklad[1] = sklad[1] - 1 
            sklad[2] = sklad[2] - 1
            return "Оу-е кофе"
        else:
            return "Наши запасы не равны вашим запросам"
    elif name == "Маккиато":
        if sklad[0] >= 4 and sklad[1] >= 4 and sklad[2] >= 4:
            sklad[0] = sklad[0] - 4
            sklad[1] = sklad[1] - 4 
            sklad[2] = sklad[2] - 4
            return "Оу-е макиато, единственный и не повторимый"
        else:
            return "Наши запасы не равны вашим запросам"
    else:
        return "Иди-ка отсюда, кофе ему не нравится"
        
        
sklad = [4, 4, 4]  # Молоко, сливки, зерна
print(chocolate(input('Пить или есть?')))
#Тут есть ошибка