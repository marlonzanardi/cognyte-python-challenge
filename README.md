### Desafio Técnico - Python TCP Server

Este repositório contém a implementação de um servidor TCP desenvolvido em Python. O software recebe dados via rede, salva-os em arquivos locais e é capaz de dividir os arquivos conforme o tamanho máximo configurado. O servidor também é acompanhado por um cliente que envia os dados ao servidor e testes unitários.

### Como rodar o projeto

- Para rodar o servidor:

```bash
./run_app.sh -run
```

Isso vai iniciar o servidor em um container Docker, escutando na porta configurada no arquivo `config.cfg`.

- Para rodar os testes unitários:

```bash
./run_app.sh -test
```

Isso vai rodar os testes unitários definidos para o projeto, utilizando o framework `unittest`.

- Para visualizar as opções disponíveis:

```bash
./run_app.sh -h
```

### Configuração

O projeto utiliza um arquivo de configuração `config.cfg` para definir parâmetros como a porta do servidor, o tamanho máximo dos arquivos, o prefixo dos arquivos gerados, etc.

- Exemplo de configuração:

```ini
[DEFAULT]
SERVER_IP = 127.0.0.1
PORT = 8080
MAX_FILE_SIZE = 1024  # Tamanho máximo do arquivo em bytes
FILE_PREFIX = data
```

### Entregáveis

Aqui estão os entregáveis que foram atingidos na conclusão do desafio:

- [x] **Código-fonte**: O código-fonte de tudo o que foi desenvolvido, esteja o software funcionando ou não, deverá ser disponibilizado no Github.
      
- [x] **Script de deploy**: Um script necessário para subir a aplicação. No caso deste projeto, o script `run_app.sh` é utilizado para rodar o servidor e os testes.
      
- [x] **Comunicação**: Utilizar comunicação TCP.
      
- [x] **Armazenamento dos dados**: TODOS os dados transmitidos devem ser armazenados corretamente.
      
- [x] **Gerenciamento de arquivos grandes**: Implementar a lógica para dividir corretamente os arquivos com base no tamanho máximo.
      
- [x] **Configuração dinâmica**: Implementar a leitura dinâmica de parâmetros como `MAX_FILE_SIZE` e garantir que o servidor e os testes funcionassem de acordo com a configuração.
      
- [x] **Prefixo**: O nome do arquivo deve ser configurável, como um prefixo, ao qual deve ser anexado uma marca de tempo do momento da abertura do arquivo.
      
- [x] **Testes unitários**: Testes que validam o comportamento de divisão de arquivos.
      
- [x] **Bibliotecas utilizadas**: Informações sobre as bibliotecas e versões utilizadas no projeto: basicamente foi utilizado 'socket' para cuidar das conexões, 'configparser' para realizar o parseamento do arquivo de configuração, bibiotecas de uso geral (time,os) e 'unittest' para os testes unitários.
      
- [x] **Tempo gasto no desenvolvimento**: O tempo aproximado gasto no desenvolvimento deste software foi de 4 horas, contendo desenvolvimento, testes e documentação.
      
- [x] **Dificuldades enfrentadas**: Durante o desenvolvimento, a principal dificuldade foi quebrar o arquivo de acordo com o limite maximo estabelecido no arquivo de configuração, gerando corretamente as partes.

### Screenshots

![image](https://github.com/user-attachments/assets/9b70e4a2-9e86-49c6-8f36-7b56ded3a902)

![image](https://github.com/user-attachments/assets/9289569d-4c24-4f5d-96a6-ce8f2d9cfc05)

![image](https://github.com/user-attachments/assets/5b99a05f-34f6-4608-8fa0-a93669dd782f)

![image](https://github.com/user-attachments/assets/6c9bc296-425e-4e17-8096-c1fc0704e98e)

![image](https://github.com/user-attachments/assets/17d8537d-68fb-4679-a0ff-7bcf4653daa4)



