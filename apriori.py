class AprioriCustom:
    def __init__(self, min_support=0.05):
        
        #Salva o limite de 5% dentro do objeto
        self.min_support = min_support
        #Cria o dicionario vazio 
        self.frequent_itemsets = {}
        #Variavel que vai guardar o número total de vendas
        self.num_transactions = 0

    def _calcular_suporte(self, transactions, candidato):
        #Percorre as vendas gerenado um número "1" sempre que o combo estiver no carrinho de compras e soma retornando o toal vendido
        count = sum(1 for transacao in transactions if candidato.issubset(transacao))
        #Retorna a porcetagem 
        return count / self.num_transactions
    
    def extrair_itemsets_frequentes(self, dataset_transacoes):
        #Converte a lista de venda pra um conjuto matemático
        transactions = [set(t) for t in dataset_transacoes]
        self.num_transactions = len(transactions)

        #Cria um cojuto vazio e varrem cada peça de roupa vendida e tranforma num frozenset
        itens_unicos = set()
        for transacao in transactions:
            for item in transacao:
                itens_unicos.add(frozenset([item]))

        
        itemsets_atuais = set()
        for candidato in itens_unicos:
            #Calcula a frenquência da peça
            suporte = self._calcular_suporte(transactions, candidato)
            #Verifica se a peça vendeu mais do que o mínimo
            if suporte >= self.min_support:
                itemsets_atuais.add(candidato)
                self.frequent_itemsets[candidato] = suporte

        #"K" é o tamanho do combo
        k = 2
        #Roda enquanto exitir combinações aprovadas no bloco anterior
        while itemsets_atuais:
            candidatos_k = set()
            lista_atuais = list(itemsets_atuais)

            for i in range(len(lista_atuais)):
                for j in range(i + 1, len (lista_atuais)):
                    #Une dois conjuntos para tentar criar um combo maior
                    novo_candidato = lista_atuais[i].union(lista_atuais[j])
                    
                    #Só aceita um novo combo criado se ele for do mesmo tamnho de "K"
                    if len(novo_candidato) == k:
                        candidatos_k.add(novo_candidato)

            #Calcula o suporte dos novos combos gerados e se aprovado ele entra no dicionário
            itemsets_atuais = set()
            for candidato in candidatos_k:
                suporte = self._calcular_suporte(transactions, candidato)
                if suporte >= self.min_support:
                    itemsets_atuais.add(candidato)
                    self.frequent_itemsets[candidato] = suporte

            #Aumentaa o tamanho da busca na proximá volta do while
            k += 1

        print(f"[Sucesso] O Apriori terminou! Encontradas {len(self.frequent_itemsets)} combinações frequentes.")
        return self.frequent_itemsets