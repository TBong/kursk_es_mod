init 2:

    image Dst dst1 = getFile("gui/Dust1.png")
    image Dst dst2 = getFile("gui/Dust2.png")
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

    $ sos_lodka = getFile("sound/music/sos_lodka.mp3")