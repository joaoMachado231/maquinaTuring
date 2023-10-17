class MaquinaTuringUniversal:
    def __init__(self):
        self.fita = ['B']
        self.cabecaLeituraGravacao = 0
        self.estadoTransicao = 'q0'
        self.regrasTransicao = {}

    def setRegrasTransicao(self, rules):
        self.regrasTransicao = rules

    def setPalavra(self, palavraInput):
        self.fita = ['B'] + list(palavraInput) + ['B']
        self.cabecaLeituraGravacao = 1  # Inicia na primeira célula da fita
        self.estadoTransicao = 'q0'  # Define o estado inicial

    def executar(self):
        while True:
            simbolo = self.fita[self.cabecaLeituraGravacao]
            if (self.estadoTransicao, simbolo) not in self.regrasTransicao:
                return ''.join(self.fita).strip('B')
            novoEstado, novoSimbolo, movimentoLeitor = self.regrasTransicao[(self.estadoTransicao, simbolo)]
            self.estadoTransicao = novoEstado
            self.fita[self.cabecaLeituraGravacao] = novoSimbolo

            if movimentoLeitor == 'D':
                self.cabecaLeituraGravacao += 1
            elif movimentoLeitor == 'E':
                self.cabecaLeituraGravacao -= 1


utm = MaquinaTuringUniversal()

# Inverter 1 e 0 da palavra
transition_rules = {
    ('q0', '0'): ('q0', '1', 'D'),
    ('q0', '1'): ('q0', '0', 'D'),
    ('q0', 'B'): ('Halt', 'B', 'P'),
}


utm.setRegrasTransicao(transition_rules)
input_string = '01010101'

utm.setPalavra(input_string)
output = utm.executar()

print(f"\nExecutando regra de inverter 1 e 0 da palavra")
print(f"Entrada: {input_string}")
print(f"Saida: {output}")

#Soma 1 ao numero binario

transition_rules2 = {
    ('q0', '0'): ('q0', '0', 'D'),
    ('q0', '1'): ('q0', '1', 'D'),
    ('q0', 'B'): ('q1', 'B', 'E'),
    ('q1', '0'): ('Fim', '1', 'P'),
    ('q1', '1'): ('q1', '0', 'E'),
}

input_string2 = '01111'

utm.setRegrasTransicao(transition_rules2)
utm.setPalavra(input_string2)
output = utm.executar()

print(f"\nExecutando regra de soma 1 em binario")
print(f"Entrada: {input_string2}")
print(f"Saida: {output}")

