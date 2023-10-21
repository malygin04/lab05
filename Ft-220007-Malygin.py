# Функция для шифрования текста
def caesar_cipher(text, shift):
    encrypted_text = ""
    i = 0
    while i < len(text):  # Итерируемся по каждому символу в тексте
        char = text[i]  # Получаем текущий символ
        if char.isalpha():  # Проверяем, является ли смивол буквой
            if char.isupper():  # Проверяем, является ли буква симмволом верхнего регистра
                encrypted_text += chr((ord(char) - 1040 + shift) % 33 + 1040)
                # Шифруем символ верхнего регистра с помошью алгоритма Цезаря
            else:
                encrypted_text += chr((ord(char) - 1072 + shift) % 33 + 1072)
                # Шифруем символ нижнего регистра с помошью алгоритма Цезаря
        else:
            encrypted_text += char
            # Если символ не является буквой, добавляем его без изменений
        i += 1
    return encrypted_text

# Функция для расшифровки текста
def caesar_decipher(text, shift):
    return caesar_cipher(text, -shift)
    # Дешифруем текст, используя отрицательный шаг сдвига

# Функция main() является точкой входа в программу
def main():
    text = input("Введите текст: ")
    # Получаем текст от пользователя
    shift = int(input("Введите шаг сдвига: "))
    # Получаем шаг сдвига от пользователя

    if shift < 1 or shift > 33:
        # Проверяем, что шаг сдвига находится в допустимых пределах (от 1 до 33)
        print("Ошибка: недопустимый шаг сдвига!")
        return None

    encrypted_text = caesar_cipher(text, shift)  # Шифруем текст
    decrypted_text = caesar_decipher(encrypted_text, shift)  # Дешифруем текст

    print("Зашифрованный текст:", encrypted_text)  # Выводим зашифрованный текст
    print("Расшифрованный текст:", decrypted_text)  # Выводим расшифрованный текст

# Вызываем функцию main() для запуска программы
if __name__ == "__main__":
    main()
