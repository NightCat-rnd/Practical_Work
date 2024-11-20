# Домашнее задание по теме "Оператор "with".
# Выполнил Андрей Чекунов
import string

class WordsFinder:
    __file_names = list()
    def __init__(self,*file_names:str):
        for item in file_names:
            self.__file_names.append(item)
        print(self.__file_names)

    def get_all_words(self)->dict:
        return_dict = dict()
        for item in self.__file_names:
            all_words = []
            with open(item, encoding='utf-8') as file:
                str_file = file.read().lower()
                for char in string.punctuation:
                    if char in str_file:
                        str_file = str_file.replace(char, ' ')
                all_words = list(str_file.split())
            return_dict.update({item:all_words})
        return return_dict

    def find(self,word:str)->dict:
        return_dict = dict()
        tmp_dict = self.get_all_words()
        for key, value in tmp_dict.items():
            if word.lower() in value:
                tmp_position = value.index(word.lower())
                return_dict.update({key:tmp_position})
            else:
                tmp_position = None
                return_dict.update({key:tmp_position})
        return return_dict

    def count(self,word:str)->dict:
        return_dict = dict()
        tmp_dict = self.get_all_words()
        for key, value in tmp_dict.items():
            tmp_count = value.count(word.lower())
            return_dict.update({key:tmp_count})
        return return_dict

finder2 = WordsFinder('test_file.txt','test1.py')
print(finder2.get_all_words())  # Все слова
print(finder2.find('TEXT'))  # 3 слово по счёту
print(finder2.count('teXT'))  # 4 слова teXT в тексте всего