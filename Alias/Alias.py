import os


def alias(mline):
    def is_hooks():  # определить что квадратные скобки находятся внутри пары специальных кавычек
        if mline.count('`') % 2 == 0:
            first_hook = mline.find('`')
            two_hook = mline.rfind('`')
            if first_hook < first and two_hook > two:
                return True
        return False

    def is_counter():  # найти в строке тройные специальные кавычки
        if '```' in mline and mline.count('`') == 3:
            return True
        return False

    global count_three  # делаю глобальную переменную доступной для изменения
    if is_counter():  # если нахожу тройную кавычку меняю флаг на противоположный
        count_three = not count_three

    if ('![[' not in mline) and '[[' in mline and ']]' in mline:
        first = mline.find('[[')  # нелокальная переменная
        two = mline.find(']]')  # нелокальная переменная
        my_str = mline[first:two]
        if (not count_three) and first < two and (not is_hooks()) and '|' not in my_str and '-' in my_str:
            el1, el2, el3 = my_str.partition('-')  # дефис обязательно должен присутствовать в имени файла!!!
            return mline[:first] + f'{el1}{el2}{el3}|{el3}' + mline[two:]
    return mline


def add_alias(name):
    flag = False
    with open(name, 'r', encoding='utf-8') as file:
        content = file.readlines()
        for i, line in enumerate(content):
            content[i] = alias(line)
            if (not flag) and content[i] != line:  # если были исправления в строке то изменить флаг
                flag = True
    if flag:  # если были исправления то перезаписать файл, в противном случае оставить файл неизменным(не переписывать)
        with open(name, 'w', encoding='utf-8') as file:
            file.writelines(content)


def recursion_open_dir(dir=None): # открываю рекурсивно все подпапки и файлы с расширением "*.md"

    def select(name_file):  # отбираю папки и файлы с расширением *.md
        if os.path.isdir(name_file):  # проверяю - является ли данный объект папкой
            return True
        elif name_file.endswith('.md'): # отбираю файлы с расширением "*.md"
            return True
        return False


    if dir is None:
        dir = f'{os.getcwd()}/'
    files = os.listdir(dir)
    dir_files = map(lambda x: f'{dir}{x}', files)  # добавляю путь к имени файла
    select_files = filter(select, dir_files)  # отбираю папки или файлы с расширением *.md

    for name in select_files:
        if os.path.isdir(name): # если объект является папкой то нужно вновь рекурсивно вызвать функцию
            recursion_open_dir(f'{name}/')
        else:
            add_alias(name)



count_three = False  # глобальная переменная
recursion_open_dir() # запуск программы
