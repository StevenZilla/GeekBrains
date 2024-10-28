# Определение русского алфавита, включая букву 'ё'
alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'

# Функция для шифрования текста по методу Цезаря
def caesar_cipher(string, user_shift):
    
    # Создание списка зашифрованных символов
    char_list = [(alphabet[(alphabet.index(sym) + user_shift % len(alphabet)]
                       if sym in alphabet else sym)
              for sym in string]

    # Преобразование списка символов в строку
    new_str = ''.join(char_list)
    return new_str

# Ввод пользователем исходного сообщения и сдвига
input_str = input('Введите сообщение: ')
shift = int(input('Введите сдвиг: '))
# Шифрование сообщения
output_str = caesar_cipher(input_str, shift)

# Вывод зашифрованного сообщения
print('Зашифрованное сообщение:', output_str)
