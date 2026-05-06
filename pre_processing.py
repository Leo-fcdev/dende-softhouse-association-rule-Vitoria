import pandas as pd

df = pd.read_csv('vendas_dataset.csv')

#Remover linhas nulas
df = df.dropna(subset=['descricao_produtos', 'id_transacao'])

#Remover marcas

marcas_para_remover = ['nike', 'adidas', 'puma', 'lacoste', 'gucci', 'polo', 'micol', 'pimpolho', 'luziane', 'bilu', 'nikko', 'stylo']

def limpar_descricao(texto):
    texto = str(texto).lower()
    for marca in marcas_para_remover:
        texto = texto.replace(marca, '')
    return ' '.join(texto.split())

df['descricao_limpa'] = df['descricao_produtos'].apply(limpar_descricao)