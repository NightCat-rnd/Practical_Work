# Домашнее задание по теме "Позиционирование в файле".
# выполнил Андрей Чекунов
import io
def custom_write(file_name:str, strings:list)->dict:
    return_dict = dict()
    file = open(file_name, 'w', encoding='utf8')
    for i, item in enumerate(strings):
        tuple_ = (i+1,file.tell())
        return_dict.update({tuple_:item})
        file.write(item+'\n')
    file.close()
    return return_dict

info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]

result = custom_write('test.txt', info)
for elem in result.items():
    print(elem)