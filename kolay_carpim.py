"""
not: basit bir islem oldugu icin, kodlar karalama formatinda yazilmistir.
python3 ile calistiriniz.
-------------------------------------------------------------------------
bu, fark ettigim bir carpma formulunun basari oranini gormek icin yazildi.
ornek ile algoritma/mantik:
    1. iki basamakli iki adet sayi alinir. (ornegin: 15 ve 14)
    2. iki sayinin birler basamagi carpilir. (4x5=20)
    3. sonuc tek basamakliysa en saga yazilir(sonraki sayilar soluna yazilacak)
    4. sonuc cift basamakliysa, birler basamagi en saga yazilir, onlar basamagi
    elde var olarak tutulur, sonraki sayiyla toplayacagiz. (..0 - elde var 2)
    5. iki sayinin yine birler basamagi, toplanir. varsa, 4. adimdan kalan
    degerle de toplanir. (9 + elde var 2 = 11) Eger cift basamakliysa, 4. adim
    tekrarlanir. (.10 - elde var 1)
    6. iki sayinin onlar basamagi carpilir. (1x1=1) 5. adimdan kalan elde var
    ile toplanir. (1+1=2)
    7. en sola yazilir. (210)
    8. sonuc 210 olmalidir, formule gore.
    ---
    10 - 19 arasi tum iki basamakli sayilarin birbiriyle carpilmasinda sonuc
    dogru bulunuyor. sonrasinda ise, sadece 10 ve katlari arasindaki carpimlar
    dogru cikiyor. 10x20 20x30 20x40 gibi..
"""


# sayinin n. basamagini dondurur.
# sayima sagdan baslar, baslangic sifirdir
def get_digit(number, n):
    return number // 10**n % 10


# elde var sistemini simule eder.
# sagdaki sayinin onlar basamagini soldakine ekler,
# sagdaki sayiyi da kendisinin birler basamagina esitler
def rex(left, right):
    left, right = int(left), int(right)
    left += get_digit(right, 1)
    right = get_digit(right, 0)

    return left, right


# asil hesap burada yapilmaktadir.
# once iki sayinin da birler basamagini carpar
# sonra iki sayinin da birler basamagini toplar
# sonra iki sayinin da onlar basamagini carpar
def calculate(i, y):
    first = get_digit(i, 0) * get_digit(y, 0)
    second = get_digit(i, 0) + get_digit(y, 0)
    third = get_digit(i, 1) * get_digit(y, 1)

    if len(str(first)) > 1:
        second, first = rex(second, first)

    if len(str(second)) > 1:
        third, second = rex(third, second)

    first, second, third = str(first), str(second), str(third)
    result = third + second + first

    return int(result)


# dogrular, yanlislar
right, wrong = list(), list()


# iki haneli tum sayilari, iki haneli tum sayilarla
# carptigimiz ana kisim burasidir
for i in range(10, 100):
    for y in range(i, 100):
        result = calculate(i, y)
        real_result = i * y

        # formulle bulunan sayi, asil sonuc ile ayni ise
        if result == real_result:
            # dogrular listesine ekle
            right.append(("{} x {} = {}".format(i, y, result)))
        else:  # degilse
            # yanlislar listesine ekle
            wrong.append(("{} x {} = {} ({})".format(
                            i, y, result, real_result)))

# dogrulari ekrana bastir
for i in right:
    print(i)

print('='*15)

# iki basamakli tum sayilarin birbiri ile carpimina gore:
print('Right: {}'.format(len(right)))  # toplam dogru sayisi
print('Wrong: {}'.format(len(wrong)))  # toplam yanlis sayisi

# sonuclara bakildiginda gorulecektir ki, 10-19 arasi tum sayilarin carpiminda
# formul basarilidir. ayrica 10 ve katlarinin carpimlarinda da
# (ornegin 20x30) basarilidir
# diger islemlerde basarisizdir
