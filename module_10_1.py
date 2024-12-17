# Домашнее задание по теме "Введение в потоки".
# выполнил Андрей Чекунов

from time import sleep, perf_counter
import threading

def write_words(word_count:int, file_name:str):
    with open(file_name,'w') as fp:
        for i in range(word_count):
            fp.write(f'Какое-то слово №{i+1}\n')
            sleep(0.1)
        print(f'Завершилась запись в файл {file_name}')

if __name__ == '__main__':
    time_start = perf_counter()
    write_words(10, 'example1.txt')
    write_words(30, 'example2.txt')
    write_words(200, 'example3.txt')
    write_words(100, 'example4.txt')
    time_end = perf_counter()
    print(f'Работа потоков {time_end - time_start:0.2f} секунд')

    time_start = perf_counter()
    thread1 = threading.Thread(target=write_words, args=(10, 'example5.txt'))
    thread2 = threading.Thread(target=write_words, args=(30, 'example6.txt'))
    thread3 = threading.Thread(target=write_words, args=(200, 'example7.txt'))
    thread4 = threading.Thread(target=write_words, args=(100, 'example8.txt'))
    thread1.start()
    thread2.start()
    thread3.start()
    thread4.start()
    thread1.join()
    thread2.join()
    thread3.join()
    thread4.join()
    time_end = perf_counter()
    print(f'Работа потоков {time_end - time_start:0.2f} секунд')
