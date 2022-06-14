class Leito:
    def __init__(self, un_intercanao, tipo_leito):
        self._un_internacao = un_intercanao
        self._tipo_leito = tipo_leito
    def mostra_leito(self):
        print (f'\n Mostra Leito {self._tipo_leito}, {self._un_internacao}') 
        
        