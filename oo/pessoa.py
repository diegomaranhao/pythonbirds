class Pessoa:
    olhos = 2

    def __init__(self, *filhos, nome=None, idade=34):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'olá {id(self)}'


if __name__ == '__main__':
    miguel = Pessoa(nome='Miguel')
    dom = Pessoa(miguel, nome='DOM')
    print(Pessoa.cumprimentar(dom))
    print(id(dom))
    print(dom.cumprimentar())
    print(dom.nome)
    for filho in dom.filhos:
        print(filho.nome)

    dom.sobrenome = 'Oliveira'
    print(dom.sobrenome)
    dom.olhos = 3
    del dom.filhos
    del dom.olhos
    print(dom.__dict__)
    print(miguel.__dict__)
    print(Pessoa.olhos)
    print(dom.olhos)
    print(id(Pessoa.olhos), id(dom.olhos), id(miguel.olhos))
