init 2:

    #Изображения
    image air_car = gFile("cg/air_car.jpg")
    image vmf = gFile("cg/vmf.jpg")
    image kp = gFile("cg/kp.jpg")
    image k141_parade = gFile("cg/k141_parade.jpg")
    image vmf_pride = gFile("cg/vmf_pride.jpg")
    image kursk1 = gFile("screens/menu/kursk_1.jpg")
    image kursk2 = gFile("cg/kursk_2.jpg")
    image kursk3 = gFile("cg/kursk_3.jpg")
    image kursk4 = gFile("cg/kursk_4.jpg")

    #Музыка
    $ sos_lodka = gFile("sound/music/sos_lodka.mp3")

    #GUI
    image Dst dst1 = gFile("gui/Dust1.png")
    image Dst dst2 = gFile("gui/Dust2.png")
    image DustB:
        truecenter
        zoom 1.5
        contains:
            SnowBlossom("Dst dst1", 20, 50, (-30,-25), (-30,30), 25, False, True)
        contains:
            SnowBlossom("Dst dst1", 20, 50, (25,30), (-30,30), 25, False, True)
        contains:
            SnowBlossom("Dst dst2", 20, 50, (-30,-25), (-30,30), 25, False, True)
        contains:
            SnowBlossom("Dst dst2", 20, 50, (25,30), (-30,30), 25, False, True)

    #Шрифт
    $ furore = gFile("font/Furore.ttf")

    #Музыка
    $ sos_lodka = gFile("sound/music/sos_lodka.mp3")
    $ ddt_kolesnikov = gFile("sound/music/ddt_kolesnikov.mp3")