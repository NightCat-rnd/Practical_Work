# Домашнее задание по теме "Многопроцессное программирование"
# выполнил Андрей Чекунов

import time
import multiprocessing

def read_info(name:str):
    all_data = []
    with open(name,'r') as fp:
        line = True
        while line:
            line = fp.readline()
            all_data.append(line)
    #print(all_data)

if __name__ == '__main__':
    filenames = [f'./file {number}.txt' for number in range(1,5)]
    start_time = time.perf_counter()
    for item in filenames:
        read_info(item)
    end_time = time.perf_counter()
    print(f'Время последовательного выполнения: {end_time-start_time:0.2f} секунд')

    start_time = time.perf_counter()
    with multiprocessing.Pool() as pool:
        pool.map(read_info, filenames)
    end_time = time.perf_counter()
    print(f'Время параллельного выполнения: {end_time - start_time:0.2f} секунд')


