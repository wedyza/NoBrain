label firstCourse:
    scene bg living
    show mainHero_stable at left
    show bogdan_stable at right

    mainHero "Опять проспал... Да как же так! Три будильника, ни один не услышал. Похоже, пора покупать сирену."
    mainHero "*Ладно, пока не об этом, нужно скорее скидать все вещи в рюкзак и бежать. Повезло хоть, что общежитие недалеко от института.*"

    play sound "audio/firstaudio.mp3"

    mainHero "Ручки. Тетради. Кольцо… ГДЕ ТЕЛЕФОН?! А, вот он… Ноутбук…"
    mainHero "*Я собирал вещи, Богдан наблюдал за всем этим и, естественно, не мог не оставить свой комментарий.*"

    bogdan "Ха! Дружище, да куда спешить, не думаю, что без тебя не начнут. Или ты сегодня лекцию ведешь?"

    mainHero "Ха-ха, смешно оборжатьтся и не жить. Мог бы и разбудить, знаешь же, что у меня, в отличие от тебя, пары в пятницу."

    bogdan "Я тебе на коменданта похож, чтобы все обо всех знать и помнить? Носки за шкафом."

    mainHero "Спасибо."

    "Богдан любит меня подколоть, потому что Я заставляю его поддерживать чистоту в комнате. Однако носки за шкафом намекают, что Я и сам начинаю забывать правило о порядке."

    bogdan "Ну ты это, смотри из аудитории не опоздай выйти."

    mainHero "Да ну тебя."

    hide bogdan_stable
    show bg rtf 
    mainHero "*Я бежал так, что если бы сейчас был на физре, то мне бы проставили автоматы на два курса вперед. Усэйн Болд смотрел бы на мои сияющие пятки вдалеке. *"
    mainHero "*Добежав до здания, Я, не останавливаясь, влетел в открытые двери*"

    show bg koridor1
    show defender_stable at right

    defender "КУДА ЛЕТИМ?! КОЛЬЦО ПОКАЗЫВАЕМ!"

    mainHero "*Черт. Забыл совсем. Развернувшись на одной ноге, Я показал кольцо и, провернув этот пируэт снова, помчался в аудитории.*"
    mainHero "Издалека Я услышал, как Охранница меня проклинала. Она была очень недовольна, но сейчас у меня не было даже минуты, чтобы извиниться и объяснить ситуацию. УТРО ДОБРЫМ НЕ БЫ-ВА-ЕТ!"

    hide defender_stable
    "Математика."

    mainHero "*Любимый предмет, но ровно до того момента, пока Я не замешкаюсь хотя бы на секунду. А тут Я потерял уже половину пары! Эх, снова тратить часа два после пар, чтобы понять упущенное.*"
    scene bg clasroom1
    show math
    "Если и есть в этом мире безграничное хранилище знаний, то это Математичка. Она не говорит, она стреляет терминами, теоремами, правилами. Вне пар это добрый и милый человек, но во время лекций хоть двумя руками пиши, все не запишешь."
    mainHero "*Я за три пары трачу одну ручку и 2 тетради. Интересно, что закончится быстрее – бумага в местных канцтоварах или человеческий ресурс*"
    "полсе пары:"
    scene bg koridor1
    show mainHero_stable
    mainHero "Хорошо, что Я все-таки пришел на пару, иначе бы столько времени убил после. Возьму кофе, чтобы взбодриться."    
    mainHero "*Столько всего нужно знать, чтобы Я смог реализовать задумки ИИ. Ну, никто не говорил, что этот путь будет легким. Знал на что шел.*"
    mainHero "*И все-таки, нельзя мне так просыпать пары. Нужно быть более ответственным в этом плане, если не хочу стать отстающим.*"

    
    mainHero "*Следующей парой вроде… История? Кто бы мог подумать, что на втором курсе будет история. Мне казалось, что срез знаний о прошлом нужно было делать на первом. Ладно, не мне это решать*"
    scene bg lection
    mainHero "*Так, пара будет здесь, но… Почему резко стало так тяжело двигаться? Может, недосып сказывается…*"
    mainHero "*Открыв дверь в аудиторию, Я почувствовал, будто всем телом упал во что-то вязкое. Будто тону в болоте.*"
    mainHero "*Движения стали медленными, мысли расплывчатыми. Еле как Я уселся за парту.*"
    show mainHero_stable at right
    show penpen_stable:
        xalign 0.0 yalign 1.9

    mainHero "Хоть пара и началась, препода до сих пор не было… Или…* ЭТО ЧТО, ПИНГВИН?!"
    mainHero "*Его не было видно за трибуной, но теперь он вышел к столам. Как? Что? А какой вопрос вообще может подойти к этой ситуации?!*"
    mainHero "*Одно Я понял – вся эта аура исходит именно от него. И будто этого было мало, пингвин начал говорить…*"
    mainHero "*Вся аудитория была окружена непонятными звуками, издали напоминающими человеческую речь. Со взглядом злым и твердым, как у орла, пингвин то восклицал, то говорил уныло. То грозно и торжественно, то тихо, будто бы говорит что-то неправильное.*"
    mainHero "*Как сказал сосед по ряду, его зовут Пэн Пинович. Какая неожиданность…*"
    mainHero "*Я обязательно выстою эту пару… Наверное.*"

    "после пары:"

    mainHero "*Я без сил выполз из аудитории. Мне кажется, биться с печенегами было бы проще, чем разобрать хоть слово Пэн Пиновича. Ощущения, будто из головы выдавили все, что было, заменив водой. *"
    mainHero "*Я обернулся и увидел, как из аудитории также тяжко выходить пингвин. Глубоко вздохнув, он пошлепал в сторону буфета. Похоже, ему тоже непросто проводить эти лекции.*"
    mainHero "*Что ж пары закончились, теперь можно заняться своими делами. Нужно идти в библиотеку*"
    hide penpen_stable
    show bg library
    "в библиотеке:"

    "«Среди ученых неоднократно поднимался вопрос этичности использования ИИ. Три закона Робототехники были признаны бесполезными для развивающейся науки из-за размытости формулировок.»"
    "«Далай-Лама XIV не исключают наличия сознания на компьютерной основе. Это дает основание считать, что у полностью сформированного ИИ может быть душа.»"
    "«Искусственный интеллект быстро развивается. Если еще в 2013 году средний ИИ был на уровне 4-летнего ребенка, то уже год спустя одному из компьютеров удалось решить одну из математических задач Эрдёша.»"

    "вечером:"
    show bg classroom1
    mainHero "*Надеюсь, вся эта внеучебка идет мне только на пользу. Выйдя из библиотеки, Я пошел в коворкинг отдохнуть и перекусить.*"
    mainHero "*В коворкинге Я заметил Гавриила, который что-то делал в ноутбуке. Однако Гавриил меня тоже увидел, отведя свое внимание от экрана.*"

    show kostya_stable at left
    with dissolve

    kostya "И ты здесь, ошибка человечества."

    mainHero "Язык прикуси, подобие человека."

    kostya "Что мне твой пустой треп. Ты бы на деле показал, что да как. Ходишь, прохлаждаешься, пока взрослые люди заняты достижением целей."

    mainHero "И в чем ты повзрослел? Неужели уже бриться начал?"

    kostya "Я этому обучил ИИ, чтобы тебе помогал. У тебя же не руки, а культяпы, ничего ими сделать не можешь."

    mainHero "Посмотрим, Я уже сильно продвинулся в коде своего ИИ. Уже скоро он сможет иметь визуальную оболочку. С такими темпами мой будет за твоим, как за грудничком ухаживать."

    kostya "Чеши больше, бестолочь."

    mainHero "Иди ты..."

    hide kostya_stable

    mainHero "*Я вышел из коворкинга, не хотел оставаться там с этим скотом. Делать в институте все равно уже нечего, можно и обратно в комнату*"
    show bg koridor1
    mainHero "*У входа Я заметил, как Охранница с тоской смотрела на закипающий чайник, стоящий на подоконнике.*"
    mainHero "*От ее тоски Я даже свои обиды забыл. Я подошел к ней*"

    show defender_stable at left

    mainHero "Извините меня за то, что сегодня так нагло пролетел и заставил вас кричать. Я не хотел проявить какое-то неуважение к вам."

    defender "Да ну тебя, все вы студенты одинаковые. Проходите мимо меня, проклинаете за то, что задерживаю из-за колец. Черт бы с вами…"

    mainHero "Нет, правда. Я поступил неправильно и заставил вас нервничать. Может Я могу вам как-то помочь в знак извинения?"

    defender "Что, такой честный и правильный да? Ну раз вызвался, то перетащи эти коробки в подсобку. У меня спина больная, а тут доставка тяжелая для деканата."

    "*перетащив все коробки*"

    defender "Гляди-ка, видать и правда стыдно. Ну ладно, прощаю тебя. Эх, знал бы ты, как мне это все уже надоело. Вот вы, молодые, как спички ведь. Чуть что, вспыхнули. "
    defender "И меня уже за человека не держите, и будто Я этот дурацкий ритуал придумала. Я же и так вижу кольцо, но должна останавливать. Такая работа"

    mainHero "Мне жаль, что с вами такое происходит."

    defender "Я же женщина. О цветах мечтаю, о разговорчиках. Но каждый день слышу только «Да проходил Я уже», «Да вы ж меня знаете», «Надоели со своей проверкой». "
    defender "Последний раз хорошее слово в свой адрес слышала в день акции в ТЦ. И то это была реклама."

    mainHero "Правда? Даже невооруженным взглядом видно, что душа у вас чистая. Такая хмурая только потому, что получаете тонну негатива в свой адрес каждый день."

    defender "*улыбнулась* Что, прям чистая душа?"

    mainHero "Ну во-о-от. Уже улыбаетесь. Улыбка вам к лицу, светлее становитесь."

    defender "*засмеялась* Ну льстец. Спасибо тебе, что выслушал меня, давно надо было кому-нибудь рассказать, а некому. Тебе уж в общежитие, наверное, пора. Беги, а завтра на чай подходи. Как тебя звать то?"

    mainHero "Спасибо за приглашение, Саша Я. Всего хорошего вам."

    defender "И тебе всего, Саша."

    scene bg living
    show mainHero_stable
    
    mainHero "*Я вернулся в комнату, Богдан был полностью увлечен игрой, поэтому Я не стал его тревожить. Лег на свою кровать и стал думать, какая же все-таки студенческая жизнь – сумасшедшая гонка. Благо, такой темп Я держать умею.*"

    "*ночь*"

    scene bg code
    stop sound
    "Экран монитора ослеплял меня холодным белым светом, но Я был полностью увлечен кодом. Этой ночью мой ИИ получит тело. Он уже будет не просто программой, а 3D моделью помощником."
    menu:
        mainHero "Но прежде мне нужно выбрать, что получит ИИ сначала"

        "Возможность видеть":
            $firstCharacteristic = "eyes"

            jump secondCourse

        "Возможность слышать":
            $firstCharacteristic = "ears"

            jump secondCourse

        "Возможность говорить":
            $firstCharacteristic = "mouth"

            jump secondCourse