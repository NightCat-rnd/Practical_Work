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

def main_mono_thread():
    count_filenames = [(10,'example1.txt'), (30,'example2.txt'), (200,'example3.txt'), (100,'example4.txt')]
    for count, filenames in count_filenames:
        write_words(count, filenames)

def main_multi_thread():
    count_filenames = [(10, 'example5.txt'), (30, 'example6.txt'), (200, 'example7.txt'), (100, 'example8.txt')]
    threads = [threading.Thread(target=write_words, args=(count, filename)) for count, filename in count_filenames]
    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()


if __name__ == '__main__':
    start_time = perf_counter()
    main_mono_thread()
    end_time = perf_counter()
    print(f'Работа потоков {end_time-start_time:0.2f} секунд')

    start_time = perf_counter()
    main_multi_thread()
    end_time = perf_counter()
    print(f'Работа потоков {end_time - start_time:0.2f} секунд')