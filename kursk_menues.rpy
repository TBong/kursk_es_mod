#Главное меню
screen k_main_menu:
    tag menu
    modal True
    imagebutton:
        auto gFile("screens/menu/nachat_2_%s.png")
        xpos 55
        ypos 200
        action [ Jump ('k_main') ]
    imagebutton:
        auto gFile("screens/menu/load_2_%s.png")
        xpos 55
        ypos 400
    imagebutton:
        xpos 55
        ypos 600
        auto gFile("screens/menu/settings_2_%s.png")
        action [ ShowMenu('preferences') ]
    imagebutton:
        auto  gFile("screens/menu/exit_2_%s.png")
        xpos 55
        ypos 800
        action [MainMenu() ]
    text "{font=[patternFont]}{color=#ac0c0c}КУРСК":
        xpos 1548
        ypos 80
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

screen dpa_Load:
    tag menu
    modal True
    window:
        add "menu_back":
            xpos -6
            ypos -6

        textbutton ["Загрузить игру"]:
            ypos 950
            xalign 0.5
            text_style "text_save_load"
            style "button_none"
            action [FileLoad(selected_slot) ]

        textbutton ["Удалить"]:
            xpos 1500
            ypos 950
            text_style "text_save_load"
            style "button_none"
            action FileDelete(selected_slot)

        textbutton ["Назад"]:
            xpos 30
            ypos 950
            text_style "text_save_load"
            style "button_none"
            action Return()

        vbox:
            xalign 0.037
            yalign 0.52
            grid 1 9:
                for i in range(1, 10):
                    textbutton str(i):
                        right_padding 55
                        text_size 60
                        text_style "text_save_load"
                        style "button_none"
                        xpos getXPos(i)
                        action (FilePage(str(i)), SetVariable("selected_slot", False))
        grid 4 3:
            xpos 0.11
            ypos 0.2
            xmaximum 0.81
            ymaximum 0.65
            transpose False
            xfill True
            yfill True
            for i in range(1, 13):
                fixed:
                    add FileScreenshot(i):
                        xpos 10
                        ypos 10
                    button:
                        action SetVariable("selected_slot", i)
                        xfill False
                        yfill False
                        style "file_load_button"
                        fixed:
                            text ( "%s." % i
                                   + FileTime(i, format=' %d.%m.%y, %H:%M', empty=" "+translation["Empty_slot"][_preferences.language])
                                   + "\n" +FileSaveName(i)):
                                xpos 15
                                ypos 15