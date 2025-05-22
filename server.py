import socket
import serial
import time

# Configuração da porta serial
serial_port_name = '/dev/ttyACM0' 
serial_port = serial.Serial(serial_port_name, 9600, timeout=1)  # Definir um timeout para a leitura da porta serial
time.sleep(2)  # Espera a comunicação serial ser inicializada

# Função para negar o acesso (aciona LED vermelho)
def negar_acesso():
    # Envia comando para o Arduino acionar o LED vermelho
    print("Senha incorreta, acesso negado.")
    serial_port.write('NEGA_ACESSO\n'.encode('utf-8'))  # Envia para o Arduino acionar LED vermelho
    serial_port.write('CLOSE_DOOR\n'.encode('utf-8'))  # Envia comando para fechar o portão (caso esteja aberto)

# Função para liberar o acesso (aciona LED verde)
def liberar_acesso():
    print("Senha correta, cofre aberto.")
    serial_port.write('LIBERA_ACESSO\n'.encode('utf-8'))  # Envia para o Arduino acionar LED verde
    serial_port.write('OPEN_DOOR\n'.encode('utf-8'))  # Envia comando para abrir o portão

def start_server():
    # Criação do socket para o servidor
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('10.1.25.177', 5000))  # IP e porta para escutar
    server_socket.listen(5)
    print("Server waiting for connection...")

    client_socket, client_address = server_socket.accept()  # Aceita a conexão do cliente
    print(f"Connection established with {client_address}")

    try:
        while True:
            message = client_socket.recv(1024).decode('utf-8')  # Recebe mensagem do cliente

            if message.lower() == 'exit':  # Caso o cliente envie "exit", encerra a conexão
                print("Connection closed by the client.")
                break

            if message:  # Verifica se há alguma mensagem
                print(f"Client: {message}")
                # Verifica a senha enviada pelo cliente
                if message == "1234":  # Senha correta
                    liberar_acesso()  # Envia comando para liberar o acesso
                    client_socket.send("Cofre Aberto".encode('utf-8'))  # Envia mensagem de sucesso para o cliente
                else:  # Senha incorreta
                    negar_acesso()  # Envia comando para negar o acesso
                    client_socket.send("Acesso Negado".encode('utf-8'))  # Envia mensagem de falha para o cliente

    except Exception as e:
        print(f"An error occurred: {e}")

    finally:
        # Fechar as conexões
        client_socket.close()
        server_socket.close()
        serial_port.close()

if __name__ == "__main__":
    start_server()
