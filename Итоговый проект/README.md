## Задание
____

+ Вам необходимо написать программу, которая будет читать файл (текстовый файл находится в ZIP архиве task_file.txt.zip ) хранящий сведения о сотрудниках и формировать на основе его данных почтовые адреса для сотрудников, генерировать пароли безопасности для входа в почту, заносить информацию в этот файл и перезаписывать его.

#### Этапы выполнения работы:

1. В данном упражнении вам необходимо написать функцию, которая будет генерировать надежный пароль случайным образом (для написания такой функции можно использовать модуль random).

    + Отметим, что пароль считается надежным, если его длина составляет не менее 12 символов, при этом он должен содержать хотя бы одну заглавную букву, хотя бы одну строчную букву, хотя бы одну цифру и хотя бы один спецсимвол.

2. Текстовый файл находится в ZIP архиве (task_file.txt.zip), вам необходимо скачать его, распаковать и переместить текстовый документ в папку, где будет лежать файл с программой для решения данной задачи.  
   - Файл представляет собой список данных людей со следующими заголовками:  
EMAIL	NAME	LAST_NAME	TEL	CITY
 
   - Столбец EMAIL пустой у всех. Остальные позиции могут быть заполнены или нет.
   
    *Представим следующую ситуацию: вы являетесь сотрудником IT отдела некой компании. Ваша компания открывает новый филиал с переводом необходимого количества сотрудников из разных городов. Новый филиал имеет свой почтовый домен. Вам, как сотруднику IT отдела, необходимо создать каждому сотруднику, переходящему в новый филиал, свой уникальный почтовый адрес. У вас есть неотформатированный список сотрудников, который заполняли недобросовестно.*
    + Программа должна читать исходный текстовый файл  
    
    + Программа должна содержать функцию (представленную ниже), которая по имени и фамилии сотрудника составляет его уникальный почтовый адресов

    *Функция принимает список списков [['Имя_1', 'Фамилия_1'], ['Имя_2', 'Фамилия_2'], ['Имя_3', 'Фамилия_3']] из имен и фамилий list_of_names. Далее создается пустой список emails, который в ходе выполнения, заполнится почтовыми адресами. Запускается цикл для каждого списка из имени и фамилии ['Имя_1', 'Фамилия_1']. Устанавливается окончание среза letter = 1. Далее проходит проверка на совпадение, если в списке адресов уже есть такой же адрес (например имя и фамилия сотрудников совпадают), то срез i[0][0:letter] увеличивается на 1 символ. После в список адресов добавляется новый адрес. Адреса присваиваются пользователям по следующей формуле: берется фамилия сотрудника, добавляется точка, затем добавляется первая буква имени и остаточная часть '@company.io'. Если имена и фамилии сотрудников совпадают, к первой букве имени добавляется вторая и т.д.*

    ##### Пример выполнения:

    print(email_gen([['Ivan', 'Petrov'], ['Ivan', 'Petrov'], ['Ivan', 'Petrov']]))  
    ['Petrov.I@company.io', 'Petrov.Iv@company.io', 'Petrov.Iva@company.io'] 

3. Ваша программа должна очистить файл от всех невалидных данных (строки с пустыми данными, некорректными именами, некорректными телефонами и городами) должны удаляться из него и сохраняться в отдельный текстовый файл.

4. Поиск информации в файле должен осуществляться с помощью регулярных выражений.

5. Сгенерированные пароли должны заноситься в исходный файл в отдельный столбец "PASSWORD".



