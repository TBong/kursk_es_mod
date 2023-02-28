label k_main:
    $ updVisual()
    call k_menu
    return

label k_prolog:
    stop music fadeout 3
    scene black with dissolve2
    $ new_chapter(0, u"Курск: Предыстория")
    $ updVisual()
    play music history_sound fadein 3
    scene kursk3 with Dissolve(5)
    pause (1)
    $ set_mode_nvl()
    "{font=[patternFont]}{color=#900}К-141 «Курск»{/font}{/color} – Российский атомный подводный ракетоносный крейсер проекта 949А «Антей». Заложен на «Севмаше» в 1990 году, спущен на воду в мае, принят в эксплуатацию в декабре 1994 года."
    "Свое почётное название подлодка получила в честь подвига советского народа на Курской дуге в годы Великой Отечественной войны. С 1995 по 2000 год находилась в составе Северного флота ВМФ России. пункт базирования — Видяево."
    scene air_car with dissolve2
    pause (1)
    "В 1999 году во время операции НАТО против Югославии «Курск» вёл скрытное наблюдение за авианосцем ВМС США «Теодор Рузвельт», самолёты с которого наносили удары по Югославии. За время средиземноморского похода «Курск» отработал 5 условных атак по реальным целям."
    "В августе-октябре 1999 года лодка участвовала в автономном походе в Атлантический океан и Средиземное море, перед этим выполнив на «отлично» ракетные стрельбы на приз главкома ВМФ России."
    scene k141_parade with dissolve2
    pause (1)
    "По итогам соревнования, К-141 — лучший в 7-й дивизии."
    "25 июля 1999 года экипаж «Курска» принимал участие в военно-морском параде, посвящённом Дню Военно-морского флота в Североморске."
    scene vmf_pride with dissolve2
    pause (1)
    "Экипаж АПРК был сформирован на Северном флоте в июне 1991 года, бóльшая его часть — специалисты 1-го и 2-го классов. Лодка под командованием капитана 1-го ранга готовилась к новому дальнему походу в составе мощной корабельной группы."
    "На 15 октября 2000 года из Североморска планировался выход в Средиземное море авианосно-маневренной группы Северного флота, включавшей «Курск»."
    scene kursk4 with dissolve2
    pause (1)
    "До этого, 10 августа 2000 года, согласно плану учений Северного флота, «Курск» должен был выйти море для выполнения учебно-боевого задания недалеко от Кольского залива."
    "С этого и началась трагическая история крупнейшей катастрофы в послевоенной истории советского и российского подводного флота."
    nvl clear
    stop music fadeout 3
    scene black with Dissolve(5)
    jump k_9aug_video

label k_9aug_video:
    $ renpy.movie_cutscene(gFile("video/9_aug.webm"))
    jump k_before

label k_before:
    $ new_chapter(1, u"Курск: Подготовка лодки и экипажа к учениям. Североморск, 9 августа")
    $ updVisual()
    play music chayki fadein 2
    scene kursk5 with Dissolve(5)
    "9 августа, за день до назначенной даты, в порту идёт подготовка АПЛ к учениям."
    "Моряки-подводники приняли лодку, провели осмотр всех отсеков."
    window hide
    stop music fadeout 2
    scene kp with dissolve2
    play ambience insideKursk fadein 2 volume 0.3
    window show
    "Радисты сверяют маршруты, устанавливают связь с отсеками и другими кораблями."
    "Помимо 111-ти человек штатного экипажа, во время проведения операции на подлодке будут находиться ещё 7 других специалистов: 5 офицеров штаба дивизии, военпред и инженер с завода «Дагдизель»."
    "Для них выделяются отдельные каюты в жилом отсеке №4."
    "На лодку они должны попасть непосредственно перед отплытием."
    "Вечером, командир, проверив выполненную работу и заполнив чек-лист, отдаёт экипажу команду отдыхать и набираться сил перед грядущим выходом в море."
    "Ночь с 9-го на 10-ое число моряки проводят непосредственно на подлодке."
    window hide
    scene black with Dissolve(3)
    play music entsan volume 0.1 fadein 2
    scene rest with Dissolve(3)
    window show
    "В одной из жилых кают, где-то в глубине субмарины, вокруг телевизора собралась небольшая группа подводников."
    "Они весело проводят время за прослушиванием музыки."
    "Вдруг в каюту заходит капитан."
    su "Ну, парни, как настрой?"
    hor "Отличный!"
    "Хором отвечают моряки."
    su "Так держать!"
    su "А ты, Быков, чего кислый?"
    bk "Ничего такого, товарищ капитан, просто хочу быстрее вернуться домой!"
    su "К чему же спешить! Разве здесь не хорошо?"
    su "Или у тебя другая причина есть?"
    sk "И правда, Федька, ты чего весь день ходишь, как не свой?"
    "Спросил Быкова мичман Симонов."
    "Фёдор смотрел на товарищей сверкающими зелёными глазами."
    bk "Ну... {w=0.5}в общем, жена в роддоме лежит. {w=0.5}Вот на днях сын родится!"
    su "А говорил ничего такого! {w=0.5}И чего же ты молчал?!"
    "Капитан, крепким рукопожатием поздравил Быкова."
    su "Не волнуйся, через пару дней вернешься ты к своей пассии!"
    su "А сын твой пусть тоже в подводники идёт!"
    bk "Так точно!"
    su "Ладно, я пошёл, отдыхайте тут, завтра будет много работы."
    hor "Есть отдыхать!"
    "Командир подлодки ушёл к себе."
    "Остальные члены экипажа, находящиеся в каюте, начали распрашивать Быкова."
    mo "Федь, ты чего нам раньше то не сказал?"
    bk "Да как-то не подумал."
    sk "Ничего себе, не подумал. У меня когда жена рожала - все знакомые знали!"
    mo "Вот именно, а ты вдруг отмалчиваться решил."
    bk "Извиняйте мужики, забылся я что-то. {w=0.5}Сам жду не дождусь когда уже смогу сынишку на руках подержать!"
    mo "Ладно тебе, успеешь ещё."
    mo "Так, товарищи подводники, кажется, пора спать!"
    window hide
    stop music fadeout 5
    stop ambience fadeout 5
    scene black with Dissolve(5)
    jump k_10aug_6_video

label k_10aug_6_video:
    $ renpy.movie_cutscene(gFile("video/10_aug_6.webm"))
    jump k_sailing

label k_sailing:
    $ new_chapter(2, u"Курск: День отплытия. Североморск, 10 августа, 6:00")
    $ updVisual()
    scene black
    play ambience insideKursk fadein 5 volume 0.3
    scene torpeda1 with Dissolve(5)
    window show
    "Все моряки поднялись в 6 утра и заняли свои посты."
    "На борт поднимаются в 7 человек, в числе которых два гражданских специалиста, один из которых должен будет наблюдать за пуском торпед."
    "Прикомандованный начальством инженер находится в отсеке №1, и вместе с экипажем проверяет торпедный боезапас."
    "Почти в то же время запускается ядерный реактор."
    window hide
    stop ambience fadeout 5
    scene black with Dissolve(5)
    $ renpy.movie_cutscene(gFile("video/reactor.webm"))
    play ambience insideKursk fadein 5 volume 0.9
    scene cafeteria with Dissolve(5)
    window show
    "Через час командиры отсеков докладывают капитану о проведённой работе."
    "В ходе небольшого брифинга ни о каких нарушениях в работе систем подлодки заявлено не было."
    "Руководством было дано разрешение старт на учений."
    "Они будут проходить в три этапа."
    "Первый - атака крылатой ракетой «Гранит» эскадры боевых кораблей."
    "Второй - пуск торпеды «65-76»."
    "Третий - возвращение на базу незамеченными."
    window hide
    stop ambience fadeout 5
    scene black with Dissolve(5)
    jump k_sailing_video

label k_sailing_video:
    $ renpy.movie_cutscene(gFile("video/sailling.webm"))
    jump k_after_sailing

label k_after_sailing:
    $ new_chapter(3, u"Курск: Отплытие. Североморск, 10 августа, 7:00")
    $ updVisual()
    play ambience ambience_lake_shore_day fadein 5
    scene captains with Dissolve(5)
    window show
    s_adm "А ведь эта лодка создавалась под предлогом незаметности. Ни один радар не сможет её засечь, если те, кто находится на ней, этого захотят."
    s_adm "Удивительно, не правда ли?"
    adm "В этом плане «Тайфун» куда лучше. Он сам тебя найдет."
    adm "Лишь одни эти лодки вселяют страх на все штаты."
    s_adm "Неудивительно, почему американцы готовы платить нам, только бы мы их утилизировали."
    window hide
    stop ambience fadeout 5
    play ambience insideKursk fadein 5
    scene black with Dissolve(5)
    scene kp with Dissolve(5)
    window show
    su "Глубина какая?"
    sk "40 метров!"
    su "Продуть балласт! Всплытие 10 дифферент 3!"
    sk "Есть всплытие 10 дифферент 3!"
    "Заработали насосы, вода из балласта начала покидать лодку под действием сжатого воздуха."
    su "Приготовиться к пуску ракеты!"
    window hide
    scene torpeda1 with dissolve2
    window show
    torp "Что там с ней?"
    dag "За последние 20 минут температура повысилась на 15 градусов."
    torp "Это плохо."
    radio "Экипажу приготовиться к пуску ракеты."
    radio "Пуск через: 3, {w=0.5}2, {w=0.5}1."
    window hide
    scene black
    show torpeda1 at k_shaking
    play sound rocketFire
    pause (1)
    window show
    radio "Пуск успешный."
    torp "Всё, через час распрощаемся с нашим «толстяком»."
    dag "Скорее бы. Перекисно-водородные торпеды высокую температуру не любят."
    torp "Главное её выпустить, а там с ней будь что будет."
    window hide
    scene kp with Dissolve(5)
    window show
    su "C Петра Великого докладывают, об успешном поражении цели, молодцы!"
    su "Погружение до 40 метров, дифферент на нос 5, взять курс на 130 градусов, установить скорость 25 узлов."
    sk "Есть погружение 40 дифферент 5, курс 130, скорость 25!"
    window hide
    stop ambience fadeout 5
    scene black with Dissolve(5)
    jump k_norv_base_video

label k_norv_base_video:
    $ renpy.movie_cutscene(gFile("video/norv_base.webm"))
    jump norv_base

label norv_base:
    $ new_chapter(4, u"Курск: Норвегия, «Оласверн»")
    $ updVisual()
    play ambience inside_norv fadein 5
    scene norv1 with Dissolve(5)
    window show
    com "Driver Russerne øvelser i Barentshavet igjen?{color=#a5a5a5}{vspace=5}{space=20}-{space=20}Русские снова проводят учения в баренцевом море?"
    nrv "Ja, sir.{color=#a5a5a5}{vspace=5}{space=20}-{space=20}Да, сэр."
    com "I hvilken sammensetning denne gangen?{color=#a5a5a5}{vspace=5}{space=20}-{space=20}В каком составе на этот раз?"
    nrv "Hangarskip «Admiral Kuznetsov», cruiser «Peter Den Store», APC «Kursk» Oscar klasse II, flere destroyere.{color=#a5a5a5}{vspace=5}{space=20}-{space=20}Авианесущий крейсер «Адмирал Кузнецов», крейсер «Пётр Великий», АПРК «Курск» класса Oscar II, несколько эсминцев."
    nrv "Totalt - 50 skip og en ubåt.{color=#a5a5a5}{vspace=5}{space=20}-{space=20}Всего - 50 кораблей и одна субмарина."
    com "Oscar II... Typer av våpen?{color=#a5a5a5}{vspace=5}{space=20}-{space=20}Оскар II... Тип вооружения?"
    nrv "24 anti-skip missiler P-700 «Granitt», torpedoer.{color=#a5a5a5}{vspace=5}{space=20}-{space=20}24 противокорабельные ракеты П-700 «Гранит», торпеды."
    com "Vis det på radarene.{color=#a5a5a5}{vspace=5}{space=20}-{space=20}Покажите на радарах."
    nrv "Umulig. Det er usynlig, stille.{color=#a5a5a5}{vspace=5}{space=20}-{space=20}Невозможно. Она невидимая, бесшумная."
    com "Dårlig. Fortsett å se.{color=#a5a5a5}{vspace=5}{space=20}-{space=20}Плохо. Продолжайте наблюдение."
    window hide
    stop ambience fadeout 5
    scene black with Dissolve(5)
    jump torp_boom

label torp_boom:
    $ new_chapter(5, u"Курск: Загрузка торпеды, 11:25")
    $ updVisual()
    play ambience insideKursk fadein 5
    scene kp with Dissolve(5)
    window show
    sk "Корабельная группа докладывает на берег и в скором времени будет готова продолжить."
    su "Через пол часа переходим ко второму этапу учений."
    su "Первому отсеку начать загрузку торпеды."
    sk "Так точно!"
    window hide
    scene torpeda1 with dissolve2
    play sound ra_1
    window show
    p_radio "Первый отсек, состояние учебной торпеды?"
    play sound ra_1
    torp "Торпеда «65-76» в норме, но внутреннее давление и температура повышены."
    play sound ra_1
    p_radio "В пределах допустимого?"
    play sound ra_1
    torp "Так точно."
    play sound ra_1
    p_radio "Принято. Начинайте погрузку."
    play sound ra_1
    torp "Слушаюсь."
    window hide
    scene torpeda2 with dissolve2
    window show
    dag "Торпедный аппарат готов."
    torp "Загружай."
    stop ambience fadeout 5
    window hide
    play sound torp_2
    camera:
        perspective True
        zpos 0
        linear 10.3 ypos -70 xpos 20 zpos -500
    pause (10.3)
    play sound_1 clock volume 0.3 fadein 8
    play sound_2 smth_comming volume 0.5
    camera:
        perspective True
        xpos 0 zpos 0 ypos 0
    scene torpeda1 with dissolve
    pause (1)
    window show
    dag "Торпеда в аппарате."
    window hide
    pause (0.65)
    window show
    torp "Сколько время? У меня нет часов."
    window hide
    pause (0.65)
    window show
    dag "11:28"
    window hide
    pause (0.65)
    window show
    torp "Cкорее бы от неё избавиться."
    window hide
    pause (2.0)
    play sound_2 boom_2
    stop sound_1
    stop ambience fadeout 1
    scene black
    show fire_torpeda1
    with dissolve
    play sound_1 boom_1 volume 0.5   
    pause (0.75)  
    pause (0.75)
    scene black
    show fire_torpeda2 
    with dspr
    pause (1)
    stop sound_1 fadeout 3
    scene black
    show fire_torpeda3 
    with dspr
    stop sound_1 fadeout 2
    stop sound_2 fadeout 2
    scene black with dissolve2
    jump k_first_explosion_video

label k_first_explosion_video:
    $ renpy.movie_cutscene(gFile("video/first_explosion.webm"))
    jump aft_first_explosion

label aft_first_explosion:
    $ new_chapter(6, u"Курск: Взрыв торпеды")
    $ updVisual()
    play ambience insideKursk fadein 2
    scene black
    show turb3
    with dissolve
    window show
    sk "Что это было?!"
    bk "Что случилось?!"
    gb "Почему мы так резко набрали глубину?!"
    window hide
    scene turb2 with dissolve2
    window show
    "Опомнившийся командир отсека начал действовать согласно установленным правилам поведения экипажа при не штатных ситуациях."
    mo "Герметезировать отсек! Все клапаны закрыть!"
    mo "Задраить носовую переборку! Задраить все люки!"
    mo "Наладить связь с центральным отсеком!"
    window hide
    scene turb1 with dissolve2
    window show
    play sound ra_1
    mo "Центральный, центральный, ответьте седьмому, приём!"
    play sound ra_1
    mo "Повторяю, ответьте седьмому, приём!"
    bk "Почему центральный не отвечает?"
    sk "Потому что они мертвы!"
    mo "Тихо."
    bk "Почему мы не всплываем?"
    gb "А ты как думаешь?!"
    mo "Тихо я сказал!"
    window hide
    scene black with Dissolve(3)
    stop ambience fadeout 1
    play sound_loop fire fadein 1
    scene kp_fire with Dissolve(3)
    window show
    radio "Центральный, ответьте седьмому, приём!"
    window hide
    pause (1)
    window show
    radio "Центральный, ответьте, приём!"
    window hide
    play ambience insideKursk fadein 2
    stop sound_loop fadeout 2
    scene turb4 with Dissolve(3)
    window show
    gb "Товарищ командир, в первом и отсекe пожар!"
    mo "Температура детонации?"
    sk "Торпеды на стелажах взорвутся при температуре 250 градусов."
    bk "Сколько сейчас?"
    gb "270."
    gb "С каждой секундой растёт!"
    window hide
    scene turb1 with dissolve2
    window show
    bk "Что нам делать?"
    mo "Всё как нас учили."
    mo "Герметизируем отсек, задраиваем переборку."
    mo "В случае задымления расчехляем ПДА!{color=#a5a5a5}{vspace=10}{space=100}ПДА{space=10}-{space=10}Портативный дыхательный аппарат"
    gb "Температура зашкалила!"
    mo "Без паники..."
    window hide
    pause (3)
    scene black with Dissolve(4)
    jump k_second_explosion_video

label k_second_explosion_video:
    $ renpy.movie_cutscene(gFile("video/second_explosion.webm"))
    jump aft_second_explosion

label aft_second_explosion:
    $ new_chapter(7, u"Курск: Взрыв боезапаса")
    $ updVisual()
    "а"



    
    





    




    