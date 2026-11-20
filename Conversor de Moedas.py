print("Bem Vindo ao Conversor de Moedas!! (18/11/2026)")

valor = float(input("Digite o valor que deseja converter (Em Reais): "))

# 0.strip() remove espaços extras nas pontas e o .casefold() padroniza tudo para minúsculo
moedaescolhida = input("Escolha a moeda que deseja converter (USD, EUR, JPY): ").strip().upper()


if moedaescolhida == "USD":
    resultado = valor / 5.87
    print(f"O Valor Convertido corresponde a: {resultado:.2f} Dólares")

elif moedaescolhida == "EUR":
    resultado = valor / 6.44
    print(f"O Valor Convertido corresponde a: {resultado:.2f} Euros")

else:
    resultado = valor / 0.037
    print(f"O Valor Convertido corresponde a: {resultado:.3f} Ienes Japoneses")