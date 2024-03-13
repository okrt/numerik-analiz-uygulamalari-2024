import time
"""
Newton-Raphson Yöntemi
Karekök 2'nin sayısal değerini Newton Raphson yöntemiyle hesaplayalım.

x^2-2=0 denkleminin kökünün karekök 2 olduğunu biliyoruz.

Bunu fonksiyon halinde yazıp türevini alalım:
f(x)=x**2-2
f'(x)=2*x
Bu değerleri kullanarak Newton-Raphon methodunu uygulayabiliriz.
yeni kök tahmini=eski kök tahmini- (f(x)-f'(x))

"""
def f(x):
	return x**2-2

def f_turev(x):
	return 2*x


def newton_raphson(x,tolerans=0.000001):
	iterasyon=0
	s=time.time()
	bolum = f(x)/f_turev(x)
	while abs(bolum)>=tolerans:
		iterasyon+=1
		bolum = f(x)/f_turev(x)
		# yeni x = eski x - f(x) / f'(x)
		x = x - bolum
	
	print("Bulunan Kök : ",x,"İterasyon:",iterasyon,"Süre:", time.time()-s)

# Başlangıç için köke tahmini bir değer verelim.
baslangic_degeri = 10
newton_raphson(baslangic_degeri)