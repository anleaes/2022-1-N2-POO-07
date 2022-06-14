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
        self.prontuario.print_paciente
        self.prontuario.mostra_profissional

#inseri atributo teste, pois não sei como usar esta classe para uma unica função de mostrar as informações de todas as classes    