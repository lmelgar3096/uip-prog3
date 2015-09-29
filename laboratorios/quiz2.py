recorrido = 0


while recorrido < 5:
	chance = float(input("total: "))
      
	recorrido += 1 
  
     
	if chance >= 500:
		descuento = chance * 0.30
		subtotal = chance - descuento
		total = subtotal
		print("Su total es:{0} " .format(total))

	elif chance < 500 and chance >= 200:
		descuento = chance * 0.20
		subtotal = chance - descuento
		total = subtotal
		print("Su total es:{0} " .format(total))

	elif chance < 200 and chance >= 100:
		descuento = chance * 0.10
		subtotal = chance - descuento
		total = subtotal
		print("Su total es:{0} " .format(total))

	else:
		print("Su monto no tiene margen de descuento, Gracias")

else:
	print("Gracias por su compra")

 