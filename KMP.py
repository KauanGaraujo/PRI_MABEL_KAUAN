n = int(input("Insira a quantidade de dias: "))


total_consumo = 0
dias_meta_cumprida = 0
maior_consumo = None
menor_consumo = None


meta = 150


for i in range(1, n + 1):
    consumo = int(input(f"Insira o consumo do dia {i}: "))


    if consumo >= meta:
        dias_meta_cumprida += 1

    
    total_consumo += consumo

  
    if maior_consumo is None or consumo > maior_consumo:
        maior_consumo = consumo
    if menor_consumo is None or consumo < menor_consumo:
        menor_consumo = consumo

