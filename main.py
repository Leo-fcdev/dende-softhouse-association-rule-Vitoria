from pre_processing import carregar_e_limpar_dados
from apriori import AprioriCustom
from metricas import gerar_regras_associacao

def executar_pipeline():
    print("=== INICIANDO PIPELINE DE MINERAÇÃO DE DADOS ===")
    
    # 1. Pré-processamento
    print("[1/3] Carregando e limpando os dados...")
    caminho_csv = 'vendas_dataset.csv' # Arquivo de origem
    transacoes = carregar_e_limpar_dados(caminho_csv)
    print(f"Total de transações válidas: {len(transacoes)}")
    
    # 2. Algoritmo Apriori
    print("[2/3] Extraindo itens frequentes (Apriori)...")
    # Define o suporte mínimo para filtrar os itens (1% = 0.01)
    motor_apriori = AprioriCustom(min_support=0.01)
    itemsets_frequentes = motor_apriori.extrair_itemsets_frequentes(transacoes)
    
    # 3. Geração de Regras e Métricas
    print("[3/3] Gerando regras de associação e métricas...")
    # Define a confiança mínima para formar uma regra (20% = 0.2)
    regras_finais = gerar_regras_associacao(itemsets_frequentes, confianca_minima=0.2)
    
    # 4. Apresentação dos Resultados
    print("\n=== MELHORES REGRAS DE ASSOCIAÇÃO ENCONTRADAS ===")
    if not regras_finais:
        print("Nenhuma regra atingiu os critérios mínimos de suporte e confiança.")
    else:
        print(f"Total de regras geradas: {len(regras_finais)}\n")
        
        # Exibe os resultados formatados para análise
        for i, regra in enumerate(regras_finais, 1):
            print(f"#{i} {regra['Regra']}")
            print(f"   Suporte: {regra['Suporte']:.2%}")
            print(f"   Confiança: {regra['Confianca']:.2%}")
            print(f"   Lift: {regra['Lift']:.2f}\n")
            
if __name__ == '__main__':
    executar_pipeline()