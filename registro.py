from asyncio.windows_events import NULL


class Registro:

    def __init__ (self, registro_pcte, paciente):
        self._registro_pcte = registro_pcte
        self._paciente = paciente

    def atribui_registro(self):
        self._registro_pcte = 888
        if self._paciente != NULL: 
            self._registro_pcte = self._registro_pcte+1
            print("Registro numero {self._registro_pcte}")
        