#!/bin/bash

show_help() {
  echo "Uso: ./run_app.sh [-run | -test]"
  echo ""
  echo "Opções:"
  echo "  -run   Executar o servidor"
  echo "  -test  Rodar os testes unitários"
}

run_server() {
  # Remove o container caso ja esteja rodando
  if [ "$(docker ps -a -q -f name=tcp_server)" ]; then
      docker rm -f tcp_server
  fi

  docker build -t python_tcp_server .
  docker run -d -p 8080:8080 --name tcp_server python_tcp_server
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

# Verifica o parâmetro fornecido
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
