# İmza Karşılaştırma Uygulaması

Bu proje, iki farklı imza görüntüsünü karşılaştırarak benzerlik derecesini hesaplayan bir Python uygulamasıdır. İmza karşılaştırma işlemi, OpenCV kullanılarak yapılan şablon eşleştirme (template matching) yöntemi ile gerçekleştirilir. Benzerlik skoru hesaplanır ve kullanıcının imzaların ne kadar benzer olduğunu anlayabileceği bir açıklama ile birlikte sunulur.

## Özellikler

- İki farklı imza dosyasını seçme ve karşılaştırma imkanı.
- İmzaların benzerlik skorunu hesaplama.
- Benzerlik skoruna göre "Çok Benzer", "Benzer", "Orta Derece Benzerlik", "Düşük Benzerlik", "Çok Düşük Benzerlik" açıklamaları.
- Kullanıcı dostu Tkinter arayüzü.
- İmza görüntülerinin arayüzde gösterilmesi.

## Ekran Görüntüleri

Aşağıda uygulamanın ekran görüntülerini bulabilirsiniz:


![Ekran görüntüsü_20241009_154639](https://github.com/user-attachments/assets/1082a590-d738-4802-947e-3eab26117f11)


![Ekran görüntüsü_20241008_131701](https://github.com/user-attachments/assets/91dbf3e3-5521-4ce1-ac0b-17405fbb0b72)


## Not:
Ekran görüntülerinden de görüldüğü gibi, Şablon Eşleştirme (Template Matching), sabit ve temiz imza verileri ile hızlı ve düşük maliyetli bir çözüm sunmaktadır; ancak ölçekleme ve döndürme gibi değişimlere karşı savunmasızdır. ORB algoritması ile geliştirilen imza karşılaştırma uygulaması, Şablon Eşleştirme yöntemine kıyasla daha dayanıklı ve esnek bir yaklaşım sunarak, farklı açılardaki ve boyutlardaki imzaları daha doğru bir şekilde karşılaştırabilmektedir. Geliştirdiğim ORB tabanlı uygulamayada buradan ulaşabilirsiniz: https://github.com/bilalakb/Signature-Comparison-Application-Using-ORB 


## Gereksinimler

Bu proje aşağıdaki kütüphaneleri gerektirir:

- **OpenCV**: Görüntü işleme işlemleri için.
- **NumPy**: Matris ve dizi işlemleri için.
- **Tkinter**: Grafik kullanıcı arayüzü için.
- **Pillow (PIL)**: Tkinter'da görüntüleri göstermek için.

Kütüphaneleri kurmak için:

```bash
pip install opencv-python numpy pillow
