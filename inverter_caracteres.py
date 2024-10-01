while True:
    # Solicitar ao usuário que insira uma string
    entrada = input("Digite uma string para inverter (ou 'sair' para encerrar): ")

    # Verificar se o usuário deseja sair
    if entrada.lower() == 'sair':
        print("Programa encerrado.")
        break

    # Inicializar uma variável para armazenar a string invertida
    string_invertida = ""

    # Inverter a string usando um loop
    for caractere in entrada:
        string_invertida = caractere + string_invertida

    # Exibir a string invertida
    print("String invertida:", string_invertida)
