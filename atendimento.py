from profissional import Profissional
from prescricao import Prescricao

class Atendimento(Profissional, Prescricao):
    def __init__(self, item, profissional, evolucao, sinais):
        super().__init__()
        self._item = item
        self._evolucao = evolucao
        self._sinais = sinais

def mostra_atendimento(self):
    print ("** MOSTRA REGISTRO ATENDIMENTO DO PACIENTE**")
    print (f'\n {self.paciente.nome}')
    print (f'\nDados do Profissional: \n- {self.profissional.nome}, {self.profissional.conselho}' )
    print (f'\nDados da Evolucao: - {self.atendimento.evolucao}')
