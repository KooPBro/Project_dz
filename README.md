# Программа шифрования и дешифрования текстовых сообщений
Это простая программа, реализованная на языке Python, которая предоставляет возможность шифрования и дешифрования текстовых сообщений с использованием **шифра Цезаря** и **шифра Виженера.**

## Шифр Цезаря
Шифр Цезаря - это метод шифрования, в котором каждая буква в сообщении заменяется другой буквой с фиксированным смещением. Например, если смещение равно 3, то буква "А" будет заменена на "Г", "Б" на "Д", и так далее.

## Шифр Виженера
Шифр Виженера - это полиалфавитный шифр, который использует последовательность ключей для шифрования текста. Каждый символ текста шифруется с помощью соответствующего символа ключа. При дешифровании используется та же последовательность ключей.

## Возможности программы
+ Шифрование текста с помощью шифра Цезаря с заданным ключом.
+ Шифрование текста с помощью шифра Виженера с заданным ключевым словом.
+ Дешифрование текста, автоматически определяя ключ для шифра Цезаря или длину ключа для шифра Виженера.
## Использование
1. Запустите программу, используя интерпретатор Python.
2. Введите текст, который нужно зашифровать или расшифровать.
3. Выберите действие:
   + Для шифрования выберите '1'.
   + Для дешифрования выберите '2'.
4. Если выбрано шифрование:
   +Для шифра Цезаря введите ключ в виде целого числа.
   +Для шифра Виженера введите ключевое слово.
5. Если выбрано дешифрование, программа автоматически определит ключ для шифра Цезаря или длину ключа для шифра Виженера.
6. Программа выведет результат шифрования или дешифрования.
7. Введите 'Да', если текст правильно расшифрован и вы хотите продолжить, или введите любое другое значение, чтобы завершить программу.
## Зависимости
Программа написана на языке Python и не требует установки дополнительных зависимостей.

# Автор
Программа разработана: Студент гр. АСУбз-22-1 Вакулин А.В
