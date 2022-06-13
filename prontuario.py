from abc import abstractmethod
from paciente import Paciente
from cid import Cid
from profissional import Profissional
from leito import Leito
from prescricao import Prescricao
from atendimento import Atendimento

class Prontuario (Cid, Profissional, Leito, Prescricao, Atendimento):
    @abstractmethod
    def mostra(self):
        pass
