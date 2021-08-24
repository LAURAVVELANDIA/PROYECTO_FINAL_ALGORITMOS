a=str(input("Digite su nombre completo: "))

#punto_2
tiempo=input("Cúal es la hora de entrada del Vehiculo al parqueadero (HH:MM): ").split(":")
Tipo=str(input("Indique si es carro, moto o bicicleta: "))
placa=input("Ingrese la placa del vehiculo ")
numero_entradas=int(input("Número de veces que ha estado en el parqueadero: "))
hora_entrada_hora, hora_entrada_minutos=tiempo
hora_entrada_hora=int(hora_entrada_hora)
hora_entrada_minutos=int(hora_entrada_minutos)

#punto_4
tiempo_salida=input("Cúal es la hora de salida del Vehiculo al parqueadero (HH:MM): ").split(":")
hora_salida_hora, hora_salida_minutos=tiempo_salida
hora_salida_hora=int(hora_salida_hora)
hora_salida_minutos=int(hora_salida_minutos)
horas=abs((hora_entrada_hora*60)-(hora_salida_hora*60))
total_minutos=abs((hora_entrada_minutos+hora_salida_minutos)-horas)

#punto_3
cobro_sin_descuento=110*total_minutos
cobro_con_descuento=(cobro_sin_descuento-(cobro_sin_descuento*0.20))

print(" ")
print(" ")
print(" ")
print(("Nombre del cliente: ")+ str(a))
print("La hora de entrada del vehiculo fue: "+str(hora_entrada_hora)+":"+str(hora_entrada_minutos))
print(("El tiempo en el parqueadero fue de: ")+(str(total_minutos))+(" minutos"))
print(("El cobro por minuto es de: ")+(str(110))+(" pesos"))
if(numero_entradas>5):
  print(("El valor a pagar, con un descuento del 20% es de: ")+str(cobro_con_descuento))
else:
  print(("No aplica para descuento, debe pagar: ")+str(cobro_sin_descuento))
