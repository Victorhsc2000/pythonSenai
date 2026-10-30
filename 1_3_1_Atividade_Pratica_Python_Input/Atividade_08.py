# Programa para calcular a velocidade média usando a variação do espaço (ΔS) e do tempo (ΔT)


def calcular_velocidade_media():
  try:
    print('--- VARIAÇÃO DO ESPAÇO (ΔS) ---')
    espaco_inicial = float(input('Digite a posição inicial (S₀): '))
    espaco_final = float(input('Digite a posição final (S): '))

    print('\n--- VARIAÇÃO DO TEMPO (ΔT) ---')
    tempo_inicial = float(input('Digite o instante inicial (t₀): '))
    tempo_final = float(input('Digite o instante final (t): '))

    # Cálculo das variações (Delta)
    delta_s = espaco_final - espaco_inicial
    delta_t = tempo_final - tempo_inicial

    # Validações físicas e matemáticas
    if delta_t == 0:
      print('\nErro: O tempo final não pode ser igual ao tempo inicial (ΔT = 0). Divisão por zero!')
      return
    elif delta_t < 0:
      print('\nErro: O tempo final não pode ser menor que o tempo inicial (ΔT negativo). O tempo só avança!')
      return

    # Cálculo da velocidade média (Vm = ΔS / ΔT)
    velocidade_media = delta_s / delta_t

    # Exibição dos resultados detalhados
    print('\n================ RESULTADO ================')
    print(f'Variação do espaço (ΔS): {delta_s:.2f}')
    print(f'Variação do tempo  (ΔT): {delta_t:.2f}')
    print(f'Velocidade Média   (Vm): {velocidade_media:.2f}')
    print('=========================================')

  except ValueError:
    print('\nErro: Por favor, insira apenas números válidos.')


# Executa a função
calcular_velocidade_media()
