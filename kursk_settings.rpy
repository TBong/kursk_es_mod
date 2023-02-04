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

init -1 python:
    
    def saveOldVisual():
        renpy.display.screen.screens[("dpa_say_gui_old",None)] = renpy.display.screen.screens[("say",None)]
        renpy.display.screen.screens[("dpa_game_menu_selector_old",None)] = renpy.display.screen.screens[("game_menu_selector",None)]
        renpy.display.screen.screens[("dpa_nvl_old",None)] = renpy.display.screen.screens[("nvl",None)]
        renpy.display.screen.screens[("dpa_choice_old",None)] = renpy.display.screen.screens[("choice",None)]

    def updVisual():
        renpy.display.screen.screens[("say",None)] = renpy.display.screen.screens[("dpa_say_gui_reborn",None)]
        renpy.display.screen.screens[("game_menu_selector",None)] = renpy.display.screen.screens[("dpa_menu_selector",None)]
        renpy.display.screen.screens[("choice",None)] = renpy.display.screen.screens[("dpa_choice",None)]
        renpy.display.screen.screens[("nvl",None)] = renpy.display.screen.screens[("dpa_nvl",None)]
    
    def rollbackVisual(*arg):
        renpy.display.screen.screens[("say",None)] = renpy.display.screen.screens[("dpa_say_gui_old",None)]
        renpy.display.screen.screens[("game_menu_selector",None)] = renpy.display.screen.screens[("dpa_game_menu_selector_old",None)]
        renpy.display.screen.screens[("choice",None)] = renpy.display.screen.screens[("dpa_choice_old",None)]
        renpy.display.screen.screens[("nvl",None)] = renpy.display.screen.screens[("dpa_nvl_old",None)]

    def toDefaultSettings(*arg):
        Call("initVars")
        rollbackVisual()
    
    def dpaNewChapter(dayNum, chapterName):
        dpaSetChapter(dayNum, chapterName)
        updVisual()    

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