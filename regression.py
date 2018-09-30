from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
import xlrd
import numpy as np 
import numpy.polynomial.polynomial as poly
import matplotlib.pyplot as plt

book = xlrd.open_workbook('toddurtype.xlsx')
sheet = book.sheet_by_name('Sheet1')
data = np.array([[sheet.cell_value(r+1, c) for c in range(sheet.ncols)] for r in range(sheet.nrows-1)])
n=0
while data[n, 2] == "Study":
	n+=1


#fake data
x = np.asarray(data[0:n, 0], dtype = float)
y = np.asarray(data[0:n, 1], dtype = float)
#x_new = np.linspace(x[0], x[-1], num=len(x)*10)

z = np.polyfit(x, y, 4)
print(z)

m=n
while data[m, 2] == "Sport":
	m+=1

#fake data
x2 = np.asarray(data[n:m, 0], dtype = float)
y2 = np.asarray(data[n:m, 1], dtype = float)
#x_new = np.linspace(x[0], x[-1], num=len(x)*10)

a = np.polyfit(x2, y2, 4)
print(a)

o=m
while data[(o), 2] == "Leisure":
	o+=1
	if o>= len(data):
		break

#fake data
x3 = np.asarray(data[m:(o), 0], dtype = float)
y3 = np.asarray(data[m:(o), 1], dtype = float)
#x_new = np.linspace(x[0], x[-1], num=len(x)*10)

b = np.polyfit(x3, y3, 4)
print(b)


	#print(coefs)
	#ffit = poly.polyval(x_new, coefs)
	#plt.plot(x_new, ffit)
	#fig1 = plt.figure()                                                                                           
	#ax1 = fig1.add_subplot(111)                                                                                   
	#ax1.scatter(x, y, facecolors='None')                                                                     
	#ax1.plot(x_new, ffit(x_new))                                                                     
	#plt.show()


#ffit = poly.Polynomial(coefs)    
#plt.plot(x_new, ffit(x_new))
