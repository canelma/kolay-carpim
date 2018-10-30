# Kolay Çarpım

Bu repodaki kodlar, fark ettiğim bir çarpma formülünün başarı oranını görmek için yazıldı.

### Ne işe yarar?  
10 - 19 arası tüm iki basamaklı sayıların birbiriyle çarpılmasında sonuç doğru bulunuyor. Sonrasında ise, sadece 10 ve katları arasındaki çarpımlar doğru çıkıyor. 10x20 20x30 20x40 gibi..


### Bir örnek ile algoritma ve mantık:  
İşlem yalnızca iki veya üç adımda tamamlansa da, aşağıda detaylıca işlenmiştir.
1. İki basamaklı iki adet sayı alınır. (Örneğin: 15 ve 14)
2. İki sayının birler basamağı çarpılır. (4x5=20)
3. Sonuç tek basamaklıysa en sağa yazılır(sonraki sayılar soluna yazılacak)
4. Sonuç çift basamaklıysa, birler basamağı en sağa yazılır, onlar basamağı elde var olarak tutulur, sonraki sayıyla toplayacağız. (..0 - elde var 2)
5. İki sayının yine birler basamağı, toplanır. Varsa, 4. adımdan kalan değerle de toplanır. (9 + elde var 2 = 11) eğer çift basamaklıysa, 4. adım tekrarlanır. (.10 - elde var 1)
6. İki sayının onlar basamağı çarpılır. (1x1=1) 5. adımdan kalan elde var ile toplanır. (1+1=2)
7. En sola yazılır. (210)
8. Sonuç 210 olmalıdır, formüle göre.
---

**Not:** Basit bir işlem olduğu için, kodlar karalama formatında yazılmıştır.
Python3 ile çalıştırınız.
