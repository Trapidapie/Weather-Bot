import telebot as tb
import requests
import json

bot = tb.TeleBot('6814642919:AAHjw8ZiDAnZR36n2wnUhf4_dF2rhgcvLlU')
API = 'd51ddae702562e646452936479fa4784'

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id,'Hi')

@bot.message_handler(content_types=['text'])
def get_weather_now(message):
    city = message.text.strip().lower()
    res = requests.get(f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API}&units=metric')
    data = json.loads(res.text)
    if res.status_code == 200:
        temp = data['main']['temp']
        weather = data['weather'][0]['description']
        wind = data['wind']['speed']
        weather_emojis = {
            'clear sky': '☀️',
            'few clouds': '🌤',
            'broken clouds': '🌤',
            'overcast clouds': '☁️',
            'scattered clouds': '☁️',
            'light rain': '🌦',
            'moderate rain': '🌧',
            'light intensity shower rain': '🌧',
            'heavy intensity rain': '⛈',
            'snow': '☃️'
        }
        country_emojis = {
            'AL': '🇦🇱',  # Албания
            'AD': '🇦🇩',  # Андорра
            'AT': '🇦🇹',  # Австрия
            'BY': '🇧🇾',  # Беларусь
            'BE': '🇧🇪',  # Бельгия
            'BA': '🇧🇦',  # Босния и Герцеговина
            'BG': '🇧🇬',  # Болгария
            'HR': '🇭🇷',  # Хорватия
            'CY': '🇨🇾',  # Кипр
            'CZ': '🇨🇿',  # Чехия
            'DK': '🇩🇰',  # Дания
            'EE': '🇪🇪',  # Эстония
            'FI': '🇫🇮',  # Финляндия
            'FR': '🇫🇷',  # Франция
            'DE': '🇩🇪',  # Германия
            'GR': '🇬🇷',  # Греция
            'HU': '🇭🇺',  # Венгрия
            'IS': '🇮🇸',  # Исландия
            'IE': '🇮🇪🍀',  # Ирландия
            'IT': '🇮🇹🍕',  # Италия
            'LV': '🇱🇻',  # Латвия
            'LT': '🇱🇹',  # Литва
            'LU': '🇱🇺',  # Люксембург
            'MK': '🇲🇰',  # Северная Македония
            'MT': '🇲🇹',  # Мальта
            'MD': '🇲🇩',  # Молдавия
            'MC': '🇲🇨',  # Монако
            'ME': '🇲🇪',  # Черногория
            'NL': '🇳🇱',  # Нидерланды
            'NO': '🇳🇴',  # Норвегия
            'PL': '🇵🇱',  # Польша
            'PT': '🇵🇹',  # Португалия
            'RO': '🇷🇴',  # Румыния
            'RU': '🇷🇺🐷',  # Россия
            'SM': '🇸🇲',  # Сан-Марино
            'RS': '🇷🇸',  # Сербия
            'SK': '🇸🇰',  # Словакия
            'SI': '🇸🇮',  # Словения
            'ES': '🇪🇸',  # Испания
            'SE': '🇸🇪',  # Швеция
            'CH': '🇨🇭',  # Швейцария
            'UA': '🇺🇦✌️',  # Украина
            'GB': '🇬🇧',  # Великобритания
            'VA': '🇻🇦',  # Ватикан
            'AF': '🇦🇫',  # Афганистан
            'AM': '🇦🇲',  # Армения
            'AZ': '🇦🇿',  # Азербайджан
            'BH': '🇧🇭',  # Бахрейн
            'BD': '🇧🇩',  # Бангладеш
            'BT': '🇧🇹',  # Бутан
            'BN': '🇧🇳',  # Бруней
            'KH': '🇰🇭',  # Камбоджа
            'CN': '🇨🇳',  # Китай
            'GE': '🇬🇪',  # Грузия
            'AB': '🇬🇪',  # Abkhazia
            'IN': '🇮🇳',  # Индия
            'ID': '🇮🇩',  # Индонезия
            'IR': '🇮🇷',  # Иран
            'IQ': '🇮🇶',  # Ирак
            'IL': '🇮🇱🫰🏻',  # Израиль
            'JP': '🇯🇵🍥',  # Япония
            'JO': '🇯🇴',  # Иордания
            'KZ': '🇰🇿',  # Казахстан
            'KW': '🇰🇼',  # Кувейт
            'KG': '🇰🇬',  # Киргизия
            'LA': '🇱🇦',  # Лаос
            'LB': '🇱🇧',  # Ливан
            'MY': '🇲🇾',  # Малайзия
            'MV': '🇲🇻',  # Мальдивы
            'MN': '🇲🇳',  # Монголия
            'MM': '🇲🇲',  # Мьянма
            'NP': '🇳🇵',  # Непал
            'KP': '🇰🇵',  # Северная Корея
            'OM': '🇴🇲',  # Оман
            'PK': '🇵🇰',  # Пакистан
            'PS': '🇮🇱',  # Палестина
            'PH': '🇵🇭',  # Филиппины
            'QA': '🇶🇦',  # Катар
            'SA': '🇸🇦',  # Саудовская Аравия
            'SG': '🇸🇬',  # Сингапур
            'KR': '🇰🇷',  # Южная Корея
            'LK': '🇱🇰',  # Шри-Ланка
            'SY': '🇸🇾',  # Сирия
            'TW': '🇹🇼',  # Тайвань
            'TJ': '🇹🇯',  # Таджикистан
            'TH': '🇹🇭',  # Таиланд
            'TR': '🇹🇷',  # Турция
            'TM': '🇹🇲',  # Туркменистан
            'AE': '🇦🇪',  # Объединенные Арабские Эмираты
            'UZ': '🇺🇿',  # Узбекистан
            'VN': '🇻🇳',  # Вьетнам
            'YE': '🇾🇪',  # Йемен
            'US': '🇺🇸🦅',  # США
            'CA': '🇨🇦',  # Канада
            'MX': '🇲🇽',  # Мексика
            'BR': '🇧🇷',  # Бразилия
            'AR': '🇦🇷',  # Аргентина
            'CL': '🇨🇱',  # Чили
            'CO': '🇨🇴',  # Колумбия
            'PE': '🇵🇪',  # Перу
            'EC': '🇪🇨',  # Эквадор
            'BO': '🇧🇴',  # Боливия
            'PY': '🇵🇾',  # Парагвай
            'UY': '🇺🇾',  # Уругвай
            'GY': '🇬🇾',  # Гайана
            'SR': '🇸🇷',  # Суринам
            'AN': '🇦🇼',  # Аруба
            'AW': '🇧🇶',  # Бонэйр, Синт-Эстатиус и Саба
            'PR': '🇵🇷',  # Пуэрто-Рико
            'DO': '🇩🇴',  # Доминиканская Республика
            'CU': '🇨🇺',  # Куба
            'JM': '🇯🇲',  # Ямайка
            'HT': '🇭🇹',  # Гаити
            'BS': '🇧🇸',  # Багамы
            'NI': '🇳🇮',  # Никарагуа
            'CR': '🇨🇷',  # Коста-Рика
            'HN': '🇭🇳',  # Гондурас
            'SV': '🇸🇻',  # Сальвадор
            'GT': '🇬🇹',  # Гватемала
            'BZ': '🇧🇿',  # Белиз
            'PA': '🇵🇦',  # Панама
            'VE': '🇻🇪',  # Венесуэла
            'ZA': '🇿🇦',  # Южная Африка
            'NG': '🇳🇬',  # Нигерия
            'KE': '🇰🇪',  # Кения
            'EG': '🇪🇬',  # Египет
            'ET': '🇪🇹',  # Эфиопия
            'SD': '🇸🇩',  # Судан
            'DZ': '🇩🇿',  # Алжир
            'MA': '🇲🇦',  # Марокко
            'TN': '🇹🇳',  # Тунис
            'LY': '🇱🇾',  # Ливия
            'SL': '🇸🇱',  # Сьерра-Леоне
            'CI': '🇨🇮',  # Кот-д'Ивуар
            'GH': '🇬🇭',  # Гана
            'CM': '🇨🇲',  # Камерун
            'UG': '🇺🇬',  # Уганда
            'RW': '🇷🇼',  # Руанда
            'TZ': '🇹🇿',  # Танзания
            'ZM': '🇿🇲',  # Замбия
            'ZW': '🇿🇼',  # Зимбабве
            'MW': '🇲🇼',  # Малави
            'AO': '🇦🇴',  # Ангола
            'MZ': '🇲🇿',  # Мозамбик
            'NA': '🇳🇦',  # Намибия
            'BW': '🇧🇼',  # Ботсвана
            'LS': '🇱🇸',  # Лесото
            'SZ': '🇸🇿',  # Свазиленд
            'EH': '🇪🇭',  # Экваториальная Гвинея
            'AU': '🇦🇺',  # Австралия
            'NZ': '🇳🇿',  # Новая Зеландия
            'FJ': '🇫🇯',  # Фиджи
            'PG': '🇵🇬',  # Папуа — Новая Гвинея
            'SB': '🇸🇧',  # Соломоновы Острова
            'TO': '🇹🇴',  # Тонга
            'VU': '🇻🇺',  # Вануату
            'WS': '🇼🇸',  # Самоа
            'KI': '🇰🇮',  # Кирибати
            'FM': '🇫🇲',  # Микронезия
            'MH': '🇲🇭',  # Маршалловы Острова
            'NR': '🇳🇷',  # Науру
            'PW': '🇵🇼',  # Палау
            'TV': '🇹🇻',  # Тувалу
            'TK': '🇹🇰',  # Токелау
            'PW': '🇵🇼',  # Палау
            'MH': '🇲🇭',  # Маршалловы Острова
            'NR': '🇳🇷',  # Науру
            'PW': '🇵🇼',  # Палау
            'TV': '🇹🇻',  # Тувалу
            'TK': '🇹🇰',  # Токелау
        }
        country_smile = ''
        if data['sys']['country'] in country_emojis:
            country_smile = country_emojis[data['sys']['country']]
            if data['name'] == 'Krym':
                country_smile = '🇺🇦✌️'
        else:
            country_smile = '🌍'
        temp_smile = ''
        if weather in weather_emojis:
            bot.send_message(message.chat.id, weather_emojis[weather])
        else:
            bot.send_message(message.chat.id, '🌡')
        if temp > 20:
            temp_smile = '🥵'
        elif 0 > temp > -10:
            temp_smile = '❄️'
        elif temp < -10:
            temp_smile = '🥶'
        else:
            temp_smile = '🌡'
        message_text = f'{message.text.title()}{country_smile}\ntemp is: {temp}°C{temp_smile}\n{weather.title()}💨 wind:{wind} m/s'
        bot.reply_to(message, message_text)
    else:
        bot.reply_to(message, f'Error, location named {message.text} was not found, please try again')

if __name__ == '__main__':
    bot.polling(none_stop=True)