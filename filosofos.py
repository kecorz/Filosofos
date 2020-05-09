#python3
# ## ###############################################
#
# 
# Problema de los cinco filósofos de E. Dikjstra
#
#  Materia: Fundamentos de Sistemas Embebidos
#  Fecha: 04 /Mayo/2020
#
# ## ###############################################

#Importa la funcioón Thread del módulo threading
from threading import Thread, Lock
#Importa la librería para el uso de hilos 
import threading
#Importa la librería para realizar lectyra de línea de comandos
import sys
import time
#Importa la librería para la generación de números aleatorios
import random



#Variables con valores dafault
tiempo = 30
filosofos = 5

ultimo_filosfo = 0
lista_tenedores= []


#Despliega la ayuda (Forma correcta de compilar el programa)
def ayuda ():
	print("""
		Ingresaste mal los argumentos, intenta:
		filosofos.py [tiempo en segundos] [numero de filosofos]""")

def deja_tenedor(id_filosofo):
	global ultimo_filosfo
	global lista_tenedores
	#El filósofo libera el recurso (tenedor de la izquierda)
	lista_tenedores[int(id_filosofo)].release()	
	print("filósofo {} deja el palillo izquierdo".format(id_filosofo))
	if id_filosofo != 0:
		lista_tenedores[int(id_filosofo) - 1].release()	
		#El filósofo libera el recurso (tenedor de la derecha)
		print("filósofo {} deja el palillo derecho".format(id_filosofo))
	else:
		lista_tenedores[int(ultimo_filosfo) -1].release()


def toma_tenedor(id_filosofo):
	global ultimo_filosfo
	global lista_tenedores
	#El filósofo ocupa el recurso (tenedor de la izquierda)
	lista_tenedores[int(id_filosofo)].acquire()	
	print("filósofo {} toma el palillo izquierdo".format(id_filosofo))
	if id_filosofo != 0: 
		#El filósofo ocupa el recurso (tenedor de la derecha)
		lista_tenedores[int(id_filosofo) - 1].acquire()	
		print("filósofo {} toma el palillo derecho".format(id_filosofo))
	else:
		lista_tenedores[int(ultimo_filosfo) -1].acquire()


def vida_filosofo(id_filosofo):

	t_end = time.time() + tiempo 
	while time.time() < t_end: #Ciclo que controla los segundos ingresados
		
		#Generación de tiempo aleatorip entre 100 y 800 milisegundos
		tiempo_dormir = random.randint(100,800) 
		tiempo_dormir = tiempo_dormir/1000
		print("El filosofo {} esta pensando por {} [ms]".format(id_filosofo ,tiempo_dormir*1000))
		#El filosofo piensa por el tiempo calculado
		time.sleep(tiempo_dormir)
		print("Despertando hilo :"+(id_filosofo))
		toma_tenedor(id_filosofo) #llamada a la funcion toma_tenedor
		#Generación de tiempo aleatorio entre 100 y 200 milisegundos
		tiempo_comer = random.randint(100,200) 
		tiempo_comer = tiempo_comer/1000
		print("El filosofo {} esta comiendo por {} [ms]".format(id_filosofo ,tiempo_comer*1000))
		#El filosofo come por el tiempo calculado
		time.sleep(tiempo_comer)
		print("filosofo {} termino de comer".format(id_filosofo))
		deja_tenedor(id_filosofo)#llamada a la funcion deja_tenedor


	


def filosofo(f):

	#Creacion e inicio de hilos 
	for i in range(f):
		h = threading.Thread(target=vida_filosofo, args= (str(i)), name=str(i))
		h.start()#iniciamos los hilos

	for i in range(f):
		h.join


def main():
	global tiempo 
	global filosofos 

	global ultimo_filosfo 
	global lista_tenedores

	#Obtención de datos por argumentos ingresados desde linea de comandos
	argumentos = sys.argv
	#Limpia la lista argumentos
	argumentos.pop(0) 


	# Validaciones de argumentos 

	if len(argumentos) == 2:
		try:	
			#si los argumentos son dos numeros el programa realiza el algoritmo 
			tiempo = int(argumentos[0])
			filosofos = int(argumentos[1])

			lista_tenedores = [True]*filosofos
			ultimo_filosfo = int(argumentos[1])

			for k in range(0,filosofos):
				#Crea una lista Lock de la cantidad de filosofos ingresados
				lista_tenedores[k] = threading.Lock()		
			#llamada a la funcion que crea los hilos
			filosofo(filosofos)
				
		except :
			#Si los datos ingresados no son númericos, se despliega la ayuda
			print("Los argumentos ingresados no son númericos")
			ayuda()
			

	elif len(argumentos) ==  0:
		#Cuando no se ingresan argumentos, se inicia con valores deafult

		print("Comenzando programa con valores predeterminados")

		lista_tenedores = [True]*filosofos
		ultimo_filosfo = filosofos

		for k in range(0,filosofos):
			#Crea una lista Lock de la cantidad de filosofos default
			lista_tenedores[k] = threading.Lock()
		#llamada a la funcion que crea los hilos
		filosofo(filosofos)

	else: #En el caso de solo ingresar un argumento se despliega la ayuda
		if len(argumentos) == 1:
			print("Pocos argumentos \nPor favor ingresa dos argumentos")
			ayuda()	

		else: #En el caso de ingresar más de dos argumentos se despliega la ayuda
			print("Demasiados argumentos\nPor favor ingresa dos argumentos")
			ayuda()
			

#Llamada a la función mainn 
main()