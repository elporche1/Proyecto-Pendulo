'''
Funciones con ecuaciones diferenciales para los distintos pendulos
'''

# ---Imports---
# numpy (np): manejo de arrays
import numpy as np

# ---Funciones---
def Simple(params, t, g, L, b, m):
	'''
	Ecuacion diferencial del pendulo simple

	---Parametros---
	* params: tupla con los valores (th,w)
	* t: tiempo
	* g: gravedad
	* L: longitud de la barra
	* b: coeficiente de rozamiento con el aire

	---Return---
	* <lista>: [diff1 de th, diff2 de th]
	'''
	th, w = params

	a = - b/m * w - g/L * np.sin(th)

	return [w, a]

def Doble(params, t, g, L1, L2, m1, m2):
	'''
	Ecuacion diferencial del pendulo doble

	---Parametros---
	* params: tupla con los valores (th1,w1,th2,w2)
	* t: tiempo
	* g: gravedad
	* L1: longitud de la barra 1
	* L2: longitud de la barra 2
	* m1: masa de la bola 1
	* m2: masa de la bola 2

	---Return---
	* <lista>: [diff1 de th1, diff2 de th1, diff1 de th2, diff2 de th2]
	'''
	th1, w1, th2, w2 = params

	dth = th1-th2; sdth = np.sin(dth); cdth = np.cos(dth)
	Lth1 = w1**2*L1; Lth2 = w2**2*L2
	A = 2*m1+m2; B = (A-m2*np.cos(2*dth))

	a1 = (-g*(A*np.sin(th1)+m2*np.sin(th1-2*th2))-2*m2*sdth*(Lth2+Lth1*cdth))/(L1*B)
	a2 = (2*sdth*((m1+m2)*(Lth1+g*np.cos(th1))+Lth2*m2*cdth)) / (L2*B)

	return [w1, a1, w2, a2]

def Triple(params, t, g, L1, L2, L3, m1, m2, m3):
	'''
	Ecuacion diferencial del pendulo triple

	---Parametros---
	* params: tupla con los valores (th1,w1,th2,w2,th3,w3)
	* t: tiempo
	* g: gravedad
	* L1: longitud de la barra 1
	* L2: longitud de la barra 2
	* L3: longitud de la barra 3
	* m1: masa de la bola 1
	* m2: masa de la bola 2
	* m3: masa de la bola 3

	---Return---
	* <lista>: [diff1 de th1, diff2 de th1, diff1 de th2, diff2 de th2, diff1 de th3, diff2 de th3]
	'''
	th1, w1, th2, w2, th3, w3 = params

	m12 = m1 + m2; m23 = m2 + m3
	th21 = th2 - th1; th32 = th3 - th2; th31 = th3 - th1
	den = m1*m3*np.cos(2*th32)+m2*m23*np.cos(2*th21)-m12*m3-m2**2-2*m1*m2

	a1 = (L3/L1*m2*m3*(np.sin(th32-th21)-np.sin(th31))*w3**2-2*L2/L1*m2*m23*np.sin(th21)*w2**2-m2*m23*np.sin(2*th21)*w1**2+g/L1*(0.5*m1*m3*(np.sin(2*th32-th1)-np.sin(2*th32+th1))-m2*m23*np.sin(th2+th21)+(m12*m3+m2**2+2*m1*m2)*np.sin(th1)))/den
	a2 = (L3/L2*m3*(m2*np.sin(th31+th21)-(m12+m1)*np.sin(th32))*w3**2+(m2*m23*np.sin(2*th21)-m1*m3*np.sin(2*th32))*w2**2+L1/L2*(((m12+m1)*m3+2*m12*m2)*np.sin(th21)-m1*m3*np.sin(th32+th31))*w1**2+g/L2*(-0.5*m1*m3*np.sin(th32+th31-th1)-0.5*m1*m3*np.sin(th32+th3)+(0.5*(m12+m2)*m3+m2*m12)*np.sin(th21-th1)+(0.5*(m12+m2)*m3+m2*m12)*np.sin(th2)))/den
	a3 = (m1*m3*np.sin(2*th32)*w3**2+2*L2/L3*m1*m23*np.sin(th32)*w2**2+L1/L3*m1*m23*(np.sin(th32-th21)+np.sin(th31))*w1**2+0.5*g/L3*m1*m23*(np.sin(th32-th21+th1)+np.sin(th32-th2)+np.sin(th31-th1)+np.sin(th3)))/den

	return [w1, a1, w2, a2, w3, a3]

def Esferico(params, t, g, L):

	'''
	Ecuacion diferencial del pendulo esferico

	---Parametros---
	* params: tupla con los valores (th,wth,ph,wph)
	* t: tiempo
	* g: gravedad
	* L: longitud de la barra

	---Return---
	* <lista>: [diff1 de th, diff2 de th, diff1 de ph, diff2 de ph]
	'''
	th, wth, ph, wph = params

	ath = -2*wth*wph/np.tan(ph)
	aph = wth**2*np.sin(ph)*np.cos(ph)-g/L*np.sin(ph)

	return [wth, ath, wph, aph]

def a_simple(th, w, ctes):
	'''
	Define la ecuacion diferencial de las aceleraciones de un pendulo simple

	---Parametros---
	* th: lista con un unico elemento que es el angulo
	* w: lista con un unico elemento que es la velocidad angular
	* ctes: tupla con las constantes del experimento (g,L,b)

	---Return---
	* <lista>: un unico elemento que es la aceleracion angular
	'''
	g, L, b, m = ctes

	return [- b/m * w[0] - g/L * np.sin(th[0])]

def a_doble(th, w, ctes):
	'''
	Define la ecuacion diferencial de las aceleraciones de un pendulo doble

	---Parametros---
	* th: lista con el angulo para cada bola
	* w: lista con la velocidad angular para cada bola
	* ctes: tupla con las constantes del experimento (g,m1,m2,L1,L2)

	---Return---
	* <float>: aceleracion angular de la bola 1
	* <float>: aceleracion angular de la bola 2
	'''
	g, m1, m2, L1, L2 = ctes
	th1, th2 = th
	w1, w2 = w

	A = 2*m1+m2
	dth = th1-th2
	sdth = np.sin(dth)
	cdth = np.cos(dth)
	Lth1 = w1**2*L1
	Lth2 = w2**2*L2
	B = (A-m2*np.cos(2*dth))

	a1 = (-g*(A*np.sin(th1)+m2*np.sin(th1-2*th2))-2*m2*sdth*(Lth2+Lth1*cdth))/(L1*B)
	a2 = (2*sdth*((m1+m2)*(Lth1+g*np.cos(th1))+Lth2*m2*cdth)) / (L2*B)

	return a1, a2

def a_triple(th, w, ctes):
	'''
	Define la ecuacion diferencial de las aceleraciones de un pendulo triple

	---Parametros---
	* th: lista con el angulo para cada bola
	* w: lista con la velocidad angular para cada bola
	* ctes: tupla con las constantes del experimento (g,m1,m2,m3,L1,L2,L3)

	---Return---
	* <float>: aceleracion angular de la bola 1
	* <float>: aceleracion angular de la bola 2
	* <float>: aceleracion angular de la bola 3
	'''
	g, m1, m2, m3, L1, L2, L3 = ctes
	th1, th2, th3 = th
	w1, w2, w3 = w

	m12 = m1 + m2
	m23 = m2 + m3
	th21 = th2 - th1
	th32 = th3 - th2
	th31 = th3 - th1
	den = m1*m3*np.cos(2*th32)+m2*m23*np.cos(2*th21)-m12*m3-m2**2-2*m1*m2

	a1 = (L3/L1*m2*m3*(np.sin(th32-th21)-np.sin(th31))*w3**2-2*L2/L1*m2*m23*np.sin(th21)*w2**2-m2*m23*np.sin(2*th21)*w1**2+g/L1*(0.5*m1*m3*(np.sin(2*th32-th1)-np.sin(2*th32+th1))-m2*m23*np.sin(th2+th21)+(m12*m3+m2**2+2*m1*m2)*np.sin(th1)))/den
	a2 = (L3/L2*m3*(m2*np.sin(th31+th21)-(m12+m1)*np.sin(th32))*w3**2+(m2*m23*np.sin(2*th21)-m1*m3*np.sin(2*th32))*w2**2+L1/L2*(((m12+m1)*m3+2*m12*m2)*np.sin(th21)-m1*m3*np.sin(th32+th31))*w1**2+g/L2*(-0.5*m1*m3*np.sin(th32+th31-th1)-0.5*m1*m3*np.sin(th32+th3)+(0.5*(m12+m2)*m3+m2*m12)*np.sin(th21-th1)+(0.5*(m12+m2)*m3+m2*m12)*np.sin(th2)))/den
	a3 = (m1*m3*np.sin(2*th32)*w3**2+2*L2/L3*m1*m23*np.sin(th32)*w2**2+L1/L3*m1*m23*(np.sin(th32-th21)+np.sin(th31))*w1**2+0.5*g/L3*m1*m23*(np.sin(th32-th21+th1)+np.sin(th32-th2)+np.sin(th31-th1)+np.sin(th3)))/den

	return a1, a2, a3

def a_esferico(ang, w, ctes):
	'''
	Define la ecuacion diferencial de las aceleraciones de un pendulo doble

	---Parametros---
	* ang: lista con los dos angulos
	* w: lista con las dos velocidades angulares
	* ctes: tupla con las constantes del experimento (g,L)

	---Return---
	* <float>: aceleracion angular de theta
	* <float>: aceleracion angular de phi
	'''
	g, L = ctes
	th, ph = ang
	wth, wph = w

	ath = -2*wth*wph/np.tan(ph)
	aph = wth**2*np.sin(ph)*np.cos(ph)-g/L*np.sin(ph)

	return ath, aph
