class ContaPoupanca(Conta):
    def __int__(self, numero):
        super().__init__(numero)

    def render_juros(self, taxa):
        self.creditar(self.get_saldo).__init__(numero)