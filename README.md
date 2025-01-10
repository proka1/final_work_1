Название проекта: 
TravelBuddy — найди попутчика мечты!
Ищешь компанию для следующего путешествия? TravelBuddy соединяет искателей приключений со всего мира! 🗺️
Что может бот?
- Поможет найти попутчика с похожими интересами.
- Подберёт людей для совместного отдыха. 
- Упростит организацию совместных поездок.
Общайся, планируй и отправляйся в путь с новыми друзьями!
TravelBuddy — твой путеводитель в мир дружбы и открытий.

Описание:
Данный бот предназначен для поиска партнеров для путешествия. 
На данный момент реализован процесс верификации с загрузкой фотографий в БД для дальнейшего использования.
Создана система донатов(в формате заглушек).
Далее бот собирает всю информацию по человеку, который ищет партнеров по путешествию и затем при нажатии кнопки "Найти совпадения" ищет всех людей в БД которая подходят по  параметрам поиска и выдает их данные. 

Инструкция по установке чат-бота:
Данная инструкция поможет вам установить и запустить чат-бота

Требования
Перед началом убедитесь, что у вас установлены:
- Python версии 3.8 или выше
- Менеджер пакетов `pip`
- Git (для клонирования репозитория, если нужно)

Установка

1.Клонирование репозитория**  
Склонируйте репозиторий чат-бота на ваш компьютер:
```bash
git clone https://github.com/proka1/final_work_1
cd final_work_1
````

2.Создание виртуального окружения
Рекомендуется использовать виртуальное окружение для установки зависимостей:
```bash
Копировать код
python -m venv venv
source venv/bin/activate       # Для Linux/MacOS
venv\Scripts\activate          # Для Windows
```

3. Установка зависимостей
Установите все необходимые библиотеки, перечисленные в requirements.txt:
```bash
pip install -r requirements.txt
```

4. Установите свой API Key для подключения к своему боту в файл config.py
(Чтобы подключить API-ключ с помощью BotFather, нужно:
-Найти BotFather в Telegram. Обычно это делается через поиск: нужно ввести «BotFather» в строку поиска в Телеграме. 
-Открыть диалог с BotFather и нажать кнопку «start» или «/start» в строке ввода, если вы впервые используете BotFather. Затем ввести команду «/newbot» для создания нового бота.
-Выбрать имя для бота. BotFather попросит вас выбрать название для вашего бота. Можно использовать русский язык и пробелы. Это имя можно потом поменять — его выбор некритичен. 
-Выбрать username для бота. Это внутреннее название для Telegram, которое будет использоваться, когда вы внутри Telegram будете давать ссылку на своего бота. Важно ответственно подойти к выбору username, так как это имя потом нельзя будет поменять. Оно должно заканчиваться на «bot», например, «mytestbot» или «my_test_bot». 
-Получить API-токен. После выбора имени бота, BotFather сгенерирует уникальный API-токен для вашего бота. Этот токен является ключом к вашему боту, и он будет использоваться для подключения бота к конструктору.

!!!Берегите токен: с этим токеном кто угодно сможет управлять вашим ботом. Если токен украдут, вам придётся получить новый у BotFather. !!!

5.Запуск чат-бота
Запустите чат-бота с помощью следующей команды:
```bash
python bot.py
```


