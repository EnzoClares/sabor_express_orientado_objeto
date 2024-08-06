class ContaBancaria:
    contas = []
    def __init__(self, titular, saldo):
        self._titular = titular.title()
        self._saldo = saldo
        self._ativo = False
        ContaBancaria.contas.append(self)

    def __str__(self):
        return f'{self._titular} | {self._saldo} | {self._ativo}'
    
    @classmethod
    def listar_contas(cls):
        print(f'{'Titular da conta'.ljust(25)} | {'Saldo em conta'.ljust(25)} | {'Status'}')
        for conta in cls.contas:
            print(f'{conta._titular.ljust(25)} | {conta._saldo.ljust(25)} | {conta.ativo}')

    @property
    def ativo(self):
        return '✅' if self._ativo else '❌'
    

usuario1 = ContaBancaria('valdemar', '12400')
usuario1.listar_contas()
