# L1 = {w | w possui aa ou bb como subpalavras}

class AFD:
    def __init__(self):
        self.estado_atual = 'q0'
        self.estados_finais = {'qf'}

    def transicao(self, entrada):
        # Função de transição do autômato
        transicoes = {
            'q0': {'a': 'q1', 'b': 'q2'},
            'q1': {'a': 'qf', 'b': 'q2'},
            'q2': {'a': 'q1', 'b': 'qf'},
            'qf': {'a': 'qf', 'b': 'qf'}
        }

        if entrada in transicoes[self.estado_atual]:
            self.estado_atual = transicoes[self.estado_atual][entrada]
        else:
            # Se a transição não estiver definida, mudamos para um estado inválido
            self.estado_atual = 'invalido'

    def verificar_palavra(self, palavra):
        self.estado_atual = 'q0'
        for letra in palavra:
            self.transicao(letra)
            if self.estado_atual == 'invalido':
                return False
        return self.estado_atual in self.estados_finais

# Exemplo de uso:
afd = AFD()
palavras = ["abcde", "baab", "bbb", "aabb"]
for palavra in palavras:
    if afd.verificar_palavra(palavra):
        print(f'A palavra "{palavra}" possui "aa" ou "bb" como subpalavras')
    else:
        print(f'A palavra "{palavra}" não possui "aa" ou "bb" como subpalavras')
