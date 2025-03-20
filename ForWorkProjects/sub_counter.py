import instaloader
import time

def get_followees(profile):
    subscriptions = []
    try:
        for followee in profile.get_followees():
            subscriptions.append(followee.username)
            time.sleep(2)  # Додаємо паузу в 2 секунди між запитами
    except instaloader.exceptions.ConnectionException as e:
        print(f"Помилка з'єднання: {e}")
    except instaloader.exceptions.ProfileNotExistsException:
        print("Профіль не існує або закритий.")
    except Exception as e:
        print(f"Невідома помилка: {e}")
    return subscriptions

# Створюємо екземпляр Instaloader
L = instaloader.Instaloader()

# Авторизуємося (введіть свій логін та пароль)
USERNAME = ''
PASSWORD = ''
L.login(USERNAME, PASSWORD)

# Отримуємо профіль іншого користувача
TARGET_USERNAME = ''
profile = instaloader.Profile.from_username(L.context, TARGET_USERNAME)

# Отримуємо список підписок
subscriptions = get_followees(profile)

# Зберігаємо список підписок у файл
with open(f'{TARGET_USERNAME}_subscriptions.txt', 'w') as file:
    for username in subscriptions:
        file.write(f"{username}\n")

print(f"Список підписок користувача {TARGET_USERNAME} збережено у файлі {TARGET_USERNAME}_subscriptions.txt")
