from paciente import Paciente
from cid import Cid
from profissional import Profissional
from leito import Leito
from prescricao import Prescricao
from atendimento import Atendimento

class Prontuario (Paciente, Cid, Profissional, Leito, Prescricao, Atendimento):
    def __init__(self, teste):
        super().__init__()
        self._teste = teste