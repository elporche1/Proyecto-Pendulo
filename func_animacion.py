'''
Implementa funciones que permiten animar pendulos con matplotlib.
'''

# ---Imports---
# matplotlib.pyplot (plt): impresion grafica 2D
import matplotlib.pyplot as plt
# matplotlib.animation (anim): animacion grafica
import matplotlib.animation as anim
# mpl_toolkits.mplot3d.Axes3D: impresion grafica 3D
from mpl_toolkits.mplot3d import Axes3D


# ---Funciones---
def Animacion2D(t, size, x, y, fasex, fasey, fasex_label = '', fasey_label = '', m = [1]):
	'''
	Realiza una animacion en 2D con matplotlib de pendulos iterados.

	---Parametros---
	* t: array de tiempos
	* size: radio del espacio que ocupa el pendulo
	* x: lista que contiene arrays de posiciones x para cada bola a animar
	* y: lista que contiene arrays de posiciones y para cada bola a animar
	* fasex: array de variable para representar en espacio de fases en eje x
	* fasey: array de variable para representar en espacio de fases en eje y
	* fasex_label: label del eje x en el espacio de fases
	* fasey_label: label del eje y en el espacio de fases
	* m: lista con las masas de cada bola

	---Return---
	* <ArtistAnimation>: realiza la animacion
	'''
	# Creacion de la figura y los axes y configuraciones esteticas
	fig, ax = plt.subplots(1,2,figsize = (10,10))
	ax[0].set_aspect('equal')
	ax[0].set_xlim(-size, size)
	ax[0].set_ylim(-size, size)
	ax[1].set_xlabel(fasex_label)
	ax[1].set_ylabel(fasey_label)

	# Se crea una lista con colores para usarse en la animacion
	colores = ['red','blue','green']

	# Se inicializa la lista que contendra el pendulo y el temporizador
	objetos = []

	# Se itera para cada instante de tiempo
	for i, ti in enumerate(t):

		# Se inicializa la lista que contendra las distintas secciones del pendulo
		pendulo = []

		# Se itera para cada bola tomando sus componentes x e y
		for j, xj in enumerate(x):

			# Se crea la barra correspondiente y se añade a la lista
			barra, = ax[0].plot((0,xj[i]), (0,y[j][i]), '-', color='black') if j == 0 else ax[0].plot((x[j-1][i],xj[i]), (y[j-1][i],y[j][i]), '-', color='black')
			pendulo.append(barra)

			# Se crea la bola correspondiente y se añade a la lista
			bola = ax[0].scatter(xj[i], y[j][i], s=100 * m[j], color=colores[j % len(colores)], zorder=3)
			pendulo.append(bola)

			# Se crea la traza en el espacio de fases y se añade a la lista
			fases, = ax[1].plot(fasex[:i],fasey[:i],'k.', markersize=1)
			pendulo.append(fases)

		# Se crea el temporizador y se añade a la lista
		tempo = ax[0].text(0.05, 0.9, 't = %.2fs' % (ti), transform=ax[0].transAxes)
		pendulo.append(tempo)

		# Se añaden la instantanea del pendulo a la lista
		objetos.append(pendulo)

	# Se realiza la animacion al retornar un ArtistAnimation
	return anim.ArtistAnimation(fig, objetos, interval=1)

def Animacion3D(t, size, x, y, z, fasex, fasey, fasex_label = '', fasey_label = ''):
	'''
	Realiza una animacion en 3D con matplotlib de pendulos esfericos iterados.

	---Parametros---
	* t: array de tiempos
	* size: radio del espacio que ocupa el pendulo
	* x: lista que contiene arrays de posiciones x para cada bola a animar
	* y: lista que contiene arrays de posiciones y para cada bola a animar
	* z: lista que contiene arrays de posiciones y para cada bola a animar
	* fasex: array de variable para representar en espacio de fases en eje x
	* fasey: array de variable para representar en espacio de fases en eje y
	* fasex_label: label del eje x en el espacio de fases
	* fasey_label: label del eje y en el espacio de fases

	---Return---
	* <ArtistAnimation>: realiza la animacion
	'''
	# Creacion de la figura y los axes y configuraciones esteticas
	fig = plt.figure()
	ax1 = fig.add_subplot(1, 2, 1, projection = '3d')
	ax2 = fig.add_subplot(1, 2, 2)
	ax1.set_xlim((-size, size))
	ax1.set_ylim((-size, size))
	ax1.set_zlim((-size, size))
	ax2.set_xlabel(fasex_label)
	ax2.set_ylabel(fasey_label)

	# Se crea una lista con colores para usarse en la animacion
	colores = ['red','blue','green']

	# Se inicializa la lista que contendra el pendulo y el temporizador
	objetos = []

	# Se itera para cada instante de tiempo
	for i, ti in enumerate(t):

		# Se inicializa la lista que contendra las distintas secciones del pendulo
		pendulo = []

		# Se itera para cada bola tomando sus componentes x, y, z
		for j, xj in enumerate(x):

			# Se crea la barra correspondiente y se añade a la lista
			barra, = ax1.plot((0,xj[i]), (0,y[j][i]), (0,z[j][i]), '-', color='black') if j == 0 else ax1.plot((x[j-1][i],xj[i]), (y[j-1][i],y[j][i]), (z[j-1][i],z[j][i]),'-', color='black')
			pendulo.append(barra)

			# Se crea la bola correspondiente y se añade a la lista
			bola, = ax1.plot((xj[i],xj[i]), (y[j][i],y[j][i]), (z[j][i],z[j][i]), 'o', color=colores[j%len(colores)])
			pendulo.append(bola)

			# Se crea la traza en el espacio de fases y se añade a la lista
			fases, = ax2.plot(fasex[:i],fasey[:i],'k.', markersize=1)
			pendulo.append(fases)

		# Se crea el temporizador y se añade a la lista
		tempo = ax1.text(0.05, 0.9, 0.05, 't = %.2fs' % (ti), transform=ax1.transAxes)
		pendulo.append(tempo)

		# Se añade la instantanea del pendulo a la lista
		objetos.append(pendulo)

	# Se realiza la animacion
	return anim.ArtistAnimation(fig, objetos, interval=1)
