3. Строки и обработка текста

1. В заданном предложении найти пару слов, из которых
одно является обращением другого.

sentence = input("Введите предложение: ")
words = sentence.split()

# Очищаем слова от знаков препинания
clean_words = []
for w in words:
    clean_words.append(w.strip(".,!?;:").lower())

# Ищем пары
for i in range(len(clean_words)):
    for j in range(i + 1, len(clean_words)):
        word1 = clean_words[i]
        word2 = clean_words[j]
        if word1 == word2[::-1]:
            print("Пара:", word1, "и", word2)

            
2. Дан email в строке. Определить, является ли он корректным
(наличие символа @ и точки, наличие не менее двух символов
 после последней точки и т.д.).

email = input("Введите email: ").strip()

if "@" in email and "." in email:
    parts = email.split("@")
    # Проверяем, что ровно один символ @ и домена не пуста
    if len(parts) == 2 and parts[0] != "" and "." in parts[1]:
        domain_parts = parts[1].split(".")
        # Проверяем, что после последней точки хотя бы 2 символа
        if len(domain_parts[-1]) >= 2:
            print("Email корректен")
        else:
            print("Email некорректен")
    else:
        print("Email некорректен")
else:
    print("Email некорректен")

    
3. Дана строка. Определите, является ли она действительным числом.

s = input("Введите строку: ").strip()

try:
    val = float(s)
    print("Это действительное число")
except ValueError:
    print("Это НЕ действительное число")

    
4. Удалите в строке все символы "!".

s = input("Введите строку: ")
result = s.replace("!", "")
print("Результат:", result)

5. Дана строка, содержащая полное имя файла
(например, 'c:\WebServers\home\testsite\www\myfile.txt').
Выделите из этой строки имя файла без расширения.

path = r"c:\WebServers\home\testsite\www\myfile.txt"

# Заменяем обратные слэши на прямые и разделяем по '/'
filename = path.replace("\\", "/").split("/")[-1]  # myfile.txt

# Отделяем название от расширения
name_only = filename.split(".")[0]                  # myfile

print("Имя файла без расширения:", name_only)

6. ан текст. Заменить все цифры соответствующими словами.

digits_words = ["ноль", "один", "два", "три", "четыре", "пять", "шесть", "семь", "восемь", "девять"]

text = input("Введите текст: ")
result = ""

for char in text:
    if char.isdigit():
        result += digits_words[int(char)] + " "
    else:
        result += char

print("Результат:", result)

7. Дано натуральное число. Получить строку, в которой
тройки цифр этого числа разделены пробелом, начиная
с правого конца (например, 1234567 $\rightarrow$ 1 234 567).

n = int(input("Введите число: "))

# Форматирование с разделением тысяч встроенными средствами Python
result = f"{n:,}".replace(",", " ")
print("Результат:", result)