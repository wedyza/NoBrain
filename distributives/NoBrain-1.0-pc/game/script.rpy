# Вы можете расположить сценарий своей игры в этом файле.

# Определение персонажей игры.
define teacherNoName = Character('Учитель', color="#c8ffc8")
define teacherKozo = Character('Учитель Тимофей', color="#c8ffc8")
define mainHero = Character('Юра', color="#c8ffc8")
define voice = Character('Закадровый голос', color="#c8ffc8")
define penpen = Character('Пен-пен', color="c8ffc8")
# Вместо использования оператора image можете просто
# складывать все ваши файлы изображений в папку images.
# Например, сцену bg room можно вызвать файлом "bg room.png",
# а eileen happy — "eileen happy.webp", и тогда они появятся в игре.

# Игра начинается здесь:
label start:

    scene bg rtf


    mainHero "1 сентября.. Вокруг столько незнакомых людей... Слава богу, что я взял с собой свой любимый чай."
    voice "Юра - асоциальный парень, не любит, когда вокруг него так много людей.."
    mainHero "Что за странный дед идет ко мне навстречу?"


    show teacher stable

    teacherNoName "Здравствуйте, молодой человек!"
    mainHero "Здравствуйте, эээмм.."
    teacherNoName "Звать меня Тимофей Иванович"
    teacherKozo "Я подошел к вам, чтобы вас попросить кое-что сделать.. Вы видите то существо?"

    show penpen beer

    teacherKozo "Учитель показал на крупного пингвина, в лапе у него сумка с пивом"
    teacherKozo "Не могли вы бы с ним обсудить вопрос трансгрессирования по вселенным?"

    hide teacher stable

    mainHero "Что? Какого черта? Почему там стоит пингвин с пивом в руках, и почему я должен у него что-то спросить про транс.. трансгендеров..?"
    voice "Юра подошел к пингвину и легонько задел его"
    mainHero "П-привет, меня зовут Юра, учитель Тимофей попросил меня узнать у тебя что-то насчет трансгендеров"
    penpen "Прррривет! Меня зовут Пен-Пен, я - говорящий пингвин, каких трансгендеров?"

    return
