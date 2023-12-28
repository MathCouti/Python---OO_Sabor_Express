from Models.avaliacao import Avaliacao

class Restaurante:
    restaurantes = []

    def __init__(self, nome, categoria):
        self._nome = nome.title()
        self._categoria = categoria.upper()
        self._ativo = False
        self._avaliacao = []
        Restaurante.restaurantes.append(self)
              
    def __str__(self):
        return f'Nome: {self._nome}\nCategoria: {self._categoria}\nEstado: {self._ativo}\n'
    
    @classmethod
    def listar_restaurantes(cls):
        for item in cls.restaurantes:
            print(f'Nome: {item._nome}\nCategoria: {item._categoria}\nEstado: {item._ativo}\n{item.media_avaliacoes}\n')

    @property
    def ativo(self):
        return 'Verdadeiro' if self._ativo else 'Falso'

    def alternar_estado(self):
        self._ativo = not self._ativo

    def receber_avaliacao(self, cliente, nota):
        avaliacao = Avaliacao(cliente, nota)
        self._avaliacao.append(avaliacao)

    @property
    def media_avaliacoes(self):
        if not self._avaliacao:
            return 0
        soma_das_notas = sum(avaliacao._nota for avaliacao in self._avaliacao)
        quantidade_de_notas = len(self._avaliacao)
        media = round(soma_das_notas / quantidade_de_notas,1)
        return media
