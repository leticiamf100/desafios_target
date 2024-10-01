import json

# Dados de faturamento em formato JSON
dados_json = '''
{
    "faturamento": [
        {"dia": 1, "valor": 1200.00},
        {"dia": 2, "valor": 1800.00},
        {"dia": 3, "valor": 0.00},
        {"dia": 4, "valor": 2300.00},
        {"dia": 5, "valor": 2700.00},
        {"dia": 6, "valor": 0.00},
        {"dia": 7, "valor": 1600.00},
        {"dia": 8, "valor": 2900.00},
        {"dia": 9, "valor": 2500.00},
        {"dia": 10, "valor": 0.00},
        {"dia": 11, "valor": 3100.00},
        {"dia": 12, "valor": 2000.00}
    ]
}
'''

def carregar_faturamento(dados_json):
    """Carrega os dados de faturamento de uma string JSON."""
    dados = json.loads(dados_json)
    return dados['faturamento']

def calcular_faturamento(faturamento):
    """Calcula o menor, maior e o número de dias acima da média."""
    valores = [dia['valor'] for dia in faturamento if dia['valor'] > 0]

    if not valores:
        return None, None, 0  # Se não houver faturamento

    menor_valor = min(valores)
    maior_valor = max(valores)
    media = sum(valores) / len(valores)
    
    dias_acima_media = sum(1 for valor in valores if valor > media)

    return menor_valor, maior_valor, dias_acima_media

def main():
    faturamento = carregar_faturamento(dados_json)
    
    menor, maior, dias_acima_media = calcular_faturamento(faturamento)
    
    print(f'Menor valor de faturamento: R${menor:.2f}')
    print(f'Maior valor de faturamento: R${maior:.2f}')
    print(f'Dias com faturamento acima da média: {dias_acima_media}')

if __name__ == "__main__":
    main()
