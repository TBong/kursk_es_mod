init 2:

    #Изображения
    image kp = gFile("cg/kp.jpg")
    image kursk1 = gFile("screens/menu/kursk_1.jpg")
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