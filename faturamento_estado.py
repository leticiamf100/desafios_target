# Faturamento mensal por estado
faturamento = {
    'SP': 678236.43,
    'RJ': 365678.66,
    'MG': 292629.88,
    'ES': 271865.48,
    'Outros': 919849.53
}

# Cálculo do faturamento total
faturamento_total = sum(faturamento.values())

# Cálculo do percentual de representação
percentuais = {estado: (valor / faturamento_total) * 100 for estado, valor in faturamento.items()}

# Exibição dos resultados
print("Percentual de representação por estado:")
for estado, percentual in percentuais.items():
    print(f"{estado}: {percentual:.2f}%")
