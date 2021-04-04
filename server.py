from socket import *

sockobj = socket(AF_INET, SOCK_STREAM)
sockobj.bind(('', 5400))
sockobj.listen(5)
while True:
    connection, address = sockobj.accept()  # ждем сообщение от клиента, устонавливаем соединение с клиентом, получаем ip адрес

    bin_data = connection.recv(1024)  # количество байтов
    str_data = bin_data.decode('utf-8')
    ip_addr = address[0]  # ip адрес
    ip_dict = {'192.168.1.60': 'ruslan',
               '192.168.1.61': 'Я',
               '192.168.1.64': 'Arthur',
               '192.168.1.69': 'Tumur',
               '192.168.1.35': 'Matvey'}

    print("Я получил сообщение от " + str_data + "\n" +  "От: " + ip_dict[ip_addr] + "\n")

    if str_data == 'привет':
        connection.send('Приветствую!'.encode('utf-8'))

    if str_data == 'пока':
        connection.send('Досвидания!'.encode('utf-8'))

    if str_data == 'спасибо':
        connection.send('Всегда пожалуйста!'.encode('utf-8'))

    str_answer = 'я получил: ' + str_data + '\n' + 'Длинной ' + str(len(str_data)) + ' байт'

    connection.send(str_answer.encode('utf-8'))

    connection.close()
