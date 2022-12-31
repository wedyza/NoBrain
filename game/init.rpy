init:
    define unknown = Character('???', color="c8ffc8")
    define mainHero = Character('Саша', color="c8ffc8")
    image mainHero_stable = "images/gg.png"
    define defender = Character('Охранница', color="c8ffc8")
    image defender_stable = "images/defender.png"
    define timur = Character('Тимур', color="c8ffc8")
    image timur_stable = "images/timur.png" 
    define historyTeacher = Character('Пен-пен', color="c8ffc8")
    image historyTeacher_stable = "images/historyTeacher.png"
    define mentor = Character('Наставница', color="c8ffc8")
    image mentor_stable = "images/mentor.png"
    define kostya = Character('Гавриил', color="c8ffc8")
    image kostya_stable = "images/1.png"
    define cristina = Character('Кристина', color="c8ffc8")
    image cristina_stable = "images/cristina.png"
    define tutor = Character('Тьютор', color="c8ffc8")
    image tutor_stable = "images/tutor.png"
    define bogdan = Character('Богдан', color="c8ffc8")
    image bogdan_stable = "images/bogdan.png"
    define penpen = Character('Пен-Пинович', color="c8ffc8")
    image penpen_stable = "images/historyTeacher.png"
    define dima = Character('Нудима Сергеевич', color="c8ffc8")
    image dima_stable = "images/dima.png"
    define ded = Character('Максим Альбертович', color="c8ffc8")
    image ded_stable = "images/ded.png"
    define ii = Character('Воскресенье', color="c8ffc8")
    define random = Character('Олицетворение случайности', color="c8ffc8")
    image math = "images/math.png"
    image ghost = "images/ghost.png"


    image bg summer = "images/bg summer.jpg"
    image bg summer busstop = "images/bg summer busstop.jpg"
    image bg guk = "images/guk.jpg"
    image bg rtf = "images/bg rtf.jpg"
    image bg living = "images/bg living room.jpg"
    image bg lection = "images/bg lection.jpg"
    image bg library = "images/library.jpg"
    image bg classroom1 = "images/bg classroom1.jpeg"
    image bg classroom = "images/classroom.jpeg"
    image bg door = "images/bg door.jpg"
    image bg code = "images/bg code.jpeg"
    image bg cristina room = "images/bg cristina room.jpg"
    image bg basement = "images/basement.jpg"
    image bg good = "images/good.jpg"

    $timur_attitude = 0
    $cristina_attitude = 0
    $repairing = 0


    python:
    
        import math

        class Shaker(object):
        
            anchors = {
                'top' : 0.0,
                'center' : 0.5,
                'bottom' : 1.0,
                'left' : 0.0,
                'right' : 1.0,
                }
        
            def __init__(self, start, child, dist):
                if start is None:
                    start = child.get_placement()
                #
                self.start = [ self.anchors.get(i, i) for i in start ]  # центральная позиция
                self.dist = dist    # максимальное расстояние, в пикселях, от начальной точки
                self.child = child
                
            def __call__(self, t, sizes):
                # Число с плавающей точкой в целое число... превращает числа с плавающей точкой
                # в целые.      
                def fti(x, r):
                    if x is None:
                        x = 0
                    if isinstance(x, float):
                        return int(x * r)
                    else:
                        return x

                xpos, ypos, xanchor, yanchor = [ fti(a, b) for a, b in zip(self.start, sizes) ]

                xpos = xpos - xanchor
                ypos = ypos - yanchor
                
                nx = xpos + (1.0-t) * self.dist * (renpy.random.random()*2-1)
                ny = ypos + (1.0-t) * self.dist * (renpy.random.random()*2-1)

                return (int(nx), int(ny), 0, 0)
        
        def _Shake(start, time, child=None, dist=100.0, **properties):

            move = Shaker(start, child, dist=dist)
        
            return renpy.display.layout.Motion(move,
                          time,
                          child,
                          add_sizes=True,
                          **properties)

        Shake = renpy.curry(_Shake)