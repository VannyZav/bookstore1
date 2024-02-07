# Bookstore1

задание:<br/>
Нужно расширить сервис, который мы сделали и добавить поддержку персистентного хранилища,
к примеру SQLite. При этом нужно продолжить следовать DDD и взаимодействовать с базой
не напрямую, а через паттерн Repository.<br/>

### для развертывание проекта выполните следующие команды:
1. склонируйте репозиторий к себе на компьютер или скачайте проект zip файлом.<br/>
   git clone https://github.com/VannyZav/bookstore1.git
2. создайте виртуальное окружение:<br/>
   python -m venv myenv<br/>
   source myenv/bin/activate  # для Linux и macOS<br/>
   myenv\Scripts\activate     # для Windows<br/>
   где myenv — это название вашего виртуального окружения.<br/>
3. установите зависимости pip install -r requirements.txt
4. в консоли зайдите в папку проекта и оттуда запустите приложение командой:<br/>
>> flask --app bookstore --debug run 

# инструкция к API интернет магазина в Postman:

1. Добавить книгу в магазин:<br/>
   - http://127.0.0.1:5000/books/
   - в Body указать {   
    "title": str,
    "author": str,
    "publish_year": int,
    "pages_count": int
}
   - использовать метод POST
     

2. Запросить все книги:<br/>
   - http://127.0.0.1:5000/books/
   - использовать метод GET


3. Запросить продукт по id:<br/>
   - http://127.0.0.1:5000/books/id
   - использовать метод GET

