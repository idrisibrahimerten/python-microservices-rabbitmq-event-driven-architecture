# python-microservices-rabbitmq-event-driven-architecture
Python Microservices - Olay Odaklı Mimari ve RabbitMQ ile
Bu proje, Python kullanarak geliştirilmiş bir mikro hizmetler örneğidir. Olay odaklı mimari kullanılarak RabbitMQ mesaj kuyruğu ile iletişim sağlanmaktadır.

Proje Açıklaması
Bu proje, mikro hizmetler mimarisi ve olay odaklı tasarımın bir örneğini sunmaktadır. Python dili kullanılarak geliştirilen mikro hizmetler, RabbitMQ mesaj kuyruğu üzerinden iletişim kurmaktadır. Bu sayede olaylar abone edilir ve gelen olaylar ilgili hizmetler tarafından işlenir.

Proje Kurulumu
Bu projeyi klonlayın:

```bash
git clone https://github.com/kullanici_adi/proje-adi.git


```bash
pip install -r requirements.txt
Proje dosyalarını çalıştırın:

```bash
python main.py
Uygulamayı test etmek için ayrı bir terminal penceresi açın ve aşağıdaki komutu çalıştırın:

```bash
python publisher.py
Katkılar
Katkıda bulunmak isterseniz, lütfen yeni bir dal oluşturun ve değişiklikleriniz için bir pull talebi gönderin.

English README.md Sample:

Python Microservices - Event-Driven Architecture with RabbitMQ
This project is an example of microservices developed using Python. It showcases an event-driven architecture with communication facilitated through RabbitMQ message queue.

Project Description
This project demonstrates an example of microservices architecture and event-driven design using Python. The microservices, developed in Python, communicate through the RabbitMQ message queue. Events are subscribed and processed by the respective services.

Project Setup
Clone this project:

```bash
git clone https://github.com/username/project-name.git

```bash
pip install -r requirements.txt
Run the project files:

```bash
python main.py
To test the application, open a separate terminal window and run the following command:

```bash
python publisher.py
Contributions
If you'd like to contribute, please create a new branch and submit a pull request with your changes.