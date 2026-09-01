from dataclasses import dataclass
from abc import ABC, abstractmethod

class IConta(ABC):
    @abstractmethod
    def consultar_dados():
        pass

    @abstractmethod
    def gerar_extrato():
        pass

    @abstractmethod
    def depositar(valor):
        pass

    @abstractmethod
    def sacar(valor):
        pass


@dataclass
class Pessoa:
    nome: str
    cpf: str

    def __str__(self):
        return f"Nome: {self.nome}\nCPF: {self.cpf}"

@dataclass
class Conta(IConta):
    pessoa: Pessoa
    agencia: str
    n_conta: str
    saldo: float

    def __str__(self):
        return f"{str(self.pessoa)}\nAgencia: {self.agencia}\nN_conta: {self.n_conta}\nSaldo: {float(self):.2f}"

    def __float__(self):
        return self.saldo

    def consultar_dados(self):
        return str(self)

    def gerar_extrato(self):
        with open("atividade_06/extrato/extrato.txt","w",encoding="utf8") as f:
            f.write(f"{str(self.pessoa)}\nSaldo: {float(self):.2f}")
        return f"{str(self.pessoa)}\nSaldo: {float(self):.2f}"

    def depositar(self,valor):
        self.saldo += valor
        return self.saldo

    def sacar(self,valor):
        self.saldo -= valor
        return self.saldo