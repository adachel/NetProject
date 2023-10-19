from asyncio import sleep
import socket
import threading  # многопоточность

ya_sock = socket.socket()  # открываем сокет по умолч TCP. В скобках можно менять
addr = ('87.250.250.242', 443)  # адресс это массив ip yandex и порт 443, т.к. TCP
ya_sock.connect(addr)  # коннектим к яндексу

data_out = b"GET / HTTP/1.1\r\nHost:ya.ru\r\n\r\n"  # b - перевод в двоичный код, HTTP запрос, Get - тип запроса, 1.1 - версия, \r\n - перевод каретки
ya_sock.send(data_out)  # отправляем запрос

data_in = b""


def recieving():
    global data_in  # нужна, т.к. data_in лежит вне ф-ции
    while True:
        data_chunk = ya_sock.recv(
            1024)  # перехватываем обратный трафик и записываем в data_in. 1024 - это размер буфера сетевухи
        data_in = data_in + data_chunk


rec_thread = threading.Thread(target=recieving)  # создали поток
rec_thread.start()  # старт потока
sleep(4)  # задержка
print(data_in)

ya_sock.close()  # закрыли сокет