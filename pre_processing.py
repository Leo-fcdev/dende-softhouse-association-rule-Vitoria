import pandas as pd

#Lista as marcas para remover
marcas_para_remover = ['nike', 'adidas', 'puma', 'lacoste', 'gucci', 'polo', 'micol', 'pimpolho', 'luziane', 'bilu', 'nikko', 'stylo']

# Função para a limpeza do df
def limpar_descricao(texto):
    # Garante que o valor é string e converte tudo para minúsculo para padronizar
    texto = str(texto).lower()

    # Percorre a lista de marcas, se ela existir no texto, substitui ele por 'nada'
    for marca in marcas_para_remover:
        texto = texto.replace(marca, '')

    # O split() separa as palavras e o join() juntas apenas com um espaço. Isso remove espaços duplos ou em branco que sobraram onde as marcas foram apagas
    return ' '.join(texto.split())

def carregar_e_limpar_dados(caminho_arquivo):

    #Carrega o dataset
    df = pd.read_csv(caminho_arquivo)

    #Remover linhas nulas
    df = df.dropna(subset=['descricao_produtos', 'id_transacao'])


    #Aplica a limpeza, pega a coluna original, passa cada linha da função limpar_descricao e guarda o resultado na nova coluna
    df['descricao_limpa'] = df['descricao_produtos'].apply(limpar_descricao)


    #O dataset original junta todos os produtos de uma mesma compra em um texto apenas
    #É usado a função anônima lambda para pegar o texto e 'cortar' com split no ponto e vírgula.
    #O strip() garante que não fique nenhum espaço em branco sobrando no inicio ou final de cada item
    df['lista_produto'] = df['descricao_limpa'].apply(
        lambda texto: [produto.strip().split()[0] for produto in texto.split(';') if produto.strip()]
    )

    #Pega a coluna 'lista_produto' e converte do formato Pandas para uma lista pura do Python
    lista_de_vendas = df['lista_produto'].tolist()

    return lista_de_vendas