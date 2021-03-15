# Урок три задание один
def div(*args):
    try:
        arg1 = int(input('Введите делимое '))
        arg2 = int(input('Ведите делитель '))
        res = arg1 / arg2
    except ValueError:
        return 'Ошибка'
    except ZeroDivisionError:
        return 'Вы не можете использовать ноль в качестве делителя'

    return res

    '''
    if arg2 != 0:
        return arg1 / arg2
    else:
        print('Делитель не может быть нулевым')
    '''


print(f'{div()}')
