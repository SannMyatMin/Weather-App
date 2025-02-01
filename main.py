import sys
import requests
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QLabel, QLineEdit
from PyQt5.QtCore import Qt


class WeatherApp(QWidget):
    def __init__(self):
        super().__init__()
        self.enter_city_name = QLabel("Enter City Name",self)
        self.input_city      = QLineEdit(self)
        self.get_weather     = QPushButton("Get Weather",self)
        self.temperature     = QLabel(self)
        self.emoji           = QLabel(self)
        self.description     = QLabel(self)

        self.UiUx()


    def UiUx(self):
        self.setWindowTitle("Weather Application for Cities")

        vbox = QVBoxLayout()
        vbox.addWidget(self.enter_city_name)
        vbox.addWidget(self.input_city)
        vbox.addWidget(self.get_weather)
        vbox.addWidget(self.temperature)
        vbox.addWidget(self.emoji)
        vbox.addWidget(self.description)
        self.setLayout(vbox)

        self.enter_city_name.setAlignment(Qt.AlignCenter)
        self.input_city.setAlignment(Qt.AlignCenter)
        self.temperature.setAlignment(Qt.AlignCenter)
        self.emoji.setAlignment(Qt.AlignCenter)
        self.description.setAlignment(Qt.AlignCenter)

        self.enter_city_name.setObjectName("EnterCity")
        self.input_city.setObjectName("I_City")
        self.get_weather.setObjectName("GetW")
        self.temperature.setObjectName("Temp")
        self.emoji.setObjectName("Emj")
        self.description.setObjectName("Desc")

        self.setStyleSheet("""
                            #EnterCity
                            { 
                                font-size   : 24px;
                                font-family : Aerial;
                                font-style  : italic;
                            }
                            #I_City
                            {
                                font-size : 22px;
                            }
                            #GetW
                            {
                                font-size   : 17px;
                                font-weight : bold;
                            }
                            #Temp
                            {
                                font-size : 28px;
                            }
                            #Emj
                            {
                                font-size   : 80px;
                                font-family : segoe UI emoji;
                            }
                            #Desc
                            {
                                font-size : 23px;
                            }
                          """)
        self.get_weather.clicked.connect(self.get_weather_data)

    def get_weather_data(self):
        api_key  = "f85efd938fa3d5894ffbc9af37cef8cb"
        city     = self.input_city.text()
        url      = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"

        try:
            response = requests.get(url)
            response.raise_for_status()
            data     = response.json()
            if data["cod"] == 200:
                self.display_weather(data)
        except requests.exceptions.HTTPError as http_error:
            match response.status_code:
                case 400:
                    self.error_message("Wrong request.Check your input")
                case 401:
                    self.error_message("Unauthorized.Invalid API key ")
                case 403:
                    self.error_message("Forbidden.Access is denied")
                case 404:
                    self.error_message("City is not found")
                case 500:
                    self.error_message("Internal server error")
                case 502:
                    self.error_messaget("Invalid gateway")
                case 503:
                    self.error_message("Service unavailable")
                case 504:
                    self.error_message("Gateway timeout")
                case _:
                    self.error_message(f"HTTP error : {http_error}")

        except requests.exceptions.ConnectionError:
            self.error_message("Connection Error")
        except requests.exceptions.Timeout:
            self.error_message("Timeout error")
        except requests.exceptions.TooManyRedirects:
            self.error_message("Too many redirect.Check url")
        except requests.exceptions.RequestException as req_error:
            self.error_message(f"Request error : {req_error}")


    def error_message(self,message):
        self.temperature.setStyleSheet("font-size:20px; color:red;")
        self.temperature.setText(message)
        self.emoji.clear()
        self.description.clear()

    def display_weather(self,data):
        temperature_in_kelvin    = data["main"]["temp"]
        temperature_in_celcius   = temperature_in_kelvin - 273.15
        temperature_in_fahrnheit = (temperature_in_kelvin * 9/5) - 459.67
        self.temperature.setText(f"{temperature_in_celcius:.2f}°C")

        weather_id = data["weather"][0]["id"]
        self.emoji.setText(self.weather_emoji(weather_id))

        weather_description = data["weather"][0]["description"]
        self.description.setText(weather_description)

    @staticmethod
    def weather_emoji(weather_id):
        if   200<= weather_id <=232: return "⛈️"
        elif 300<= weather_id <=321: return "🌦️"
        elif 500<= weather_id <=531: return "🌧️"
        elif 600<= weather_id <=622: return "🌨️"
        elif 801<= weather_id <=804: return "☀️"
        elif 731<= weather_id <=761: return "🌪️"
        elif 701== weather_id : return "🌫️"
        elif 711== weather_id : return "💨"
        elif 721== weather_id : return "☁️"
        elif 741== weather_id : return "🌫️"
        elif 751== weather_id : return "💨"
        elif 762== weather_id : return "💨"
        elif 771== weather_id : return "🌬️ "
        elif 781== weather_id : return "🌪️"
        else:return "☀️"

def main():
    app           = QApplication(sys.argv)
    weatherWindow = WeatherApp()
    weatherWindow.show()
    sys.exit(app.exec_())


if __name__=="__main__":
    main()