<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>=-Hyprland-=</title>
    <style>
      html {
        font-family: Arial, Helvetica, sans-serif;
        color: white;
      }
      body {
        height: 100vh;
        background-color: black;
        padding: 50px;
      }
      .links {
        display: flex;
        align-items: center;
        justify-content: center;
        gap: 100px;
      }
      .ashki a {
        color: white; 
        text-shadow: 0px 0px 20px white;
        text-decoration: none;
        background-color: rgb(27, 27, 27);
        padding: 10px;
        border-radius: 5px;
        border: 1px solid rgb(46, 46, 46);
        transition: all 500ms;
      }
      .ashki a:hover {
        background-color: black;
        text-shadow: 0px 0px 10px white;
        color: rgb(105, 105, 105);
        box-shadow: 0px 0px 20px white;
        transform: translateY(-5px);
      }
      .ashki a:active {
        background-color: white;
      }
      .ashki {
        display: flex;
        gap: 10px;
      }
      header {
        background-color: rgb(14, 14, 14);
        box-shadow: 0px 0px 20px rgb(14, 14, 14);
      }
      .wii {
        margin-top: 100px;
        padding: 100px;
      }
      .pop {
        background-color: rgb(22, 22, 22);
        padding: 20px;
        border-radius: 10px;
        transition: all 600ms;
      }
      .pop:hover {
        box-shadow: 0px 0px 50px rgb(102, 102, 102);
      }
      .pop:active {
        padding: 30px;
      }
      .ppop {
        font-size: 30px;
      }
      .kp {
        padding: 100px;
        margin-top: 100px;
      }
       a {
        color: white;
        text-shadow: 0px 0px 10px white;
      }
      .imgi {
        padding: 20px;
      }
      .img {
        width: 500px ;
        transition: 600ms;
      }
      .img:hover {
        width: 700px;
      }
      .end-h {
        text-align: center;
        color: white;
        margin-bottom: 50px;
        justify-content: center;
        align-items: center;
      }
      .contacts {
        display: flex;
        gap: 20px;
        align-items: center;
        text-align: center;
        justify-content: center;
        margin: 100px;
        font-size: 50px;
        background-color: rgb(19, 19, 19);
        border-radius: 10px;
      }
      
    </style>
  </head>
  <header>
    <div class="links">
      <div><h1>Hyprland</h1></div>
      <div class="ashki">
        <a href="#wii">что это?</a> <a href="#kp">как пользаватся?</a>
        <a href="#kk">как выглядит?</a> <a href="#gr">где работатет?</a>
      </div>
      <div><h3>Не является оффициальным сайтом Hyprland</h1></div>
    </div>
  </header>
  <body>
    <section id="wii" class="wii">
        <h1 style="text-align: center;">Что такое Hyprland?</h1>
        <div class="pop"><p class="ppop">Hyprland - это WM то есть windows manager то есть оконный менеджер или менеджер окон на linux. Он похож на i3 или другие оконные менеджеры у него есть много эффектов blur и других анимаций </p>
        <p class="nex">Главная Задача: <br> 1. размещение окон - hyprland сам размещеняет окна чтобы было удобно для пользавателя <br> 2. запуск сервисов - по типу waybar и другие сервисы для удобства пользавателя <br> 3. украшение окон - hyprland применяет стили для окон которые вы задали</p>
      </div>
    </section>
    <section id="kp" class="kp">
      <div class="pop">
      <h1 style="text-align: center;">как пользаватся Hyprland?</h1>
      <p class="ppop">hyprland работает на wayland что даёт вам настроить его как вам удобно</p>
      <p class="nex">1. Начало работы: Настройкра конфига - Вся "магия" находится в 1 файле hyprland.conf он обычно находится в ~/.config/hypr/. Это просто текствовый файл конфига в котором если вы что-то напишите то это же моментально измениться в hyprland даже перезагружать не надо. Если вы не будете настраивать hyprland то у вас не получится перемещать окна, открывать окна, да или вообще что-то делать, вы только сможете выключить компьютер или ноутбук и выйти с hyprland. Но вы можете скачать готовый конфиг для hyprland например <a href="https://github.com/prasanthrangan/hyprdots">hyprdots</a> или <a href="https://github.com/HyDE-Project/hyde-config">HyDE</a> <br> 2. основа: keybinds - вам нужно самим настроить все бинды в файле конфига пример: binddm = $mainMod, Z, $d hold to move window , movewindow. это обозначает если вы будете зажимать win + z и двигать мышькой то окно будет перемещатся. <br> 3. робочие столы - это главное в настройки hyprland. Рабочие столы на hyprland намного лучше и удобнее чем в том же windows или plasma. Рабочие столы очень удобны потому что тутда легко перемещатся если вы сделаете удоный бинд и там легко туда перемещать окна например вы можете писать код и переместиться на бразур проверить и вы просто используете бинд чтобы переместится в робочий чтол с окном с браузером. Я обычно остовляю на 1 окно 1 робочий стол. <br> 4. Экосистема - В hyprland легко скачать дополнительный софт и в конфигурационном файле сделать так чтобы он запускался автоматически при заходе в hyprland. я рекомендую ставить: Панель - waybar, Блокировка экрана - hyprlock, уведомления - Mako, Dunst, SwayNC.</p>
    </div>
    </section>
    <section id="kk" class="imga">
      <div class="pop">
      <h1 style="text-align: center;">Как выглядит hyprland?</h1>
      <p class="ppop">Как выглядит hyprland вы можете посмотреть на фото ниже </p>
      <div class="imgi">
        <img class="img" src="./image.png" alt="image.png">
        <img class="img" src="./image2.png" alt="image2.png">
        <img class="img" src="./image3.png" alt="image3.png">
        <p class="nex">И не стоит забывать что это только мои настройки hyprland и поэтему hyprland у других может выглядить вообще по другому но у меня стоит hyprland который удобный мне.</p>
      </div>
    </div>
    </section>
    <section style="padding: 100px;" id="gr" class="gde">
      <div class="pop">
        <p class="ppop">Где работает hyprland?</p>
         <p class="nex">Если вы думали что hyprland работает на всех дистрибутивах linux то это не так. Hyprland стабильно работает только на arch linux или других дистрибутивах которые написаны на arch по типу manjaro или EndeavourOS и другие. Hyprland может работать и на debian и fedora но очень большой шанс что он не запуститься так как это просто порт с arch linux который редко обнавляется.</p>
      </div>
    </section>
    <footer>
      <h1 class="end-h">contact us</h1>
      <div class="contacts">
        <a href="https://api.whatsapp.com/send/?phone=77052255071&text&type=phone_number&app_absent=0">whatsapp</a>
        <a href="https://t.me/adubam">telegram</a>
        <a href="./discord.html">discord</a>
      </div>
    </footer>
  </body>
</html>
