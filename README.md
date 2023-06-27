# Python RabbitMQ ile Olay Odaklı Microservices Projesi

Bu proje, Python kullanılarak geliştirilmiş bir olay odaklı mikro hizmetler örneğidir. Projede Docker kullanılmıştır.

## Proje Açıklaması

Bu proje, mikro hizmetler mimarisi kullanılarak olay odaklı bir sistem tasarımını göstermektedir. RabbitMQ mesaj kuyruğu, mikro hizmetler arasındaki iletişimi sağlamaktadır. Her bir mikro hizmet, olaylara abone olur ve gelen olayları işler.

## Proje Kurulumu

1. Bu projeyi klonlayın:

   ```bash
   git clone https://github.com/kullanici_adi/proje-adi.git


2. Proje dizinine gidin:

   ```bash
   cd proje-adi


3. Docker konteynerlerini başlatmak için aşağıdaki komutu çalıştırın:

   ```bash
   docker-compose up


Bu komut, RabbitMQ ve diğer mikro hizmetleri içeren Docker konteynerlerini oluşturacak ve başlatacaktır.

4. Mikro hizmetlerin çalıştığından emin olmak için bir web tarayıcısıyla `http://localhost` adresine gidin. Mikro hizmetlerin başarılı bir şekilde çalıştığını görmelisiniz.

## Katkılar

Katkıda bulunmak isterseniz, lütfen yeni bir dal oluşturun ve değişiklikleriniz için bir pull talebi gönderin.


