import sys
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
                                font-size  : 26px;
                                font-style : italic;
                            }
                            #I_City
                            {
                                font-size : 25px;
                            }
                            #GetW
                            {
                                font-size : 20px;
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
                                font-size : 30px;
                            }
          
                          """)
        self.get_weather.clicked.connect(self.get_weather_data)

    def get_weather_data(self):
        print("got")

    def error_message(self,message):
        pass

    def display_weather(self):
        pass


def main():
    app           = QApplication(sys.argv)
    weatherWindow = WeatherApp()
    weatherWindow.show()
    sys.exit(app.exec_())


if __name__=="__main__":
    main()