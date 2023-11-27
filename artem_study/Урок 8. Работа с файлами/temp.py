def copy_line(source_file, destination_file, line_number):
    try:
        with open(source_file, 'r') as source:
            lines = source.readlines()
            if 1 <= line_number <= len(lines):
                line_to_copy = lines[line_number - 1]
                with open(destination_file, 'a') as destination:
                    destination.write(line_to_copy)
                print(f"Строка {line_number} скопирована из {source_file} в {destination_file}.")
            else:
                print("Недопустимый номер строки.")
    except FileNotFoundError:
        print("Один из файлов не найден.")

if __name__ == "__main__":
    source_file = input("Введите имя исходного файла: ")
    destination_file = input("Введите имя файла, в который нужно скопировать строку: ")
    line_number = int(input("Введите номер строки для копирования: "))

    copy_line(source_file, destination_file, line_number)
