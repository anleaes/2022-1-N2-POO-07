from profissional import Profissional
from prescricao import Prescricao

class Atendimento (Profissional, Prescricao):
    def __init__(self, nome, conselho, num_conselho, item, profissional, registro_pcte, evolucao, sinais):
        super().__init__(nome, conselho, num_conselho)
        self._nome = nome
        self._conselho = conselho
        self._num_conselho = num_conselho
        self._item = item
        self._profissional = profissional 
        self._registro_pcte = registro_pcte 
        self._evolucao = evolucao
        self._sinais = sinais

def print_atendimento(self):
    print ("** MOSTRA REGISTRO ATENDIMENTO DO PACIENTE**")
    print (f'\n {self.paciente.nome}')
    print (f'\nDados do Profissional: \n- {self.profissional.nome}, {self.profissional.conselho}' )
    print (f'\nDados da Evolucao: - {self.atendimento.evolucao}')
