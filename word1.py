

def hello():
    print('Hello, команды:\n'
          '1 load filename.txt — загрузить слова из файла filename.txt;\n'
          '2 wordcount червяк — отобразить число раз, которое программа встретила слово «червяк» в загруженных файлах;\n'
          '3 clear-memory — очистить все данные о прочитанных словах из памяти.')


def load():
    with open(filename) as file:
        text = file.read()
    text = text.replace("\n", " ")
    text = text.replace(",", "").replace(".", "").replace("?", "").replace("!", "").replace("—", "")
    text = text.lower()
    words = text.split()

    return print(words)


def wordcount():
    with open(filename) as file:
        text = file.read()
    text = text.replace("\n", " ")
    text = text.replace(",", "").replace(".", "").replace("?", "").replace("!", "").replace("—", "")
    text = text.lower()
    words = text.split()
    print('Введите слово которое нужно посчитать:')
    word = input(str)
    if word in words:
        return print(words.count(word))


def delete():
    exit()


def ask():
    while True:
        print("Введите команду")
        com = input(str)
        if com == 'load':
            load()
        elif com == 'wordcount':
            wordcount()
        elif com == 'clear-memory':
            delete()


while True:
    hello()
    print("Введите название файла")
    filename = input()

    ask()
