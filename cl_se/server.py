# Программа сервера для получения приветствия от клиента и отправки ответа
from socket import *
import time
import sys
import argparse
import pickle

def createParser ():
    parser = argparse.ArgumentParser()
    parser.add_argument ('-p', '--port', nargs='?', type=int, default=7777)# порт для работы
    parser.add_argument ('-a', '--addr', nargs='?', default='')# адрес прослушивания
    return parser

s = socket(AF_INET, SOCK_STREAM)  # Создает сокет TCP

parser = createParser()
namespace = parser.parse_args(sys.argv[1:])

s.bind((namespace.addr, namespace.port))# Присваивает порт
s.listen(5)                       # Переходит в режим ожидания запросов;
                                  # Одновременно обслуживает не более
                                  # 5 запросов.
while True:
    client, add_r = s.accept()
    data = client.recv(1024)
    print(pickle.loads(data))
    
    response = {
        "response": 200,
        "alert":"Необязательное сообщение/уведомление"
    }

    client.send(pickle.dumps(response))
    client.close()
    