# Больше предыдущего
# На вход программе подается строка текста из натуральных чисел. Из неё формируется список чисел.
# Напишите программу подсчета количества чисел, которые больше предшествующего им в этом списке числа,
# то есть, стоят вслед за меньшим числом. 
# Формат входных данных
# На вход программе подается строка текста из разделенных пробелами натуральных чисел.
# Формат выходных данных
# Программа должна вывести одно число – количество элементов списка, больших предыдущего.
# Тестовые данные
# Sample Input 1:
# 1 2 3 4 5
# Sample Output 1:
# 4
# Sample Input 2:
# 1 1 3 2 2 1 1 1 1
# Sample Output 2:
# 1
# Sample Input 3:
# 5 4 3 2 1
# Sample Output 3:
# 0

number_str = "1 2 3 4 5"
spisok = []
for i in number_str:
    try:
        i = int(i)
        spisok.append(i)
    except:
        continue
count = 0
max = spisok[0]
for i in spisok:
    if i > max:
        max = i
        count += 1
print(f"Количество чисел соответствующих условию: {count}")





# 'a', 'b', 'v', 'g', 'd', 'e', 'zh', 'z', 'i', 'y', 'k', 'l', 'm', 'n', 'o', 'p', 'r', 's', 't', 'u', 'f', 'kh', 'ts', 'ch', 'sh', 'shch', '', 'y', '', 'e', 'yu', 'ya'

# transleterate = \
#   {'а': 'a','б': 'b','в': 'v','г' : 'g','д' : 'd','е' : 'e','ж' : 'zh','з' : 'z','и' : 'i',
#   'й' : 'y','к' : 'k','л' : 'l','м' : 'm','н' : 'n','о' :'o','п' : 'p','р' : 'r','с' : 's',
#   'т' : 't','у' : 'u','ф' : 'f','х' : 'kh','ц' : 'ts','ч' : 'ch','ш' : 'sh','щ' : 'shch',
#   'ь' : '\'','ы' :'y','ъ' : '','э' : 'e','ю' : 'yu','я' : 'ya'}
# text = input('input: ')

# for i in text:
#     print(transleterate[i], end = "")







# aplphabetE = \
# ['a', 'b', 'v', 'g', 'd', 'e', 'yo', 'zh', 'z', 'i', 'y', 'k', 'l', 'm', 'n', 'o', 'p','r', 
# 's', 't', 'u', 'f', 'kh', 'ts', 'ch', 'sh', 'shch', '', 'y', '\'', 'e', 'yu', 'ya']

# aplphabetR = \
# ['а', 'б', 'в', 'г', 'д', 'е', 'ё', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 
# 'с', 'т', 'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я']

# base = input('Введите слово: ')
# word=[]

# for i in range(len(base)):
#     word.append(aplphabetR.index(base[i]))
#     index = word[i]
#     print(aplphabetE[index], end='')







# for i in range(len(base)):
#     print(base[i].replace(aplphR[aplphR.index(base[i])],aplphE[aplphR.index(base[i])]), end = '')
