import re
import zipfile
import random
import string

# 1. Открытие ZIP-архива и извлечение файла

with zipfile.ZipFile('task_file.txt.zip', 'r') as zip_file:
    zip_file.extractall()
    file_path = zip_file.extract('task_file.txt')

# 1.1 Чтение данных из файла

lst = []
with open('task_file.txt', 'r') as f:
    for line in f:
        lst.append(line.rstrip().split(","))
print(f"Всего строк с данными в исходном файле = {len(lst) - 1}")

# 1.2 Валидация данных

result_lst = []
error_lst = []
for i in range(1, len(lst)):
    if re.match(r"^[A-Z]{1}[a-z]{2,}", lst[i][1].strip()) \
            and re.match(r"^[A-Z]{1}[a-z]{2,}", lst[i][2].strip())\
            and len(lst[i][3].strip()) >= 7\
            and not re.match(r"^[0]{1,}", lst[i][3].strip())\
            and lst[i][3].strip().isdigit():
        result_lst.append(lst[i])
    else:
        error_lst.append(lst[i])

for i in range(len(result_lst)):
    for j in range(5):
        result_lst[i][j] = result_lst[i][j].replace(" ", "")

print(f"Всего строк с корректными данными = {len(result_lst)}")
print(f"Всего строк с ошибками = {len(error_lst)}")

# 2. Формирование почтовых адресов на основе ФИО

def email_gen(list_of_names):
    emails = []
    for i in list_of_names:
        letter = 1
        while i[2] + '.' + i[1][0:letter] + '@company.io' in emails:
            letter += 1
        emails.append(i[2] + '.' + i[1][0:letter] + '@company.io')
    return emails

emails = email_gen(result_lst)


# 3. Генерация паролей безопасности

def generate_password(letters=8, digits=2, punctuation=2):
    password = list(random.choice(string.ascii_letters) for i in range(letters))
    password += list(random.choice(string.digits) for i in range(digits))
    password += list(random.choice('!#$%^&*()_-+=[]{}\|/?><.') for i in range(punctuation))
    password = random.sample(password, len(password))
    return ''.join(password)

# 4. Сохранить информацию в файл

# 4.1. Сохранить данные с ошибками
with open('error_file.txt', 'wt') as f:
    print("EMAIL, NAME, LAST_NAME, TEL, CITY", file=f)
    for i in range(len(error_lst)):
        print(f"{error_lst[i][0]}, {error_lst[i][1]}, {error_lst[i][2]}, {error_lst[i][3]}, {error_lst[i][4]}", file=f)
    print(f"Данные с ошибками сохранены в файл error_file.txt, всего строк = {len(error_lst)}")

with open('result_file.txt', 'wt') as f:
    print("EMAIL, PASSWORD, NAME, LAST_NAME, TEL, CITY", file=f)
    for i in range(len(result_lst)):
        print(f"{emails[i]}, {generate_password()}, {result_lst[i][1]}, {result_lst[i][2]}, {result_lst[i][3]}, {result_lst[i][4]}", file=f)
    print(f"Данные с e-mail и password сохранены в файл result_file.txt, всего строк = {len(result_lst)}")