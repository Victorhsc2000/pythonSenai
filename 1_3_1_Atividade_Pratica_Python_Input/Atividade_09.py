# Atividade 09 - Lei da Gravitação Universal de Isaac Newton

# Constante de gravitação universal (G)
G = 6.67e-11  # Representa 6.67 x 10^-11

try:
    # Entrada de dados (substituindo vírgula por ponto para evitar erros de conversão)
    m1 = float(input("Digite a massa do primeiro corpo em kg (m1): ").replace(",", "."))
    m2 = float(input("Digite a massa do segundo corpo em kg (m2): ").replace(",", "."))
    d = float(input("Digite a distância entre os centros dos corpos em metros (d): ").replace(",", "."))
    
    # Validação para evitar divisão por zero
    if d <= 0:
        print("Erro: A distância deve ser maior que zero.")
        exit()

    # Tratamento de dados (Fórmula: F = G * (m1 * m2) / (d ** 2))
    forca_gravitacional = G * (m1 * m2) / (d ** 2)

    # Exibição do resultado formatado em notação científica ou com casas decimais
    print(f"\nA força gravitacional entre os corpos é de: {forca_gravitacional:.2e} N")

except ValueError:
    print("Erro: Por favor, digite apenas números válidos.")
