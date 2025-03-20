import os
import shutil
import pandas as pd

# Запитати користувача шлях до папки з PDF-файлами
source_dir = input("Введіть шлях до папки з PDF-файлами: ").strip()

# Перетворити шлях у сирий рядок
source_dir = r"{}".format(source_dir)

# Зчитати таблицю з файлами
files_df = pd.read_csv('C:\\Users\\user\\Desktop\\test_py\\test_24.07.2024\\test_4.csv')

# Перебір файлів у таблиці
for filename in files_df['filenames']:
    # Шлях до файлу
    file_path = os.path.join(source_dir, filename)
    
    # Цільова папка (створюємо папку з ім'ям файлу без розширення)
    folder_name = os.path.splitext(filename)[0]
    target_folder = os.path.join(source_dir, folder_name)
    
    # Перевірка, чи існує цільова папка, якщо ні - створити її
    if not os.path.exists(target_folder):
        os.makedirs(target_folder)
    
    # Шлях до переміщеного файлу
    target_path = os.path.join(target_folder, filename)
    
    # Переміщення файлу
    if os.path.exists(file_path):
        shutil.move(file_path, target_path)
        print(f"Переміщено {filename} до {target_folder}")
    else:
        print(f"Файл {filename} не знайдено у папці {source_dir}")

print("Всі файли переміщено!")
