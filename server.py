import socket
servidor = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# AF_INET = IPV4... SOCK_DGRAM = TIPO UDP
servidor.bind(('localhost',12000))
# '' é o endereço do host, como é local, localhost. 12000 é a porta
# função bind escuta em endereço basicamente.. fica escutando requisições feitas no end. e porta
# ao trabalhar com IPV4, precisamos de um par, especificando host e porta

while True: 
    mensagem_bytes, endereco_ip_cliente = servidor.recvfrom(10) # coloco nas duas variáveis o ip e o pacote de 1024 bytes recebido pelo servidor
    print(mensagem_bytes)
    print(endereco_ip_cliente)
    # mensagem_resposta = mensagem_bytes.decode().upper() # quero enviar o arquivo de volta... mas em UPPER CASE.. como só consigo enviar em bytes, primeiro coloco pra UPPER case
    # input("HEY")
    # servidor.sendto("funcionou".encode(),endereco_ip_cliente) # e agora, coloco pra bytes, especificando o ip do cliente
    # # esse exemplo considera que o server só recebe string