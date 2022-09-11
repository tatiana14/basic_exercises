# Вывести последнюю букву в слове
word = 'Архангельск'
print("====== Task1 ======")
print(word[-1])

# Вывести количество букв "а" в слове
word = 'Архангельск'
print("====== Task2 ======")
print(word.lower().count('а'))

# Вывести количество гласных букв в слове
word = 'Архангельск'
vowels = set("аоыэуеюия")
count = 0
for letter in word.lower():
    if letter in vowels:
        count += 1
print("====== Task3 ======")
print(count)

# Вывести количество слов в предложении
sentence = 'Мы приехали в гости'
words = sentence.split(' ')
print("====== Task4 ======")
print(len(words))

# Вывести первую букву каждого слова на отдельной строке
sentence = 'Мы приехали в гости'
words = sentence.split(' ')
print("====== Task5 ======")
for word in words:
    print(word[0])

# Вывести усреднённую длину слова в предложении
sentence = 'Мы приехали в гости'
words = sentence.split(' ')
avg = sum(len(word) for word in words)/len(words)
print("====== Task6 ======")
print(avg)
