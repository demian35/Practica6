from dotenv import load_dotenv
from os.path import join, dirname, isdir
from os import environ
import pymysql

# 'from connectionBasedeDatosJuego import BasedeDatosJuego' para menu y tablero.

class BasedeDatosJuego():

	def __init__(self):
		dotenv_path = join(dirname(__file__), ".env")
		load_dotenv(dotenv_path)

		dbname=environ.get("db_name")
		host=environ.get("db_host")
		username=environ.get("db_username")
		password=environ.get("db_password")

		self.connection = pymysql.connect(
			user=username,
			password=password,
            host=host,
            database=dbname,
            charset='utf8mb4')

		self.cursor = self.connection.cursor()
		print ("Conexion Establecida")

	def actualizarNombreJugador(self ,id , nombre):
		sql = "UPDATE Jugador SET nombre = '{}' WHERE pk_id_jugador = {}".format(nombre,id) 
		self.connection.commit()
		try:
			self.cursor.execute(sql)
			self.connection.commit()
		except Exception as e:
			raise

	def mostrarUsuario(self,id):
		sql = "SELECT pk_id_jugador , nombre , password FROM Jugador WHERE pk_id_jugador = {}".format(id)

		try:
			self.cursor.execute(sql)
			Jugador = self.cursor.fetchone()
			if Jugador == None:
				print ("El Usuario con  Id: " + str(id) + " no existe")
			else :
				print ("Id :", Jugador[0])
				print ("nombre :", Jugador[1])
				print ("contraseña:", Jugador[2])
				print ("_____\n")

		except Exception as e:
			raise

	def mostrarUsuarios(self):
		
		sql = "SELECT pk_id_jugador , nombre , password FROM Jugador"
		
		try:
			self.cursor.execute(sql)
			Jugadores = self.cursor.fetchall()
			for i in range(0,len(Jugadores)):
				print (str(Jugadores [i])+ "\n")

			for Jugador in Jugadores:
				print ("Id :", Jugador[0] , "nombre :", Jugador[1] ,"contraseña:", Jugador[2])
				print ("_____\n")

		except Exception as e :
			raise


	def cantidadDeUsuarios(self):
		sql = "SELECT pk_id_jugador FROM Jugador"
		try:
			self.cursor.execute(sql)
			Jugadores = self.cursor.fetchall()
			print ("Se tienen usuarios " + str(len(Jugadores)) + " registrados.")
		except Exception as e :
			raise

	def cantidadDePartidas(self):
		sql = "SELECT pk_id_partida FROM Partida"
		try:
			self.cursor.execute(sql)
			Partidas = self.cursor.fetchall()
			print ("Se tienen " + str(len(Partidas)) + " partidas." )
		except Exception as e :
			raise e
 
	def agregarUsuario(self,nombre,password):
		sql = "INSERT INTO Jugador (nombre,password) VALUES ('{}' ,'{}')".format(nombre,password)
		self.cursor.execute(sql)
		self.connection.commit()

	def agregarPartida(self,tablero_cifrado,fk_id_jugador_en_turno,fk_id_creador,fk_id_oponente):
		sql = "INSERT INTO Partida (tablero_cifrado , fk_id_jugador_en_turno, fk_id_creador, fk_id_oponente) VALUES ('{}',{},{},{}) ".format(tablero_cifrado,fk_id_jugador_en_turno,fk_id_creador,fk_id_oponente)
		self.cursor.execute(sql)
		self.connection.commit()

	def asignarResultado(self,id,resultado):
		sql = "UPDATE Partida SET resultado = '{}' WHERE pk_id_partida = {}".format(resultado,id)
		self.cursor.execute(sql)
		self.connection.commit()

	def asignarGanador(self,pk_id_partida):
		self.asignarResultado(pk_id_partida,"gana")

	def asignarPerdedor(self,pk_id_partida):
		self.asignarResultado(pk_id_partida,"pierde")

	def asignarEmpate(self,pk_id_partida):
		self.asignarResultado(pk_id_partida,"empate")

	def conexionFinalizada(self):
		self.connection.close()
		print ("Se ha desconectado la base da datos.")


database = BasedeDatosJuego()

 # self.connection.commit() insertar/actualizemos,borremos un registro)