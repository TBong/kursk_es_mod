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
    $ new_chapter(1, u"Курск: Подготовка лодки")
    $ updVisual()
    play music chayki fadein 2
    scene kursk5 with Dissolve(5)
    "9 августа, за день до назначенной даты, в порту идёт подготовка АПЛ к учениям."
    "Моряки-подводники приняли лодку, провели осмотр всех отсеков."
    window hide
    stop music fadeout 2
    scene kp with dissolve2
    play ambience kp_ambience fadein 2 volume 0.3
    window show
    "Радисты устанавливают связь с отсеками и другими кораблями."
    "Помимо 111-ти человек штатного экипажа, во время проведения операции на подлодке будут находиться ещё 7 других специалистов: 5 офицеров штаба дивизии, военпред и инженер с завода «Дагдизель»."
    "Для них выделяются отдельные каюты в жилом отсеке №4."
    "На лодку они должны попасть непосредственно перед отплытием."
    "Вечером, командир, проверив выполненную работу и заполнив чек-лист, отдаёт экипажу команду отдыхать перед грядущим выходом в море."
    window hide
    stop ambience fadeout 3
    scene black with Dissolve(3)
    play ambience insideKursk fadein 3 volume 0.5
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
    $ new_chapter(2, u"Курск: День отплытия")
    $ updVisual()
    scene black
    play ambience insideKursk fadein 5 volume 0.3
    scene torpeda1 with Dissolve(5)
    window show
    "Все моряки поднялись в 6 утра и заняли свои посты."
    "На борт поднимаются в 7 человек, в числе которых два гражданских специалиста, один из которых должен будет наблюдать за пуском торпед."
    "Прикомандованный начальством инженер находится в отсеке №1, и вместе с экипажем проверяет торпедный боезапас."
    window hide
    stop ambience fadeout 5
    scene black with Dissolve(5)
    jump reactor_start

label reactor_start:
    $ renpy.movie_cutscene(gFile("video/reactor.webm"))
    jump briefing

label briefing:
    $ updVisual
    $ new_chapter(3, u"Курск: День отплытия")
    play ambience insideKursk fadein 5 volume 0.9
    scene cafeteria with Dissolve(5)
    window show
    "Через час командиры отсеков докладывают капитану о проведённой работе."
    "В ходе небольшого брифинга ни о каких нарушениях в работе систем подлодки заявлено не было."
    "Руководством было дано разрешение старт на учений."
    "Они будут проходить в три этапа."
    "Первый - атака крылатой ракетой «Гранит» эскадры боевых кораблей."
    "Второй - пуск торпеды «65-76ПВ»."
    "Третий - возвращение на базу незамеченными."
    window hide
    stop ambience fadeout 5
    scene black with Dissolve(5)
    jump k_sailing_video

label k_sailing_video:
    $ renpy.movie_cutscene(gFile("video/sailling.webm"))
    jump k_after_sailing

label k_after_sailing:
    $ new_chapter(4, u"Курск: Стрельба ракетой")
    $ updVisual()
    play ambience ambience_lake_shore_day fadein 5
    scene captains with Dissolve(5)
    window show
    s_adm "А ведь эта лодка создавалась под предлогом незаметности. Ни один радар не сможет её засечь, если те, кто находится на ней, этого захотят."
    s_adm "Удивительно, не правда ли?"
    adm "В этом плане «Тайфун» куда лучше. Он сам тебя найдет."
    adm "Одни лишь эти подлодки вселяют страх на все соединённые штаты."
    s_adm "Неудивительно, почему американцы готовы платить нам, только бы мы их утилизировали."
    window hide
    stop ambience fadeout 5
    play ambience kp_ambience fadein 5
    scene black with Dissolve(5)
    scene kp with Dissolve(5)
    window show
    su "Скорость хода?"
    st "22 узла!"
    su "Глубина?"
    st "40 метров!"
    su "Продуть балласт! Всплытие 10 дифферент 5!"
    "Заработали насосы, вода из балласта начала покидать лодку под действием сжатого воздуха."
    "Субмарина задрала нос и всплыла на заданную глубину."
    su "Стоп машина! Полная остановка!"
    "Турбины крутят винты в обратную сторону, 150-ти метровая махина постепенно останавливается."
    su "Открыть крышку над ракетными шахтами 1 и 2, открыть люк шахты первой ракеты!"
    stop ambience fadeout 2
    window hide
    play ambience insideKursk fadein 2
    scene torpeda1 with dissolve2
    window show
    torp "Что там с ней?"
    dag "Температура повышена."
    torp "Сильно?"
    dag "За последние 20 минут на 15 градусов."
    torp "Это плохо."
    radio "Экипажу приготовиться к пуску ракеты."
    radio "Пуск через: 3, {w=0.5}2, {w=0.5}1."
    scene black
    show torpeda1 at k_shaking
    play sound rocketFire
    window hide
    stop ambience fadeout 4
    scene black with Dissolve(4)
    jump k_rocket_fire_video

label k_rocket_fire_video:
    $ renpy.movie_cutscene(gFile("video/rocket_fire.webm"))
    jump k_norv_base_video

label k_norv_base_video:
    $ renpy.movie_cutscene(gFile("video/norv_base.webm"))
    jump norv_base

label norv_base:
    $ new_chapter(5, u"Курск: «Оласверн»")
    $ updVisual()
    play ambience inside_norv fadein 5
    scene norv1 with Dissolve(5)
    window show
    com "Driver Russerne øvelser i Barentshavet igjen?{color=#a5a5a5}{vspace=5}{space=20}-{space=20}Русские снова проводят учения в баренцевом море?"
    nrv "Ja, sir.{color=#a5a5a5}{vspace=5}{space=20}-{space=20}Да, сэр."
    com "I hvilken sammensetning denne gangen?{color=#a5a5a5}{vspace=5}{space=20}-{space=20}В каком составе на этот раз?"
    nrv "Hangarstip «Admiral Kuznetsov», cruiser «Peter Den Store», APC «Kursk» Oscar klasse II, flere destroyere.{color=#a5a5a5}{vspace=5}{space=20}-{space=20}Авианесущий крейсер «Адмирал Кузнецов», крейсер «Пётр Великий», АПРК «Курск» класса Oscar II, несколько эсминцев."
    nrv "Totalt - 50 stip og en ubåt.{color=#a5a5a5}{vspace=5}{space=20}-{space=20}Всего - 50 кораблей и одна субмарина."
    com "Oscar II... Typer av våpen?{color=#a5a5a5}{vspace=5}{space=20}-{space=20}Оскар II... Тип вооружения?"
    nrv "24 anti-stip missiler P-700 «Granitt», torpedoer.{color=#a5a5a5}{vspace=5}{space=20}-{space=20}24 противокорабельные ракеты П-700 «Гранит», торпеды."
    com "Vis det på radarene.{color=#a5a5a5}{vspace=5}{space=20}-{space=20}Покажите на радарах."
    nrv "Umulig. Det er usynlig, stille.{color=#a5a5a5}{vspace=5}{space=20}-{space=20}Невозможно. Она невидимая, бесшумная."
    com "Dårlig. Fortsett å se.{color=#a5a5a5}{vspace=5}{space=20}-{space=20}Плохо. Продолжайте наблюдение."
    window hide
    stop ambience fadeout 5
    scene black with Dissolve(5)
    jump aft_rocket_fire

label aft_rocket_fire:
    $ new_chapter(6, u"Курск: Скачок показателей торпеды")
    $ updVisual()
    play ambience insideKursk fadein 4
    scene torpeda1 with Dissolve(4)
    window show
    radio "Пуск успешный."
    torp "Через час распрощаемся с нашим «толстяком»."
    dag "Перекисно-водородные торпеды высокую температуру не любят. Я бы рекомендовал избавиться от неё."
    dag "Бог его знает где она лежала до нас, и что с ней не так."
    torp "Пожалуй, соглашусь с тобой."
    torp "Лучше не рисковать."
    window hide
    stop ambience fadeout 5
    scene black with Dissolve(5)
    jump torp_attention

label torp_attention:
    $ new_chapter(7, u"Курск: Загрузка торпеды")
    $ updVisual()
    play ambience kp_ambience fadein 5
    scene kp with Dissolve(5)
    window show
    su "Погружение до 40 метров с дифферентом на нос 5, взять курс на 130 градусов, установить скорость 25 узлов."
    st "Товарищ капитан, корабельная группа докладывает на берег."
    st "В скором времени будут готовы продолжить."
    su "В течение получаса переходим ко второму этапу учений."
    su "Не забудьте открыть вентиляцию между отсеками, иначе мы все рискуем получить контузию при стрельбе."
    play sound ra_1
    p_radio "Центральный, это первый, соедините с капитаном."
    play sound ra_1
    su "Первый, это центральный, говорит капитан, что у вас?"
    play sound ra_1
    p_radio "Проблемы с «65-76ПВ», показатели скакнули."
    play sound ra_1
    su "Состояние торпеды?"
    play sound ra_1
    p_radio "Торпеда в норме, но давление и температура повышены. Запрашиваю разрешение на аварийный сброс в целях безопасности."
    play sound ra_1
    su "Внутренние показатели в пределах допустимого?"
    play sound ra_1
    p_radio "Так точно."
    play sound ra_1
    su "Аварийный сброс запрещаю. Через пять минуты начинайте погрузку в аппарат."
    play sound ra_1
    p_radio "Слушаюсь."
    window hide 
    stop ambience fadeout 2
    jump torp_boom

label torp_boom:
    $ updVisual
    $ new_chapter(8, u"Курск: Погрузка торпеды")
    play ambience insideKursk fadein 2
    scene torpeda1 with dissolve2
    window show
    dag "Что капитан сказал?"
    torp "Говорит, что пока показатели в норме - продолжаем работать."
    dag "Не с проста она злится."
    dag "Я с такими торпедами работал мало, но на заводе слышал, что их слабое место - резервуары с перекисью водорода."
    torp "Думаешь протечка?"
    dag "Не знаю."
    dag "Это можно понять только заглянув внутрь."
    torp "И зачем их вообще на вооружение поставили? Дешёвые и опасные."
    dag "Время 11:28, пора загружать."
    window hide
    scene torpeda2 with dissolve2
    torp "Торпедный аппарат готов. Начинаем."
    stop ambience fadeout 5
    play sound torp_2
    camera:
        perspective True
        zpos 0
        linear 10.3 ypos -70 xpos 20 zpos -500
    pause (10.3)
    scene black with dissolve 
    camera:
        perspective True
        xpos 0 zpos 0 ypos 0
    scene torpeda1 with dissolve
    play sound_1 clock volume 0.3 fadein 8
    play sound_2 smth_comming volume 0.3
    pause (1)
    window show
    torp "Торпеда в аппарате."
    dag "Надо пополнить резервуар с воздухом."
    torp "Сейчас шланг КСПВ подключу.{color=#a5a5a5}{vspace=10}{space=100}КСПВ{space=10}-{space=10}корабельная система подачи воздуха"
    window hide
    pause (1)
    window show
    torp "С богом!"
    play sound press_button
    window hide
    pause (0.1)
    play sound vacum
    pause (3.0)
    play sound_2 boom_2
    stop sound
    stop sound_1
    stop ambience fadeout 1
    scene black
    show fire_torpeda1
    with dissolve
    play sound_1 boom_1 volume 0.5   
    pause (1)  
    scene black
    show fire_torpeda4 
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
    $ new_chapter(9, u"Курск: Взрыв торпеды")
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
    "Опомнившийся командир седьмого отсека начал действовать согласно установленным правилам."
    mo "{cps=70}{size=+2}Герметезировать отсек!"
    mo "{cps=70}{size=+2}Задраить носовую переборку! Задраить все люки!"
    window hide
    scene turb1 with dissolve2
    window show
    "У моряков-подводников есть определённый набор правил поведения экипажа при не штатных ситуациях."
    "Следующим после герметизации в нём идёт установление связи."
    play sound ra_1
    mo "Центральный, центральный, ответьте седьмому, приём!"
    play sound ra_1
    mo "Повторяю, ответьте седьмому, приём!"
    bk "Почему центральный не отвечает?"
    sk "Потому что они мертвы!"
    mo "Тихо!"
    bk "Почему мы не всплываем?"
    gb "А ты как думаешь?!"
    mo "{cps=70}{size=+2}Тихо я сказал!"
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
    gb "Товарищ командир, в первом отсекe пожар!"
    mo "Найди документацию, какая температура детонации?"
    sk "Торпеды на стелажах взорвутся при 250 градусов."
    mo "Сколько сейчас?"
    gb "270."
    gb "Черт... С каждой секундой растёт!"
    window hide
    scene turb1 with dissolve2
    window show
    bk "Что нам делать?"
    mo "Без паники!"
    mo "Всё как нас учили."
    mo "Герметизируем отсек, задраиваем переборку."
    mo "В случае задымления расчехляем ПДА, покидаем отсек.{color=#a5a5a5}{vspace=10}{space=100}ПДА{space=10}-{space=10}Портативный дыхательный аппарат"
    gb "Температура зашкалила! Сейчас шарахнет!"
    window hide
    pause (3)
    scene black with Dissolve(2)
    jump k_second_explosion_video

label k_second_explosion_video:
    $ renpy.movie_cutscene(gFile("video/second_explosion.webm"))
    jump aft_second_explosion

label aft_second_explosion:
    $ new_chapter(10, u"Курск: Взрыв боезапаса")
    $ updVisual()
    window hide
    play ambience water_coming fadein 5
    play music violence
    play sound sparks_fast
    scene aft_explosion_2 with Dissolve(5)
    window show
    "Мощнейший взрыв заставил прочный корпус лодки ходить ходуном."
    "Через образовавшиеся трещины внутрь начала поступать забортная вода."
    mo "{cps=70}{size=+2}Покинуть отсек! В корму!"
    play sound sparks_fast
    mo "{cps=70}{size=+2}Все в девятый отсек! Все в корму!"
    window hide
    scene aft_explosion_3 with Dissolve(2)
    window show
    play sound ra_1
    mo "Пятый отсек, приём!"
    play sound ra_1
    mo "Пятый отсек ответьте, приём!"
    play sound ra_1
    play sound_1 sparks_fast volume 0.2
    p_radio "Это пятый!"
    play sound ra_1
    mo "Саша, уходите оттуда!"
    play sound ra_1
    mo "Слышишь? Уходите в корму!"
    play sound ra_1
    p_radio "Коля, мы не можем уйти!"
    play sound ra_1
    play sound_1 sparks_fast volume 0.2
    p_radio "Компенсирующие решётки опустились не до конца! Нам придётя опускать их вручную!"
    play sound ra_1
    mo "Саша..."
    play sound ra_1
    p_radio "Коля, спасайся, мы справимся."
    play sound ra_1
    p_radio "Прощай..."
    play sound ra_1
    mo "Прощай."
    window hide
    scene black with dissolve2
    scene aft_explosion_5 with dissolve2
    window show
    mo "Ещё кто-нибудь есть?"
    mat "Я последний!"
    mo "Бегом в девятый отсек!"
    mo "Вперёд, вперёд, вперёд, уходим!"
    window hide
    scene black with dissolve2
    play ambience section_9 fadein 5
    scene otsek_9 with dissolve2
    window show
    bk "Что произошло? Почему мы здесь?"
    gb "На носу что-то взорвалось, мы выжили только потому что мы в корме."
    bk "Что нам делать?"
    gb "Откроем люк и свалим отсюда."
    mo "Нет! Мы не знаем на какой глубине находимся."
    mo "Если мы выйдем - умрём от компрессионной болезни."
    sk "И что тогда делать? Ждать пока нас вытащят отсюда?"
    mo "Да, будет ждать, других вариантов нет."
    sk "Как они поймут где мы находимся?"
    mo "Артур, найди молоток, нужно дать сигнал чтобы нас нашли."
    gb "Сейчас."
    mo "Федь, проверь насосы, воды по колено."
    bk "Понял."
    window hide
    stop music fadeout 5
    scene black with dissolve
    scene stuk with dissolve
    window show
    gb "Два раза по 4 удара, каждый час в начале часа."
    mo "Четыре удара, затем ещё четыре."
    gb "Да."
    window hide
    scene black with dissolve
    window show
    gb "3, {w=0.5}2, {w=0.5}1."
    window hide
    play sound bump
    play ambience under_water fadein 5
    pause (5)
    show kursk7 with Dissolve(4.5):
        pos (0, 0)
        linear 20.0 pos (-1580,0)
    pause(2)
    play sound bump_under_water
    pause(8)
    stop ambience fadeout 5
    scene black with Dissolve(4.5)
    jump norv_attention_video

label norv_attention_video:
    $ renpy.movie_cutscene(gFile("video/norv_base.webm"))
    jump norv_attention

label norv_attention:
    $ new_chapter(11, u"Курск: Сейсмические явления")
    $ updVisual()
    play ambience inside_norv fadein 5
    scene norv1 with Dissolve(5)
    window show
    com "Hva er det der?{color=#a5a5a5}{vspace=5}{space=20}-{space=20}Что там?"
    nrv "Russiske ødeleggere cruise på et torg, resten av skipene går i sirkler med liten radius.{color=#a5a5a5}{vspace=5}{space=20}-{space=20}Русские эсминцы курсируют в квадрате, остальные корабли ходят кругами небольшого радиуса."
    nrv "Seismiske fenomener observeres i området.{color=#a5a5a5}{vspace=5}{space=20}-{space=20}В районе наблюдаются сейсмические явления."
    com "Seismikk? Mer detaljert.{color=#a5a5a5}{vspace=5}{space=20}-{space=20}Сейсмические? Поподробнее."
    nrv "Ett lite trykk, ett større.{color=#a5a5a5}{vspace=5}{space=20}-{space=20}Один маленький толчок, один крупнее."
    nrv "3,9 på Richters skala.{color=#a5a5a5}{vspace=5}{space=20}-{space=20}3,9 баллов по шкале Рихтера."
    nrv "Klokka 11:28 med en forskjell på to minutter.{color=#a5a5a5}{vspace=5}{space=20}-{space=20}В 11:28 с разницей в две минуты."
    window hide
    scene norv3 with dissolve2
    window show
    com "Herre... De har mistet ubåten!{color=#a5a5a5}{vspace=5}{space=20}-{space=20}Господи... Они потеряли подлодку!"
    com "David, seismologers data om Barentshavet.{color=#a5a5a5}{vspace=5}{space=20}-{space=20}Дэвид, данные сейсмологов по Баренцеву морю."
    nrv "Ja, sir.{color=#a5a5a5}{vspace=5}{space=20}-{space=20}Есть сэр."
    com "Be Amerikanerne om å omdirigere kommunikasjonssatellitten til havnene I Murmansk.{color=#a5a5a5}{vspace=5}{space=20}-{space=20}Попросите американцев перенаправить спутник связи на порты Мурманска."
    




    