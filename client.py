import socket
import configparser

def load_config():
    config = configparser.ConfigParser()
    config.read('config.cfg')
    return config['DEFAULT']

def send_data(data):
    config = load_config()
    server_ip = config['SERVER_IP']
    server_port = int(config['PORT'])

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print(f"Conectando ao servidor {server_ip}:{server_port}")
    client_socket.connect((server_ip, server_port))
    
    print(f"Enviando {len(data)} bytes de dados")
    client_socket.sendall(data)
    client_socket.close()
    print("Dados enviados com sucesso!")

if __name__ == "__main__":
    send_data(b"Dados teste conexao servidor cliente")
