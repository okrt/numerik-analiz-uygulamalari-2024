import time
def regula_falsi(f,a,b,tolerans=0.001,maks_iter=1000):
    iter=0
    s=time.time()
    if f(a)*f(b)>=0:
        print("Hata,  girilen aralıkta kökün iki tarafında fonksiyon farklı işarette olmalı")
    else:
        for i in range(maks_iter):
            iter+=1
            c=(a*f(b)-b*f(a))/(f(b)-f(a))
            if f(c)==0:
                print("İterasyon sayısı: ",iter," Süre: ",time.time()-s)
                print("Kesin Kök Bulundu!")
                return c

            elif abs(f(c))<tolerans:
                print("İterasyon sayısı: ",iter," Süre: ",time.time()-s)
                print("Yaklaşık Kök Bulundu!")
                return c
            if f(c)*f(a)<0:
                b=c
            else:
                a=c
        print("Kök bulunamadı")



def f(x):
    return x-(2**(-x))

kok=regula_falsi(f,0,1,tolerans=0.00001,maks_iter=1000)
print("Kök= ",kok)