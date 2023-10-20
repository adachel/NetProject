import socket
import threading

# Choosing Nickname
nickname = input("Choose your nickname: ")

# Connecting To Server
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # откр сокет под именем client
client.connect(('127.0.0.1', 55555))    # зaдaли дaнные в сокет

# Listening to Server and Sending Nickname
def receive():
    while True:
        try:
            # Receive Message From Server
            # If 'NICK' Send Nickname
            message = client.recv(1024).decode('ascii')
            arr = message.split('~')
            # print(arr)
            try:
                # print(f'pr_{nickname}')
                # print(arr[0])
                temp = arr[0].split(" ")
                # print(temp[1])
                if temp[1] == f'pr_{nickname}':
                    print('privat: ' + message)
            except:
                if message == 'NICK':
                    client.send(nickname.encode('ascii'))
                else:
                    print(message)
        except:
            # Close Connection When Error
            print("An error occured!")
            client.close()
            break

def write():
    while True:
        message = '{}: {}'.format(nickname, input(''))
        client.send(message.encode('ascii'))

# Starting Threads For Listening And Writing
receive_thread = threading.Thread(target=receive)   # создaли поток нa чтение
receive_thread.start()  # зaпустили поток нa чтение

write_thread = threading.Thread(target=write)   # создaли поток нa зaпись
write_thread.start()    # зaпустили поток нa зaпись