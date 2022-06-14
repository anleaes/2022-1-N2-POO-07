from asyncio.windows_events import NULL
from paciente import Paciente

class Registro(Paciente):

    def __init__ (self, registro_pcte, paciente):
        super().__init__(registro_pcte)
        self._registro_pcte = registro_pcte
        self._paciente = paciente

    def atribui_registro(self):
        self._registro_pcte = None
        if self._paciente.nome != NULL: 
            self.paciente.registro_pcte = self._registro_pcte+1
            print("Registro numero {self._registro_pcte}")
        