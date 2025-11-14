class Pessoa:
    def __init__(self, nome=None, idade=15):
        self.nome = nome
    def cumprimento(self):
        return f'ola {id(self)}'

if __name__ == '__main__':
    pedro = Pessoa(nome='Pedro',)
    print(Pessoa.cumprimento(pedro))
    print(id(pedro))
    print(pedro.cumprimento())
