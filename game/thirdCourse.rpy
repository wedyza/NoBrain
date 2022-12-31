label thirdCourse:
    scene black
    "третий курс.."

    mainHero "*Прошел целый курс, а Я все не мог оставить ту историю с призраками. Я спрашивал преподавателей, донимал студентов, пытался узнать что-нибудь у охранницы.*"

    "«Вы бы сбавили нагрузку, Александр. Похоже, она идет вам во вред.»"
    "«Сань, ты игрушек наигрался? Какие призраки?»"
    "«Саша, ты меня пугаешь. Может, стоит сходить ко врачу провериться?»"

    mainHero "*Теперь Я местный юродивый. Просто класс. Хоть друзья меня выслушали, однако тоже с трудом верят моему рассказу.*"
    scene bg lection
    show timur_stable
    timur "Саша, ты уверен, что тебе не почудилось? Мы ведь все-таки проходили тогда подземелье в World of BattleCraft. Может, ты просто переиграл?"
    hide timur_stable
    show mainHero_stable
    mainHero "Да так, что решил максимально эффективно заняться гриндом. Так ты хочешь сказать?"
    scene bg summer
    show cristina_stable
    cristina "А мне кажется, тебе просто не хватает романтики в жизни. Может, ты как какой-нибудь писатель, от тоски и одиночества визуализируешь свои мрачные мысли."
    hide cristina_stable
    show mainHero_stable
    mainHero "Тебе напомнить, как закончили большая часть писателей Серебряного века?"
    mainHero "*Похоже, как всегда, искать ответы придется самому.*"
    scene bg classroom
    "Я искал в аудиториях. Не знаю, что Я пытался там найти, но если призраков Я видел только в институте, то почему бы не проверить аудитории? "
    "Также искал хоть какие-то зацепки в интернете."
    "Ходить в библиотеку Я наотрез отказался, поэтому просил Тимура брать для меня книги. Ну а если он наткнется на призраков, то хотя бы поверит мне. Я лучший друг на всем белом свете."
    "Но в итоге все эти действия не имели никакого толка. "
    "Я уже стал рисковать рассудком и ходить по нелюдимым частям института. Теперь Я и правда походил на юродивого. Ищу то, не знаю что, ищу там, не знаю где."
    "Сегодня, выйдя из коворкинга, решил обследовать нулевой этаж. "
    "Коридор из однотипных пластиковых дверей с голыми светло-оранжевыми стенами… Но что это?"

    show bg door

    "На вид тяжелая железная дверь была врезана в стену подобно сейфу. Сейф, который хранит то, что мне нужно?"
    "Я не заметил ни замка, ни ручки на этой двери, но попытался ее поддеть, чтобы хоть как-то сдвинуть. "

    mainHero "*Петли… Заржавели?! Да что вообще это за дверь и почему ее не демонтируют?*"

    "Однако, приложив немало усилий, Я сумел ее открыть. Внутри, хоть и тускло, горели лампы. Видимо, это заброшенная часть, но от источника питания ее не отключили. Не думаю, что это идет на пользу бюджету."

    show bg basement

    "Пространство за дверью всем своим видом показывало, что комнаты здесь давно не используются. Все заросло сантиметровым слоем пыли и паутиной."
    "Среди всяких дверей мое внимание привлекла дверь с электронным замком. Удивительно, ведь интерьеру этого места она не соответствовала. "
    "Дверь была приоткрыта, поэтому Я решил туда зайти."

    scene black with Shake((0,0,0,0), .3, dist=7)

    play sound "audio/close.mp3"

    "*хлопок*"

    mainHero "Нет...Не может быть..."
    mainHero "КАКОЙ ГЛУПЕЦ!ИДИОТ!ЧЕРТ!"
    mainHero "*Ладно, без паники. Подумаешь, здесь несколько лет не ступала нога человека, все место может посоревноваться с локациями «Пилы» в звании «самое ужасающее место года», возможно, тут даже мыши окочурились от страха. Все. В. Порядке."
    mainHero "Мне просто нужно придумать, как открыть дверь. Замок же электронный? Верно. ИИ!"

    "Я вызвал ИИ, тот предложил уйму вариантов, для одного бы даже потребовалась пропановая горелка. Есть один ньюанс. У МЕНЯ В КАРМАНАХ ТОЛЬКО ТЕЛЕФОН!"

    mainHero "Телефон! Ну конечно. Сейчас напишу Тимуру и Крис, они придут и выру… Ешка… Положение хуже некуда."

    "кажется, что прошло уже несколько часов.."

    mainHero "Какая же это глупая ситуация..."
    mainHero "Что Я могу сделать в этой ситуации? У меня есть перекус и бутылка воды, этого хватит часа на три. Связи нет, возможности открыть дверь тоже."
    mainHero "Из-за этих призраков Я гублю себя уже не только психически, но и физически."
    mainHero "И ведь ничего не узнал по итогу… Секундочку."
    mainHero "А что, если в коде этих призраков что-то есть? Кажется, Я запомнил пару строк."
    "Я достал ноутбук, на котором хватало заряда для небольшого эксперимента. Я стал прописывать эти строки в программу ИИ."
    mainHero "Мне кажется, должно сработать. Если кольцо сумеет подключиться к замку, то уже силами ИИ получится подобрать пароль. В любом случае, другого варианта у меня нет.."

    "У меня получилось подключить кольцо к замку, Я вызвал ИИ и стал ждать. Я видел, что ИИ занят каким-то процессом, но из-за того, что еще не брался за создание интерфейса кольца, Я не знал, работает ли моя задумка."

    mainHero "Похоже, что.. ПОЛУЧИЛОСЬ! ПОЛУЧИЛОСЬ!"

    scene bg koridor1

    "Выбежав из комнаты, Я наконец вернулся в коридор, а из него на нулевой этаж. Как хорошо. Боже, как хоро…"

    show mainHero_stable at left

    unknown "ЭЙ!"

    show ded_stable at right

    mainHero "Что?"

    unknown "С тобой разговариваю, шкет!"

    mainHero "Вы... Вы кто?"

    ded " Максим Альбертович, преподаватель по программированию. А тебя как зовут, студент? И что ты делал в закрытых лабораториях?"

    mainHero "Я Александр… Понимаете… Тут такая история забавная…"
    "Я решил рассказать всю правду, иначе боюсь, что вся эта история сильно навредит мне."

    ded "Ты… Ты… "

    mainHero "Знаю, как это все зву…"

    ded "За мной, в мой кабинет."

    mainHero "Хорошо…"

    scene bg classroom

    "Он рассказал мне все, что Я должен знать о призраках. Я вспомнил слова Тьютора и Наставницы 1 сентября, когда еще был абитуриентом и получил кольцо. «Это необычный ВУЗ, здесь свои ритуалы и свои особенности». "
    "Призраки – это визуализация сложных программ, кодов, которые забыты. Студенты их не используют по разным причинам: сложно, долго, непонятно."
    "Однако, если верить Максиму Альбертовичу, они несут огромную пользу и делают то, что не могут в полной мере осилить упрощенные версии, хоть это и незаметно на первый взгляд."

    show mainHero_stable at left
    show ded_stable at right
    with dissolve

    mainHero "А почему Я вас раньше не видел?"

    ded "Считай, Я призрак среди живых. Меня посчитали неспособным вести лекции, потому что Я тоже начал видеть призраков. Вас обучает программированию человек, что не имеет и представления о глубине истории программирования и способах решения поставленных задач."

    "Мы просидели до позднего вечера. За чаем Максим Альбертович рассказал мне столько, что Я бы не узнал, прочитай Я хоть все книги библиотеки. Этот человек явно может потягаться в знаниях с Математичкой."
    "Я бы слушал его часами, но Максим Альбертович сказал, что ему пора идти домой."
    "Мы попрощались, он пообещал позже поведать мне больше. "
    hide ded_stable
    scene bg koridor1
    "Идя по первому этажу, Я наткнулся на Гавриила. Только этого мне здесь не хватало."

    show mainHero_stable at left
    show kostya_stable at right
    with dissolve
    kostya "О, калека копирка на ИИ и его владелец. Знаешь, яблоко от яблони недалеко падает"

    mainHero "А давай сейчас мы и проверим, кто тут калека?"

    kostya "Охо-хо! А чего мы так расхрабрились? Неужто веришь, что сможешь со мной потягаться?"

    mainHero "В себе бы начал сомневаться."

    kostya "Ну сейчас то ты язык прикусишь. Предлагаю так: ИИ должен создать собственный шифр, а ИИ оппонента должен взломать шифр. Кто быстрее взломает, хотя в случае с тобой подойдет слово «если», тот и победил. Как тебе условия, неженка?"

    mainHero "Идет. Можешь уже сейчас начинать пускать сопли и молить о том, чтобы Я программу тебе показал."

    scene bg code

    "Я не считал это за поединок или дуэль. Со знаниями, что пришли ко мне сегодня, Я переписал код, улучшил и доработал его. Мой ИИ уже напоминал того, к которому Я стремлюсь. "
    "Естественно, у Гавриила не было и шансов, мой ИИ лидировал с разрывом в половину времени. Гавриил лишь кипел от ненависти, а Я с чистой победой пошел довольный домой."

    scene bg living
    "Я шел до общежития, а с души как камень упал. Мне стало так свободно, так легко. Призраки больше не пугали меня, Я получил доступ к новым знаниям и возможность слушать человека, который все эти знания мне по полочкам разложит."
    show mainHero_stable at left
    show bogdan_stable at right
    with dissolve
    "В комнате Я рассказал о сегодняшнем дне Богдану и даже показал код, на что тот понимающе кивнул и поздравил меня с успехами. Думаю, он искренне радовался тому, что Я оказался не сумасшедшим. Пусть так, в любом случае он за меня рад."
    mainHero "*Половина работы проделана, половина еще впереди"

    jump fourthCourse