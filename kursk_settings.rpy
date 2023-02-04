init 1:

    define config.developer = True
    $ mods["k_main"]=u"{font=[patternFont]}Курск"

    transform k_shaking:
        anchor (0.0, 0.0) pos (0.0, 0.0)
        linear 0.2 pos (-5, -5)
        linear 0.2 pos (0, 0)
        linear 0.2 pos (5, -5)
        linear 0.2 pos (0, 0)
        repeat
    

init python:
    default_k_path = "mods/kursk_es_mod/materials/"

    def gFile(file):
        return default_k_path + file
    renpy.music.register_channel("sound_1",loop=False)
    renpy.music.register_channel("sound_2",loop=False)
    renpy.music.register_channel("sound_3",loop=False)

    patternFont = gFile("font/18035.otf")

    

label k_main:
    call k_menu
    return

label k_menu:
    $ new_chapter(0, u"Меню КУРСК")
    scene kursk1 with dissolve2
    call screen k_main_menu with dissolve
    return