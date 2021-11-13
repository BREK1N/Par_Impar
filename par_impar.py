from time import sleep
while True:
    print("=" * 20)
    print(" " * 4 + "Par ou Impar")
    print("=" * 20)
    try:
        valor = int(input("Digite um valor: "))
        if valor % 2 == 0:
            print("=" * 20)
            print("Esse número e Par")
            sleep(1)
        elif valor % 2 == 1:
            print("=" * 20)
            print("Esse número e Impar")
            sleep(1)
    except ValueError:
        print("Digite um numero")
