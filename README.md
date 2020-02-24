# fakeblogger
Генератор псевдотекстов, построенных на постах в соцсетях

Как использовать: 
1. Надо сделать себе корпус текстов полученных из соцсети. Для этого существует vk_search.py -- поиск по ключевому слову в vk. Используется так: 

  python3 vk_search.py <API-ключ вконтакта> <ключевое слово> >> texts.txt

Ну например, если вы хотите, чтобы все ваши псевдопосты были про коронавирус, делайте так: 
  
  python3 vk_search.py <API-ключ вконтакта> Коронавирус >> texts.txt
  

2. Отлично, теперь можно генерить псевдопосты

  python3 generator.py texts.txt

На выходе получается 10 предложений почти связного текста. 



Класс, который я использую для скачивания постов из соцсетей придуман Лерой @for15pounds Гаркавой
Генератор текстов практически целиком взят здесь: https://habr.com/ru/post/88514/ но будет улучшаться.
Всем спасибо!
