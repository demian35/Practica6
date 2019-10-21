from BasedeDatosJuego import BasedeDatosJuego
import hashlib


def main():
	print("-------------------"'\n' + "Bienvenido al Menu" + '\n'"-------------------")
	print("1 : Registrar nuevo Jugador")
	print("2 : Iniciar Sesion")
	teclado = int(input("Escoga la funcion que quiere hacer : "))
	if(teclado == 1):
		nombrenuevo = str(input("Indique cual sera su nombre de usuario : "))
		passwordnuevo = str(input("Indique cual sera su contrasena : "))
		database = BasedeDatosJuego()
		database.cantidadDeUsuarios()
		h=hashlib.new(usuario,clave)
		print(h.digest()) 
        #sql = "INSERT INTO Jugador (nombrenuevo,passwordnuevo) VALUES ('{}' ,'{}')".format(nombre,password)
        #self.cursor.execute(sql)
        #self.connection.commit()
		database.agregarUsuario(nombrenuevo,passwordnuevo)
		database.cantidadDeUsuarios()
	if(teclado == 2):
		usuario= str(input("Teclee su nombre de usuario : "))
		clave= str(input("Teclee su contrasena : "))
		database2= BasedeDatosJuego()
		valor = database2.mostrarUsuario(usuario)
		if (valor == None) :
			print("Vuelve a ingresar un usuario valido.")
		else:
			if (valor==clave):
				print ("Puedes jugar. ")
	#if usuario in BasedeDatosJuego:
	#	if clave in BasedeDatosJuego:
	#		return 1 
	#	else:
	#		print("Este usuario no existe : ")
#	else:
	#	return 2 


if __name__ == '__main__':
    main()
