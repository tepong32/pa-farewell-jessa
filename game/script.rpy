# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define me = Character("Teppy")
define you = Character("Jessa Marie")


# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg street_summer_night with pixellate
    play music "audio/farm-birds.ogg" fadeout 1.0 fadein 1.0
    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show fs mmm at right with dissolve
    ""
    show fs happy at right

    # These display lines of dialogue.

    me "Hellooooooo, Jessa!"
    me "Mabilisang gawa ng pa-Farewell dahil sa banat mo kagabi! haha!"
    show fs neutral
    me "Iba talaga kasi ung feeling ko dun sa pagkakasabi mo na yon, you know?"
    me "At saka, heto na rin. Sample kamo kasi ng love letter, di ba?"
    show fs ehe
    me "Ikaw na una kong bibigyan after a long, long while...tapos DIGITAL pa!"
    ""
    show fs happy
    me "Come on! Ang special ha? Dahil lang sa banat na:"
    hide fs happy
    show girl neutral at slightleft1 with dissolve
    you "\"Wala ka namang pa-farewell sakin\""
    hide girl neutral with dissolve
    show fs neutral at right
    me "..."
    hide fs neutral
    show fc haist at right with dissolve
    me "Sorry na kasi."
    show fc ehe
    me "Grabe lang yung:"
    hide fc ehe with dissolve
    show girl blush at slightleft1 with dissolve
    you "Ayaw mo talaga kasi akong i-close. Napilitan ka lang."
    hide girl blush with dissolve
    show fs ehe at right with dissolve
    me "May ganun ba? \nFeeling mo ba ganun??"
    show fs happy
    me "Well, para humaba 'to, iassume na lang natin na iniisip mo talagang ganun noon. Haha!"
    hide fs happy with dissolve

    scene bg livingroom_dark with pixellate
    "Palitan nating ng BG pang-flex. Charaught!"
    show fs neutral at right with dissolve
    me "So, May 6, 2022, 8 PM ako nagdecide mag-start. \nHanap ng sprites, rename ng files, etc.,etc."
    show fs neutral
    me "Bakit ko yun sinasabi?"
    show fs ehe
    me "Para malaman mong may effort 'to kahit madalian lang ginawa."
    me "Magpe-prepare pa para sa doggy time so, malamang umaga ko na 'to matatapos."
    show fs happy
    me "Di kita dadaldalin sa chat ngayon para makatapos ako. HAHAHA!"

    scene bg livingroom_day
    show fs ehe at right with dissolve
    "Buksan natin yung ilaw. Ang dilim e."
    show fs neutral
    me "So, wala nang masyadong effect effect to. \nMagbasa ka na lang, okay? Haha!"
    me "Ganito lang din ako gumawa ng love letter noon. Conversational type. Ems."
    me "Wala nang ako, ikaw, ako ikaw chuchu ha? \nBlack BG na lang para focus ka na sa letter."
    show fs happy
    me "Yiiiiieeee! Letter!"
    me "teka teka"
    hide fs happy with dissolve

    show mhm with pixellate
    ""
    "Yan na yung kalbo kamo. HAHAHA!"
    "Tago na nga natin yan."
    hide mhm with pixellate
    show fs ehe with dissolve
    me "So, ano naman ang sasabihin ko sayo dito?"
    me "Magpe-farewell ba ko e hindi naman yata bagay?"
    show fs smile
    me "Naisip ko lang talaga tong gawin kasi yung banat mo kagabi e matindi ang dating."
    me "May tama...tapos may mali. Haha!"
    me "\"Tama\" as in tagos. Dama. May laman. Ganon."
    me "\"Mali\" kasi....mali. Mali yung term na ayaw i-close. Hakdog ka."
    show fs neutral
    me "Ang ayaw ko e yung mabigyan nila ng malisya kase...ewan ko ba sa mga yon bat pilit akong pinagjojowa."
    show fs happy
    me "(...pero feeling ko ngayon pwede nang lagyan ng malisya e? HAHAHA Charot!)"
    show fs ehe
    ""
    ""
    show fs neutral
    me "So, ano nga ba yon? Bugso ba ng damdamin ung pagkakasabi mo nun gaya ng hinala ko?"
    hide fs neutral
    show girl neutral at slightleft1 with dissolve
    menu:
        "Oo... siguro?":
            hide girl neutral
            jump choice1_yes

        "Hindi...hindi rin ako sigurado.":
            hide girl neutral
            jump choice1_no

    label choice1_yes:
        show fc ehe with dissolve
        ""
        me "Hala bakit naman ganooooon? Haha!"
        show fc ehe
        me "Di ko tuloy alam sasabihin ko."
        me "Anyway, hindi ko naman malalaman kung ano pinili mong sagot kaya okay lang yan! Haha!"
        me "Try mo na nga lang yung isang option! >.<"
        hide fc ehe with dissolve
        jump choice1_done

    label choice1_no:
        show fc haist with dissolve
        ""
        me "Ganyan ka naman sumagot e...abnormal."
        me "Pero basta may tama yun kaya napagawa ako nito ngayon."
        me "...Website ung kinakana ko these past few days e...."
        hide fc haist with dissolve
        jump choice1_done

    label choice1_done:
        show fs smile at right with dissolve
        me "So, ayun na nga. Nevermind that first part na. Pinahaba ko lang talaga e. ;)"
        me "Pupunta pa pala ko jan sa bahay mo ulet. Pabakasyon."
        hide fs smile with dissolve
        show girl neutral at slightleft1 with dissolve

    menu:
        "Bawal. Solo na ko sa bahay.":
            hide girl neutral
            jump choice2_no

        "Drawing ka naman e.":
            hide girl neutral
            jump choice2_yes

    label choice2_no:
        show fc ehe at right with dissolve
        me "...... \nBat ko ba nilagay yun? haha"
        me "I-schedule naman ulet eeehh... Chachat ko ulit si mabustam. >.<"
        me "...o kaya sige, sa labas na lang den. Mag inom tayo para makita ko yung bully na ikaw. HAHA!"
        hide fc ehe
        jump choice2_done

    label choice2_yes:
        show fc haist at right with dissolve
        me "Circumstances lang naman kasi ung last time. E alam mo naman ung sitwasyon kaya pinagbigyan ko na."
        me "Isa pa, masyado talaga akong mabait. Charot."
        hide fc haist
        jump choice2_done

    label choice2_done:
        show fs ehe at right with dissolve
        me "Anyway, bahala na nga."
        me "Binigyan lang talaga kita ng sampol gaya ng hinihingi mo kaya ko ginawa 'to."
        show fs neutral
        me "Impromptu kaya di masyado organized yung thoughts...pagbigyan mo na."
        me "Pwede naman na siguro 'to for now...? \nIlang oras ko rin sya ginawa ha?"
        me ""
        me ""
        show fs happy
        me "Osya! Last shift mo na jan, galingan mo magpaalam sa kanila."
        me "Maggala ka pa ng maggala kase balik-bahay ka na naman next week! Haha!"
        me "Good night, Jessa! \nIngat pauwe."




    "the end--------"
    ""

    return
