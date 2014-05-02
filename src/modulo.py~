
PI=3.1415926535
import sys


#funcion para calculo de pi
def calculo(n):
  suma=0.0
  for i in range (1,n+1):
    if(n<0):
      return suma
    x_i= float ((i-0.5)/n)      #calculo del intervalo xi
    fx_i= float (4./(1+x_i**2)) #calculo de f(xi)
    suma = suma + fx_i          #sumatorio de f(xi) desde i hasta n+1 
  r = float (1/float(n) * suma) #aproximacion de pi
  return r

if __name__=="__main__":
  l=[]
  n = int(sys.argv[1])           
  m = int(sys.argv[2]) 
  print calculo(n)
  print calculo(m)
  for i in range (1,m+1): 
    r=calculo(i*n)                  #utiliza la funcion aprox para calcular pi
    l=l+[r]                  #lista que suma la aproximacion (cuanto mas valores calcula mas aproximado esta a pi)
  print l 