# Функция для шифрования текста
def caesar_cipher(text, shift, lang):
    encrypted_text = ""
    i = 0
    while i < len(text):  # Итерируемся по каждому символу в тексте
        char = text[i]  # Получаем текущий символ
        if char.isalpha():  # Проверяем, является ли смивол буквой
            if lang == 'Ru':
                if char.isupper():  # Проверяем, является ли буква симмволом верхнего регистра
                    encrypted_text += chr((ord(char) - 1040 + shift) % 33 + 1040)
                    # Шифруем символ верхнего регистра с помошью алгоритма Цезаря
                else:
                    encrypted_text += chr((ord(char) - 1072 + shift) % 33 + 1072)
                    # Шифруем символ нижнего регистра с помошью алгоритма Цезаря
            elif lang == 'En':
                if char.isupper():
                    encrypted_text += chr((ord(char) - 65 + shift) % 26 + 65)
                else:
                    encrypted_text += chr((ord(char) - 97 + shift) % 26 + 97)
        else:
            encrypted_text += char
            # Если символ не является буквой, добавляем его без изменений
        i += 1
    return encrypted_text

# Функция для расшифровки текста
def caesar_decipher(text, shift, lang):
    return caesar_cipher(text, -shift, lang)
    # Дешифруем текст, используя отрицательный шаг сдвига

# Функция main() является точкой входа в программу
def main():
    alphabet_ru = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
    alphabet_en = "abcdefghijklmnopqrstuvwxyz"

    text = input("Введите текст: ")
    # Получаем текст от пользователя
    shift = int(input("Введите шаг сдвига: "))
    # Получаем шаг сдвига от пользователя
    lang = input('Выберите язык Ru/En: ')    
    
        if lang == "Ru":
        alphabet = alphabet_ru
    elif lang == "En":
        alphabet = alphabet_en
    else:
        print("Некорректный выбор языка")
        return

    if shift < 1 or shift > len(alphabet):
        print("Ошибка: недопустимый шаг сдвига!")
        return None

    encrypted_text = caesar_cipher(text, shift, lang)  # Шифруем текст
    decrypted_text = caesar_decipher(encrypted_text, shift, lang)  # Дешифруем текст

    print("Зашифрованный текст:", encrypted_text)  # Выводим зашифрованный текст
    print("Расшифрованный текст:", decrypted_text)  # Выводим расшифрованный текст

# Вызываем функцию main() для запуска программы
if __name__ == "__main__":
    main()
