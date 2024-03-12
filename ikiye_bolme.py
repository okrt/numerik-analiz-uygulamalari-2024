import time
def ikiye_bolme(f,a,b,tolerans=0.001,maks_iter=1000):
    iter=0
    s=time.time()
    if f(a)*f(b)>=0:
        print("Hata,  girilen aralıkta kökün iki tarafında fonksiyon farklı işarette olmalı")
    else:
        for i in range(maks_iter):
            iter+=1
            c=(a+b)/2
            print(f(c))
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
    return x**3+4*x**2-10

kok=ikiye_bolme(f,1,2,maks_iter=1000,tolerans=0.01)
print("Kök= ",kok)