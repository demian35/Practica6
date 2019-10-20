from pymysql import BasedeDatosJuego
import hashlib


##def main():

    print("-------------------"'\n' + "Bienvenido al Menu" + '\n'"-------------------")
    menu_opciones()
def menu_opciones():
    print("1 : Registrar nuevo Jugador")
    print("2 : Iniciar Sesion")
    teclado = input("Escoga la funcion que quiere hacer : ")
    if(teclado == 1):
         nombrenuevo = input("Indique cual sera su nombre de usuario : ")
        passwordnuevo = input("Indique cual sera su contrasena : ")
        #sql = "INSERT INTO Jugador (nombrenuevo,passwordnuevo) VALUES ('{}' ,'{}')".format(nombre,password)
        #self.cursor.execute(sql)
        #self.connection.commit()
        registronew= BasedeDatosJuego().agregarUsuario(nombrenuevo,passwordnuevo)
    if(teclado == 2):
        usuario= input("Teclee su nombre de usuario : ")
        clave= input("Teclee su contrasena : ") 
        if usuario in BasedeDatosJuego:
            if clave in BasedeDatosJuego:
                return 1 
            else:
                print("Este usuario no existe : ")
        else:
            return 2 


##if __name__ == '__main__':
##    print main()
