# Урок четвертый

# 1 задание
def amount_payment(payment):
    summ = 0
    for pay in payment:
       summ += pay
    return summ


payment_list = [10, 100, 200, -34, -155]
fullsumm = amount_payment(payment_list)
print (fullsumm)
# ***

# 2 задание
# # При аналізі даних часто виникає необхідність позбавитися екстремальних значень, перш ніж почати працювати з даними далі.
# # Напишіть функцію prepare_data, яка видаляє з переданого списку найбільше та найменше значення, сортує його в порядку зростання і повертає змінений список як результат.

def prepare_data(data):

    new_data = sorted(data)
    new_data.pop(0)
    new_data.pop(-1)
    return new_data

dat = [10, 50, 1, 2540, 250 , 3478, 45, 888]
print (prepare_data(dat))
# ***

# 3 задание
# Ми розробляємо кулінарний блог. І в рецептах, при написанні списку інгредієнтів, ми розділяємо їх комами, а перед останнім ставимо союз "and", як у прикладі нижче:

# 2 eggs, 1 liter sugar, 1 tsp salt and vinegar
# Напишіть функцію format_ingredients, яка прийматиме на вхід список з інгредієнтів["2 eggs", "1 liter sugar", "1 tsp salt", "vinegar"]
# та повертатиме рядок зібраний з його елементів в описаний вище спосіб. Ваша функція має вміти обробляти списки будь-якої довжини.

#  1 вариант
def format_ingredients(items):

    for item in items:
        if item == "2 eggs":
           try:
               eggs = item +', '
           except:
               eggs = ''
        elif item == "1 liter sugar":
            try:
                liter_sugar = item + ', '
            except:
                liter_sugar = ''
        elif item == "1 tsp salt":
            try:
                tsp_salt = item + ' and '
            except:
                tsp_salt = ' and '

        elif item == "vinegar":
            try:
                vinegar = item
            except:
                vinegar = ''

    return eggs + liter_sugar + tsp_salt + vinegar

ite = ["2 eggs", "1 liter sugar", "1 tsp salt", "vinegar"]
print (format_ingredients(ite))

#2 вариант
def format_ingredients(items):

    full_pecept = None

    if "2 eggs" in items:
       full_pecept = "2 eggs"

    if "1 liter sugar" in items:
        if full_pecept != None:
            full_pecept += ', ' + "1 liter sugar"
        else:
            full_pecept = "1 liter sugar"

    if "1 tsp salt" in items:
        if full_pecept != None:
            full_pecept += ', ' + "1 tsp salt"
        else:
            full_pecept = "1 tsp salt"

    if "vinegar" in items:
        if full_pecept != None:
            full_pecept += " and " + "vinegar"
        else:
            full_pecept = "vinegar"

    if full_pecept == None:
        full_pecept = ''

    return full_pecept

#  3 вариант
def format_ingredients(items):
    if len(items) > 1:
        first_three = items[0:len(items)-1]
        end = ", ".join(first_three)
        end += " and "
        last = items[-1]
        end += last
    else:
       end = "".join(items)
    return end

item = ["1 tsp salt",  "vinegar", "1 liter sugar"]
print(format_ingredients(item))
# "2 eggs",
# ***

# 4 задание
# Оцінка	Бали	Оцінка ECTS	Пояснення
# 1	0-34	F	Unsatisfactorily
# 2	35-59	FX	Unsatisfactorily
# 3	60-66	E	Enough
# 3	67-74	D	Satisfactorily
# 4	75-89	C	Good
# 5	90-95	В	Very good
# 5	96-100	A	Perfectly

def get_grade(key):

    c_idx = getgrade.get(key)
    print (c_idx)

def get_description(key):

    c_idx = getdescription.get(key)
    print (c_idx)

def get_ball(ball):

    if 0 >= ball <= 34:
        balllist = bal_list[0]
    elif 35 >= ball <= 59:
        balllist = bal_list[1]
    elif 60 >= ball <= 66:
        balllist = bal_list[2]
    elif 67 >= ball <= 74:
        balllist = bal_list[3]
    elif 75 >= ball <= 89:
        balllist = bal_list[4]
    elif 90 >= ball <= 95:
        balllist = bal_list[5]
    # else:
        #  balllist = bal_list[6]
    elif 96 >= ball <= 100:
        balllist = bal_list[6]
    else:
        balllist = None

    get_grade(balllist)
    get_description(balllist)

getgrade = {'F':1, 'FX':2, 'E':3, 'D':3, 'C':4, 'B':5, 'A':5}
getdescription = {'F': 'Unsatisfactorily', 'FX': 'Unsatisfactorily','E': 'Enough', 'D': 'Satisfactorily', 'C': 'Good', 'B': 'Very good', 'A': 'Perfectly'}
bal_list = ['F', 'FX', 'E', 'D', 'C', 'B', 'A']

bal = int(input('Введите баллы полученные студентом за здачу екзамена: '))
get_ball(bal)
# ***

# 5 задание
# Як ми знаємо, ключ у словнику має бути унікальним, тоді як значення його ні.
# Реалізуйте функцію lookup_key для пошуку всіх ключів за значенням у словнику.
# Першим параметром у функцію ми передаємо словник, а другим — значення, що хочемо знайти.
# Таким чином, результат може бути як список ключів, так і порожній список, якщо ми нічого не знайдемо.
#  data, value - дата словарь, валие - значенеи ключа

def lookup_key(data, value):

    data_list = []

    for key, data_value in data.items():

        for key_value in value:
            if str(key_value) == key:
                data_list.append(data_value)

    return data_list

def lookup_key(data, value):

    data_list = []

    for key in data.keys():

        for key_value in value:
            if str(key_value) == key:
                data_list.append(key)

    return data_list

def lookup_key(data, value):

    data_list = []

    for key, val  in data.items():

        if val == value:

            data_list.append(key)

    return data_list


print(lookup_key({'1':1, '2':2, '3':3}, 2))
print(lookup_key({'key1': 1, 'key2': 2, 'key3': 3, 'key4': 2}, 2))
print(lookup_key({'1': 1, '2': 2, '3': 3}, 4))
print(lookup_key({}, 4))
# ***

# 6 задание
# У нас є список показників студентів групи – це список з отриманими балами з тестування.
# Необхідно поділити список на дві частини. Напишіть функцію split_list, яка приймає список(цілі числа), знаходить середнє значення бала у списку та ділить його на два списки.
# У перший потрапляють значення менше середнього, включаючи середнє значення, тоді як у другий — строго більше від середнього. Функція повертає кортеж цих двох списків.
# Для порожнього списку повертаємо два порожні списки.

# *** 1 вариант 
def split_list(grade):
    list_grate_min = []
    list_grate_max = []
    
    # grate_max = max(grade)        
    
    for i_grade in grade:
    
        list_grate_min.append(i_grade) if i_grade <= (max(grade)/2) else list_grate_max.append(i_grade)
    
    print(list_grate_min)
    print(list_grate_max)
    
    grade_tpls = (list_grate_min, list_grate_max)
    
    return grade_tpls

list_ = (1, 12, 45, 87, 99, 100, 45, 5, 78)

print(split_list(list_))

# *** 2 вариант
def split_list(grade):
    
    list_grate_min = []
    list_grate_max = []

    sred_grade = sum(grade) / len(grade)
    # print(len(grade), sum(grade), sred_grade)
    
    for i_grade in grade:

        list_grate_min.append(i_grade) if i_grade <= sred_grade else list_grate_max.append(i_grade)

    # print(list_grate_min)
    # print(list_grate_max)

    grade_tpls = (list_grate_min, list_grate_max)

    return grade_tpls


# list_ = (1, 12, 45, 87, 99, 100, 45, 5, 78)

list_ = (1, 12, 3, 5, 24)

print(split_list(list_))
# ***

# 7 задание
# """
#     Є чотирикутна схема польотів дронів з координатами (1, 2, 3, 4). 
#     У нас є словник points, ключі якого — кортежі, точки польоту між координатами чотирикутника, вигляду (1, 2). Значення словника — це відстані між вказаними точками.

#     Приклад:

#     points = {(0, 1): 2, (0, 2): 3.8, (0, 3): 2.7, (1, 2): 2.5, (1, 3): 4.1, (2, 3): 3.9}
#     Напишіть функцію calculate_distance, яка на вхід приймає список координат чотирикутника зі словника виду [0, 1, 3, 2, 0]. 
#     Функція повинна підрахувати, використовуючи вказаний словник, яку загальну відстань пролетить дрон, рухаючись між точками польоту.

#     Примітки:

#         коли беремо у словника points значення, у ключі кортежі завжди має бути першою координата з меншим значенням — (2, 3), але не (3, 2);
#         для порожнього списку та списку з однією координатою функція calculate_distance має повертати 0.
# """

def calculate_distance(coordinates):
    
    sum_rastoynie = 0    
    coordinate1 = coordinate2 = None

    if len(coordinates) <= 1: 
        return 0
    
    for i in coordinates:
    
        if coordinate1 != None and coordinate2 != None:
           
            coordinate1, coordinate2 = coordinate2,  i

            if coordinate1 > coordinate2:
                val_points = points.get((coordinate2, coordinate1))
            else:
                val_points = points.get((coordinate1, coordinate2))
            
            sum_rastoynie += val_points
        else:
            if coordinate1 != None and coordinate2 == None:
                coordinate2 = i 
                
                val_points = points.get((coordinate1, coordinate2))
                sum_rastoynie += val_points
                
            elif coordinate1 == None:
                coordinate1 = i
                
        
    return sum_rastoynie

points = {(0, 1): 2,  (0, 2): 3.8,  (0, 3): 2.7, (1, 2): 2.5,  (1, 3): 4.1, (2, 3): 3.9, }
polet_list = [0, 1, 3, 2, 0]
#  01, 13, 23  02
polet_list1 = []
polet_list2 = [0, ]

# 2 + 4.1 + 3.9 + 3.8 = 13.8 

print(calculate_distance(polet_list))
print(calculate_distance(polet_list1))
print(calculate_distance(polet_list2))
# ***

# 8 задание
# Потрібно написати функцію реалізації наступного ігрового алгоритму. 
# На вхід функції game подається два аргументи: список, що складається зі списків, та початкове значення power - енергія гравця. 
# Внутрішні списки — це списки з числовим значенням енергії, які може поглинути гравець, якщо вони менші або дорівнюють його енергії. 
# Після поглинання елементу списку він рухається за списком далі та, або поглинає список повністю до кінця, або, якщо знаходить енергію вище за власну, 
# залишає його і переходить до наступного списку. Наприкінці обходу всіх списків функція повинна повернути загальну отриману енергію гравця.

# Приклад списку:

# [[1, 1, 5, 10], [10, 2], [1, 1, 1]]
# Для цього списку і початкової енергії рівної 1 гравець поглине з першого списку перші два значення і залишить його, зустрівши значення 5, через те, 
# що на цей момент матиме енергію в 3. Другий список пропустить відразу, а третій повністю поглине та отримає остаточну енергію в 6.

def game(terra, power):
    # power_ = 0
    for i in terra:
        # power_ = power
        for ii in i:
            if ii <= power:
                power += ii
            else:
                break
    return power


# ([[1, 2, 5, 10], [2, 10, 2], [1, 3, 1]], 1) == 11
terra_ = [[1, 1, 5, 10], [10, 2], [1, 1, 1]]
# terra_ = [[1, 2, 5, 10], [2, 10, 2], [1, 3, 1]]
power_ = 1
print(game(terra_, power_))
# ***

# 9 задание
def is_valid_pin_codes(pin_codes):
    
    pin_code_examination = None
    
    pin_code_examination = True if len(pin_codes) != 0 else False 
    
    pin_code_examination = True if len(set(pin_codes)) == len(pin_codes) and pin_code_examination else False
    
    if pin_code_examination:
        
        for pin_item in pin_codes:
            
            #  проверка тип строка и длина 
            pin_code_examination = True if type(pin_item) == str and len(pin_item) == 4 else False
            
            #  проверка что в списке все цыфры
            if pin_code_examination:
                pin_items = set(pin_item)
                for item in pin_item:
                    try:
                        pin_code_examination = True if int(item) else False
                    except:
                        pin_code_examination = False
       
    return pin_code_examination

pin_codes_ = ['1101', '9034', '0011']
pin_codes_1 = ['1101', '9034', '0011', '9034']
pin_codes_2 = ['1101', '9034', '0d11']
pin_codes_3 = ['1101', '9034', '001a']
pin_codes_4 = []
print(is_valid_pin_codes(pin_codes_))
print(is_valid_pin_codes(pin_codes_1))
print(is_valid_pin_codes(pin_codes_2))
print(is_valid_pin_codes(pin_codes_3))
print(is_valid_pin_codes(pin_codes_4))
# ***

# 10 задание
from random import randint

def get_random_password():
    
    pass_ = ''
    
    for i in range(0,8):
        random_num = randint(40,126)
        pass_ += str(chr(random_num))
    
    return pass_

print(get_random_password())
# ***

# 11 задание
from random import randint
def is_valid_password(password):
    
    password_ = True if len(password) >= 8 else False
    
    if password_:
    
        # Прописные буквы
        upper_list = []
        for i in range(65, 91):
            upper_list.append(chr(i))
        # строчные буквы
        lower_list = []
        for i in range(97, 123):
            lower_list.append(chr(i))
        # числа
        numeric_list = []
       
        for i in range(48, 58):
            numeric_list.append(chr(i))
        
        password_upper = password_lower = password_numeric = 0
        
        for item_pass in password:
            if password_upper == 0:
                try:
                    password_upper = upper_list.index(item_pass)
                except:
                    password_upper = 0
            
            if password_lower == 0:
                try:
                    password_lower = lower_list.index(item_pass)
                except:
                    password_lower = 0
            
            if password_numeric == 0:
                try:
                    password_numeric = numeric_list.index(item_pass)
                except:
                    password_numeric = 0
    
        password_ = True if password_upper and password_lower and password_numeric else False
    
    return password_


# password_ = input('Input password: ')
password_ =  'NmlDl1V0'
print(is_valid_password(password_))
# ***

# 12 задание
from random import randint

def get_random_password():
    result = ""
    count = 0
    while count < 8:
        random_symbol = chr(randint(40, 126))
        result = result + random_symbol
        count = count + 1
    return result


def is_valid_password(password):
    has_upper = False
    has_lower = False
    has_num = False

    for ch in password:
        if "A" <= ch <= "Z":
            has_upper = True
        elif "a" <= ch <= "z":
            has_lower = True
        elif "0" <= ch <= "9":
            has_num = True
    if len(password) == 8 and has_upper and has_lower and has_num:
        return True
    return False


def get_password():
    
    count = 0
    
    while count < 100:
        
        result_pass = get_random_password()
        pass_ = is_valid_password(result_pass)
        count += 1 if is_valid_password(get_random_password()) else 0
    
    return result_pass

print(get_password())
# ***

# 13 задание
from pathlib import *

def parse_folder(path):
    files = []
    folders = []
    
    for item in path.iterdir():
        
        folders.append(item.name) if item.is_dir() else files.append(item.name)
    
    return files, folders

path_ = Path('E:\\LessonsPython\\GoIT')
print (parse_folder(path_))
# ***

# 14 задание
# Створіть функцію parse_args, яка повертає рядок, складений з аргументів командного рядка, розділених пробілами. 
# Наприклад, якщо скрипт був викликаний командою: python run.py first second, то функція parse_args повинна повернути рядок наступного виду 'first second'.
import sys

def parse_args():
    
    result = ""
    
    for agr in sys.argv:
        return ' '.join(sys.argv[1:])        
        # result += '' if '.py' in agr else agr + ' '
        # result.strip()
    return result

print (parse_args())

