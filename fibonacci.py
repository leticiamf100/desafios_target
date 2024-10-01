def fibonacci_until(n):
    """Gera a sequência de Fibonacci até o número n."""
    fib_sequence = [0, 1]
    while True:
        next_fib = fib_sequence[-1] + fib_sequence[-2]
        if next_fib > n:
            break
        fib_sequence.append(next_fib)
    return fib_sequence

def pertence_a_fibonacci(num):
    """Verifica se um número pertence à sequência de Fibonacci."""
    fib_sequence = fibonacci_until(num)
    return num in fib_sequence

def main():
    while True:
        entrada = input("Digite um número (ou 'sair' para encerrar): ")
        if entrada.lower() == 'sair':
            print("Programa encerrado.")
            break
        try:
            numero = int(entrada)
            if pertence_a_fibonacci(numero):
                print(f"O número {numero} pertence à sequência de Fibonacci.")
            else:
                print(f"O número {numero} não pertence à sequência de Fibonacci.")
        except ValueError:
            print("Por favor, digite um número inteiro válido.")

if __name__ == "__main__":
    main()
