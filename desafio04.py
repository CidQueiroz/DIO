def calcula_valor_final(valor_inicial1, taxa_juros1, periodo1):
    # Calcula o valor final com juros compostos
    valor_final = valor_inicial1 * (1 + taxa_juros1) ** periodo1
    return round(valor_final, 2)


# Entrada de dados
valor_inicial = float(input())
taxa_juros = float(input())
periodo = int(input())

# Chama a função para calcular o valor final
resultado = calcula_valor_final(valor_inicial, taxa_juros, periodo)

# Imprime o resultado
print("Valor final do investimento: R$", resultado)
