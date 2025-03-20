# my bad solution 1
# 
# file_name = input('Enter file name: ')
# file_handler = open(file_name)
# lyrics = list()
# counter = 0
# for lines in file_handler:
#     line = lines.strip()
#     word = line.split()
#     lyrics.append(word)
#     counter += 1
 
# print(counter)#using counter variable
# print(len(lyrics))#using built-in method

    
# better solution 1
    
# file_name = input('Enter file name: ')
# file_handler = open(file_name)

# word_count = 0  # Лічильник слів

# for line in file_handler:
#     words = line.split()  # Розбиваємо рядок на слова
#     word_count += len(words)  # Додаємо кількість слів у рядку

# file_handler.close()  # Закриваємо файл
# print(f'Total word count: {word_count}')


# 2

# file_name = input('Enter file name: ')
# file_handler = open(file_name)

# often_words = dict()
# tpl = list()

# for line in file_handler:
#     words = line.split()  # Розбиваємо рядок на слова
    

#     for word in words:       
    
#         often_words[word] = often_words.get(word, 0) + 1

    
# for keys, values in often_words.items():
#     tpl.append((values, keys))
    
# tpl = sorted(tpl, reverse=True)

# often_words = dict(tpl)
# for keys, values in tpl[:5]:
#     print(keys, values)

# file_handler.close()  # Закриваємо файл

# pro solution with collections and counter
# from collections import Counter

# file_name = input('Enter file name: ')
# file_handler = open(file_name)

# word_count = Counter()

# for line in file_handler:
#     words = line.lower().split()  # Приводимо до нижнього регістру і розбиваємо
#     word_count.update(words)  # Додаємо слова в лічильник

# file_handler.close()  # Закриваємо файл

# # Отримуємо 5 найчастіших слів
# top_words = word_count.most_common(5)

# # Виводимо результат
# for word, count in top_words:
#     print(count, word)



# 3 my solution: (before i learn lambda it's the best solution!)


# file_name = input('Enter file name: ')
# file_handler = open(file_name)

# emails = dict()

# for line in file_handler:
#     if not line.startswith("From "): continue
#     line = line.rstrip().split()
#     email = line[1]    
#     emails[email] = emails.get(email, 0) + 1
    
# biggest_email = None
# biggest_count = None

# for email, value in emails.items():
#     if biggest_count is None or value > biggest_count:
#         biggest_count = value
#         biggest_email = email
        
# print(f"Most frequent email: {biggest_email}, {biggest_count} times")

# giga solution: (with unknown lambda)

# from collections import Counter

# file_name = input('Enter file name: ')

# with open(file_name) as file_handler:
#     emails = Counter(line.split()[1] for line in file_handler if line.startswith("From "))

# # Знаходимо email з найбільшою кількістю повторень
# biggest_email, biggest_count = max(emails.items(), key=lambda x: x[1])

# print(f"Most frequent email: {biggest_email}, {biggest_count} times")



# 4 my solution:

# file_name = input('Enter file name: ')
# file_handler = open(file_name)

# times = dict()
# clock = list()

# for line in file_handler:
#     if not line.startswith("From "): continue
#     line = line.rstrip()
#     words = line.split()
#     separator = line.find(":")
#     time = line[separator-2:separator]
#     times[time] = times.get(time, 0) + 1
    
# for keys, values in times.items():
#     clock.append((keys, values))
# clock = sorted(clock)
# times = clock
# for keys, values in clock:
#     print(keys, values)


# giga solution:
    
# file_name = input('Enter file name: ')  

# with open(file_name) as file_handler:
#     times = dict()

#     for line in file_handler:
#         if not line.startswith("From "): 
#             continue
#         words = line.split()
#         time = words[-2].split(":")[0]  # Отримуємо години (HH) через split(":") 
#         times[time] = times.get(time, 0) + 1  

# # Сортуємо за ключами (годинами) і виводимо
# for hour, count in sorted(times.items()):
#     print(hour, count)

# def bmi(weight, height):    
#     bmi = weight / (height * height)
#     if bmi <= 18.5:
#         return "Underweight"
#     elif bmi <= 25:
#         return "Normal"
#     elif bmi <= 30:
#         return "Overweight"
#     elif bmi > 30:
#         return "Obese"


# def remove_char(s):
#     if len(s) > 2:
#         s = s[1:len(s)-1]
#         return s
#     else:
#         return ""
    
# def find_average(numbers):
#     avg = sum(numbers)/len(numbers)
#     return avg


# def get_turkish_number(num):
#     iter = 0
#     turk = ['sıfır', 'bir', 'iki', 'üç', 'dört', 'beş', 'altı', 'yedi', 'sekiz', 'dokuz']
#     for i in turk:
#         print(i, iter)
#         iter+=1
        
    
    
# iter = 0
# turk = ['sıfır', 'bir', 'iki', 'üç', 'dört', 'beş', 'altı', 'yedi', 'sekiz', 'dokuz']
# for i in turk:
#     print(i, iter)
#     iter+=1
            

# def summation(num):
#     for i in range(num):
#         num += i
#     return num

# print(summation(int(input())))
        
        
# def human_years_cat_years_dog_years(human_years):
#     cat_years = 0
#     dog_years = 0
#     if human_years == 1:
#         cat_years = 15
#         dog_years = 15
#     elif human_years == 2:
#         cat_years = 24
#         dog_years = 24
#     elif human_years > 2:
#         cat_years = 24 + (human_years - 2) * 4
#         dog_years = 24 + (human_years - 2) * 5
    
    
    
    
#     return [human_years, cat_years, dog_years]

# print(human_years_cat_years_dog_years(int(input())))

# we have given numbers in input. we must return reversed numbers in list
# def digitize(n):
#     return [int(x) for x in str(n)][::-1]

# print(digitize(int(input())))