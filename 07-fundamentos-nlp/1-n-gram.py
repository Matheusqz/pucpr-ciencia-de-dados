# Cálculo do N-Gram


def get_ngram_unicos(palavra):
    ngram = set()
    for i in range(len(palavra) - 1):
        ngram.add(palavra[i : i + 2])
    return ngram


def get_ngram(palavra):
    ngram = list()
    for i in range(len(palavra) - 1):
        ngram.append(palavra[i : i + 2])
    return ngram


def ngram_score(palavra1, palavra2):
    n_gram_unico1 = get_ngram_unicos(palavra1)
    n_gram_unico2 = get_ngram_unicos(palavra2)
    uniao = len(n_gram_unico1.intersection(n_gram_unico2))
    return (2 * uniao) / (len(n_gram_unico1) + len(n_gram_unico2))


def analise_ngram(palavra):
    print(f"{palavra} : {get_ngram(palavra)} | total = {len(get_ngram(palavra))}")
    print(
        f"Únicos = {get_ngram_unicos(palavra)} | total = {len(get_ngram_unicos(palavra))}"
    )


def analise_sintatica(palavra1, palavra2, inclue_primeiro=True):
    print(f'Para as palavras: "{palavra1}" e "{palavra2}" temos:')
    if inclue_primeiro:
        analise_ngram(palavra1)
    analise_ngram(palavra2)
    print(
        f"Compartilhados = {print_set(get_ngram_unicos(palavra1).intersection(get_ngram_unicos(palavra2)))}"
    )
    print(f"Score = {ngram_score(palavra1, palavra2)}")
    print('-----------------------')
    # return "-------------------------------------------"

def print_set(conjunto):
    if len(conjunto) > 0:
        return conjunto
    return 0


if __name__ == "__main__":
    lexico = ["abacate", "abacaxi", "abobora", "abobrinha", "ananás", "maça", "mamão", "manga", "melancia", "melão", "mexerica", "morango"]
    max = 0
    min = 1
    melhores = set()
    piores = set()
    similares = set()
    
    palavra = input('Digite uma palavra para comparar: ')

    for lex in lexico:
        analise_ngram(palavra)
        analise_sintatica(palavra, lex, False)
        score = ngram_score(palavra, lex)
        if score > 0.7:
            similares.add(lex)
        if score >= max:
            max = score
            melhores.add(lex)
        if score <= min:
            min = score
            piores.add(lex)
    print('-----------------------')
    print(f'Final da analise de similaridades da palavra: "{palavra}"')
    if similares:
        print(f'Lista de palavras similares (scores maiores que 0.7)= {print_set(similares)}')
    else:
        print('Não houve nenhuma palavra com score maior que 0.7')
    print(f'Melhores similaridade = {melhores}')
    print(f'Piores similaridade = {piores}')
