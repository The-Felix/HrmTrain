
    
###################REQUEST_23 (Level 06) (55 pt.) (Give handjob to a classmate). (Available during daytime only).#####################################################################################
label new_request_23: #LV.6 (Whoring = 15 - 17)
    
    $ current_payout = 55 #Used when haggling about price of the favour.
    
    #__#hide screen hermione_main 
    #__#with d3
    $herView.hideQQ()
    m "{size=-4}(Приказать ей передернуть одному из своих одноклассников?){/size}"
    $ menu_x = 0.5 #Default position of the menu (0.5). Version B is $ menu_x = 0.2
    menu:
        "\"(Да, давай сделаем это!)\"":
            pass
        "\"(Не сейчас.)\"":
            jump new_personal_request
            
    
    $ pos = POS_140
    
    if request_23_points == 0: # <================================================================================ FIRST TIME
        if whoring <=14 or request_20_points <= 1: # Counts how many times you sent Hermione to kiss a girl.
            m "Мисс Грейнджер, я хочу, чтобы сегодня вы сделали кое-что новенькое..."
            #__#hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            #__#with d3                                                                                                                                                                                                                        #HERMIONE
            $herView.hideQQ()
            #__#$ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                       #HERMIONE
            #__#$ h_body = "03_hp/13_hermione_main/body_07.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            #__#show screen hermione_main                                                                                                                                                                                 #HERMIONE
            #__#with d3                                                                                                                                                                                                                        #HERMIONE
            $herView.showQQ( "body_07.png", pos )
            her "...?"
            m "Я хочу, чтобы вы подрочили своему однокласснику."
            jump too_much
        m "Мисс Грейнджер, я хочу, чтобы сегодня вы сделали кое-что новенькое..."
        #__#hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        #__#with d3                                                                                                                                                                                                                        #HERMIONE
        $herView.hideQQ()
        #__#$ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                       #HERMIONE
        #__#$ h_body = "03_hp/13_hermione_main/body_15.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        #__#show screen hermione_main                                                                                                                                                                                 #HERMIONE
        #__#with d3                                                                                                                                                                                                                        #HERMIONE
        $herView.showQQ( "body_15.png", pos )
        her "..........."
        m "Я хочу, чтобы вы вышли отсюда и занялись сексом с одним из своих одноклассников."
        stop music
        #__#hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        #__#with d3                                                                                                                                                                                                                        #HERMIONE
        $herView.hideQQ()
        #__#$ h_body = "03_hp/13_hermione_main/body_48.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        #__#show screen hermione_main                                                                                                                                                                                 #HERMIONE
        #__#with d3                     
        $herView.showQQ( "body_48.png", pos )
        with hpunch                                                                                                                                                                                                               #HERMIONE
        her "{size=+5}Что?!!{/size}"
        #__#hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        #__#with d3                                                                                                                                                                                                                        #HERMIONE
        $herView.hideQQ()
        #__#$ h_body = "03_hp/13_hermione_main/body_47.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        #__#show screen hermione_main                                                                                                                                                                                 #HERMIONE
        #__#with d3                                                                                                                                                                                                                        #HERMIONE
        $herView.showQQ( "body_47.png", pos )
        play music "music/Chipper Doodle v2.mp3" fadein 1 fadeout 1 # HERMIONE'S THEME.
        her "Вот теперь все, сэр! Вы пересекли линию!"
        her "Я знаю что я продала вам парочку достаточно необычных услуг в прошлом..."
        #__#hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        #__#with d3                                                                                                                                                                                                                        #HERMIONE
        $herView.hideQQ()
        #__#$ h_body = "03_hp/13_hermione_main/body_86.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        #__#show screen hermione_main                                                                                                                                                                                 #HERMIONE
        #__#with d3                                                                                                                                                                                                                        #HERMIONE
        $herView.showQQ( "body_86.png", pos )
        with vpunch
        her "{size=+5}Но ЭТО?!{/size}"
        her "Я не могу поверить, что вы сказали одной из своих учениц за... за..."
        #__#hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        #__#with d3                                                                                                                                                                                                                        #HERMIONE
        $herView.hideQQ()
        #__#$ h_body = "03_hp/13_hermione_main/body_76.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        #__#show screen hermione_main                                                                                                                                                                                 #HERMIONE
        #__#with d3                                                                                                                                                                                                                        #HERMIONE
        $herView.showQQ( "body_76.png", pos )
        her "Все кончено, сэр!"
        m "Хорошо, хорошо, успокойся, ладно?"
        #__#hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        #__#with d3                                                                                                                                                                                                                        #HERMIONE
        $herView.hideQQ()
        #__#$ h_body = "03_hp/13_hermione_main/body_30.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        #__#show screen hermione_main                                                                                                                                                                                 #HERMIONE
        #__#with d3                                                                                                                                                                                                                        #HERMIONE
        $herView.showQQ( "body_30.png", pos )
        her "Я определенно не успокоюсь сэр! Это за гранью неприемлимого!"
        m "Хорошо, ладно, может, я и впрямь немного переступил черту в этот раз..."
        #__#hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        #__#with d3                                                                                                                                                                                                                        #HERMIONE
        $herView.hideQQ()
        #__#$ h_body = "03_hp/13_hermione_main/body_47.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        #__#show screen hermione_main                                                                                                                                                                                 #HERMIONE
        #__#with d3                                                                                                                                                                                                                        #HERMIONE
        $herView.showQQ( "body_47.png", pos )
        her "Немного, сэр?! Немного!!?"
        m "Да, я извиняюсь..."
        #__#hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        #__#with d3                                                                                                                                                                                                                        #HERMIONE
        $herView.hideQQ()
        #__#$ h_body = "03_hp/13_hermione_main/body_79.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        #__#show screen hermione_main                                                                                                                                                                                 #HERMIONE
        #__#with d3                                                                                                                                                                                                                        #HERMIONE
        $herView.showQQ( "body_79.png", pos )
        her "........."
        m "Давайте мы вместо этого попробуем что-нибудь менее... увлекательное?"
        #__#hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        #__#with d3                                                                                                                                                                                                                        #HERMIONE
        $herView.hideQQ()
        #__#$ h_body = "03_hp/13_hermione_main/body_120.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        #__#show screen hermione_main                                                                                                                                                                                 #HERMIONE
        #__#with d3                                                                                                                                                                                                                        #HERMIONE
        $herView.showQQ( "body_120.png", pos )
        her "............"
        m "Я подарю \"Грифиндору\" пятьдесят пять очков."
        m "Все, что я попрошу взамен..."
        #__#hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        #__#with d3                                                                                                                                                                                                                        #HERMIONE
        $herView.hideQQ()
        #__#$ h_body = "03_hp/13_hermione_main/body_187.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        #__#show screen hermione_main                                                                                                                                                                                 #HERMIONE
        #__#with d3                                                                                                                                                                                                                        #HERMIONE
        $herView.showQQ( "body_187.png", pos )
        her "..........?"
        m "...так это выйти и подрочить какому-нибудь счастливцу..."
        #__#hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        #__#with d3                                                                                                                                                                                                                        #HERMIONE
        $herView.hideQQ()
        #__#$ h_body = "03_hp/13_hermione_main/body_47.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        #__#show screen hermione_main                                                                                                                                                                                 #HERMIONE
        #__#with d3                                                                                                                                                                                                                        #HERMIONE
        $herView.showQQ( "body_47.png", pos )
        her "!!!......"
        m "Ой, да брось... Всего лишь разок невинно замарать ручки."
        #__#hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        #__#with d3                                                                                                                                                                                                                        #HERMIONE
        $herView.hideQQ()
        #__#$ h_body = "03_hp/13_hermione_main/body_66.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        #__#show screen hermione_main                                                                                                                                                                                 #HERMIONE
        #__#with d3                                                                                                                                                                                                                        #HERMIONE
        $herView.showQQ( "body_66.png", pos )
        her "..."
        m "Пятьдесят пять очков..."
        #__#hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        #__#with d3                                                                                                                                                                                                                        #HERMIONE
        $herView.hideQQ()
        #__#$ h_body = "03_hp/13_hermione_main/body_69.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        #__#show screen hermione_main                                                                                                                                                                                 #HERMIONE
        #__#with d3                                                                                                                                                                                                                        #HERMIONE
        $herView.showQQ( "body_69.png", pos )
        her ".............."
        #__#hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        #__#with d3                                                                                                                                                                                                                        #HERMIONE
        $herView.hideQQ()
        #__#$ h_body = "03_hp/13_hermione_main/body_79.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        #__#show screen hermione_main                                                                                                                                                                                 #HERMIONE
        #__#with d3                                                                                                                                                                                                                        #HERMIONE
        $herView.showQQ( "body_79.png", pos )
        her "Я рада, что вы пришли в чувство, сэр."
        m "Ох, конечно. Спасибо за заботу."
        m "Это значит, что вы согласны?"
        #__#hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        #__#with d3                                                                                                                                                                                                                        #HERMIONE
        $herView.hideQQ()
        #__#$ h_body = "03_hp/13_hermione_main/body_69.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        #__#show screen hermione_main                                                                                                                                                                                 #HERMIONE
        #__#with d3                                                                                                                                                                                                                        #HERMIONE
        $herView.showQQ( "body_69.png", pos )
        her "Я попробую..."
        m "Отлично... Тогда увидимся вечером."

    else: # <================================================================================ NOT FIRST TIME
        if whoring >= 15 and whoring <= 17: # LEVEL 06 FIRST EVENT.
            m "Сегодняшней услугой будет..."
            #__#hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            #__#with d3                                                                                                                                                                                                                        #HERMIONE
            $herView.hideQQ()
            #__#$ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                       #HERMIONE
            #__#$ h_body = "03_hp/13_hermione_main/body_117.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            #__#show screen hermione_main                                                                                                                                                                                 #HERMIONE
            #__#with d3                                                                                                                                                                                                                        #HERMIONE
            $herView.showQQ( "body_117.png", pos )
            her "........."
            m "Ублажение рукой любого парня! На твой выбор!"
            #__#hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            #__#with d3                                                                                                                                                                                                                        #HERMIONE
            $herView.hideQQ()
            #__#$ h_body = "03_hp/13_hermione_main/body_118.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            #__#show screen hermione_main                                                                                                                                                                                 #HERMIONE
            #__#with d3                                                                                                                                                                                                                        #HERMIONE
            $herView.showQQ( "body_118.png", pos )
            her "...опять?"
            m "Конечно, почему нет?"
            m "И, конечно же, еще пятьдесят пять очков \"Гриффиндору\"."
            #__#hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            #__#with d3                                                                                                                                                                                                                        #HERMIONE
            $herView.hideQQ()
            #__#$ h_body = "03_hp/13_hermione_main/body_29.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            #__#show screen hermione_main                                                                                                                                                                                 #HERMIONE
            #__#with d3                                                                                                                                                                                                                        #HERMIONE
            $herView.showQQ( "body_29.png", pos )
            her ".........."
            m "Итак... Вы согласны, сударыня?"
            #__#hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            #__#with d3                                                                                                                                                                                                                        #HERMIONE
            $herView.hideQQ()
            #__#$ h_body = "03_hp/13_hermione_main/body_69.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            #__#show screen hermione_main                                                                                                                                                                                 #HERMIONE
            #__#with d3                                                                                                                                                                                                                        #HERMIONE
            $herView.showQQ( "body_69.png", pos )
            her "Я посмотрю, что я могу сделать..."
            m "Шикарно!"
        
        elif whoring >= 18 and whoring <= 20: # LEVEL 07
            m "Еще не готова к сексу с одноклассником?"
            #__#hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            #__#with d3                                                                                                                                                                                                                        #HERMIONE
            $herView.hideQQ()
            #__#$ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                       #HERMIONE
            #__#$ h_body = "03_hp/13_hermione_main/body_72.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            #__#show screen hermione_main                                                                                                                                                                                 #HERMIONE
            #__#with d3                                                                                                                                                                                                                        #HERMIONE
            $herView.showQQ( "body_72.png", pos )
            stop music fadeout 1.0
            her "Что?"
            #__#hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            #__#with d3                                                                                                                                                                                                                        #HERMIONE
            $herView.hideQQ()
            #__#$ h_body = "03_hp/13_hermione_main/body_30.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            #__#show screen hermione_main                                                                                                                                                                                 #HERMIONE
            #__#with d3                                                                                                                                                                                                                        #HERMIONE
            $herView.showQQ( "body_30.png", pos )
            her "Конечно нет! Я никогда--"
            m "Тогда как насчет кому-нибудь передернуть?"
            #__#hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            #__#with d3                                                                                                                                                                                                                        #HERMIONE
            $herView.hideQQ()
            #__#$ h_body = "03_hp/13_hermione_main/body_69.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            #__#show screen hermione_main                                                                                                                                                                                 #HERMIONE
            #__#with d3                                                                                                                                                                                                                        #HERMIONE
            $herView.showQQ( "body_69.png", pos )
            her "..............."
            m "Да ладно тебе. Ты делала это раньше."
            #__#hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            #__#with d3                                                                                                                                                                                                                        #HERMIONE
            $herView.hideQQ()
            #__#$ h_body = "03_hp/13_hermione_main/body_79.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            #__#show screen hermione_main                                                                                                                                                                                 #HERMIONE
            #__#with d3                                                                                                                                                                                                                        #HERMIONE
            $herView.showQQ( "body_79.png", pos )
            her "Хм.........."
            her "Пятьдесят пять очков?"
            m "Естественно."
            #__#hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            #__#with d3                                                                                                                                                                                                                        #HERMIONE
            $herView.hideQQ()
            #__#$ h_body = "03_hp/13_hermione_main/body_118.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            #__#show screen hermione_main                                                                                                                                                                                 #HERMIONE
            #__#with d3                                                                                                                                                                                                                        #HERMIONE
            $herView.showQQ( "body_118.png", pos )
            her "Ну ладно... Я посмотрю, что я смогу сделать..."

        elif whoring >= 21: # LEVEL 08+
            play music "music/Chipper Doodle v2.mp3" fadein 1 fadeout 1 # HERMIONE'S THEME.
            m "Мисс Грейнджер..."
            m "Что вы думаете о том, чтобы подарить очередному однокласснику оргазм с помощью ваших ручек?"
            #__#hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            #__#with d3                                                                                                                                                                                                                        #HERMIONE
            $herView.hideQQ()
            #__#$ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                       #HERMIONE
            #__#$ h_body = "03_hp/13_hermione_main/body_71.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            #__#show screen hermione_main                                                                                                                                                                                 #HERMIONE
            #__#with d3                                                                                                                                                                                                                        #HERMIONE
            $herView.showQQ( "body_71.png", pos )
            her "Я не возражаю, сэр."
            m "Серьезно?"
            #__#hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            #__#with d3                                                                                                                                                                                                                        #HERMIONE
            $herView.hideQQ()
            #__#$ h_body = "03_hp/13_hermione_main/body_68.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            #__#show screen hermione_main                                                                                                                                                                                 #HERMIONE
            #__#with d3                                                                                                                                                                                                                        #HERMIONE
            $herView.showQQ( "body_68.png", pos )
            her "Да... В смысле, я же всего лишь передерну..."
            m "Отлично. Тогда идите и повеселитесь!"
            m "И приходите после уроков с отчетом, как обычно."
            #__#hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            #__#with d3                                                                                                                                                                                                                        #HERMIONE
            $herView.hideQQ()
            #__#$ h_body = "03_hp/13_hermione_main/body_74.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            #__#show screen hermione_main                                                                                                                                                                                 #HERMIONE
            #__#with d3                                                                                                                                                                                                                        #HERMIONE
            $herView.showQQ( "body_74.png", pos )
            her "Конечно, сэр."
    
    
    

    
    $ request_23 = True

    hide screen bld1
    #__#hide screen hermione_main
    $herView.hideQ() #"WARNING_Z"
    hide screen blktone 
    hide screen hermione_02
    hide screen ctc
    with d3

    $ walk_xpos=400 #Animation of walking chibi. (From)
    $ walk_xpos2=610 #Coordinates of it's movement. (To)
    $ hermione_speed = 02.0 #The speed of moving the walking animation across the screen.
    show screen hermione_walk_01_f 
    pause 2
    hide screen hermione_walk_01_f 
    $ renpy.play('sounds/door.mp3') #Sound of a door opening.
    with Dissolve(.3)

    call music_block
    
    $ hermione_takes_classes = True
    jump day_main_menu
    


label new_request_23_complete: # <=================================================================================================== EVENING
    
    $ walk_xpos=520 #Animation of walking chibi. (From)
    $ walk_xpos2=400 #Coordinates of it's movement. (To)
    $ hermione_speed = 02.0 #The speed of moving the walking animation across the screen.
    $ renpy.play('sounds/door.mp3') #Sound of a door opening.
    show screen hermione_walk_01 
    with d4
    pause 1.7 
    $ hermione_chibi_xpos = 400 #Near the desk.
    show screen hermione_02 #Hermione stands still.
    pause.5
    show screen bld1
    with Dissolve(.3)

    $ pos = POS_370
    $ herView.data().saveState()

    if whoring >= 15 and whoring <= 17: # LEVEL 06                    
        if one_out_of_three == 1: ### EVENT (A)
            m "Мисс Грейнджер, как все прошло?"
            show screen blktone
            with d3
            #__#hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            #__#with d3                                                                                                                                                                                                                        #HERMIONE
            $herView.hideQQ()
            #__#$ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                       #HERMIONE
            #__#$ h_body = "03_hp/13_hermione_main/body_09.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            #__#show screen hermione_main                                                                                                                                                                                 #HERMIONE
            #__#with d3                                                                                                                                                                                                                        #HERMIONE
            $herView.showQQ( "body_09.png", pos )
            play music "music/Chipper Doodle v2.mp3" fadein 1 fadeout 1 # HERMIONE'S THEME.
            her "Конечно же... ужасно..."
            m "Просто расскажи мне, что произошло, девочка..."
            #__#hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            #__#with d3                                                                                                                                                                                                                        #HERMIONE
            $herView.hideQQ()
            #__#$ h_body = "03_hp/13_hermione_main/body_66.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            #__#show screen hermione_main                                                                                                                                                                                 #HERMIONE
            #__#with d3                                                                                                                                                                                                                        #HERMIONE
            $herView.showQQ( "body_66.png", pos )
            her "Я выставила себя полной дурой, сэр - вот что произошло."
            her "....."
            m "..."
            #__#hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            #__#with d3                                                                                                                                                                                                                        #HERMIONE
            $herView.hideQQ()
            #__#$ h_body = "03_hp/13_hermione_main/body_29.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            #__#show screen hermione_main                                                                                                                                                                                 #HERMIONE
            #__#with d3                                                                                                                                                                                                                        #HERMIONE
            $herView.showQQ( "body_29.png", pos )
            her ".........."
            #__#hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            #__#with d3                                                                                                                                                                                                                        #HERMIONE
            $herView.hideQQ()
            #__#$ h_body = "03_hp/13_hermione_main/body_69.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            #__#show screen hermione_main                                                                                                                                                                                 #HERMIONE
            #__#with d3                                                                                                                                                                                                                        #HERMIONE
            $herView.showQQ( "body_69.png", pos )
            her "Я не хочу говорить об этом..."
            her "Вы сказали мне пойти и потрогать мужской член и я сделала именно это, профессор."
            #__#hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            #__#with d3                                                                                                                                                                                                                        #HERMIONE
            $herView.hideQQ()

            #__#$ h_body = "03_hp/13_hermione_main/body_31.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            #__#show screen hermione_main                                                                                                                                                                                 #HERMIONE
            #__#with d3                                                                                                                                                                                                                        #HERMIONE
            $herView.showQQ( "body_31.png", pos )
            her "Пожалуйста, просто отдайте мне мои очки, сэр..."
            m "Я не говорил вам \"идите и трогайте мужской член\", сударыня."
            m "Я сказал вам идти и хорошо подрочить вашему однокласснику."
            #__#hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            #__#with d3                                                                                                                                                                                                                        #HERMIONE
            $herView.hideQQ()
            #__#$ h_body = "03_hp/13_hermione_main/body_79.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            #__#show screen hermione_main                                                                                                                                                                                 #HERMIONE
            #__#with d3                                                                                                                                                                                                                        #HERMIONE
            $herView.showQQ( "body_79.png", pos )
            her "Ну, да... конечно же я это и имела в виду..."
            m "Раз так, то вы заставили его кончить?"
            #__#hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            #__#with d3                                                                                                                                                                                                                        #HERMIONE
            $herView.hideQQ()
            #__#$ h_body = "03_hp/13_hermione_main/body_31.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            #__#show screen hermione_main                                                                                                                                                                                 #HERMIONE
            #__#with d3                                                                                                                                                                                                                        #HERMIONE
            $herView.showQQ( "body_31.png", pos )
            her "Сэр?"
            m "Его \"пи-пи\" стрельнула в тебя белой штукой?"
            #__#hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            #__#with d3                                                                                                                                                                                                                        #HERMIONE
            $herView.hideQQ()
            #__#$ h_body = "03_hp/13_hermione_main/body_29.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            #__#show screen hermione_main                                                                                                                                                                                 #HERMIONE
            #__#with d3                                                                                                                                                                                                                        #HERMIONE
            $herView.showQQ( "body_29.png", pos )
            her "Ну..."
            #__#hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            #__#with d3                                                                                                                                                                                                                        #HERMIONE
            $herView.hideQQ()
            #__#$ h_body = "03_hp/13_hermione_main/body_33.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            #__#show screen hermione_main                                                                                                                                                                                 #HERMIONE
            #__#with d3                                                                                                                                                                                                                        #HERMIONE
            $herView.showQQ( "body_33.png", pos )
            her "Нет, не стрельнула..."
            menu: 
                "\"Ну, тогда это не считается.\"":
                    stop music fadeout 4.0
                    #__#hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                    #__#with d3                                                                                                                                                                                                                        #HERMIONE
                    $herView.hideQQ()
                    #__#$ h_body = "03_hp/13_hermione_main/body_119.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
                    #__#show screen hermione_main                                                                                                                                                                                 #HERMIONE
                    #__#with d3                                                                                                                                                                                                                        #HERMIONE
                    $herView.showQQ( "body_119.png", pos )
                    her "Что?"
                    her "Но сэр, я..."
                    m "Если ты не заставила его кончить, значит это нельзя назвать хорошей дрочкой. Конец."
                    #__#hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                    #__#with d3                                                                                                                                                                                                                        #HERMIONE
                    $herView.hideQQ()
                    #__#$ h_body = "03_hp/13_hermione_main/body_117.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
                    #__#show screen hermione_main                                                                                                                                                                                 #HERMIONE
                    #__#with d3                                                                                                                                                                                                                        #HERMIONE
                    $herView.showQQ( "body_117.png", pos )
                    her "Но... Тогда что это было...?"
                    m "Откуда мне знать? Массаж члена?"
                    #__#hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                    #__#with d3                                                                                                                                                                                                                        #HERMIONE
                    $herView.hideQQ()

                    $ pos = POS_140
                    #__#$ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                       #HERMIONE
                    #__#$ h_body = "03_hp/13_hermione_main/body_118.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
                    #__#show screen hermione_main                                                                                                                                                                                 #HERMIONE
                    #__#with d3                                                                                                                                                                                                                        #HERMIONE
                    $herView.showQQ( "body_118.png", pos )
                    her "Оууу..."
                    her "Но я правда старалась..."
                    m "Нет дрочки - нет баллов, мисс Грейнджер."
                    #__#hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                    #__#with d3                                                                                                                                                                                                                        #HERMIONE
                    $herView.hideQQ()
                    #__#$ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                       #HERMIONE
                    #__#$ h_body = "03_hp/13_hermione_main/body_117.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
                    #__#show screen hermione_main                                                                                                                                                                                 #HERMIONE
                    #__#with d3                                                                                                                                                                                                                        #HERMIONE
                    $herView.showQQ( "body_117.png", pos )
                    her "....."
                    m "Вы свободны."
                    #__#hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                    #__#with d3                                                                                                                                                                                                                        #HERMIONE
                    $herView.hideQQ()
                    #__#$ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                       #HERMIONE
                    #__#$ h_body = "03_hp/13_hermione_main/body_69.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
                    #__#show screen hermione_main                                                                                                                                                                                 #HERMIONE
                    #__#with d3                                                                                                                                                                                                                        #HERMIONE
                    $herView.showQQ( "body_69.png", pos )
                    her "........."
                    $ mad +=9
                    $ request_23_points += 1 
                    $ request_23 = False 
                    $ hermione_sleeping = True
                    jump could_not_flirt #Sent here when choose "Favor failed! No points for you!" (Hermione is leaving without getting any points).
                "\"Тогда ты получишь только половину платы.\"":
                    $ current_payout = 27 #Used when haggling about price of th favour.
                    #__#hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                    #__#with d3                                                                                                                                                                                                                        #HERMIONE
                    $herView.hideQQ()
                    #__#$ h_body = "03_hp/13_hermione_main/body_31.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
                    #__#show screen hermione_main                                                                                                                                                                                 #HERMIONE
                    #__#with d3                                                                                                                                                                                                                        #HERMIONE
                    $herView.showQQ( "body_31.png", pos )
                    her "Ох...?"
                    m "Это проблема, мисс Грейнджер?"
                    #__#hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                    #__#with d3                                                                                                                                                                                                                        #HERMIONE
                    $herView.hideQQ()
                    #__#$ h_body = "03_hp/13_hermione_main/body_118.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
                    #__#show screen hermione_main                                                                                                                                                                                 #HERMIONE
                    #__#with d3                                                                                                                                                                                                                        #HERMIONE
                    $herView.showQQ( "body_118.png", pos )
                    her "Нет, сэр... Я думаю, что это честно..."
                    m "Конечно честно!"
                "\"Ну, ты попыталась. Вот очки.\"":
                    #__#hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                    #__#with d3                                                                                                                                                                                                                        #HERMIONE
                    $herView.hideQQ()
                    #__#$ h_body = "03_hp/13_hermione_main/body_117.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
                    #__#show screen hermione_main                                                                                                                                                                                 #HERMIONE
                    #__#with d3                                                                                                                                                                                                                        #HERMIONE
                    $herView.showQQ( "body_117.png", pos )
                    her "Правда?"
                    #__#hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                    #__#with d3                                                                                                                                                                                                                        #HERMIONE
                    $herView.hideQQ()
                    #__#$ h_body = "03_hp/13_hermione_main/body_87.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
                    #__#show screen hermione_main                                                                                                                                                                                 #HERMIONE
                    #__#with d3                                                                                                                                                                                                                        #HERMIONE
                    $herView.showQQ( "body_87.png", pos )
                    her "Спасибо, сэр!"
                    #__#hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                    #__#with d3                                                                                                                                                                                                                        #HERMIONE
                    $herView.hideQQ()
                    #__#$ h_body = "03_hp/13_hermione_main/body_45.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
                    #__#show screen hermione_main                                                                                                                                                                                 #HERMIONE
                    #__#with d3                                                                                                                                                                                                                        #HERMIONE
                    $herView.showQQ( "body_45.png", pos )
                    her "Обещаю, в следующий раз я буду больше стараться!"
                    #__#hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                    #__#with d3                                                                                                                                                                                                                        #HERMIONE
                    $herView.hideQQ()
                    #__#$ h_body = "03_hp/13_hermione_main/body_44.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
                    #__#show screen hermione_main                                                                                                                                                                                 #HERMIONE
                    #__#with d3                                                                                                                                                                                                                        #HERMIONE
                    $herView.showQQ( "body_44.png", pos )
                    her "Эм... В смысле, если в будущем вы дадите похожее задание..."

        elif one_out_of_three == 2: ### EVENT (B)
            m "Мисс Грейнджер, как все прошло?"
            show screen blktone
            with d3
            #__#hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            #__#with d3                                                                                                                                                                                                                        #HERMIONE
            $herView.hideQQ()
            #__#$ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                       #HERMIONE
            #__#$ h_body = "03_hp/13_hermione_main/body_31.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            #__#show screen hermione_main                                                                                                                                                                                 #HERMIONE
            #__#with d3                                                                                                                                                                                                                        #HERMIONE
            $herView.showQQ( "body_31.png", pos )
            her "Все прошло хорошо, сэр..."
            play music "music/(Orchestral) Playful Tension by Shadow16nh.mp3" fadein 1 fadeout 1 # SEX THEME.
            her "Я попросила одного из \"Гриффиндорских\" парней дать мне сделать ему \"это\"..."
            #__#hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            #__#with d3                                                                                                                                                                                                                        #HERMIONE
            $herView.hideQQ()
            #__#$ h_body = "03_hp/13_hermione_main/body_183.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            #__#show screen hermione_main                                                                                                                                                                                 #HERMIONE
            #__#with d3                                                                                                                                                                                                                        #HERMIONE
            $herView.showQQ( "body_183.png", pos )
            her "К моему удивлению, он с радостью согласился."
            m "Поразительно..."
            #__#hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            #__#with d3                                                                                                                                                                                                                        #HERMIONE
            $herView.hideQQ()
            #__#$ h_body = "03_hp/13_hermione_main/body_127.png" #Sprite of Hermione's upper body.                                                                  #HERMIONE
            #__#show screen hermione_main                                                                                                                                                                                 #HERMIONE
            #__#with d3                                                                                                                                                                                                                        #HERMIONE
            $herView.showQQ( "body_127.png", pos )
            her "Ну, мы спрятались за одним из тех огромных гобеленов в восточном крыле..."
            #__#hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            #__#with d3                                                                                                                                                                                                                        #HERMIONE
            $herView.hideQQ()
            #__#$ h_body = "03_hp/13_hermione_main/body_69.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            #__#show screen hermione_main                                                                                                                                                                                 #HERMIONE
            #__#with d3                                                                                                                                                                                                                        #HERMIONE
            $herView.showQQ( "body_69.png", pos )
            her "И я... подрочила ему, пока он не кончил..."
            her "........."
            #__#hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            #__#with d3                                                                                                                                                                                                                        #HERMIONE
            $herView.hideQQ()
            #__#$ h_body = "03_hp/13_hermione_main/body_117.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            #__#show screen hermione_main                                                                                                                                                                                 #HERMIONE
            #__#with d3                                                                                                                                                                                                                        #HERMIONE
            $herView.showQQ( "body_117.png", pos )
            her "И я попросила держать все это в секрете, но..."
            m "Что такое, барышня?"
            m "Сомневаетесь в честности вашего \"Гриффиндорского\" товарища?"
            #__#hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            #__#with d3                                                                                                                                                                                                                        #HERMIONE
            $herView.hideQQ()
            #__#$ h_body = "03_hp/13_hermione_main/body_120.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            #__#show screen hermione_main                                                                                                                                                                                 #HERMIONE
            #__#with d3                                                                                                                                                                                                                        #HERMIONE
            $herView.showQQ( "body_120.png", pos )
            her "Конечно нет, сэр."
            #__#hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            #__#with d3                                                                                                                                                                                                                        #HERMIONE
            $herView.hideQQ()
            #__#$ h_body = "03_hp/13_hermione_main/body_118.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            #__#show screen hermione_main                                                                                                                                                                                 #HERMIONE
            #__#with d3                                                                                                                                                                                                                        #HERMIONE
            $herView.showQQ( "body_118.png", pos )
            her "..........................."
            #__#hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            #__#with d3                                                                                                                                                                                                                        #HERMIONE
            $herView.hideQQ()
            #__#$ h_body = "03_hp/13_hermione_main/body_117.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            #__#show screen hermione_main                                                                                                                                                                                 #HERMIONE
            #__#with d3                                                                                                                                                                                                                        #HERMIONE
            $herView.showQQ( "body_117.png", pos )
            her "Однако... Выполнение такого рода заданий может по-настоящему навредить моей репутации..."
            m "Вы так просите надбавки, сударыня?"
            m "Пятьдесят пять очков - это все, что я могу дать вам за это."
            #__#hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            #__#with d3                                                                                                                                                                                                                        #HERMIONE
            $herView.hideQQ()
            #__#$ h_body = "03_hp/13_hermione_main/body_118.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            #__#show screen hermione_main                                                                                                                                                                                 #HERMIONE
            #__#with d3                                                                                                                                                                                                                        #HERMIONE
            $herView.showQQ( "body_118.png", pos )
            her "Ох... конечно..."
            m "Конечно, если вы не передумали насчет секса с одним из одноклассников?"
            #__#hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            #__#with d3                                                                                                                                                                                                                        #HERMIONE
            $herView.hideQQ()
            #__#$ h_body = "03_hp/13_hermione_main/body_48.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            #__#show screen hermione_main                                                                                                                                                                                 #HERMIONE
            #__#with d3                                                                                                                                                                                                                        #HERMIONE
            $herView.showQQ( "body_48.png", pos )
            her "Что?"
            #__#hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            #__#with d3                                                                                                                                                                                                                        #HERMIONE
            $herView.hideQQ()
            #__#$ h_body = "03_hp/13_hermione_main/body_118.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            #__#show screen hermione_main                                                                                                                                                                                 #HERMIONE
            #__#with d3                                                                                                                                                                                                                        #HERMIONE
            $herView.showQQ( "body_118.png", pos )
            her "Сэр, я не проститутка!"
            m "Что ж, в таком случае..."
            
        elif one_out_of_three == 3: ### EVENT (C) Event level: 01.
            # HERMIONE HAVE A CUM-STAIN ON HER SHOULDER.
            m "Мисс Грейнджер, как все прошло?"
            #__#$ aftersperm = True #Shows stains on Hermione's uniform.
            #__#$ uni_sperm = True  #Universal sperm.
            #__#$ u_sperm = "03_hp/13_hermione_main/auto_08.png"
            $herView.data().addItem( 'sperm', CharacterExItem( herView.mMiscFolder, "sperm_05.png", G_Z_FACE + 1 ) )
            $herView.data().addItem( 'sperm_after', CharacterExItem( herView.mMiscFolder, "sperm_00_after.png", G_Z_FACE + 2 ) )
            play music "music/Chipper Doodle v2.mp3" fadein 1 fadeout 1 # HERMIONE'S THEME.
            show screen blktone
            with d3
            #__#hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            #__#with d3                                                                                                                                                                                                                        #HERMIONE
            $herView.hideQQ()
            #__#$ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                       #HERMIONE
            #__#$ h_body = "03_hp/13_hermione_main/body_32.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            #__#show screen hermione_main                                                                                                                                                                                 #HERMIONE
            #__#with d3                                                                                                                                                                                                                        #HERMIONE
            $herView.showQQ( "body_32.png", pos )
            her "Ужасно, сэр. Просто ужасно..."
            m "У тебя что-то... в волосах..."
            #__#hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            #__#with d3                                                                                                                                                                                                                        #HERMIONE
            $herView.hideQQ()
            #__#$ h_body = "03_hp/13_hermione_main/body_31.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            #__#show screen hermione_main                                                                                                                                                                                 #HERMIONE
            #__#with d3                                                                                                                                                                                                                        #HERMIONE
            $herView.showQQ( "body_31.png", pos )
            her "Хах?"
            #__#hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            #__#with d3                                                                                                                                                                                                                        #HERMIONE
            $herView.hideQQ()
            #__#$ h_body = "03_hp/13_hermione_main/body_189.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            #__#show screen hermione_main                                                                                                                                                                                 #HERMIONE
            #__#with d3                                                                                                                                                                                                                        #HERMIONE
            $herView.showQQ( "body_189.png", pos )
            her "О нет! Я думала, что я все вытерла..."
            show screen ctc
            pause
            show screen blkfade 
            with d3
            pause.5
            #__#$ uni_sperm = False  #Universal sperm.
            $herView.data().delItem( 'sperm' )
            $herView.addFaceName( "body_120.png" )
            #__#$ h_body = "03_hp/13_hermione_main/body_120.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            hide screen blkfade
            with d3
            pause
            hide screen ctc
            m "Хм... Итак, я полагаю, что вы выполнили свое задание?"
            #__#hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            #__#with d3                                                                                                                                                                                                                        #HERMIONE
            $herView.hideQQ()
            #__#$ h_body = "03_hp/13_hermione_main/body_69.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            #__#show screen hermione_main                                                                                                                                                                                 #HERMIONE
            #__#with d3                                                                                                                                                                                                                        #HERMIONE
            $herView.showQQ( "body_69.png", pos )
            her "Выполнила, сэр..."
            m "Тогда в чем проблема?"
            #__#hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            #__#with d3                                                                                                                                                                                                                        #HERMIONE
            $herView.hideQQ()
            #__#$ h_body = "03_hp/13_hermione_main/body_29.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            #__#show screen hermione_main                                                                                                                                                                                 #HERMIONE
            #__#with d3                                                                                                                                                                                                                        #HERMIONE
            $herView.showQQ( "body_29.png", pos )
            her ".........."
            #__#hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            #__#with d3                                                                                                                                                                                                                        #HERMIONE
            $herView.hideQQ()
            #__#$ h_body = "03_hp/13_hermione_main/body_30.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            #__#show screen hermione_main                                                                                                                                                                                 #HERMIONE
            #__#with d3                                                                                                                                                                                                                        #HERMIONE
            $herView.showQQ( "body_30.png", pos )
            her "Все парни - придурки! Вот в чем проблема, сэр!"
            #__#hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            #__#with d3                                                                                                                                                                                                                        #HERMIONE
            $herView.hideQQ()
            #__#$ h_body = "03_hp/13_hermione_main/body_87.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            #__#show screen hermione_main                                                                                                                                                                                 #HERMIONE
            #__#with d3                                                                                                                                                                                                                        #HERMIONE
            $herView.showQQ( "body_87.png", pos )
            her "Я хорошенько подрочила тому парню..."
            her "И как, вы думаете, он отблагодарил меня?"
            #__#hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            #__#with d3                                                                                                                                                                                                                        #HERMIONE
            $herView.hideQQ()
            #__#$ h_body = "03_hp/13_hermione_main/body_86.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            #__#show screen hermione_main                                                                                                                                                                                 #HERMIONE
            #__#with d3                                                                                                                                                                                                                        #HERMIONE
            $herView.showQQ( "body_86.png", pos )
            her "Заляпал меня своей спермой!.."
            #__#hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            #__#with d3                                                                                                                                                                                                                        #HERMIONE
            $herView.hideQQ()
            #__#$ h_body = "03_hp/13_hermione_main/body_30.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            #__#show screen hermione_main                                                                                                                                                                                 #HERMIONE
            #__#with d3                                                                                                                                                                                                                        #HERMIONE
            $herView.showQQ( "body_30.png", pos )
            her "И я знаю, он сделал это нарочно!"
            #__#hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            #__#with d3                                                                                                                                                                                                                        #HERMIONE
            $herView.hideQQ()
            #__#$ h_body = "03_hp/13_hermione_main/body_29.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            #__#show screen hermione_main                                                                                                                                                                                 #HERMIONE
            #__#with d3                                                                                                                                                                                                                        #HERMIONE
            $herView.showQQ( "body_29.png", pos )
            her "Противный, никчемный \"когтевранец\"..."
            m "А я бы сказал, что работа выполнена на отлично!"
            

    elif whoring >= 18 and whoring <= 20: # LEVEL 07                    
        if one_out_of_three == 1: ### EVENT (A)
            play music "music/Chipper Doodle v2.mp3" fadein 1 fadeout 1 # HERMIONE'S THEME.
            m "Мисс Грейнджер, вы выполнили задание?"
            show screen blktone
            with d3
            #__#hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            #__#with d3                                                                                                                                                                                                                        #HERMIONE
            $herView.hideQQ()
            #__#$ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                       #HERMIONE
            #__#$ h_body = "03_hp/13_hermione_main/body_31.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            #__#show screen hermione_main                                                                                                                                                                                 #HERMIONE
            #__#with d3                                                                                                                                                                                                                        #HERMIONE
            $herView.showQQ( "body_31.png", pos )
            her "Эм..."
            her "Еще нет, сэр..."
            m "\"Еще нет\"?"
            #__#hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            #__#with d3                                                                                                                                                                                                                        #HERMIONE
            $herView.hideQQ()
            #__#$ h_body = "03_hp/13_hermione_main/body_29.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            #__#show screen hermione_main                                                                                                                                                                                 #HERMIONE
            #__#with d3                                                                                                                                                                                                                        #HERMIONE
            $herView.showQQ( "body_29.png", pos )
            her "Да.. Давайте я объясню, сэр..."
            #__#hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            #__#with d3                                                                                                                                                                                                                        #HERMIONE
            $herView.hideQQ()
            #__#$ h_body = "03_hp/13_hermione_main/body_31.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            #__#show screen hermione_main                                                                                                                                                                                 #HERMIONE
            #__#with d3                                                                                                                                                                                                                        #HERMIONE
            $herView.showQQ( "body_31.png", pos )
            her "Хм... Ну..."
            her "Я дрочила тому парню в одном из пустых классов..."
            her "И тут вошел тот противный призрак - Пивз..."
            #__#hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            #__#with d3                                                                                                                                                                                                                        #HERMIONE
            $herView.hideQQ()
            #__#$ h_body = "03_hp/13_hermione_main/body_29.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            #__#show screen hermione_main                                                                                                                                                                                 #HERMIONE
            #__#with d3                                                                                                                                                                                                                        #HERMIONE
            $herView.showQQ( "body_29.png", pos )
            her "Или, я бы сказала, влетел через потолок..."
            #__#hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            #__#with d3                                                                                                                                                                                                                        #HERMIONE
            $herView.hideQQ()
            #__#$ h_body = "03_hp/13_hermione_main/body_31.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            #__#show screen hermione_main                                                                                                                                                                                 #HERMIONE
            #__#with d3                                                                                                                                                                                                                        #HERMIONE
            $herView.showQQ( "body_31.png", pos )
            her "И как только он понял, что я делала тому парню..."
            her "Он начал орать и ругаться на нас..."
            her "Так что, нам пришлось быстро уйти..."
            m "Ясно..."
            #__#hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            #__#with d3                                                                                                                                                                                                                        #HERMIONE
            $herView.hideQQ()
            #__#$ h_body = "03_hp/13_hermione_main/body_69.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            #__#show screen hermione_main                                                                                                                                                                                 #HERMIONE
            #__#with d3                                                                                                                                                                                                                        #HERMIONE
            $herView.showQQ( "body_69.png", pos )
            her "Это не все, сэр..."
            m "Продолжай..."
            #__#hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            #__#with d3                                                                                                                                                                                                                        #HERMIONE
            $herView.hideQQ()
            #__#$ h_body = "03_hp/13_hermione_main/body_87.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            #__#show screen hermione_main                                                                                                                                                                                 #HERMIONE
            #__#with d3                                                                                                                                                                                                                        #HERMIONE
            $herView.showQQ( "body_87.png", pos )
            her "Ну, я в некотором роде дала обещание тому парню..."
            her "Я пообещала встретить его после уроков и..."
            #__#hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            #__#with d3                                                                                                                                                                                                                        #HERMIONE
            $herView.hideQQ()
            #__#$ h_body = "03_hp/13_hermione_main/body_79.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            #__#show screen hermione_main                                                                                                                                                                                 #HERMIONE
            #__#with d3                                                                                                                                                                                                                        #HERMIONE
            $herView.showQQ( "body_79.png", pos )
            her "...и закончить то, что начала..."
            m "Понятно..."
            m "Выполнила?"
            #__#hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            #__#with d3                                                                                                                                                                                                                        #HERMIONE
            $herView.hideQQ()
            #__#$ h_body = "03_hp/13_hermione_main/body_117.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            #__#show screen hermione_main                                                                                                                                                                                 #HERMIONE
            #__#with d3                                                                                                                                                                                                                        #HERMIONE
            $herView.showQQ( "body_117.png", pos )
            her "Нет сэр. Пока нет..."
            her "Я собираюсь встретиться с ним как только мы закончим здесь, сэр."
            m "Хм..."
            #__#hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            #__#with d3                                                                                                                                                                                                                        #HERMIONE
            $herView.hideQQ()
            #__#$ h_body = "03_hp/13_hermione_main/body_118.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            #__#show screen hermione_main                                                                                                                                                                                 #HERMIONE
            #__#with d3                                                                                                                                                                                                                        #HERMIONE
            $herView.showQQ( "body_118.png", pos )
            her "Так что если бы вы могли просто дать эти очки заранее..."
            her "Я бы сразу же встретилась с тем парнем, и..."
            #__#hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            #__#with d3                                                                                                                                                                                                                        #HERMIONE
            $herView.hideQQ()
            #__#$ h_body = "03_hp/13_hermione_main/body_189.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            #__#show screen hermione_main                                                                                                                                                                                 #HERMIONE
            #__#with d3                                                                                                                                                                                                                        #HERMIONE
            $herView.showQQ( "body_189.png", pos )
            her "Подрочила бы ему как полагается..."
            menu:
                "\"Нет. Ты провалила это задания, девочка.\"":
                    stop music fadeout 3.0
                    #__#hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                    #__#with d3                                                                                                                                                                                                                        #HERMIONE
                    $herView.hideQQ()
                    #__#$ h_body = "03_hp/13_hermione_main/body_183.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
                    #__#show screen hermione_main                                                                                                                                                                                 #HERMIONE
                    #__#with d3                                                                                                                                                                                                                        #HERMIONE
                    $herView.showQQ( "body_183.png", pos )
                    her "Н-но..."
                    #__#hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                    #__#with d3                                                                                                                                                                                                                        #HERMIONE
                    $herView.hideQQ()
                    #__#$ h_body = "03_hp/13_hermione_main/body_119.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
                    #__#show screen hermione_main                                                                                                                                                                                 #HERMIONE
                    #__#with d3                                                                                                                                                                                                                        #HERMIONE
                    $herView.showQQ( "body_119.png", pos )
                    her "Но я дала ему слово..."
                    her "Я поклялась именем Годрика Гриффиндора..."
                    #__#hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                    #__#with d3                                                                                                                                                                                                                        #HERMIONE
                    $herView.hideQQ()
                    #__#$ h_body = "03_hp/13_hermione_main/body_118.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
                    #__#show screen hermione_main                                                                                                                                                                                 #HERMIONE
                    #__#with d3                                                                                                                                                                                                                        #HERMIONE
                    $herView.showQQ( "body_118.png", pos )
                    her "И теперь мне прийдется дрочить ему не смотря ни на что..."
                    m "Ну, я не заставлял тебя давать это обещание, ведь так?"
                    #__#hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                    #__#with d3                                                                                                                                                                                                                        #HERMIONE
                    $herView.hideQQ()
                    #__#$ h_body = "03_hp/13_hermione_main/body_117.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
                    #__#show screen hermione_main                                                                                                                                                                                 #HERMIONE
                    #__#with d3                                                                                                                                                                                                                        #HERMIONE
                    $herView.showQQ( "body_117.png", pos )
                    her "......"
                    #__#hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                    #__#with d3                                                                                                                                                                                                                        #HERMIONE
                    $herView.hideQQ()
                    #__#$ h_body = "03_hp/13_hermione_main/body_32.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
                    #__#show screen hermione_main                                                                                                                                                                                 #HERMIONE
                    #__#with d3                                                                                                                                                                                                                        #HERMIONE
                    $herView.showQQ( "body_32.png", pos )
                    her "Это просто не честно!"
                    $ mad +=20
                    $ request_23 = False 
                    call music_block
                    jump could_not_flirt #Sent here when choose "Favor failed! No points for you!" (Hermione is leaving without getting any points).
                
                "\"Хорошо. Думаю, что я могу тебе доверять.\"":
                    #__#hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                    #__#with d3                                                                                                                                                                                                                        #HERMIONE
                    $herView.hideQQ()
                    #__#$ h_body = "03_hp/13_hermione_main/body_45.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
                    #__#show screen hermione_main                                                                                                                                                                                 #HERMIONE
                    #__#with d3                                                                                                                                                                                                                        #HERMIONE
                    $herView.showQQ( "body_45.png", pos )
                    her "Спасибо, сэр."
                    her "Я знала, что вы поймете."
                    m "Просто убедись, что в этот раз ты доделала работу до конца."
                    #__#hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                    #__#with d3                                                                                                                                                                                                                        #HERMIONE
                    $herView.hideQQ()
                    #__#$ h_body = "03_hp/13_hermione_main/body_74.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
                    #__#show screen hermione_main                                                                                                                                                                                 #HERMIONE
                    #__#with d3                                                                                                                                                                                                                        #HERMIONE
                    $herView.showQQ( "body_74.png", pos )
                    her "Конечно, сэр. Я подарю ему лучший фап в его жизни, обещаю!"
            
        elif one_out_of_three == 2: ### EVENT (B)
            m "Мисс Грейнджер, вы выполнили задание?"
            show screen blktone
            with d3
            #__#hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            #__#with d3                                                                                                                                                                                                                        #HERMIONE
            $herView.hideQQ()
            #__#$ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                       #HERMIONE
            #__#$ h_body = "03_hp/13_hermione_main/body_16.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            #__#show screen hermione_main                                                                                                                                                                                 #HERMIONE
            #__#with d3                                                                                                                                                                                                                        #HERMIONE
            $herView.showQQ( "body_16.png", pos )
            her "Да, сэр..."
            #__#hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            #__#with d3                                                                                                                                                                                                                        #HERMIONE
            $herView.hideQQ()
            #__#$ h_body = "03_hp/13_hermione_main/body_29.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            #__#show screen hermione_main                                                                                                                                                                                 #HERMIONE
            #__#with d3                                                                                                                                                                                                                        #HERMIONE
            $herView.showQQ( "body_29.png", pos )
            her "Хотя, я все еще не уверена, как мне к этому относиться..."
            m "Ваши личные чувства меня не волнуют, мисс Грейнджер."
            m "Просто расскажите мне, как все прошло."
            #__#hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            #__#with d3                                                                                                                                                                                                                        #HERMIONE
            $herView.hideQQ()
            #__#$ h_body = "03_hp/13_hermione_main/body_31.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            #__#show screen hermione_main                                                                                                                                                                                 #HERMIONE
            #__#with d3                                                                                                                                                                                                                        #HERMIONE
            $herView.showQQ( "body_31.png", pos )
            her "Ну, особо нечего рассказывать, сэр..."
            play music "music/(Orchestral) Playful Tension by Shadow16nh.mp3" fadein 1 fadeout 1 # SEX THEME.
            her "Сегодня я снова подрочила своему однокласснику..."
            #__#hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            #__#with d3                                                                                                                                                                                                                        #HERMIONE
            $herView.hideQQ()
            #__#$ h_body = "03_hp/13_hermione_main/body_87.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            #__#show screen hermione_main                                                                                                                                                                                 #HERMIONE
            #__#with d3                                                                                                                                                                                                                        #HERMIONE
            $herView.showQQ( "body_87.png", pos )
            her "Я, Гермиона Грейнджер..."
            #__#hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            #__#with d3                                                                                                                                                                                                                        #HERMIONE
            $herView.hideQQ()
            #__#$ h_body = "03_hp/13_hermione_main/body_118.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            #__#show screen hermione_main                                                                                                                                                                                 #HERMIONE
            #__#with d3                                                                                                                                                                                                                        #HERMIONE
            $herView.showQQ( "body_118.png", pos )
            her "Бесплатно дрочу парням в школьном туалете..."
            m "Стоп. Что ты имеешь в виду под \"бесплатно\"?"
            #__#hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            #__#with d3                                                                                                                                                                                                                        #HERMIONE
            $herView.hideQQ()
            #__#$ h_body = "03_hp/13_hermione_main/body_117.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            #__#show screen hermione_main                                                                                                                                                                                 #HERMIONE
            #__#with d3                                                                                                                                                                                                                        #HERMIONE
            $herView.showQQ( "body_117.png", pos )
            her "Ох, конечно... Мне платят за это очки..."
            her "Но никто не знает об этом..."
            her "И для всех это выглядело так, будто какая-то девка делала это просто ради развлечения..."
            #__#hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            #__#with d3                                                                                                                                                                                                                        #HERMIONE
            $herView.hideQQ()
            #__#$ h_body = "03_hp/13_hermione_main/body_87.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            #__#show screen hermione_main                                                                                                                                                                                 #HERMIONE
            #__#with d3                                                                                                                                                                                                                        #HERMIONE
            $herView.showQQ( "body_87.png", pos )
            her "Наверное, они думают, что я - шлюха..."
            #__#hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            #__#with d3                                                                                                                                                                                                                        #HERMIONE
            $herView.hideQQ()
            #__#$ h_body = "03_hp/13_hermione_main/body_88.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            #__#show screen hermione_main                                                                                                                                                                                 #HERMIONE
            #__#with d3                                                                                                                                                                                                                        #HERMIONE
            $herView.showQQ( "body_88.png", pos )
            her ".............."
            #__#hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            #__#with d3                                                                                                                                                                                                                        #HERMIONE
            $herView.hideQQ()
            #__#$ h_body = "03_hp/13_hermione_main/body_190.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            #__#show screen hermione_main                                                                                                                                                                                 #HERMIONE
            #__#with d3                                                                                                                                                                                                                        #HERMIONE
            $herView.showQQ( "body_190.png", pos )
            her "Вы думаете, что я - шлюха, сэр?"
            menu:
                "\"Что? Конечно нет!\"":
                    #__#hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                    #__#with d3                                                                                                                                                                                                                        #HERMIONE
                    $herView.hideQQ()
                    #__#$ h_body = "03_hp/13_hermione_main/body_188.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
                    #__#show screen hermione_main                                                                                                                                                                                 #HERMIONE
                    #__#with d3                                                                                                                                                                                                                        #HERMIONE
                    $herView.showQQ( "body_188.png", pos )
                    her ".............."
                    #__#hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                    #__#with d3                                                                                                                                                                                                                        #HERMIONE
                    $herView.hideQQ()
                    #__#$ h_body = "03_hp/13_hermione_main/body_124.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
                    #__#show screen hermione_main                                                                                                                                                                                 #HERMIONE
                    #__#with d3                                                                                                                                                                                                                        #HERMIONE
                    $herView.showQQ( "body_124.png", pos )
                    her "Вы правы, сэр..."
                    her "Я приношу эту жертву во славу \"Гриффиндора\"."
                    #__#hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                    #__#with d3                                                                                                                                                                                                                        #HERMIONE
                    $herView.hideQQ()
                    #__#$ h_body = "03_hp/13_hermione_main/body_121.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
                    #__#show screen hermione_main                                                                                                                                                                                 #HERMIONE
                    #__#with d3                                                                                                                                                                                                                        #HERMIONE
                    $herView.showQQ( "body_121.png", pos )
                    her "Я не получаю удовольствия от такого рода занятий..."
                    #__#hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                    #__#with d3                                                                                                                                                                                                                        #HERMIONE
                    $herView.hideQQ()
                    #__#$ h_body = "03_hp/13_hermione_main/body_69.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
                    #__#show screen hermione_main                                                                                                                                                                                 #HERMIONE
                    #__#with d3                                                                                                                                                                                                                        #HERMIONE
                    $herView.showQQ( "body_69.png", pos )
                    her "Потому что, если бы я получала..."
                    her "То это бы значило, что я и впрямь шлюха..."
                    #__#hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                    #__#with d3                                                                                                                                                                                                                        #HERMIONE
                    $herView.hideQQ()
                    #__#$ h_body = "03_hp/13_hermione_main/body_118.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
                    #__#show screen hermione_main                                                                                                                                                                                 #HERMIONE
                    #__#with d3                                                                                                                                                                                                                        #HERMIONE
                    $herView.showQQ( "body_118.png", pos )
                    her "А я - нет..."
                    her "......"
                    her "Я не шлюха..."
                "\"Шлюха? Нет... Еще нет.\"":
                    #__#hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                    #__#with d3                                                                                                                                                                                                                        #HERMIONE
                    $herView.hideQQ()
                    #__#$ h_body = "03_hp/13_hermione_main/body_117.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
                    #__#show screen hermione_main                                                                                                                                                                                 #HERMIONE
                    #__#with d3                                                                                                                                                                                                                        #HERMIONE
                    $herView.showQQ( "body_117.png", pos )
                    her "\"Еще нет\"??!"
                    #__#hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                    #__#with d3                                                                                                                                                                                                                        #HERMIONE
                    $herView.hideQQ()
                    #__#$ h_body = "03_hp/13_hermione_main/body_118.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
                    #__#show screen hermione_main                                                                                                                                                                                 #HERMIONE
                    #__#with d3                                                                                                                                                                                                                        #HERMIONE
                    $herView.showQQ( "body_118.png", pos )
                    her ".........."
                    #__#hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                    #__#with d3                                                                                                                                                                                                                        #HERMIONE
                    $herView.hideQQ()
                    #__#$ h_body = "03_hp/13_hermione_main/body_72.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
                    #__#show screen hermione_main                                                                                                                                                                                 #HERMIONE
                    #__#with d3                                                                                                                                                                                                                        #HERMIONE
                    $herView.showQQ( "body_72.png", pos )
                    play music "music/Chipper Doodle v2.mp3" fadein 1 fadeout 1 # HERMIONE'S THEME.
                    her "Ну конечно!"
                    #__#hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                    #__#with d3                                                                                                                                                                                                                        #HERMIONE
                    $herView.hideQQ()
                    #__#$ h_body = "03_hp/13_hermione_main/body_15.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
                    #__#show screen hermione_main                                                                                                                                                                                 #HERMIONE
                    #__#with d3                                                                                                                                                                                                                        #HERMIONE
                    $herView.showQQ( "body_15.png", pos )
                    her "Вы как всегда правы, сэр!"
                    m "Хах?"
                    #__#hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                    #__#with d3                                                                                                                                                                                                                        #HERMIONE
                    $herView.hideQQ()
                    #__#$ h_body = "03_hp/13_hermione_main/body_14.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
                    #__#show screen hermione_main                                                                                                                                                                                 #HERMIONE
                    #__#with d3                                                                                                                                                                                                                        #HERMIONE
                    $herView.showQQ( "body_14.png", pos )
                    her "Я сделала парочку... плохих вещей..."
                    her "Но это ничего не значит!"
                    #__#hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                    #__#with d3                                                                                                                                                                                                                        #HERMIONE
                    $herView.hideQQ()
                    #__#$ h_body = "03_hp/13_hermione_main/body_12.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
                    #__#show screen hermione_main                                                                                                                                                                                 #HERMIONE
                    #__#with d3                                                                                                                                                                                                                        #HERMIONE
                    $herView.showQQ( "body_12.png", pos )
                    her "..........."
                "\"Да, именно так бы я тебя и описал.\"":
                    #__#hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                    #__#with d3                                                                                                                                                                                                                        #HERMIONE
                    $herView.hideQQ()
                    #__#$ h_body = "03_hp/13_hermione_main/body_20.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
                    #__#show screen hermione_main                                                                                                                                                                                 #HERMIONE
                    #__#with d3                                                                                                                                                                                                                        #HERMIONE
                    $herView.showQQ( "body_20.png", pos )
                    her "Я боялась, что вы это скажете, сэр..."
                    her "Но вы ошибаетесь."
                    #__#hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                    #__#with d3                                                                                                                                                                                                                        #HERMIONE
                    $herView.hideQQ()
                    #__#$ h_body = "03_hp/13_hermione_main/body_21.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
                    #__#show screen hermione_main                                                                                                                                                                                 #HERMIONE
                    #__#with d3                                                                                                                                                                                                                        #HERMIONE
                    $herView.showQQ( "body_21.png", pos )
                    her "Все должны понимать, что я не получаю удовольствия от этого..."
                    #__#hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                    #__#with d3                                                                                                                                                                                                                        #HERMIONE
                    $herView.hideQQ()
                    #__#$ h_body = "03_hp/13_hermione_main/body_23.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
                    #__#show screen hermione_main                                                                                                                                                                                 #HERMIONE
                    #__#with d3                                                                                                                                                                                                                        #HERMIONE
                    $herView.showQQ( "body_23.png", pos )
                    her "Я просто делаю то, что должно быть сделано..."
                    $ mad += 10
                    
            #__#hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            #__#with d3                                                                                                                                                                                                                        #HERMIONE
            $herView.hideQQ()
            #__#$ h_body = "03_hp/13_hermione_main/body_13.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            #__#show screen hermione_main                                                                                                                                                                                 #HERMIONE
            #__#with d3                                                                                                                                                                                                                        #HERMIONE
            $herView.showQQ( "body_13.png", pos )
            her "Сэр, могу я просто получить плату, пожалуйста?"
            m "Получить плату? Но ведь вы мне еще ничего не рассказали."
            her "Разве нет?"
            #__#hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            #__#with d3                                                                                                                                                                                                                        #HERMIONE
            $herView.hideQQ()
            #__#$ h_body = "03_hp/13_hermione_main/body_183.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            #__#show screen hermione_main                                                                                                                                                                                 #HERMIONE
            #__#with d3                                                                                                                                                                                                                        #HERMIONE
            $herView.showQQ( "body_183.png", pos )
            her "Сэр, сегодня я передернула член одному из своих одноклассников..."
            her "Я дрочила его член, пока он не кончил..."
            #__#hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            #__#with d3                                                                                                                                                                                                                        #HERMIONE
            $herView.hideQQ()
            #__#$ h_body = "03_hp/13_hermione_main/body_66.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            #__#show screen hermione_main                                                                                                                                                                                 #HERMIONE
            #__#with d3                                                                                                                                                                                                                        #HERMIONE
            $herView.showQQ( "body_66.png", pos )
            her "Не это ли вы мне сказали сделать?"
            m "Именно это я и сказал вам сделать."
            #__#hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            #__#with d3                                                                                                                                                                                                                        #HERMIONE
            $herView.hideQQ()
            #__#$ h_body = "03_hp/13_hermione_main/body_184.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            #__#show screen hermione_main                                                                                                                                                                                 #HERMIONE
            #__#with d3                                                                                                                                                                                                                        #HERMIONE
            $herView.showQQ( "body_184.png", pos )
            her "Тогда я хочу, чтобы мне заплатили."
            m "........"
            m "Ладно..."
            
            
            
        elif one_out_of_three == 3: ### EVENT (C)
            m "Mисс Грейнджер, вы завершили свое задание?"
            show screen blktone
            with d3
            #__#hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            #__#with d3                                                                                                                                                                                                                        #HERMIONE
            $herView.hideQQ()
            #__#$ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                       #HERMIONE
            #__#$ h_body = "03_hp/13_hermione_main/body_16.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            #__#show screen hermione_main                                                                                                                                                                                 #HERMIONE
            #__#with d3                                                                                                                                                                                                                        #HERMIONE
            $herView.showQQ( "body_16.png", pos )
            her "Да, сэр. Завершила."
            m "Отлично. Расскажи мне больше."
            #__#hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            #__#with d3                                                                                                                                                                                                                        #HERMIONE
            $herView.hideQQ()
            #__#$ h_body = "03_hp/13_hermione_main/body_14.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            #__#show screen hermione_main                                                                                                                                                                                 #HERMIONE
            #__#with d3                                                                                                                                                                                                                        #HERMIONE
            $herView.showQQ( "body_14.png", pos )
            play music "music/(Orchestral) Playful Tension by Shadow16nh.mp3" fadein 1 fadeout 1 # SEX THEME.
            her "Ну, сегодня был довольно занятой день..."
            her "Я была завалена учебой..."
            her "Так что у меня не было времени тщательно это спланировать, как я делала раньше..."
            her "Я просто подошла к первому парню, которого увидела..."
            #__#hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            #__#with d3                                                                                                                                                                                                                        #HERMIONE
            $herView.hideQQ()
            #__#$ h_body = "03_hp/13_hermione_main/body_69.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            #__#show screen hermione_main                                                                                                                                                                                 #HERMIONE
            #__#with d3                                                                                                                                                                                                                        #HERMIONE
            $herView.showQQ( "body_69.png", pos )
            her "И спросила, хочет ли он, чтобы я сняла его напряжение."
            her "Спустя пару минут я уже дрочила его твердый член в туалетной кабинке..."
            m "Какая эффективность..."
            #__#hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            #__#with d3                                                                                                                                                                                                                        #HERMIONE
            $herView.hideQQ()
            #__#$ h_body = "03_hp/13_hermione_main/body_79.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            #__#show screen hermione_main                                                                                                                                                                                 #HERMIONE
            #__#with d3                                                                                                                                                                                                                        #HERMIONE
            $herView.showQQ( "body_79.png", pos )
            her "Спасибо, сэр."
            #__#hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            #__#with d3                                                                                                                                                                                                                        #HERMIONE
            $herView.hideQQ()
            #__#$ h_body = "03_hp/13_hermione_main/body_69.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            #__#show screen hermione_main                                                                                                                                                                                 #HERMIONE
            #__#with d3                                                                                                                                                                                                                        #HERMIONE
            $herView.showQQ( "body_69.png", pos )
            her "Так вот, как я и рассказывала..."
            her "Я дрочила его член, пока он не кончил..."
            #__#hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            #__#with d3                                                                                                                                                                                                                        #HERMIONE
            $herView.hideQQ()
            #__#$ h_body = "03_hp/13_hermione_main/body_66.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            #__#show screen hermione_main                                                                                                                                                                                 #HERMIONE
            #__#with d3                                                                                                                                                                                                                        #HERMIONE
            $herView.showQQ( "body_66.png", pos )
            her "Но после этого он сказал лишь: \"Хорошая работа, шлюха.\" и ушел..."
            #__#hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            #__#with d3                                                                                                                                                                                                                        #HERMIONE
            $herView.hideQQ()
            #__#$ h_body = "03_hp/13_hermione_main/body_69.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            #__#show screen hermione_main                                                                                                                                                                                 #HERMIONE
            #__#with d3                                                                                                                                                                                                                        #HERMIONE
            $herView.showQQ( "body_69.png", pos )
            her "Такой мерзкий поступок..."
            #__#hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            #__#with d3                                                                                                                                                                                                                        #HERMIONE
            $herView.hideQQ()
            #__#$ h_body = "03_hp/13_hermione_main/body_120.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            #__#show screen hermione_main                                                                                                                                                                                 #HERMIONE
            #__#with d3                                                                                                                                                                                                                        #HERMIONE
            $herView.showQQ( "body_120.png", pos )
            her "Он заставил меня почувствовать себя такой дешевой... и использованной."
            her "Но потом все стало хуже..."
            her "......."
            #__#hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            #__#with d3                                                                                                                                                                                                                        #HERMIONE
            $herView.hideQQ()
            #__#$ h_body = "03_hp/13_hermione_main/body_118.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            #__#show screen hermione_main                                                                                                                                                                                 #HERMIONE
            #__#with d3                                                                                                                                                                                                                        #HERMIONE
            $herView.showQQ( "body_118.png", pos )
            her "Я думаю, что на каком-то уровне это заставило меня почувствовать..."
            her "Что все те услуги, что я продаю вам в последнее время, сэр..."
            #__#hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            #__#with d3                                                                                                                                                                                                                        #HERMIONE
            $herView.hideQQ()
            #__#$ h_body = "03_hp/13_hermione_main/body_117.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            #__#show screen hermione_main                                                                                                                                                                                 #HERMIONE
            #__#with d3                                                                                                                                                                                                                        #HERMIONE
            $herView.showQQ( "body_117.png", pos )
            her "...начинают влиять на меня."
            her "Сэр, что со мной происходит?"
            menu:
                "\"Ничего. Ты слишком много об этом думаешь!\"":
                    #__#hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                    #__#with d3                                                                                                                                                                                                                        #HERMIONE
                    $herView.hideQQ()
                    #__#$ h_body = "03_hp/13_hermione_main/body_190.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
                    #__#show screen hermione_main                                                                                                                                                                                 #HERMIONE
                    #__#with d3                                                                                                                                                                                                                        #HERMIONE
                    $herView.showQQ( "body_190.png", pos )
                    her "......."
                    #__#hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                    #__#with d3                                                                                                                                                                                                                        #HERMIONE
                    $herView.hideQQ()
                    #__#$ h_body = "03_hp/13_hermione_main/body_188.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
                    #__#show screen hermione_main                                                                                                                                                                                 #HERMIONE
                    #__#with d3                                                                                                                                                                                                                        #HERMIONE
                    $herView.showQQ( "body_188.png", pos )
                    play music "music/Chipper Doodle v2.mp3" fadein 1 fadeout 1 # HERMIONE'S THEME.
                    her "Наверное, вы правы, сэр. Как всегда..."
                    her "Это никак не влияет на меня..."
                "\"Это естественная реакция...\"":
                    #__#hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                    #__#with d3                                                                                                                                                                                                                        #HERMIONE
                    $herView.hideQQ()
                    #__#$ h_body = "03_hp/13_hermione_main/body_190.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
                    #__#show screen hermione_main                                                                                                                                                                                 #HERMIONE
                    #__#with d3                                                                                                                                                                                                                        #HERMIONE
                    $herView.showQQ( "body_190.png", pos )
                    her "Да?"
                    m "Конечно."
                    m "Ты девушка, а он парень..."
                    m "Когда ты возбуждаешься, тебе хорошо..."
                    #__#hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                    #__#with d3                                                                                                                                                                                                                        #HERMIONE
                    $herView.hideQQ()
                    #__#$ h_body = "03_hp/13_hermione_main/body_188.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
                    #__#show screen hermione_main                                                                                                                                                                                 #HERMIONE
                    #__#with d3                                                                                                                                                                                                                        #HERMIONE
                    $herView.showQQ( "body_188.png", pos )
                    her "Хм..."
                    m "А если бы ты подрочила парню с совершенным безразличием к этому..."
                    m "...это было бы... не естественно."
                    #__#hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                    #__#with d3                                                                                                                                                                                                                        #HERMIONE
                    $herView.hideQQ()
                    #__#$ h_body = "03_hp/13_hermione_main/body_190.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
                    #__#show screen hermione_main                                                                                                                                                                                 #HERMIONE
                    #__#with d3                                                                                                                                                                                                                        #HERMIONE
                    $herView.showQQ( "body_190.png", pos )
                    her "Я думаю, что вы правы, сэр."
                    #__#hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                    #__#with d3                                                                                                                                                                                                                        #HERMIONE
                    $herView.hideQQ()
                    #__#$ h_body = "03_hp/13_hermione_main/body_188.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
                    #__#show screen hermione_main                                                                                                                                                                                 #HERMIONE
                    #__#with d3                                                                                                                                                                                                                        #HERMIONE
                    $herView.showQQ( "body_188.png", pos )
                    her "Как всегда." # :)
         
                "\"Точно! Все идет точно по плану!\"":
                    #__#hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                    #__#with d3                                                                                                                                                                                                                        #HERMIONE
                    $herView.hideQQ()
                    #__#$ h_body = "03_hp/13_hermione_main/body_119.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
                    #__#show screen hermione_main                                                                                                                                                                                 #HERMIONE
                    #__#with d3                                                                                                                                                                                                                        #HERMIONE
                    $herView.showQQ( "body_119.png", pos )
                    her "Что?"
                    m "Что?"
                    #__#hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                    #__#with d3                                                                                                                                                                                                                        #HERMIONE
                    $herView.hideQQ()
                    #__#$ h_body = "03_hp/13_hermione_main/body_187.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
                    #__#show screen hermione_main                                                                                                                                                                                 #HERMIONE
                    #__#with d3                                                                                                                                                                                                                        #HERMIONE
                    $herView.showQQ( "body_187.png", pos )
                    her "Профессор, вы только что сказали \"Все идет точно по плану\"?"
                    m "Я сказал?"
                    m "Ах, да, конечно."
                    m "Тот самый план, где \"Гриффиндор\" точно получит в этом году кубок школы."
                    m "И благодаря твоим стараниям..."
                    m "Все идет согласно пик-... В смысле, плана..."
                    #__#hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                    #__#with d3                                                                                                                                                                                                                        #HERMIONE
                    $herView.hideQQ()
                    #__#$ h_body = "03_hp/13_hermione_main/body_120.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
                    #__#show screen hermione_main                                                                                                                                                                                 #HERMIONE
                    #__#with d3                                                                                                                                                                                                                        #HERMIONE
                    $herView.showQQ( "body_120.png", pos )
                    her "Хм..."
                    $ mad += 11

            
    elif whoring >= 21: # LEVEL 08+                    
        if one_out_of_three == 1: ### EVENT (A)
            if sucked_off_ron: #In public events. Give a handjob to classmate. Event level 03. Event # 1. "Jerked of and suked of Ron Weasley". Turns True after that.
                jump blowjob_ron
            else:
                $ sucked_off_ron = True #Makes sure this event is not repeated twice.
                
                stop music fadeout 1.0
                # HERMIONE HAS CUM ON HAIR.
                #$ aftersperm = True #Shows stains on Hermione's uniform.
                #__#$ uni_sperm = True  #Universal sperm.
                #__#$ u_sperm = "03_hp/13_hermione_main/auto_08.png"
                $herView.data().addItem( 'sperm', CharacterExItem( herView.mMiscFolder, "sperm_05.png", G_Z_FACE + 1 ) )
                $herView.data().addItem( 'sperm_after', CharacterExItem( herView.mMiscFolder, "sperm_00_after.png", G_Z_FACE + 2 ) )

                show screen blktone
                with d3
                #__#hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                #__#with d3                                                                                                                                                                                                                        #HERMIONE
                $herView.hideQQ()
                #__#$ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                       #HERMIONE
                #__#$ h_body = "03_hp/13_hermione_main/body_11.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
                #__#show screen hermione_main                                                                                                                                                                                 #HERMIONE
                #__#with d3                                                                                                                                                                                                                        #HERMIONE
                $herView.showQQ( "body_11.png", pos )
                her "Профессор Дамблдор, сэр..."
                m "Мисс Грейнджер..."
                #__#hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                #__#with d3                                                                                                                                                                                                                        #HERMIONE
                $herView.hideQQ()
                #__#$ h_body = "03_hp/13_hermione_main/body_10.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
                #__#show screen hermione_main                                                                                                                                                                                 #HERMIONE
                #__#with d3                                                                                                                                                                                                                        #HERMIONE
                $herView.showQQ( "body_10.png", pos )
                her "Я сделала сегодня плохую вещь, сэр..."
                m "Да что ты? Рассказывай..."
                play music "music/(Orchestral) Playful Tension by Shadow16nh.mp3" fadein 1 fadeout 1 # SEX THEME.
                her "Да, я сделала плохую вещь... очень плохую вещь..."
                #__#hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                #__#with d3                                                                                                                                                                                                                        #HERMIONE
                $herView.hideQQ()
                #__#$ h_body = "03_hp/13_hermione_main/body_09.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
                #__#show screen hermione_main                                                                                                                                                                                 #HERMIONE
                #__#with d3                                                                                                                                                                                                                        #HERMIONE
                $herView.showQQ( "body_09.png", pos )
                her "Очень плохую и дурацкую вещь..."
                her "..."
                m "...................."
                her "......................"
                #__#hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                #__#with d3                                                                                                                                                                                                                        #HERMIONE
                $herView.hideQQ()
                #__#$ h_body = "03_hp/13_hermione_main/body_22.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
                #__#show screen hermione_main                                                                                                                                                                                 #HERMIONE
                #__#with d3                                                                                                                                                                                                                        #HERMIONE
                $herView.showQQ( "body_22.png", pos )
                her "Я дрочила брату моей лучшей подруги..."
                m "Интересно..."
                #__#hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                #__#with d3                                                                                                                                                                                                                        #HERMIONE
                $herView.hideQQ()
                #__#$ h_body = "03_hp/13_hermione_main/body_21.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
                #__#show screen hermione_main                                                                                                                                                                                 #HERMIONE
                #__#with d3                                                                                                                                                                                                                        #HERMIONE
                $herView.showQQ( "body_21.png", pos )
                her "Поначалу это казалось хорошей идеей..."
                her "Да и Рон был 'за', руками и ногами..."
                #__#hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                #__#with d3                                                                                                                                                                                                                        #HERMIONE
                $herView.hideQQ()
                #__#$ h_body = "03_hp/13_hermione_main/body_139.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
                #__#show screen hermione_main                                                                                                                                                                                 #HERMIONE
                #__#with d3                                                                                                                                                                                                                        #HERMIONE
                $herView.showQQ( "body_139.png", pos )
                her "Но если бы Джинни узнала... она..."
                #__#hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                #__#with d3                                                                                                                                                                                                                        #HERMIONE
                $herView.hideQQ()
                #__#$ h_body = "03_hp/13_hermione_main/body_22.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
                #__#show screen hermione_main                                                                                                                                                                                 #HERMIONE
                #__#with d3                                                                                                                                                                                                                        #HERMIONE
                $herView.showQQ( "body_22.png", pos )
                her "Скорее всего, она бы меня убила..."
                m "Подрочила, хах? Ты уверена, что это все, что ты сделала?"
                #__#hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                #__#with d3                                                                                                                                                                                                                        #HERMIONE
                $herView.hideQQ()
                #__#$ h_body = "03_hp/13_hermione_main/body_21.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
                #__#show screen hermione_main                                                                                                                                                                                 #HERMIONE
                #__#with d3                                                                                                                                                                                                                        #HERMIONE
                $herView.showQQ( "body_21.png", pos )
                her "Сэр?"
                m "У тебя что-то в волосах..."
                #__#hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                #__#with d3                                                                                                                                                                                                                        #HERMIONE
                $herView.hideQQ()
                #__#$ h_body = "03_hp/13_hermione_main/body_19.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
                #__#show screen hermione_main                                                                                                                                                                                 #HERMIONE
                #__#with d3                                                                                                                                                                                                                        #HERMIONE
                $herView.showQQ( "body_19.png", pos )
                her "Что? Но я же все проглотила... эээ..."
                #__#hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                #__#with d3                                                                                                                                                                                                                        #HERMIONE
                $herView.hideQQ()
                #__#$ h_body = "03_hp/13_hermione_main/body_140.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
                #__#show screen hermione_main                                                                                                                                                                                 #HERMIONE
                #__#with d3                                                                                                                                                                                                                        #HERMIONE
                $herView.showQQ( "body_140.png", pos )
                her "В смысле..."
                #__#hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                #__#with d3                                                                                                                                                                                                                        #HERMIONE
                $herView.hideQQ()
                #__#$ h_body = "03_hp/13_hermione_main/body_139.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
                #__#show screen hermione_main                                                                                                                                                                                 #HERMIONE
                #__#with d3                                                                                                                                                                                                                        #HERMIONE
                $herView.showQQ( "body_139.png", pos )
                her "*Вздох*"
                her "...Я отсосала у него, сэр."
                her "Я не планировала этогo... но..."
                #__#hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                #__#with d3                                                                                                                                                                                                                        #HERMIONE
                $herView.hideQQ()
                #__#$ h_body = "03_hp/13_hermione_main/body_140.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
                #__#show screen hermione_main                                                                                                                                                                                 #HERMIONE
                #__#with d3                                                                                                                                                                                                                        #HERMIONE
                $herView.showQQ( "body_140.png", pos )
                her "Рон всегда был так добр ко мне..."
                #__#hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                #__#with d3                                                                                                                                                                                                                        #HERMIONE
                $herView.hideQQ()
                #__#$ h_body = "03_hp/13_hermione_main/body_143.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
                #__#show screen hermione_main                                                                                                                                                                                 #HERMIONE
                #__#with d3                                                                                                                                                                                                                        #HERMIONE
                $herView.showQQ( "body_143.png", pos )
                her "И я хотела поблагодарить его...*Всхлип!*"
                #__#hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                #__#with d3                                                                                                                                                                                                                        #HERMIONE
                $herView.hideQQ()
                #__#$ h_body = "03_hp/13_hermione_main/body_22.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
                #__#show screen hermione_main                                                                                                                                                                                 #HERMIONE
                #__#with d3                                                                                                                                                                                                                        #HERMIONE
                $herView.showQQ( "body_22.png", pos )
                her "А теперь Джинни меня убьет! *Всхлип!*"
                her "Она убьет меня, сэр!"
                #__#hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                #__#with d3                                                                                                                                                                                                                        #HERMIONE
                $herView.hideQQ()
                #__#$ h_body = "03_hp/13_hermione_main/body_143.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
                #__#show screen hermione_main                                                                                                                                                                                 #HERMIONE
                #__#with d3                                                                                                                                                                                                                        #HERMIONE
                $herView.showQQ( "body_143.png", pos )
                her "А если не убьет, то, скорее всего, я сама умру от стыда."
                her "Нет, нет, нет... Как я взгляну ей в глаза...?"
                m "Успокойся, девочка."
                m "Уверяю тебя, это не та вещь, о какой парень с радостью растреплет своей сестре."
                #__#hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                #__#with d3                                                                                                                                                                                                                        #HERMIONE
                $herView.hideQQ()
                #__#$ h_body = "03_hp/13_hermione_main/body_140.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
                #__#show screen hermione_main                                                                                                                                                                                 #HERMIONE
                #__#with d3                                                                                                                                                                                                                        #HERMIONE
                $herView.showQQ( "body_140.png", pos )
                her "Серьезно?"
                m "Не буть глупой."
                #__#hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                #__#with d3                                                                                                                                                                                                                        #HERMIONE
                $herView.hideQQ()
                #__#$ h_body = "03_hp/13_hermione_main/body_23.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
                #__#show screen hermione_main                                                                                                                                                                                 #HERMIONE
                #__#with d3                                                                                                                                                                                                                        #HERMIONE
                $herView.showQQ( "body_23.png", pos )
                her "Хм..."
                #__#hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                #__#with d3                                                                                                                                                                                                                        #HERMIONE
                $herView.hideQQ()
                #__#$ h_body = "03_hp/13_hermione_main/body_19.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
                #__#show screen hermione_main                                                                                                                                                                                 #HERMIONE
                #__#with d3                                                                                                                                                                                                                        #HERMIONE
                $herView.showQQ( "body_19.png", pos )
                her "Пожалуй, вы правы, сэр..."
                her "И я заставила Рона дать мне слово, что он сохранит все это в секрете..."
                #__#hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                #__#with d3                                                                                                                                                                                                                        #HERMIONE
                $herView.hideQQ()
                #__#$ h_body = "03_hp/13_hermione_main/body_10.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
                #__#show screen hermione_main                                                                                                                                                                                 #HERMIONE
                #__#with d3                                                                                                                                                                                                                        #HERMIONE
                $herView.showQQ( "body_10.png", pos )
                her "Так что я должна просто поверить, что он сдержит свое слово..."
                #__#hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                #__#with d3                                                                                                                                                                                                                        #HERMIONE
                $herView.hideQQ()
                #__#$ h_body = "03_hp/13_hermione_main/body_13.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
                #__#show screen hermione_main                                                                                                                                                                                 #HERMIONE
                #__#with d3                                                                                                                                                                                                                        #HERMIONE
                $herView.showQQ( "body_13.png", pos )
                her ".........."
                her "..."
                #__#hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                #__#with d3                                                                                                                                                                                                                        #HERMIONE
                $herView.hideQQ()
                #__#$ h_body = "03_hp/13_hermione_main/body_06.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
                #__#show screen hermione_main                                                                                                                                                                                 #HERMIONE
                #__#with d3                                                                                                                                                                                                                        #HERMIONE
                $herView.showQQ( "body_06.png", pos )
                her "Мне заплатят за это, сэр?"
                m "Конечно."

        elif one_out_of_three == 2: ### EVENT (B) (WANK DURING CLASS). Event level: 03.
            label blowjob_ron: #Sent here if sucked off Ron already.
                pass
            m "Мисс Грейнджер, вы выполнили задание?"
            show screen blktone
            with d3
            #__#hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            #__#with d3                                                                                                                                                                                                                        #HERMIONE
            $herView.hideQQ()
            #__#$ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                       #HERMIONE
            #__#$ h_body = "03_hp/13_hermione_main/body_06.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            #__#show screen hermione_main                                                                                                                                                                                 #HERMIONE
            #__#with d3                                                                                                                                                                                                                        #HERMIONE
            $herView.showQQ( "body_06.png", pos )
            her "Да сэр, выполнила."
            #__#hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            #__#with d3                                                                                                                                                                                                                        #HERMIONE
            $herView.hideQQ()
            #__#$ h_body = "03_hp/13_hermione_main/body_11.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            #__#show screen hermione_main                                                                                                                                                                                 #HERMIONE
            #__#with d3                                                                                                                                                                                                                        #HERMIONE
            $herView.showQQ( "body_11.png", pos )
            her "Но, эм..."
            m "...?"
            #__#hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            #__#with d3                                                                                                                                                                                                                        #HERMIONE
            $herView.hideQQ()
            #__#$ h_body = "03_hp/13_hermione_main/body_31.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            #__#show screen hermione_main                                                                                                                                                                                 #HERMIONE
            #__#with d3                                                                                                                                                                                                                        #HERMIONE
            $herView.showQQ( "body_31.png", pos )
            her "Ну, я не просто подрочила одному из своих одноклассников..."
            her "Я.............."
            #__#hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            #__#with d3                                                                                                                                                                                                                        #HERMIONE
            $herView.hideQQ()
            #__#$ h_body = "03_hp/13_hermione_main/body_88.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            #__#show screen hermione_main                                                                                                                                                                                 #HERMIONE
            #__#with d3                                                                                                                                                                                                                        #HERMIONE
            $herView.showQQ( "body_88.png", pos )
            her "..............."
            m "Выкладывай давай. Неопределенность убивает меня."
            #__#hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            #__#with d3                                                                                                                                                                                                                        #HERMIONE
            $herView.hideQQ()
            #__#$ h_body = "03_hp/13_hermione_main/body_87.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            #__#show screen hermione_main                                                                                                                                                                                 #HERMIONE
            #__#with d3                                                                                                                                                                                                                        #HERMIONE
            $herView.showQQ( "body_87.png", pos )
            play music "music/(Orchestral) Playful Tension by Shadow16nh.mp3" fadein 1 fadeout 1 # SEX THEME.
            her "Я сделала это во время урока..."
            m "Впечатляюще..."
            #__#hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            #__#with d3                                                                                                                                                                                                                        #HERMIONE
            $herView.hideQQ()
            #__#$ h_body = "03_hp/13_hermione_main/body_124.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            #__#show screen hermione_main                                                                                                                                                                                 #HERMIONE
            #__#with d3                                                                                                                                                                                                                        #HERMIONE
            $herView.showQQ( "body_124.png", pos )
            her "Да, я старалась вести себя как можно более натуральнее..."
            her "Даже делала заметки другой рукой..."
            #__#hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            #__#with d3                                                                                                                                                                                                                        #HERMIONE
            $herView.hideQQ()
            #__#$ h_body = "03_hp/13_hermione_main/body_127.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            #__#show screen hermione_main                                                                                                                                                                                 #HERMIONE
            #__#with d3                                                                                                                                                                                                                        #HERMIONE
            $herView.showQQ( "body_127.png", pos )
            her "И я думаю, что это был лучший фап в его жизни..."
            her "Потому что он не просто кончил."
            her "Его член буквально взорвался."
            m "Тебе понравилось это, ведь так?"
            #__#hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            #__#with d3                                                                                                                                                                                                                        #HERMIONE
            $herView.hideQQ()
            #__#$ h_body = "03_hp/13_hermione_main/body_128.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            #__#show screen hermione_main                                                                                                                                                                                 #HERMIONE
            #__#with d3                                                                                                                                                                                                                        #HERMIONE
            $herView.showQQ( "body_128.png", pos )
            her "Если быть совершенно откровенной с вами... Да."
            #__#hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            #__#with d3                                                                                                                                                                                                                        #HERMIONE
            $herView.hideQQ()
            #__#$ h_body = "03_hp/13_hermione_main/body_111.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            #__#show screen hermione_main                                                                                                                                                                                 #HERMIONE
            #__#with d3                                                                                                                                                                                                                        #HERMIONE
            $herView.showQQ( "body_111.png", pos )
            her "Было так возбуждающе заниматься чем-то подобным у всех под носом..."
            her "Закаляет характер!"
            m "Эм... конечно, да."
         
        elif one_out_of_three == 3: ### EVENT (C) Event level: 03. (Wanked off 5 boys).
            play music "music/Chipper Doodle v2.mp3" fadein 1 fadeout 1 # HERMIONE'S THEME.
            m "Мисс Грейнджер, вы выполнили свое задание?"
            show screen blktone
            with d3
            #__#hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            #__#with d3                                                                                                                                                                                                                        #HERMIONE
            $herView.hideQQ()
            #__#$ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                       #HERMIONE
            #__#$ h_body = "03_hp/13_hermione_main/body_129.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            #__#show screen hermione_main                                                                                                                                                                                 #HERMIONE
            #__#with d3                                                                                                                                                                                                                        #HERMIONE
            $herView.showQQ( "body_129.png", pos )
            her "Да сэр, выполнила..."
            her "Вообще-то даже больше, чем один раз..."
            m "Больше, чем один раз?"
            #__#hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            #__#with d3                                                                                                                                                                                                                        #HERMIONE
            $herView.hideQQ()
            #__#$ h_body = "03_hp/13_hermione_main/body_128.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            #__#show screen hermione_main                                                                                                                                                                                 #HERMIONE
            #__#with d3                                                                                                                                                                                                                        #HERMIONE
            $herView.showQQ( "body_128.png", pos )
            her "Пять раз, сэр..."
            her "Я думаю, что меня немного занесло..."
            m "В смысле, \"пять раз\"?"
            #__#hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            #__#with d3                                                                                                                                                                                                                        #HERMIONE
            $herView.hideQQ()
            #__#$ h_body = "03_hp/13_hermione_main/body_129.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            #__#show screen hermione_main                                                                                                                                                                                 #HERMIONE
            #__#with d3                                                                                                                                                                                                                        #HERMIONE
            $herView.showQQ( "body_129.png", pos )
            her "В смысле, сегодня я дрочила пятерым парням, сэр."
            m "Очень впечатляюще, мисс Грейнджер."
            #__#hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            #__#with d3                                                                                                                                                                                                                        #HERMIONE
            $herView.hideQQ()
            #__#$ h_body = "03_hp/13_hermione_main/body_128.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            #__#show screen hermione_main                                                                                                                                                                                 #HERMIONE
            #__#with d3                                                                                                                                                                                                                        #HERMIONE
            $herView.showQQ( "body_128.png", pos )
            her "Спасибо, сэр."
            m "Ты же не ждешь, что я умножу твою плату в несколько раз, ведь так?"
            #__#hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            #__#with d3                                                                                                                                                                                                                        #HERMIONE
            $herView.hideQQ()
            #__#$ h_body = "03_hp/13_hermione_main/body_188.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            #__#show screen hermione_main                                                                                                                                                                                 #HERMIONE
            #__#with d3                                                                                                                                                                                                                        #HERMIONE
            $herView.showQQ( "body_188.png", pos )
            her "Конечно нет, сэр."
            m "Тогда зачем делать это?"
            #__#hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            #__#with d3                                                                                                                                                                                                                        #HERMIONE
            $herView.hideQQ()
            #__#$ h_body = "03_hp/13_hermione_main/body_190.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            #__#show screen hermione_main                                                                                                                                                                                 #HERMIONE
            #__#with d3                                                                                                                                                                                                                        #HERMIONE
            $herView.showQQ( "body_190.png", pos )
            her "Ну, просто так получилось..."
            her "Я дрочила одному парню..."
            her "Другой парень нас застукал..."
            her "Потом он позвал своих друзей..."
            #__#hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            #__#with d3                                                                                                                                                                                                                        #HERMIONE
            $herView.hideQQ()
            #__#$ h_body = "03_hp/13_hermione_main/body_128.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            #__#show screen hermione_main                                                                                                                                                                                 #HERMIONE
            #__#with d3                                                                                                                                                                                                                        #HERMIONE
            $herView.showQQ( "body_128.png", pos )
            her "Одно за другим..."
            m "И все кончилось тем, что ты удовлетворила пять членов..."
            #__#hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            #__#with d3                                                                                                                                                                                                                        #HERMIONE
            $herView.hideQQ()
            #__#$ h_body = "03_hp/13_hermione_main/body_121.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            #__#show screen hermione_main                                                                                                                                                                                 #HERMIONE
            #__#with d3                                                                                                                                                                                                                        #HERMIONE
            $herView.showQQ( "body_121.png", pos )
            her "...да."
            m "Отличная работа, мисс Грейнджер."
            #__#hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            #__#with d3                                                                                                                                                                                                                        #HERMIONE
            $herView.hideQQ()
            #__#$ h_body = "03_hp/13_hermione_main/body_128.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            #__#show screen hermione_main                                                                                                                                                                                 #HERMIONE
            #__#with d3                                                                                                                                                                                                                        #HERMIONE
            $herView.showQQ( "body_128.png", pos )
            
            

    
    
    
    $ gryffindor += current_payout #55
    m "[current_payout] очков \"Гриффиндору\"!"
    her "Спасибо, сэр."
    
    hide screen bld1
    #__#hide screen hermione_main
    $herView.hideQ() #"WARNING_Z"
    hide screen blktone 
    hide screen hermione_02
    hide screen ctc
    with d3

    $ walk_xpos=400 #Animation of walking chibi. (From)
    $ walk_xpos2=610 #Coordinates of it's movement. (To)
    $ hermione_speed = 02.0 #The speed of moving the walking animation across the screen.
    show screen hermione_walk_01_f 
    pause 2
    hide screen hermione_walk_01_f 
    $ renpy.play('sounds/door.mp3') #Sound of a door opening.
    with Dissolve(.3)

    
 
 
    #__#$ uni_sperm = False  #Universal sperm.
    #__#$ aftersperm = False #Shows stains on Hermione's uniform.

    $herView.data().loadState()
    
    $ request_23_points += 1 
    $ request_23 = False 
    $ hermione_sleeping = True

    call music_block

    return

    