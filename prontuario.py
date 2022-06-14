from paciente import Paciente
from cid import Cid
from profissional import Profissional
from leito import Leito
from prescricao import Prescricao
from atendimento import Atendimento

class Prontuario (Paciente, Cid, Profissional, Leito, Prescricao, Atendimento):
    def __init__(self):
        super().__init__()
    def mostra_prontuario(self):
        self.prontuario.paciente.mostra_paciente()
        self.prontuario.profissional.mostra_profissional()
        self.prontuario.atendimento.mostra_atendimento()
        self.prontuario.leito.mostra_leito()
        self.prontuario.prescricao.valida_medico()
        self.prontuario.cid()