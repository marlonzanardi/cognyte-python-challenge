import unittest
import os
from server import save_data
import shutil
import time

class TestServer(unittest.TestCase):

    def setUp(self):
        """Preparação: Cria um diretorio temporario para salvar os arquivos."""
        self.test_dir = "./test_output"
        if not os.path.exists(self.test_dir):
            os.makedirs(self.test_dir)
        self.prefix = "test"
        # Fixando o max size em 10 para realizar os testes
        self.max_size = 10 
        self.timestamp = time.strftime('%Y%m%d%H%M%S')

    def tearDown(self):
        """Limpeza: Remove o diretorio de testes apos a execucao."""
        if os.path.exists(self.test_dir):
            shutil.rmtree(self.test_dir)

    def test_save_data_within_limit(self):
        """Testar se os dados cabem em um unico arquivo."""
        # 10 bytes, exatamente o limite
        data = b"1234567890"
        part_number = 1
        filename = f"{self.test_dir}/{self.prefix}_{self.timestamp}.bin"
        
        part_number = save_data(data, self.prefix, self.max_size, filename, part_number, self.timestamp, self.test_dir)
        expected_file = os.path.join(self.test_dir, f"{self.prefix}_{self.timestamp}_parte_1.bin")
        self.assertTrue(os.path.exists(expected_file), "Arquivo nao foi criado.")
        with open(expected_file, 'rb') as f:
            saved_data = f.read()
        self.assertEqual(saved_data, data, "Os dados salvos estao incorretos.")

    def test_save_data_exceeds_limit(self):
        """Testar se os dados sao divididos corretamente quando excedem o limite."""
        # 20 bytes, precisa de 2 arquivos de 10 bytes
        data = b"12345678901234567890" 
        part_number = 1
        filename = f"{self.test_dir}/{self.prefix}_{self.timestamp}.bin"
        part_number = save_data(data, self.prefix, self.max_size, filename, part_number, self.timestamp, self.test_dir)

        expected_file_1 = os.path.join(self.test_dir, f"{self.prefix}_{self.timestamp}_parte_1.bin")
        expected_file_2 = os.path.join(self.test_dir, f"{self.prefix}_{self.timestamp}_parte_2.bin")

        self.assertTrue(os.path.exists(expected_file_1), "Parte 1 do arquivo nao foi criada.")
        self.assertTrue(os.path.exists(expected_file_2), "Parte 2 do arquivo nao foi criada.")
        
        with open(expected_file_1, 'rb') as f:
            saved_data_1 = f.read()
        with open(expected_file_2, 'rb') as f:
            saved_data_2 = f.read()

        self.assertEqual(saved_data_1, b"1234567890", "Os dados da Parte 1 estao incorretos.")
        self.assertEqual(saved_data_2, b"1234567890", "Os dados da Parte 2 estao incorretos.")

    def test_save_data_multiple_parts(self):
        """Testar se os dados sao divididos corretamente em varias partes."""
        # 30 bytes, precisa de 3 arquivos
        data = b"123456789012345678901234567890"
        part_number = 1
        filename = f"{self.test_dir}/{self.prefix}_{self.timestamp}.bin"
        
        part_number = save_data(data, self.prefix, self.max_size, filename, part_number, self.timestamp, self.test_dir)

        expected_file_1 = os.path.join(self.test_dir, f"{self.prefix}_{self.timestamp}_parte_1.bin")
        expected_file_2 = os.path.join(self.test_dir, f"{self.prefix}_{self.timestamp}_parte_2.bin")
        expected_file_3 = os.path.join(self.test_dir, f"{self.prefix}_{self.timestamp}_parte_3.bin")

        self.assertTrue(os.path.exists(expected_file_1), "Parte 1 do arquivo nao foi criada.")
        self.assertTrue(os.path.exists(expected_file_2), "Parte 2 do arquivo nao foi criada.")
        self.assertTrue(os.path.exists(expected_file_3), "Parte 3 do arquivo nao foi criada.")
        
        with open(expected_file_1, 'rb') as f:
            saved_data_1 = f.read()
        with open(expected_file_2, 'rb') as f:
            saved_data_2 = f.read()
        with open(expected_file_3, 'rb') as f:
            saved_data_3 = f.read()

        self.assertEqual(saved_data_1, b"1234567890", "Os dados da Parte 1 estao incorretos.")
        self.assertEqual(saved_data_2, b"1234567890", "Os dados da Parte 2 estao incorretos.")
        self.assertEqual(saved_data_3, b"1234567890", "Os dados da Parte 3 estao incorretos.")

if __name__ == '__main__':
    unittest.main()
