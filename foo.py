import socket

cliente = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while True:
    mensagem_envio = input("Digite o nome do arquivo: ")
    with open(mensagem_envio, "rb") as f:
        data = f.read()
        print(data)
        cliente.sendto(data, ("localhost", 12000))
        mensagem_bytes, endereco_ip_servidor = cliente.recvfrom(1024)
        print(mensagem_bytes.decode())

    input("Pressione Enter para sair...")
