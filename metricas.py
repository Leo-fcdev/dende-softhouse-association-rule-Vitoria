def gerar_regras_associacao(itemsets_frequentes, confianca_minima=0.5):
    regras = []
    
    
    for itemset, suporte_conjunto in itemsets_frequentes.items():
        if len(itemset) > 1:
            
            suporte_A = itemsets_frequentes[antecedente]
            suporte_B = itemsets_frequentes[consequente]
            
            confianca = suporte_conjunto / suporte_A
            lift = confianca / suporte_B
            
            if confianca >= confianca_minima:
                regras.append({
                    'Regra': f'{antecedente} -> {consequente}',
                    'Suporte': suporte_conjunto,
                    'Confianca': confianca,
                    'Lift': lift
                })
                
    return regras