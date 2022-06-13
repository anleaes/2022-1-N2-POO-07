from registro import Registro

class paciente(Registro):
    def __init__ (self, registro_pcte, paciente, nome, endereco, documento, nascimento):
        super().__init__(registro_pcte , paciente)
        self._nome = nome
        self._endereco = endereco, 
        self._documento = documento
        self._nascimento - nascimento
        

