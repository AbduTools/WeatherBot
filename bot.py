# ░█████╗░██████╗░██████╗░██╗░░░██╗
# ██╔══██╗██╔══██╗██╔══██╗██║░░░██║    
# ███████║██████╦╝██║░░██║██║░░░██║
# ██╔══██║██╔══██╗██║░░██║██║░░░██║
# ██║░░██║██████╦╝██████╔╝╚██████╔╝
# ╚═╝░░╚═╝╚═════╝░╚═════╝░░╚═════╝░
# Developer @ABDU_UYGHUR, Copyright LTD 2022.
# ██╗░░░██╗██╗░░░██╗░██████╗░██╗░░██╗██╗░░░██╗██████╗░
# ██║░░░██║╚██╗░██╔╝██╔════╝░██║░░██║██║░░░██║██╔══██╗
# ██║░░░██║░╚████╔╝░██║░░██╗░███████║██║░░░██║██████╔╝
# ██║░░░██║░░╚██╔╝░░██║░░╚██╗██╔══██║██║░░░██║██╔══██╗
# ╚██████╔╝░░░██║░░░╚██████╔╝██║░░██║╚██████╔╝██║░░██║
# ░╚═════╝░░░░╚═╝░░░░╚═════╝░╚═╝░░╚═╝░╚═════╝░╚═╝░░╚═╝
import requests
import datetime
from pprint import pprint
from config import weather_token

def get_weather(city , weather_token):

    code_to_smile = {
            "Clear": "Ясно \U00002600",
            "Clouds": "Облачно \U00002601",
            "Rain": "Дождь \U00002614",
            "Drizzle": "Мелкий дождь \U00002614",
            "Thunderstorm": "Гроза \U000026A1",
            "Snow": "Снег \U0001F328",
            "Mist": "Туман \U0001F32B"
    }

    try: 
#api: документация AbduTools, API- документацию можете получать здесь:  https://openweathermap.org/api
        r = requests.get(
            f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={weather_token}&units=metric")
#Parsing json: Json переводим к Python   
        data = r.json()
        #pprint(data)
#Настройка утилиты:
        weather_description = data["weather"][0]["main"]
        if weather_description in code_to_smile:
            wd = code_to_smile[weather_description]
        else:
            wd = "Посмотри в окно, не пойму что там за погода!"

        city_name = data["name"]
        cur_weather = data["main"]["temp"]
        pressure = data["main"]["pressure"]
        wind = data["wind"]["speed"]
        humidity = data["main"]["humidity"]
        sunrise_timestamp = datetime.datetime.fromtimestamp(data["sys"]["sunrise"])
        sunset_timestamp = datetime.datetime.fromtimestamp(data["sys"]["sunset"])
        length_of_the_day = datetime.datetime.fromtimestamp(data["sys"]["sunset"]) - datetime.datetime.fromtimestamp(data["sys"]["sunrise"])

#Настройка сообщений:
        print(f"***{datetime.datetime.now().strftime('%Y-%m-%d %H:%M')}***\n"
              f"Погода в городе: {city_name}\nТемпература: {cur_weather}C° {wd}\n"
              f"Давление: {pressure} мм.рт.ст\nВлажность: {humidity}%\nВетер: {wind}\n"
              f"Восход солнца: {sunrise_timestamp}\nЗакат солнца: {sunset_timestamp}\nПродолжительность дня: {length_of_the_day}\n"
              f"Спасибо за использование нашего бота🤩.Если заметили ошибку, обратитесь администратору: @ABDU_UYGHUR. Хорошего вам дня😊"
              )

#Если город неправильно прописан:
    except Exception as ex:
        print(ex)
        print("Проверьте правильность названия города🛑. Повторите запрос ещё раз🙃")

def main():
    city = input("Чтобы получить информацию о погоде, введите названия города📥: ")
    get_weather(city , weather_token)

if __name__ == '__main__':
    main()