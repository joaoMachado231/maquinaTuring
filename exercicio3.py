def reconhecer_par_de_zeros(palavra, estado_atual='qf'):
    # Função de transição do autômato
    transicoes = {
        'qf': {'0': 'q1', '1': 'qf'},
        'q1': {'0': 'qf', '1': 'q1'},
    }

    if len(palavra) == 0:
        return estado_atual == 'qf'

    proxima_letra = palavra[0]

    if proxima_letra in transicoes[estado_atual]:
        proximo_estado = transicoes[estado_atual][proxima_letra]
        return reconhecer_par_de_zeros(palavra[1:], proximo_estado)
    else:
        return False

# Exemplo de uso:
palavras = ["0", "00", "000", "100", "001"]
for palavra in palavras:
    if reconhecer_par_de_zeros(palavra):
        print(f'A palavra "{palavra}" possui um número par de "0"s')
    else:
        print(f'A palavra "{palavra}" não possui um número par de "0"s')
