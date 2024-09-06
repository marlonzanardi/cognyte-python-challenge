import socket
import configparser
import os
import time

def load_config():
    config = configparser.ConfigParser()
    config.read('config.cfg')

    port_from_cfg = config['DEFAULT']['PORT']
    max_file_size_from_cfg = config['DEFAULT']['MAX_FILE_SIZE']
    file_prefix_from_cfg = config['DEFAULT']['FILE_PREFIX']

    server_port = int(os.getenv('SERVER_PORT', port_from_cfg))
    max_file_size = int(os.getenv('MAX_FILE_SIZE', max_file_size_from_cfg))
    file_prefix = os.getenv('FILE_PREFIX', file_prefix_from_cfg)

    return server_port, max_file_size, file_prefix

def save_data(data, prefix, max_size, current_file, part_number, timestamp, output_dir):
    current_file = os.path.join(output_dir, f"{prefix}_{timestamp}_parte_{part_number}.bin")

    if not os.path.exists(current_file):
        with open(current_file, 'wb') as f:
            f.write(b'')

    remaining_size = max_size

    while len(data) > remaining_size:
        with open(current_file, 'ab') as f:
            f.write(data[:remaining_size])
        
        data = data[remaining_size:]
        # Incrementa o numero da parte e cria um novo arquivo para o restante dos dados
        part_number += 1
        current_file = os.path.join(output_dir, f"{prefix}_{timestamp}_parte_{part_number}.bin")
        remaining_size = max_size

    with open(current_file, 'ab') as f:
        f.write(data)

    return part_number

def start_server():
    # Carrega os valores de configuração
    server_port, max_size, prefix = load_config()

    part_number = 1
    timestamp = time.strftime('%Y%m%d%H%M%S')
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('0.0.0.0', server_port))
    server_socket.listen(5)
    
    while True:
        conn, addr = server_socket.accept()
        while True:
            data = conn.recv(1024)
            if not data:
                break
            # Chama a funcao para salvar os dados e garantir que o arquivo nao ultrapasse o tamanho maximo
            part_number = save_data(data, prefix, max_size, f"{prefix}_{timestamp}.bin", part_number, timestamp)

        conn.close()

if __name__ == "__main__":
    start_server()
