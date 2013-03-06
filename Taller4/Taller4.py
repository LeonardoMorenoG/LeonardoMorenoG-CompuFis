import os
import numpy
import sys
#import pylab
import scipy
from scipy.optimize import curve_fit
from scipy.linalg import eigh


table = []
theta = []
var_gravity = []
avg_grav = []
pca = []
data = open('data.dat', 'w')

# corre un loop en el directorio hw4_data
for filename in os.listdir('hw4_data/' ):

        datos = []
        tiempo = []
        x = []
        y = []
        nomarch = (filename.replace('.dat','')).split('_')

        path = os.path.expanduser('hw4_data/' + filename)
       
	coso = open(path, 'r').readlines()
	
	datos = numpy.loadtxt(path)

      
        # crea los arrays con los datos de los archivos
	tiempo=datos[:,0]
	x=datos[:,1]
        y=datos[:,2]

        # encuentra las ecuacion de x y haciendo un fit
        ecx = numpy.polyfit(numpy.array(tiempo), numpy.array(x), 1.0)
        ecy = numpy.polyfit(numpy.array(tiempo), numpy.array(y), 2.0)

        # agrega a la lista una tupla con la informacion del archivo
        table.append((int(nomarch[1]),float(nomarch[3]),float(ecx[0]),float(ecy[1]),(-2.0*float(ecy[0]))))

		
		

        # Organiza los datos en orden creciente respecto al angulo
	table.sort(key=lambda tup: tup[1])
	
	# crea un archivo con los datos necesarios
	for row in table:
		for ht in row:
			data.write( '%f ' % (ht))
		data.write('\n')

print 'information exported sucessfully in data.dat'


F=[]
gmd = []
angulo = []
gmedia = []
cont = 0
cont2 = 0

for row in table:	       
	if row[1] not in angulo: #creo q sobra este if
	       angulo.append(row[1])
	

for ang in angulo:
	cont = 0.0	
	for line in table:
		if (line[1] == ang):
			cont += line[4]

       	cont /= 6.0
       	gmedia.append(cont)


for g in gmedia:
	F.append(1 -((g)/(9.81)))  



	







	      



			    


		
	



