#Главное меню
screen k_main_menu:
    tag menu
    modal True
    imagebutton:
        auto gFile("screens/menu/nachat_2_%s.png")
        xpos 55
        ypos 200
    imagebutton:
        auto gFile("screens/menu/load_2_%s.png")
        xpos 55
        ypos 400
    imagebutton:
        auto gFile("screens/menu/settings_2_%s.png")
        xpos 55
        ypos 600
    imagebutton:
        auto  gFile("screens/menu/exit_2_%s.png")
        xpos 55
        ypos 800
        action [MainMenu() ]
    text "{font=[patternFont]}{color=#ac0c0c}КУРСК":
        xpos 1548
        ypos 50
        size 118


#Маленькое меню
screen dpa_menu_selector:
    tag menu
    modal True

    $ timeofday = persistent.timeofday
    $ time_of_day = persistent.timeofday
    button:
        style "blank_button"
        xalign 0
        yalign 0
        xfill True
        yfill True
        action Return()
    
    add getFile("image/screens/menu/lil_menu_back.png"):
        xalign 0.5
        yalign 0.5

    textbutton ["Меню БЛ"]:
        xalign 0.5
        yalign 0.30
        text_style "text_save_load"
        style "button_none"
        action [ Function(toDefaultSettings), MainMenu() ]

    textbutton ["Сохранение"]:
        xalign 0.5
        yalign 0.40
        text_style "text_save_load"
        style "button_none"
        action ShowMenu('dpa_Save')
    
    textbutton ["Загрузка"]:
        xalign 0.5
        yalign 0.50
        text_style "text_save_load"
        style "button_none"
        action ShowMenu('dpa_Load')
    
    textbutton ["Настройки"]:
        xalign 0.5
        yalign 0.60
        text_style "text_save_load"
        style "button_none"
        action ShowMenu('preferences')
    
    textbutton ["Выход"]:
        xalign 0.5
        yalign 0.70
        text_style "text_save_load"
        style "button_none"
        action ShowMenu('quit')
    
    textbutton ["Откл. интерфейс мода"]:
        xalign 1.0
        yalign 1.0
        style "button_none"
        text_style "text_save_load"
        action [ Function(rollbackVisual), Return() ]