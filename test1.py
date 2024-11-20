import string
#string.punctuation
# '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'
# text
all_words = []
with open('test.py', encoding='utf-8') as file:
    str_file = file.read().lower()
    print(str_file)
    for p in string.punctuation:
        if p in str_file:
            # банальная замена символа в строке
            str_file = str_file.replace(p, ' ')
    all_words = list(str_file.split())
print(all_words)