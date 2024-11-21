import os, time
os.chdir(os.getcwd() + '/test')
for root, dirs, files in os.walk(os.getcwd()):
    #print(f'{root}, {dirs}, {files}')
    for file in files:
        filepath = os.path.abspath(file)
        filetime = os.path.getmtime(file)
        formatted_time = time.strftime("%d.%m.%Y %H:%M", time.localtime(filetime))
        filesize = os.path.getsize(file)
        parent_dir = os.path.dirname(os.getcwd())
        print(f'Обнаружен файл: {file}, Путь: {filepath}, Размер: {filesize} байт, Время изменения: {formatted_time}, Родительская директория: {parent_dir}')
