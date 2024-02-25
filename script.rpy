# Vous pouvez placer le script de votre jeu dans ce fichier.

# Déclarez sous cette ligne les images, avec l'instruction 'image'
# ex: image eileen heureuse = "eileen_heureuse.png"

# Déclarez les personnages utilisés dans le jeu.
define lockedin = Character('The Lock In Avatar', color="#999898")
define mc = Character("[playername]",color="#0084ff")
define eliza = Character("Elizabeth",color="#034888")

# Le jeu commence ici
label start:
# j'ai juste fait un ctrl 
    camera:
        perspective True
    transform zbg:
        zpos -100 zzoom True
    
    scene lock_realm

    show lock_avatar at center:
        zpos 0
        linear 1.0 zpos 200

    show lock_avatar

    lockedin "Quel est ton nom inconnu au bataillon?"
    # input qui donne le nom du joueur
    $ playername = renpy.input("Quel est ton nom compatriote?")

    #si le nom du joueur est "Elizabeth" il sera change pour "Elizabeth Wannabe"
    if playername == "Elizabeth":
        show elizabeth at left:
            zpos 200 
            linear 1.0 xpos 200 
        eliza "Nuh uh you're not me"
        eliza "There can't be two Elizabeth in this world"
        show elizabeth:
            linear 1.0 xpos 200 
        hide elizabeth
        $ playername = "Elizabeth Wannabe"
    # [playername] est pour utiliser la variable playername
    lockedin "Bienvenu dans le locked in realm, [playername]"

    lockedin "Le lock in sont les raisons par lequelles le {b}grind se revele."

    lockedin "Seuls ceux qui sont locked in, peuvent achever leur lock in."

    lockedin "Atteindre son grind exige beaucoup de grind et une energie de sigma a toute epreuve."

    #ouvre un menu qui a deux choix oui ou non et affiche le texte correspondant
    menu:
        lockedin "es-tu un hunter?"

        "oui":
            mc "Oui monsieur je suis bel et bien un hunter."
            lockedin "Que ton grind soit rempli de grind."
        "non":
            mc "Qu'est-ce un hunter? je me sens tres faible."
            lockedin "Ta sentence est d'etre la plus grande des merguez, tu me decois beaucoup futur hunter."

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
