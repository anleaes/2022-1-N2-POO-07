class Profissional:
    def __init__(self, nome, conselho, num_conselho):
        self._nome = nome
        self._conselho = conselho
        self._num_conselho = num_conselho
    def mostra_profissional(self):
        print (f'\n FUNCAO MOSTRA PROFISSIONAL \n {self.profissional.nome}, {self.profissional.conselho}, {self.profissional.conselho}')