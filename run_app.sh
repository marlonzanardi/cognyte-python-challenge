#!/bin/bash

CONFIG_FILE="config.cfg"

show_help() {
  echo "Uso: ./run_app.sh [-run | -test]"
  echo ""
  echo "Opções:"
  echo "  -run   Executar o servidor"
  echo "  -test  Rodar os testes unitários"
}

read_port_from_config() {
  if [ -f "$CONFIG_FILE" ]; then
    PORT=$(awk -F "=" '/^PORT/ {print $2}' $CONFIG_FILE | tr -d ' ')
    if [ -z "$PORT" ]; then
      echo "A porta nao foi encontrada no arquivo de configuracao. Usando a porta padrao: 8080"
      PORT=8080
    fi
  else
    echo "Arquivo de configuracao nao encontrado. Usando a porta padrao: 8080"
    PORT=8080
  fi
  echo "Usando a porta: $PORT"
}

run_server() {
  # Remove o container caso ja esteja rodando
  if [ "$(docker ps -a -q -f name=tcp_server)" ]; then
      docker rm -f tcp_server
  fi

  docker build -t python_tcp_server .

  read_port_from_config
  docker run -d -p "$PORT:$PORT" --name tcp_server python_tcp_server
}

run_tests() {
  if [ -d "venv" ]; then
    source venv/bin/activate
  fi

  echo "Rodando os testes unitarios..."
  python -m unittest -v test_server.py
}

if [ $# -eq 0 ]; then
  show_help
  exit 1
fi

# Verifica o parametro fornecido
case "$1" in
  -run)
    run_server
    ;;
  -test)
    run_tests
    ;;
  -h|--help)
    show_help
    ;;
  *)
    echo "Opcao invalida: $1"
    show_help
    exit 1
    ;;
esac
