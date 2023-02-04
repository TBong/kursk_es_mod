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

    def gFile(file):
        return default_k_path + file

    def saveOldVisual():
        renpy.display.screen.screens[("k_say_gui_old",None)] = renpy.display.screen.screens[("say",None)]
        renpy.display.screen.screens[("k_game_menu_selector_old",None)] = renpy.display.screen.screens[("game_menu_selector",None)]
        #renpy.display.screen.screens[("dpa_nvl_old",None)] = renpy.display.screen.screens[("nvl",None)]
        #renpy.display.screen.screens[("dpa_choice_old",None)] = renpy.display.screen.screens[("choice",None)]

    def updVisual():
        renpy.display.screen.screens[("say",None)] = renpy.display.screen.screens[("k_say_gui_reborn",None)]
        renpy.display.screen.screens[("game_menu_selector",None)] = renpy.display.screen.screens[("k_menu_selector",None)]
        #renpy.display.screen.screens[("choice",None)] = renpy.display.screen.screens[("dpa_choice",None)]
        #renpy.display.screen.screens[("nvl",None)] = renpy.display.screen.screens[("dpa_nvl",None)]
    
    def rollbackVisual(*arg):
        renpy.display.screen.screens[("say",None)] = renpy.display.screen.screens[("k_say_gui_old",None)]
        renpy.display.screen.screens[("game_menu_selector",None)] = renpy.display.screen.screens[("k_game_menu_selector_old",None)]
        #renpy.display.screen.screens[("choice",None)] = renpy.display.screen.screens[("dpa_choice_old",None)]
        #renpy.display.screen.screens[("nvl",None)] = renpy.display.screen.screens[("dpa_nvl_old",None)]
    
    def dpaNewChapter(dayNum, chapterName):
        dpaSetChapter(dayNum, chapterName)
        updVisual()    

    def gFileSayGui(path):
        return gFile("screens/dialog/"+path)    

    def getXPos(num):
        if num == 1:
            return 42
        return 32

#Стили
init 2 python:
    style.text_save_load                          = Style(style.default)
    style.text_save_load.font                     = gFile("font/Furore.ttf")
    style.text_save_load.size                     = 60
    style.text_save_load.color                    = "#ffffff"
    style.text_save_load.hover_color              = "#808080"
    style.text_save_load.selected_color           = "#ffffff"
    style.text_save_load.selected_idle_color      = "#ffffff"
    style.text_save_load.selected_hover_color     = "#808080"
    style.text_save_load.insensitive_color        = "#ffffff"

    style.button_none = Style(style.button)
    style.button_none.background = None
    style.button_none.hover_background = None
    style.button_none.selected_background = None
    style.button_none.selected_hover_background = None
    style.button_none.selected_idle_background = None

    style.file_load_button = Style(style.button)
    style.file_load_button.background = gFile("screens/load_save/load_Button_idle.png")
    style.file_load_button.hover_background = gFile("screens/load_save/load_Button_hover.png")
    style.file_load_button.selected_background = gFile("screens/load_save/load_Button_selected.png")
    style.file_load_button.selected_hover_background = gFile("screens/load_save/load_Button_selected.png")
    style.file_load_button.selected_idle_background = gFile("screens/load_save/load_Button_selected.png")

    style.text_select_track = Style(style.default)
    style.text_select_track.color                    = "#c2c2c2"
    style.text_select_track.hover_color              = "#ffffff"
    style.text_select_track.selected_color           = "#ffffff"
    style.text_select_track.selected_idle_color      = "#ffffff"
    style.text_select_track.selected_hover_color     = "#ffffff"
    style.text_select_track.insensitive_color        = "#9e9e9e"
    style.text_select_track.size = 30


init python:
    default_k_path = "mods/kursk_es_mod/materials/"
    
    
    renpy.music.register_channel("sound_1",loop=False)
    renpy.music.register_channel("sound_2",loop=False)
    renpy.music.register_channel("sound_3",loop=False)

    patternFont = gFile("font/18035.otf")

    

label k_main:
    $ updVisual()
    call k_menu
    return

label k_menu:
    $ updVisual()
    $ new_chapter(0, u"Меню КУРСК")
    scene kursk1 with dissolve2
    call screen k_main_menu with dissolve
    return