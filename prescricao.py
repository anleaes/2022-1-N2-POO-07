from profissional import Profissional
from registro import Registro

class Prescricao (Profissional, Registro):
    def __init__(self, nome, conselho, num_conselho, registro_pcte, paciente, item) :
        super().__init__(nome, conselho, num_conselho, registro_pcte, paciente)
        self._item = item 

    def valida_medico (self):
        if self._conselho == "CREMERS":
            print (" ** Habilitada prescricao medica ** ")


