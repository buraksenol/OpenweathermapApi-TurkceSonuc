from flask import Flask, render_template, request, url_for
import requests
import json

app = Flask(__name__)


def havaDurumu(self):
    city = self
    apiKey = 'YOUR_API_KEY'
    response = requests.get(f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={apiKey}')
    weatherData = response.json()

    skyDescription = weatherData['weather'][0]['description']
    cityName = weatherData['name']
    skyTypes = ['clear sky', 'few clouds','overcast clouds', 'scattered clouds','light rain', 'broken clouds', 'shower rain', 'rain', 'thunderstorm','snow','mist']
    skyTypesTR = ['Güneşli', 'Az Bulutlu','Çok Bulutlu(Kapalı)', 'Alçak Bulutlu', 'hafif yağmur', 'Yer Yer Açık Bulutlu', 'Sağanak Yağmurlu', 'Yağmurlu', 'Gök Gürültülü Fırtına', 'Karlı', 'Puslu']

    for i in range(len(skyTypes)):
        if skyDescription == skyTypes[i]:
            skyDescription = skyTypesTR[i]

    temp = round((weatherData['main']['temp'] - 273.15), 2)
    feels_temp = round((weatherData['main']['feels_like'] - 273.15), 2)
    temp_min = round((weatherData['main']['temp_min'] - 273.15), 2)
    temp_max = round((weatherData['main']['temp_max'] - 273.15), 2)

    havadurumuDict = {
        "Şehir": cityName,
        "Gökyüzü": skyDescription,
        "Sıcaklık": temp,
        "Hissedilen": feels_temp,
        "Minimum": temp_min,
        "Maksimum": temp_max

    }

    return havadurumuDict

@app.route("/", methods=['POST','GET'])
def index():

    if request.method == 'POST':
        city = request.form['data']
        if not city:
            return render_template('index.html')

        a = havaDurumu(city)
        return render_template('sonuc.html', sonuc = a)
    else:
        return render_template('index.html')


if __name__ == "__main__":

    app.run(debug=True)
