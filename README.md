# [FLASK]OpenweathermapApi-TurkceSonuc


### Video Tutorial : https://www.youtube.com/watch?v=qacm4Kidk24
Flask kullanarak oluşturulan web uygulaması eklendi: (Şehir ismine göre api üzerinde sonuç döndürüyor.)
        - WebAPP[Flask] klasörünü indirip flask ve diğer paketlerin kurulduğu ortam içinde "python server.py" yazarak çalıştırabilirsiniz.
        - Gereksinimler:
            (Flask),
            (render_template),
            (request),
            (url_for),
            (json)



Python ile yazdığım bu fonksiyonla "Openweathermap Api" si kullanarak alınan sonuçları "Türkçeye" ve "Celcius" derece ye çeviriyoruz.

Bulut tipleri listesi:

    İngilizce = ['clear sky', 'few clouds','overcast clouds', 'scattered clouds', 'broken clouds', 'shower rain', 'rain', 'thunderstorm','snow','mist']
    Türkçe = ['Güneşli', 'Az Bulutlu','Çok Bulutlu(Kapalı)', 'Alçak Bulutlu', 'Yer Yer Açık Bulutlu', 'Sağanak Yağmurlu', 'Yağmurlu', 'Gök Gürültülü Fırtına', 'Karlı', 'Puslu']
    
 Sıcaklık defaul "Kelvin" olarak ayarlı. "Sıcaklık - 273.15" hesaplaması ile Celcius'a çevriliyor.
 
 Fonksiyon içine string olarak şehir ismi girildiğinde sonuç döndürülüyor.
