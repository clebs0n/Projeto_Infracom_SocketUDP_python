import socket
size = 10

cliente = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # ambos cliente e server precisam ser udp
# não preciso fazer handshaking por que to usando UDP

while True :
    nome_arq = input("Digite o nome do arquivo: ")
    cliente.sendto(nome_arq.encode(), ("localhost", 12000))

    try:
        f = open(nome_arq, "rb")
        data = f.read(size)
        while data:
             if(cliente.sendto(data, ("localhost", 12000))):
                  print("enviando...")
                  data = f.read(size)
             
    except IOError:
            print("Tente novamente:(")

    # resposta_bytes, endereco_ip_servidor = cliente.recvfrom(1024)
    # print(resposta_bytes.decode())
    input("Pressione qualquer tecla para sair")
    cliente.close()
    f.close()
