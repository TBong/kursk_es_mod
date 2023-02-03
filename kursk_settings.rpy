init 1:

    define config.developer = True
    $ mods["k_main"]=u"{font=getFile[18035.otf]}Курск"

    transform k_shaking:
        anchor (0.0, 0.0) pos (0.0, 0.0)
        linear 0.2 pos (-5, -5)
        linear 0.2 pos (0, 0)
        linear 0.2 pos (5, -5)
        linear 0.2 pos (0, 0)
        repeat

init python:

    renpy.music.register_channel("sound_1",loop=False)
    renpy.music.register_channel("sound_2",loop=False)
    renpy.music.register_channel("sound_3",loop=False)

    patternFont = getFile("font/18035.otf")

    def getFile(file):
        return default_k_path + file
    
    default_k_path = "mods/kursk_es_mod/materials/"