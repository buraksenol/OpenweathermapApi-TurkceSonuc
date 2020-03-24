# [FLASK]OpenweathermapApi-TurkceSonuc

Flask kullanarak oluşturulan web uygulaması eklendi: (Şehir ismine göre api üzerinde sonuç döndürüyor.)

Python ile yazdığım bu fonksiyonla "Openweathermap Api" si kullanarak alınan sonuçları "Türkçeye" ve "Celcius" derece ye çeviriyoruz.

Bulut tipleri listesi:

    İngilizce = ['clear sky', 'few clouds','overcast clouds', 'scattered clouds', 'broken clouds', 'shower rain', 'rain', 'thunderstorm','snow','mist']
    Türkçe = ['Güneşli', 'Az Bulutlu','Çok Bulutlu(Kapalı)', 'Alçak Bulutlu', 'Yer Yer Açık Bulutlu', 'Sağanak Yağmurlu', 'Yağmurlu', 'Gök Gürültülü Fırtına', 'Karlı', 'Puslu']
    
 Sıcaklık defaul "Kelvin" olarak ayarlı. "Sıcaklık - 273.15" hesaplaması ile Celcius'a çevriliyor.
 
 Fonksiyon içine string olarak şehir ismi girildiğinde sonuç döndürülüyor.
