# Vous pouvez placer le script de votre jeu dans ce fichier.

init python:
    from math import sqrt

# Déclarez sous cette ligne les images, avec l'instruction 'image'
# ex: image eileen heureuse = "eileen_heureuse.png"

# Déclarez les personnages utilisés dans le jeu.
define lockedin = Character('???', color="#d4d4d4")
define mc = Character("[playername]",color="#0084ff")
define elizabeth = Character("Elizabeth",color="#034888")
define himgor = Character("Igor",color="#001930")

# Le jeu commence ici
label start:
    play music "character_creation.mp3" fadein 2.0

# 3D stage for the master layers
# j'ai juste fait un ctrl+c ctrl+v
    camera:
        perspective True

    show lock_avatar at center with fade:
        zpos -200
        warp sqrt 3.5 zpos 0

    lockedin "Salut. Tu es en ce moment dans un dimension qui va te\npermettre de rejondre l'autre monde."
    lockedin "Et pour le rejoindre, tu vas devoir me donner\nquelques informations sur ta personne."
    
    lockedin "Quel est ton nom ?"

    # input qui donne le nom du joueur 
    python :
        Elizabeth_Flag = False
        while True :
            playername = renpy.input("Ton nom (sans espaces, 10 charactères max):")
    
            if playername != "" and playername not in " " and len(playername) < 10:
                break
        playername = playername.capitalize()
    show lock_avatar :
        warp sqrt 0.5 xpos 350
    with None
    pause 0.5
    show screen show_created_name(playername)
    with dissolve

    lockedin "Tu viens de rentrer ton nom, merci beaucoup."
    hide screen show_created_name
    with dissolve
    show lock_avatar :
        warp sqrt 0.5 xpos 950
    lockedin "Maintenant, je vais utiliser ma PUISSANCE pour\nte tp dans l'autre monde."

    menu :
        lockedin "T'es prêt du coup ?"

        "Oui." :
            lockedin "D'accord. Prépare toi."
        
        "Non" :
            lockedin "You ARE going to {b}BRAZILLLL !!!"
# a reecrire un jour car en dessous de nos standards
    if playername == "Elizabeth":
        play music "Circustheme.mp3"
        hide lock_avatar

        show elizabeth at left:
            zpos 200 
            linear 1.0 xpos 200 
        elizabeth "Nuh uh you're not me."
        elizabeth "There can't be two Elizabeth in this world."
        hide elizabeth
        $ playername = "Elizabeth Wannabe"
        $ Elizabeth_Flag = True

        show igor
        himgor "Holy shit. \nYou fucking suck kid."
        himgor "Don't blame the AI for your awful tactics\nWhat fucking knob uses Act Freely"
        himgor "Use buffs dumbass,put down the\nguidebook and pickup some common sense"
        himgor "This game isn't even hard\n do not name yourself Elizabeth do you have some fetsih or something"
        himgor "you idiot"

    $ renpy.pause(2.0)
    
#Suite de la scene

label sequel:   
    # changement de scène go csmh >:)
    
    scene school
    
    #cacher Elizabeth et lockedin
    hide lock_avatar
    hide eliza

    show remy
    

    rmy "EHE viens ici toi je vais t'enlever tes {b}chaussettes"

    rmy "C'est interdit claquette chaussettes"

    rmy "La prochaine fois tu rentres pas à l'école"
    

    return
