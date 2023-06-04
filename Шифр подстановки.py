# Функция для шифрования текста с помощью шифра Цезаря
def caesar_encrypt(text, key):
    encrypted_text = ""

    # Итерация по каждому символу в тексте
    for char in text:
        if char.isalpha():  # Проверка, является ли символ буквой
            if char.isupper():  # Проверка, является ли буква заглавной
                # Шифрование заглавных букв
                encrypted_text += chr((ord(char) - ord('А') + key) % 32 + ord('А'))
            else:
                # Шифрование строчных букв
                encrypted_text += chr((ord(char) - ord('а') + key) % 32 + ord('а'))
        else:
            # Добавление символа без шифрования (не является буквой)
            encrypted_text += char

    return encrypted_text


# Функция для дешифрования текста с помощью шифра Цезаря
def caesar_decrypt(text):
    decrypted_text = ""

    # Попытка расшифровать текст с разными ключами
    for key in range(32):
        # Вызов функции шифрования с отрицательным ключом для дешифрования
        decrypted_text = caesar_encrypt(text, -key)
        print(f"Попытка с ключом {key}: {decrypted_text}")

        # Запрос подтверждения пользователя о правильности расшифровки
        choice = input("Если текст правильно расшифрован, введите 'Да'. В противном случае нажмите Enter для продолжения попыток: ")
        if choice.lower() == 'да':
            break

    return decrypted_text


# Функция для шифрования текста с помощью шифра Виженера
def vigenere_encrypt(text, key):
    encrypted_text = ""

    key = key.upper()  # Приведение ключа к верхнему регистру
    key_index = 0

    # Итерация по каждому символу в тексте
    for char in text:
        if char.isalpha():  # Проверка, является ли символ буквой
            if char.isupper():  # Проверка, является ли буква заглавной
                # Шифрование заглавных букв
                encrypted_text += chr((ord(char) - ord('А') + ord(key[key_index]) - ord('А')) % 32 + ord('А'))
            else:
                # Шифрование строчных букв
                encrypted_text += chr((ord(char) - ord('а') + ord(key[key_index]) - ord('А')) % 32 + ord('а'))

            key_index = (key_index + 1) % len(key)  # Переход к следующему символу ключа
        else:
            # Добавление символа без шифрования (не является буквой)
            encrypted_text += char

    return encrypted_text


# Функция для дешифрования текста с помощью шифра Виженера
def vigenere_decrypt(text):
    decrypted_text = ""
    key_length = 0

    # Определение длины ключа
    for char in text:
        if char.isalpha():
            key_length += 1

    # Попытка расшифровать текст с разными длинами ключей
    for key_length in range(1, key_length + 1):
        decrypted_text = vigenere_decrypt_with_key_length(text, key_length)
        print(f"Попытка с длиной ключа {key_length}: {decrypted_text}")

        # Запрос подтверждения пользователя о правильности расшифровки
        choice = input("Если текст правильно расшифрован, введите 'Да'. В противном случае нажмите Enter для продолжения попыток: ")
        if choice.lower() == 'да':
            break

    return decrypted_text


# Вспомогательная функция для дешифрования текста с определенной длиной ключа
def vigenere_decrypt_with_key_length(text, key_length):
    decrypted_text = ""
    key_index = 0
    key = ""

    # Создание ключа путем повторения символов из текста
    for char in text:
        if char.isalpha():
            key += text[key_index]
            key_index = (key_index + 1) % key_length

    key = key.upper()  # Приведение ключа к верхнему регистру
    key_index = 0

    # Итерация по каждому символу в тексте
    for char in text:
        if char.isalpha():  # Проверка, является ли символ буквой
            if char.isupper():  # Проверка, является ли буква заглавной
                # Дешифрование заглавных букв
                decrypted_text += chr((ord(char) - ord('А') - (ord(key[key_index]) - ord('А'))) % 32 + ord('А'))
            else:
                # Дешифрование строчных букв
                decrypted_text += chr((ord(char) - ord('а') - (ord(key[key_index]) - ord('А'))) % 32 + ord('а'))

            key_index = (key_index + 1) % key_length  # Переход к следующему символу ключа
        else:
            # Добавление символа без дешифрования (не является буквой)
            decrypted_text += char

    return decrypted_text


# Основная часть программы
text = input("Введите текст: ")

while True:
    action_choice = input("Выберите действие (1 - Зашифровать, 2 - Дешифровать): ")

    if action_choice == '1':
        encryption_choice = input("Выберите шифр (1 - Шифр Цезаря, 2 - Шифр Виженера): ")
        if encryption_choice == '1':
            key = int(input("Введите ключ для шифра Цезаря (целое число): "))
            result = caesar_encrypt(text, key)
        elif encryption_choice == '2':
            key = input("Введите ключ для шифра Виженера (слово): ")
            result = vigenere_encrypt(text, key)
        else:
            print("Некорректный выбор шифра.")
            continue
    elif action_choice == '2':
        decryption_choice = input("Выберите шифр для дешифрования (1 - Шифр Цезаря, 2 - Шифр Виженера): ")
        if decryption_choice == '1':
            result = caesar_decrypt(text)
        elif decryption_choice == '2':
            result = vigenere_decrypt(text)
        else:
            print("Некорректный выбор шифра.")
            continue
    else:
        print("Некорректный выбор действия.")
        continue

    print("Результат:", result)

    choice = input("Хотите продолжить? (Введите 'Да' для продолжения, любое другое значение для выхода): ")
    if choice.lower() != 'да':
        break
