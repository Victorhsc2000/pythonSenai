# Atividade 10 - Cálculo do Disjuntor para Chuveiro

try:
    # Entrada de dados (amperagem nominal do chuveiro)
    amperagem_chuveiro = float(input("Digite a amperagem nominal do chuveiro (em A): ").replace(",", "."))
    
    # Validação para garantir que a amperagem é positiva
    if amperagem_chuveiro <= 0:
        print("Erro: A amperagem deve ser maior do que zero.")
        exit()

    # Tratamento de dados: Amperagem + 10% de margem de sobra
    amperagem_com_margem = amperagem_chuveiro * 1.10

    # Exibição dos resultados
    print(f"\nAmperagem nominal do chuveiro: {amperagem_chuveiro:.2f} A")
    print(f"Amperagem com 10% de margem: {amperagem_com_margem:.2f} A")

    # Sugestão de disjuntor comercial padrão (opcional, mas útil para a prática)
    if amperagem_com_margem <= 20:
        disjuntor = 20
    elif amperagem_com_margem <= 25:
        disjuntor = 25
    elif amperagem_com_margem <= 32:
        disjuntor = 32
    elif amperagem_com_margem <= 40:
        disjuntor = 40
    elif amperagem_com_margem <= 50:
        disjuntor = 50
    else:
        disjuntor = 63

    print(f"Disjuntor comercial recomendado: {disjuntor} A")

except ValueError:
    print("Erro: Por favor, introduza apenas números válidos.")
