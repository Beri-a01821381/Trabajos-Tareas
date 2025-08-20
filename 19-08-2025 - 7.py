print("Venta de videojuegos")
#Entrada NewVG, UsedVG, total
#Proceso (NewVG*1000) + (UsedVG*350)
#Salida total

#Entrada
NewVG=int(input("Indique cuantos videjuegos nuevos va a comprar: "))
UsedVG=int(input("Indique cuantos videjuegos usados va a comprar: "))

#Proceso 
total=(NewVG*1000) + (UsedVG*350)
#Salida
print(f"El total a pagar = {total}")