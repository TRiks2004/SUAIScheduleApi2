from loguru import logger
import zipfile

import os

directory = 'logger/log'

import asyncio
import json

async def get_list_logs() -> list[dict]:
    di = []

    # Получаем все корни, директории и файлы
    for root, directories, files in os.walk(directory):
        for file in files:
            # Получаем полный путь к файлу
            file_path = os.path.join(root, file)
            
            # Получаем тип файла (расширение)
            file_extension = os.path.splitext(file_path)[1]

            # Получаем название файла (без расширения)
            file_name = os.path.splitext(file)[0]
            
            di.append(
                {
                    'name':file_name,
                    'type':file_extension,
                    'full_path':file_name + file_extension
                }
            )

    return di

async def get_log_file(name: str) -> dict:
    file_extension = os.path.splitext(name)[1]
    file_name = os.path.splitext(name)[0]


    if file_extension == '.zip':
        with zipfile.ZipFile(directory + '/' + name, 'r') as zip_ref:
            # Прочитываем содержимое файла в память
            with zip_ref.open(file_name) as file:
                # Читаем содержимое файла
                re = file.read().decode('utf-8')
    elif file_extension == '.json':
        with open(directory + '/' + name, 'r') as file:
            # Читаем содержимое файла
            re = file.read()

    return json.loads('{\"body\": [' + ','.join(re.split('\n')[:-1]) + ']}')







