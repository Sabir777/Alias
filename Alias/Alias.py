import os


def alias(mline):
    def is_hooks():  # ���������� ��� ���������� ������ ��������� ������ ���� ����������� �������
        if mline.count('`') % 2 == 0:
            first_hook = mline.find('`')
            two_hook = mline.rfind('`')
            if first_hook < first and two_hook > two:
                return True
        return False

    def is_counter():  # ����� � ������ ������� ����������� �������
        if '```' in mline and mline.count('`') == 3:
            return True
        return False

    if '[[' in mline and ']]' in mline:
        first = mline.find('[[')  # ����������� ����������
        two = mline.find(']]')  # ����������� ����������
        my_str = mline[first:two]
        global count_three  # ����� ���������� ���������� ��������� ��� ���������
        if is_counter():  # ���� ������ ������� ������� ����� ���� �� ���������������
            count_three = not count_three
        if (not count_three) and first < two and (not is_hooks()) and '|' not in my_str and '-' in my_str:
            el1, el2, el3 = my_str.partition('-')  # ����� ����������� ������ �������������� � ����� �����!!!
            return mline[:first] + f'{el1}{el2}{el3}|{el3}' + mline[two:]
    return mline


def add_alias(name):
    flag = False
    with open(name, 'r', encoding='utf-8') as file:
        content = file.readlines()
        for i, line in enumerate(content):
            content[i] = alias(line)
            if (not flag) and content[i] != line:  # ���� ���� ����������� � ������ �� �������� ����
                flag = True
    if flag:  # ���� ���� ����������� �� ������������ ����, � ��������� ������ �������� ���� ����������(�� ������������)
        with open(name, 'w', encoding='utf-8') as file:
            file.writelines(content)


def recursion_open_dir(dir=None): # �������� ���������� ��� �������� � ����� � ����������� "*.md"

    def select(name_file):  # ������� ����� � ����� � ����������� *.md
        if os.path.isdir(name_file):  # �������� - �������� �� ������ ������ ������
            return True
        elif name_file.endswith('.md'): # ������� ����� � ����������� "*.md"
            return True
        return False


    if dir is None:
        dir = f'{os.getcwd()}/'
    files = os.listdir(dir)
    dir_files = map(lambda x: f'{dir}{x}', files)  # �������� ���� � ����� �����
    select_files = filter(select, dir_files)  # ������� ����� ��� ����� � ����������� *.md

    for name in select_files:
        if os.path.isdir(name): # ���� ������ �������� ������ �� ����� ����� ���������� ������� �������
            recursion_open_dir(f'{name}/')
        else:
            add_alias(name)



count_three = False  # ���������� ����������
recursion_open_dir() # ������ ���������
