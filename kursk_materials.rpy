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
    image torpeda2 = gFile("cg/torpeda2.jpg")
    image kursk1 = gFile("cg/kursk_1.jpg")
    image kursk2 = gFile("cg/kursk_2.jpg")
    image kursk3 = gFile("cg/kursk_3.jpg")
    image kursk4 = gFile("cg/kursk_4.jpg")
    image kursk5 = gFile("cg/kursk_5.jpg")
    image kursk6 = gFile("cg/kursk_6.jpg")
    image captains = gFile("cg/captains.jpg")
    image cafeteria = gFile("cg/cafeteria.jpg")
    image fire_torpeda1 = gFile("cg/fire_torpeda1.jpg")
    image fire_torpeda2 = gFile("cg/fire_torpeda2.jpg")
    image fire_torpeda3 = gFile("cg/fire_torpeda3.jpg")
    image norv1 = gFile("cg/norv1.jpg")
    image norv2 = gFile("cg/norv2.jpg")

    #Музыка
    $ entsan = gFile("sound/music/EnterSandman.mp3")
    $ lowcostdrammas = gFile("sound/music/lowcostdrammas.mp3")
    $ sos_lodka = gFile("sound/music/sos_lodka.mp3")
    $ ddt_kolesnikov = gFile("sound/music/ddt_kolesnikov.mp3")
    $ violence = gFile("sound/music/MacQuayle_Violence.mp3")
    $ longing = gFile("sound/music/Santaolalla_Longing.mp3")
    $ history_sound = gFile("sound/music/history_sound.mp3")

    #Звуки
    $ inside_norv = gFile("sound/sfx/inside_norv.mp3")
    $ insideKursk = gFile("sound/sfx/inside_kursk.mp3")
    $ rocketFire = gFile("sound/sfx/rocketfire.mp3")
    $ chayki = gFile("sound/sfx/chayki.mp3")
    $ ra_1 = gFile("sound/sfx/ra_1.mp3")
    $ ra_2 = gFile("sound/sfx/ra_2.mp3")
    $ torp_1 = gFile("sound/sfx/torp_1.mp3")
    $ torp_2 = gFile("sound/sfx/torp_2.mp3")
    $ clock = gFile("sound/sfx/clock.mp3")
    $ boom_1 = gFile("sound/sfx/boom_1.mp3")
    $ boom_2 = gFile("sound/sfx/boom_2.mp3")
    $ smth_comming = gFile("sound/sfx/smth_comming.mp3")
    #Шрифт
    $ furore = gFile("font/Furore.ttf")
    $ patternFont = gFile("font/18035.otf")

    #Персонажи
    $ hor = Character (u'Моряки', color = "#1f5790", what_color = "FFFFFF")
    $ bk = Character (u'Быков', color = "#4ea0f1", what_color = "FFFFFF")
    $ sk = Character (u'Симонов', color = "#42688f", what_color = "FFFFFF")
    $ su = Character (u'Капитан', color = "#0721eb", what_color = "FFFFFF")
    $ mo = Character (u'Мотин', color = "#6873c7", what_color = "FFFFFF")
    $ adm = Character (u'Адмирал', color = "#D4AF37", what_color = "FFFFFF")
    $ s_adm = Character (u'Вице-Адмирал', color = "#ffffff", what_color = "FFFFFF")
    $ dag = Character (u'Инженер', color = "#285512", what_color = "FFFFFF")
    $ torp = Character (u'Торпедист', color = "#8c8e8f", what_color = "FFFFFF")
    $ radio = Character (u'Динамик', color = "#ff0000", what_color = "FFFFFF")
    $ p_radio = Character (u'Рация', color = "#ff0000", what_color = "FFFFFF")
    $ com = Character (u'Главнокомандующий', color = "#741111", what_color = "FFFFFF")
    $ nrv = Character (u'Норвежский офицер', color = "#0b1984", what_color = "FFFFFF")
    
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
