def gerar_regras_associacao(itemsets_frequentes, confianca_minima=0.5):
    regras = []

    for itemset, suporte_conjunto in itemsets_frequentes.items():
        # Focando em regras de pares (2 peças de roupa)
        if len(itemset) == 2:
            itens = list(itemset)
            
            # CORREÇÃO: Pegamos o item no índice 0 e o item no índice 1 separadamente
            item_A = frozenset([itens[0]])
            item_B = frozenset([itens[1]])
            
            # Pegamos o suporte de cada peça sozinha usando o .get()
            suporte_A = itemsets_frequentes.get(item_A)
            suporte_B = itemsets_frequentes.get(item_B)
            
            if not suporte_A or not suporte_B:
                continue
            
            # Testar a Regra 1: A -> B
            confianca_A_B = suporte_conjunto / suporte_A
            lift_A_B = confianca_A_B / suporte_B
            
            if confianca_A_B >= confianca_minima:
                regras.append({
                    'Regra': f'{itens[0]} -> {itens[1]}', # CORREÇÃO: Texto formatado corretamente
                    'Suporte': round(suporte_conjunto, 4),
                    'Confianca': round(confianca_A_B, 4),
                    'Lift': round(lift_A_B, 4)
                })
                
            # Testar a Regra 2 (Inversa): B -> A
            confianca_B_A = suporte_conjunto / suporte_B
            lift_B_A = confianca_B_A / suporte_A
            
            if confianca_B_A >= confianca_minima:
                regras.append({
                    'Regra': f'{itens[1]} -> {itens[0]}', # CORREÇÃO: Texto formatado corretamente
                    'Suporte': round(suporte_conjunto, 4),
                    'Confianca': round(confianca_B_A, 4),
                    'Lift': round(lift_B_A, 4)
                })
            
    regras.sort(key=lambda x: x['Lift'], reverse=True)
                
    return regras