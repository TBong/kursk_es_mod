init 2:

    #Изображения
    image air_car = gFile("cg/air_car.jpg")
    image vmf = gFile("cg/vmf.jpg")
    image kp = gFile("cg/kp.jpg")
    image kp2 = gFile("cg/kp2.jpg")
    image k141_parade = gFile("cg/k141_parade.jpg")
    image vmf_pride = gFile("cg/vmf_pride.jpg")
    image rest = gFile("cg/rest.jpg")
    image torpeda1 = gFile("cg/torpeda1.jpg")
    image kursk1 = gFile("cg/kursk_1.jpg")
    image kursk2 = gFile("cg/kursk_2.jpg")
    image kursk3 = gFile("cg/kursk_3.jpg")
    image kursk4 = gFile("cg/kursk_4.jpg")
    image kursk5 = gFile("cg/kursk_5.jpg")
    image kursk6 = gFile("cg/kursk_6.jpg")

    #Музыка
    $ entsan = gFile("sound/music/EnterSandman.mp3")
    $ lowcostdrammas = gFile("sound/music/lowcostdrammas.mp3")
    $ sos_lodka = gFile("sound/music/sos_lodka.mp3")
    $ ddt_kolesnikov = gFile("sound/music/ddt_kolesnikov.mp3")

    #Шрифт
    $ furore = gFile("font/Furore.ttf")

    #Персонажи
    $ hor = Character (u'Моряки', color = "#1f5790", what_color = "FFFFFF")
    $ bk = Character (u'Быков', color = "#4ea0f1", what_color = "FFFFFF")
    $ sk = Character (u'Симонов', color = "#4ea0f1", what_color = "FFFFFF")
    $ su = Character (u'Капитан', color = "#0721eb", what_color = "FFFFFF")

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

    $ menu_back_num = 0
    image menu_back = ConditionSwitch(
        "menu_back_num==0","kursk6",
        "menu_back_num==1","kursk2",
        True, "kursk1"
    )
