#=======INPUT Parameter=====================================================================================
#---n1=ref index Core, n2=ref index cladding kiri, n3=ref index cladding kanan---------------------------
from scipy import*
from numpy import*
import matplotlib.pyplot as plt
n1=1.55e0
n2=1.545e0
n3=1.545e0
wle=1.55e-6
nmoda=2
rentang=4000
lim=(n1)-0.00001
df_tot=zeros (((nmoda,rentang)),dtype=float) 
dne_tot=zeros(((nmoda,rentang)),dtype=float)
hasil=open ("beta.txt", 'w')
#=======mencari fx1(x)====================================================================================
def fx1(x):
	vf1=k0*sqrt(n1*n1-n2*n2)
	vf2=k0*sqrt(n1*n1-n3*n3)
	fx1=fx1=2.0e0*t*k0*sqrt(n1*n1-x*x)-(arctan(sqrt(vf1*vf1-k0*k0*(n1*n1-x*x))/(k0*sqrt(n1*n1-x*x))))-(arctan(sqrt(vf2*vf2-k0*k0*(n1*n1-x*x))/(k0*sqrt(n1*n1-x*x))))-kk*pi
	return fx1			
#=======mencari dne=======================================================================================
def dne():
	a=(n2)+0.0000001
	b=(n1)
	c=0
	e=1.0e-10
	npn=(log10((b-a)/e))/(log10((2.0e0)+0.5e0))
	npn=int(npn)
	#print ("npn=",npn)
	fa=fx1(a)
	#hasil.write ("\n")
	#hasil.write ("fa=")
	#hasil.write(str(fa))
	#hasil.write ("\n")
	#print (fa)
	#print ("fa=",fa)
	for m in range(1,npn,1):
		#print (m)
		c=(a+b)/2.0e0
		fc=fx1(c)
		#hasil.write ("fc=")
		#hasil.write (str(fc))
		#hasil.write ("\t")
		#print (fc)
		#print ("c=",c)
		if (fa*fc)<0.0:
			b=c
		else:
			a=c
	dne=c
	return dne
#=======Perhitungan LOOP Moda-moda--- MAIN PROGRAM========================================================
for kk in range (0,nmoda,1):
	print ("kk=",kk)
	hasil.write("\n")
	df=0.5e-6
	for j in range (1,rentang,1):
		#print ("j=",j)
		df=df+0.01e-6
		k0=2*pi/wle
		t=df/2.0
		dne_val=dne()
		#print (dne_val)
		if dne_val<lim:
			df_tot[(kk),(j-1)]=df
			dne_tot[(kk),(j-1)]=dne_val
			#print(kk,"\t",j,"\t",df,"\t",dne_val)
			hasil.write ("\n")
			#hasil.write (str(kk))
			#hasil.write ("\t")
			#hasil.write (str(j))
			#hasil.write ("\t")
			hasil.write (str(df))
			hasil.write ("\t")
			hasil.write (str(dne_val))
	
print (df_tot[0])
print (dne_tot[0])
plt.plot(df_tot[0], dne_tot[0], label='kk=0')
plt.plot(df_tot[1], dne_tot[1], label='kk=1')
plt.axis([5e-07,4.1e-05,1.545,1.55])
plt.xlabel('df')
plt.ylabel('dne')

plt.title("beta")

plt.legend()
plt.show()
