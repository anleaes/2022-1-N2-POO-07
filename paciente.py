from registro import Registro

class paciente(Registro):
    def __init__ (self, registro_pcte, paciente, nome, endereco, documento, nascimento):
        super().__init__(registro_pcte , paciente)
        self._registro_pcte = registro_pcte
        self._nome = nome
        self._endereco = endereco, 
        self._documento = documento
        self._nascimento - nascimento
        
    def print_paciente(self):
        print (f'\n DADOS DO PACIENTE: ')
        print(f'\nNome: {self.paciente.nome}')
        print(f'\nData de Nacimento: {self.paciente.nascimento} ')
        print(f'\nDocumento: {self.documento} ')
        print(f'\nRegistro: {self._registro_pcte}')
