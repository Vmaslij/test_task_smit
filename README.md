# Test task SMIT
После клонирования репозитория создать образ контейнера с помощью  
`docker build -t smit:mv .`  
Запустить контейнер с помощью команды  
`docker run -it -d -p 8000:8000 smit:mv` 

  
Url `/set_rates` позволяет загрузить тарифы и сохранить их в бд  
Url `/get_price` позволяет рассчитать стоимость по тарифу  
Url `/docs` отображает документацию с описанием формата данных
