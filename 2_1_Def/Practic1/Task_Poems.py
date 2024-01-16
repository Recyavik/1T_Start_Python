"""
Мечта коровы - деревенская фантастика

Корова стояла в холодном хлеву,
Жевала корова сухую траву,
Мечтала корова о лете,
О вкусном во рту букете.

Мечтала корова всем дать молока,
Белого, летнего как облака.
Корова мечтала о птицах,
О теплой в ручье водице.

О бабочках тоже мечтала,
Сладкая будет сметана.
Ветра потоки южные,
Маслице будет вкусное.

Корова мечтала песенки петь,
На арфе играть и на солнце смотреть.
Мечтала корова, мечтала,
И лето внезапно настало.


# Программист
# Пантелею-программисту
# Нравится печатать быстро.
# Целый день сидит-молчит
# И по кнопочкам стучит.
# Емельянова Ольга


# Самуил Маршак
# "Багаж"
# Дама сдавала в багаж
# Диван,
# Чемодан,
# Саквояж,
# Картину,
# Корзину,
# Картонку
# И маленькую собачонку.

""" #
def show_poem(poem_list):
    d = len(poem_list)
    if d >= 2:
        print(f'\x1b[93m Стихотворение: "{poem_list[0]}" \x1b[0m', )
        for i in range(1, d-2):
            print(f'{poem_list[i]}')
        print(f'\x1b[32m \tАвтор: {poem_list[d-1]} \x1b[0m', )

def input_poem():
    poem_list = []
    st_poem = ' '
    poem_list.append(input('Введите название стихотворения: '))
    print('Введите строки стихотворения:')
    while st_poem != '':
        if st_poem == '':
            break
        else:
            st_poem = input('-> ')
            poem_list.append(st_poem)
    poem_list.append(input('Введите автора: '))
    return poem_list


poem_list = list()
while True:
    print('Меню:')
    print('1. Ввести стихотворение')
    print('2. Показать стихотворение')
    print('3. Завершить')
    st = input('Сделайте выбор (1-3): ')
    if st == '1':
        poem_list = input_poem()
    elif st == '2':
        show_poem(poem_list)
    elif st == '3':
        break
    else:
        print('Не понятен ваш выбор. Повторите ввод!')


print('Работа программы завершена! До новых встреч!')