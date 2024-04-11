def GS_method(katsayilar, Y, tahminler):
    n = len(katsayilar) 
    for j in range(0, n):
        summ_val = Y[j]
        for i in range(0, n):
            if (j!=i):
                summ_val=summ_val-(katsayilar[j] [i] * tahminler[i])
        tahminler[j] = summ_val/katsayilar[j][j]
    # yeni tahmini döndür
    return tahminler

"""
8x1+3x2-3x3=14
-2x1-8x2+5x3=5
3x1+5x2+10x3=-2
"""
katsayilar = [[8, 3, -3],[-2, -8, 5],[3, 5, 10]] #bilinmeyenlerin katsayıları
Y = [14, 5, -8] # eşittirin sağındaki değerler
tahminler = [0, 0, 0] # yöntem için ilk tahminimiz

for i in range(10):
    tahminler = GS_method(katsayilar, Y, tahminler)
    print(tahminler)
