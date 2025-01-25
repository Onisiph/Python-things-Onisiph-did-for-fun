from tkinter import *
import random
import time
from random import choice

initial_size = 200
r = 10000

#---------------------------------User choice---------------------------------

bg_color = "black"
fg_color = "white"

Win_choice = Tk()
Win_choice.title("Windows configuration")
Win_choice.geometry("540x530+50+50")
Win_choice.config(background = bg_color)

if True: #All variables
    NB_Corner1 = 0
    NB_Corner2 = 0
    source_width = 0
    source_height = 0
    source_width2 = 0
    source_height2 = 0
    vitesse = 0
    vitesse2 = 0
    bg1 = "#eba6ff"
    fg1 = "purple"
    bg2 = "#66ffff"
    fg2 = "blue"
    B = ""
    P = ""

    fond_colore = 0
    couleur = ""
    timer = 0
    collisions = 0
    positions_en_direct = 0
    glitchy = 0
    variation_taille = 0
    vitesse_progressive = 0
    variation_vitesse = 0
    on_top = 0
    override_redirect = 0
    obstacle = 0
    obstacle_H = 0
    obstacle_V = 0
    obstacle_tournoyant = 0
    croissant = 0

    taskbar = 70
    base_speed_multiplier = 1
    base_size_multiplier = 2

N = "not"
M_C = "successfully changed" #No, "M_C" does not stand for MineCraft
F_C = "successfully changed"
S1 = "Size"
S2 = "Speed"
C = "Color"
T = "Timer"

Timing = StringVar(Win_choice)
Coloring = StringVar(Win_choice)
PurpleSuperScale = IntVar(Win_choice)
BlueSuperScale = IntVar(Win_choice)
Cancel = False

def tour_de_pass_pass():
    pass

def S_and_S_check():
    global source_width
    global source_height
    global source_width2
    global source_height2
    global vitesse
    global vitesse2
    txt = ""
    try:
        source_width = int(String_and_Var[0].get())
        source_height = source_width
        txt += f"{S1} {F_C}\n"
    except ValueError:
        source_width = 0
        source_height = 0
        txt += f"{S1} {N} {F_C}\n"
    try:
        vitesse = int(String_and_Var[1].get())
        txt += f"{S2} {F_C}"
    except ValueError:
        vitesse = 0
        txt += f"{S2} {N} {F_C}"
    Text_and_Check[1].config(text = txt, background = "Light slate blue")
    txt = ""
    try:
        source_width2 = int(String_and_Var[2].get())
        source_height2 = source_width2
        txt += f"{S1} {F_C}\n"
    except ValueError:
        source_width2 = 0
        source_height2 = 0
        txt += f"{S1} {N} {F_C}\n"
    try:
        vitesse2 = int(String_and_Var[3].get())
        txt += f"{S2} {F_C}"
    except ValueError:
        vitesse2 = 0
        txt += f"{S2} {N} {F_C}"
    Text_and_Check[3].config(text = txt, background = "Light slate blue")

def Timer_check():
    global timer
    try:
        timer = int(Timing.get())
        Timed_label.config(text = f"{T} {M_C}", background = "white")
    except ValueError:
        timer = 0
        Timed_label.config(text = f"{T} {N} {M_C}", background = "white")

def Color_check():
    global fond_colore
    global couleur
    if couleur != "":
        Text_Fonction_and_Button[-1].config(background = couleur)
    couleur = Coloring.get()
    try:
        Colored_label.config(background = couleur, text = f"{C} {F_C}")
        fond_colore = 1
    except TclError:
        couleur = ""
        if croissant:
            Colored_label.config(text = f"{C} {N} {F_C}\n(Il faut qu'elle soit écrite en anglais)", background = bg_color, foreground = fg_color)
        else:
            Colored_label.config(text = f"{C} {N} {F_C}", background = bg_color, foreground = fg_color)
        fond_colore = 0

def Sixth_row():
    global positions_en_direct 
    global glitchy 
    global variation_taille 
    if Most_of_the_stringvars[1].get() == "1":
        positions_en_direct = 1
        Most_of_the_checkbuttons[1].config(state = NORMAL, background = "spring green")
        Most_of_the_checkbuttons[5].config(state = DISABLED, background = "SpringGreen4")
        Most_of_the_checkbuttons[7].config(state = DISABLED, background = "SpringGreen4")
    elif Most_of_the_stringvars[7].get() == "1":
        glitchy = 1
        Most_of_the_checkbuttons[7].config(state = NORMAL, background = "spring green")
        Most_of_the_checkbuttons[1].config(state = DISABLED, background = "SpringGreen4")
        Most_of_the_checkbuttons[5].config(state = DISABLED, background = "SpringGreen4")
    elif Most_of_the_stringvars[5].get() == "1":
        variation_taille = 1
        Most_of_the_checkbuttons[5].config(state = NORMAL, background = "spring green")
        Most_of_the_checkbuttons[1].config(state = DISABLED, background = "SpringGreen4")
        Most_of_the_checkbuttons[7].config(state = DISABLED, background = "SpringGreen4")
    else:
        positions_en_direct = 0
        glitchy = 0
        variation_taille = 0
        Most_of_the_checkbuttons[1].config(state = NORMAL, background = "spring green")
        Most_of_the_checkbuttons[5].config(state = NORMAL, background = "spring green")
        Most_of_the_checkbuttons[7].config(state = NORMAL, background = "spring green")

def Seventh_row():
    global vitesse_progressive 
    global variation_vitesse 
    if Most_of_the_stringvars[2].get() == "1":
        vitesse_progressive = 1
        Most_of_the_checkbuttons[2].config(state = NORMAL, background = "MediumOrchid1")
        Most_of_the_checkbuttons[6].config(state = DISABLED, background = "MediumOrchid4")
    elif Most_of_the_stringvars[6].get() == "1":
        variation_vitesse = 1
        Most_of_the_checkbuttons[6].config(state = NORMAL, background = "MediumOrchid1")
        Most_of_the_checkbuttons[2].config(state = DISABLED, background = "MediumOrchid4")
    else:
        vitesse_progressive = 0
        variation_vitesse = 0
        Most_of_the_checkbuttons[2].config(state = NORMAL, background = "MediumOrchid1")
        Most_of_the_checkbuttons[6].config(state = NORMAL, background = "MediumOrchid1")

def un_active_collisions():
    global collisions
    global obstacle
    global obstacle_H
    global obstacle_V
    global obstacle_tournoyant
    if Most_of_the_stringvars[3].get() == "1":
        collisions = 1
        Most_of_the_checkbuttons[8].config(state=NORMAL, background = "turquoise1")
    else:
        collisions = 0
        Most_of_the_checkbuttons[8].config(state=DISABLED, background = "turquoise4")
        Obstacle_choice.config(state=DISABLED)
    if Most_of_the_stringvars[8].get() == "1" and Most_of_the_stringvars[3].get() == "1":
        Obstacle_choice.config(state=NORMAL)
        obstacle_type = Obstacle_choice.get()
        obstacle = 0
        obstacle_H = 0
        obstacle_V = 0
        obstacle_tournoyant = 0
        if obstacle_type == "Static obstacle" or obstacle_type == "Obstacle statique" or obstacle_type == "Cadenas statique":
            obstacle = 1
        elif obstacle_type == "Horizontal obstacle" or obstacle_type == "Obstacle horizontal" or obstacle_type == "Cadenas horizontal":
            obstacle_H = 1
        elif obstacle_type == "Vertical obstacle" or obstacle_type == "Obstacle vertical" or obstacle_type == "Cadenas vertical":
            obstacle_V = 1
        elif obstacle_type == "Spinning obstacle" or obstacle_type == "Obstacle tournoyant" or obstacle_type == "Cadenas tournoyant":
            obstacle_tournoyant = 1
    else:
        Obstacle_choice.config(state=DISABLED)

def thay_added_the_french_to_minecraft():
    '''If you were wondering, that's a quote from a NotVeryAndy video
    "Every Time Minecraft Got a 4th Dimension"'''
    global croissant
    global Most_of_the_checkbuttons_text, Text_and_Check, Text_Fonction_and_Button
    global N, M_C, F_C, S1, S2, C, T
    croissant = int(Most_of_the_stringvars[-1].get())
    if croissant:
        S1 = "Taille"
        S2 = "Vitesse"
        C = "Couleur"
        T = "Chrono"
        if random.randint(1, 100) == 1:
            croissant = "croissant"
        if not Talking_a_bit_before_changing_the_color:
            Slowly_changing_color.config(text = "Oh, salut!")
            Button_to_change_the_color.config(text = "Salut!")
    if croissant == "croissant":
        for i in range(len(Most_of_the_checkbuttons_text)):
            Most_of_the_checkbuttons_text[i] = ['Glaçage', 'Petit-déjeuner en direct', 'Mixage progressif', 'Porte du garde-manger', 'Garniture seulement', 'Variation de dîner', 'Variation de mixage', 'Déjeuner glitché', 'Cadenas sur la porte', "J'ai faim"][i]
            Most_of_the_checkbuttons[i].config(text = Most_of_the_checkbuttons_text[i])
        for i in range(4, len(Text_and_Check), 2):
            Text_and_Check[i] = ["", None, "", None, "← Taille des gâteaux →", None, "← Vitesse des gâteaux →", None, "Mélange pas bon\n↙                        ↓                      ↘", None, "← Mélange pas bon →", "This is a croissant ahahahahahahahahahahahahahahahah"][i]
        for i in range(5, len(Text_and_Check), 2):
            Text_and_Check[i].config(text = Text_and_Check[i-1])
        Text_Fonction_and_Button[0] = "Manger taille/vitesse"
        Text_Fonction_and_Button[1] = "Manger le chrono"
        Text_Fonction_and_Button[2] = "Manger la couleur du garde-manger"
        for i in range(12, 15):
            Text_Fonction_and_Button[i].config(text = Text_Fonction_and_Button[i-12])
        Obstacle_choice.config(values=["Cadenas tournoyant", "Cadenas vertical", "Cadenas horizontal", "Cadenas statique"])
        Bonuses.config(text = "← Croissants bonus →")
        tabulation[0].config(text = "↓ Couleur d'emballage ↘")
        tabulation[1].config(text = "↑ Couleur de glaçage ↗")
        if Talking_a_bit_before_changing_the_color == 14:
            entry_text = ["Ces entrées", "la couleur", "servent à changer", "des gâteaux"]
            for i in range(4):
                Color_changing_labels[i].config(text = entry_text[i])
            Color_changing_button[0].config(text = "Manger la couleur des gâteaux")
            Color_changing_button[1].config(text = "Réinitialiser")
            Slowly_changing_color.config(text = "À la prochaine!")
        Ending_button.config(text = "Créer les gâteaux")
        Cancel_button.config(text = "Détruire le repas :(")
        N = "non"
        M_C = "cuisiné avec succès"
        F_C = "cuisinée avec succès"
    elif croissant:
        for i in range(len(Most_of_the_checkbuttons_text)):
            Most_of_the_checkbuttons_text[i] = ['Fenêtres sur le dessus', 'Positions en direct', 'Vitesse progressive', 'Collisions', 'Override redirect', 'Variation de taille', 'Variation de vitesse', 'Effet glitché', 'Fenêtre obstacle', 'Croissant'][i]
            Most_of_the_checkbuttons[i].config(text = Most_of_the_checkbuttons_text[i])
        for i in range(4, len(Text_and_Check), 2):
            Text_and_Check[i] = ["", None, "", None, "← Taille des fenêtres →", None, "← Vitesse des fenêtres →", None, "Incompatible entre eux\n↙                        ↓                      ↘", None, "← Incompatible entre eux →", "This is a joke ahahahahahahahahahahahahahahahah"][i]
        for i in range(5, len(Text_and_Check), 2):
            Text_and_Check[i].config(text = Text_and_Check[i-1])
        Text_Fonction_and_Button[0] = "Vérifier taille/vitesse"
        Text_Fonction_and_Button[1] = "Vérifier le chrono"
        Text_Fonction_and_Button[2] = "Vérifier la couleur du fond"
        for i in range(12, 15):
            Text_Fonction_and_Button[i].config(text = Text_Fonction_and_Button[i-12])
        Obstacle_choice.config(values=["Obstacle tournoyant", "Obstacle vertical", "Obstacle horizontal", "Obstacle statique"])
        Bonuses.config(text = "← Coins bonus →")
        tabulation[0].config(text = "↓ Couleur de fond ↘")
        tabulation[1].config(text = "↑ Couleur de texte ↗")
        if Talking_a_bit_before_changing_the_color == 14:
            entry_text = ["Ces entrées", "la couleur", "servent à changer", "des fenêtres"]
            for i in range(4):
                Color_changing_labels[i].config(text = entry_text[i])
            Color_changing_button[0].config(text = "Vérifier la couleur des fenêtres")
            Color_changing_button[1].config(text = "Réinitialiser")
            Slowly_changing_color.config(text = "À la prochaine!")
        Ending_button.config(text = "Créer les fenêtres")
        Cancel_button.config(text = "Annuler la création")
        N = "non"
        M_C = "modifié avec succès"
        F_C = "modifiée avec succès"
    else:
        for i in range(len(Most_of_the_checkbuttons_text)):
            Most_of_the_checkbuttons_text[i] = ['Windows on top', 'Live positions', 'Progressive speed', 'Collisions', 'Override redirect', 'Size variation', 'Speed variation', 'Glitchy effect', 'Obstacle window', 'French'][i]
            Most_of_the_checkbuttons[i].config(text = Most_of_the_checkbuttons_text[i])
        for i in range(4, len(Text_and_Check), 2):
            Text_and_Check[i] = ["", None, "", None, "← Windows size →", None, "← Windows speed →", None, "Incompatible with each other\n↙                           ↓                         ↘", None, "← Incompatible with each other →", "This is a joke ahahahahahahahahahahahahahahahah"][i]
        for i in range(5, len(Text_and_Check), 2):
            Text_and_Check[i].config(text = Text_and_Check[i-1])
        Text_Fonction_and_Button[0] = "Checking size/speed"
        Text_Fonction_and_Button[1] = "Checking time"
        Text_Fonction_and_Button[2] = "Checking background color"
        for i in range(12, 15):
            Text_Fonction_and_Button[i].config(text = Text_Fonction_and_Button[i-12])
        Obstacle_choice.config(values=["Spinning obstacle", "Vertical obstacle", "Horizontal obstacle", "Static obstacle"])
        Bonuses.config(text = "← Bonuses corners →")
        tabulation[0].config(text = "↓ Background color ↘")
        tabulation[1].config(text = "↑ Foreground color ↗")
        if not Talking_a_bit_before_changing_the_color:
            Slowly_changing_color.config(text = "Oh, hey!")
            Button_to_change_the_color.config(text = "Hey!")
        elif Talking_a_bit_before_changing_the_color == 14:
            entry_text = ["These entries", "change the", "are used to", "windows colors"]
            for i in range(4):
                Color_changing_labels[i].config(text = entry_text[i])
            Color_changing_button[0].config(text = "Checking windows colors")
            Color_changing_button[1].config(text = "Reset")
            Slowly_changing_color.config(text = "See you next time!")
        Ending_button.config(text = "Create the windows")
        Cancel_button.config(text = "Cancel the creation")
        N = "not"
        M_C = "successfully changed"
        F_C = "successfully changed"
        S1 = "Size"
        S2 = "Speed"
        C = "Color"
        T = "Timer"

def scale_that_purple_scale(n):
    Purple_Bonus.config(background = ["#eba6ff", "#e074ff", "#d64afe", "#d02cff", "#c600ff", "#a800d8"][int(n)], foreground = ["purple", "purple2", "purple3", "purple4", "gray12", "black"][int(n)])

def scale_that_blue_scale(n):
    Blue_Bonus.config(background = ["#66ffff", "#36ffff", "#14ffff", "#00eded", "#00cece", "#00b1b1"][int(n)], foreground = ["blue", "blue2", "blue3", "blue4", "navy", "black"][int(n)])

def finished_choice():
    global NB_Corner1
    global NB_Corner2
    global on_top
    global override_redirect
    NB_Corner1 = PurpleSuperScale.get()
    NB_Corner2 = BlueSuperScale.get()
    if Most_of_the_stringvars[0].get() == "1":
        on_top = 1
    if Most_of_the_stringvars[4].get() == "1":
        override_redirect = 1
    S_and_S_check()
    Timer_check()
    Color_check()
    Sixth_row()
    Seventh_row()
    un_active_collisions()
    Win_choice.destroy()

def canceled_choice():
    global Cancel
    Cancel = True
    Win_choice.destroy()

if True: #Every configuration widgets
    Ligne = 0
    Colonne = 0
    String_and_Var = []
    S_and_S = []
    Text_and_Check = [""]
    for i in range(4):
        String_and_Var.append(StringVar(Win_choice))
        S_and_S.append(Entry(Win_choice, width=20, textvariable = String_and_Var[i]))
        S_and_S[i].grid(row = Ligne, column = Colonne, pady = 10)
        Ligne += 1
        if Ligne == 2:
            Text_and_Check.append(Label(Win_choice, width = 25, text=Text_and_Check[i-1], background = bg_color, foreground = "black"))
            Text_and_Check[i].grid(row = Ligne, column = Colonne, pady = 10)
            Text_and_Check.append("")
            Ligne = 0
            Colonne += 2
    Colonne = 1
    Ligne = 0
    Text_and_Check[-1] = "← Windows size →"
    for i in range(5, 8, 2):
        Text_and_Check.append(Label (Win_choice, width=25, text = Text_and_Check[i-1], background = "Light slate blue", foreground = "black"))
        Text_and_Check[i].grid(row = Ligne, column = Colonne, pady = 10)
        Ligne += 1
        Text_and_Check.append("← Windows speed →")
    Text_and_Check[-1] = "Incompatible with each other\n↙                           ↓                         ↘"
    Ligne = 5
    for i in range(9, 12, 2):
        Text_and_Check.append(Label (Win_choice, width=25, text = Text_and_Check[i-1], background = "spring green", foreground = "black"))
        Text_and_Check[i].grid(row = Ligne, column = Colonne, pady = 10)
        Ligne += 2
        Text_and_Check.append("← Incompatible with each other →")
    Text_and_Check.pop()
    Text_and_Check[-1].config(background = "MediumOrchid1", foreground = "black")
    Timed_entry = Entry(Win_choice, width = 20, textvariable = Timing)
    Timed_entry.grid(row = 3, column = 0, pady = 10)
    Timed_label = Label(Win_choice, text = "", width = 25, background = bg_color, foreground = "black")
    Timed_label.grid(row = 3, column = 2, pady = 10)
    Colored_entry = Entry(Win_choice, width = 20, textvariable = Coloring)
    Colored_entry.grid(row = 4, column = 0, pady = 10)
    Colored_label = Label(Win_choice, text = "", width = 25, background = bg_color, foreground = fg_color)
    Colored_label.grid(row = 4, column = 2, pady = 10)
    Ligne = 2
    Colonne = 1
    Text_Fonction_and_Button = ["Checking size/speed", "Checking time", "Checking background color", S_and_S_check, Timer_check, Color_check, "Light slate blue", "white", bg_color, "black", "black", fg_color]
    for i in range(12, 15):
        Text_Fonction_and_Button.append(Button(Win_choice, width = 27, text = Text_Fonction_and_Button[i-12], command = Text_Fonction_and_Button[i-9], background = Text_Fonction_and_Button[i-6], foreground = Text_Fonction_and_Button[i-3]))
        Text_Fonction_and_Button[i].grid(row = Ligne, column = Colonne, pady = 10)
        Ligne += 1
    Colonne = 0
    Most_of_the_stringvars = []
    Most_of_the_checkbuttons = []
    Most_of_the_checkbuttons_text = ["Windows on top", "Live positions", "Progressive speed", "Collisions", "Override redirect", "Size variation", "Speed variation", "Glitchy effect", "Obstacle window", "French"]
    Most_of_the_fonctions = [tour_de_pass_pass, Sixth_row, Seventh_row, un_active_collisions, tour_de_pass_pass, Sixth_row, Seventh_row, Sixth_row, un_active_collisions, thay_added_the_french_to_minecraft]
    Most_of_the_backgrounds = ["gold", "spring green", "MediumOrchid1", "turquoise1", "gold", "spring green", "MediumOrchid1", "spring green", "turquoise4", "blue"]
    for i in range(7):
        Most_of_the_stringvars.append(StringVar(Win_choice, False))
        Most_of_the_checkbuttons.append(Checkbutton(Win_choice, text=Most_of_the_checkbuttons_text[i], variable = Most_of_the_stringvars[i], onvalue=True, offvalue=False, command=Most_of_the_fonctions[i], background = Most_of_the_backgrounds[i], foreground = "black"))
        Most_of_the_checkbuttons[i].grid(row=Ligne, column = Colonne, pady = 10)
        Ligne += 1
        if Ligne == 9:
            Ligne = 5
            Colonne = 2
    Ligne = 6
    Colonne = 1
    for i in range(2):
        Most_of_the_stringvars.append(StringVar(Win_choice, False))
        Most_of_the_checkbuttons.append(Checkbutton(Win_choice, text=Most_of_the_checkbuttons_text[i+7], variable = Most_of_the_stringvars[i+7], onvalue=True, offvalue=False, command=Most_of_the_fonctions[i+7], background = Most_of_the_backgrounds[i+7], foreground = "black"))
        Most_of_the_checkbuttons[i+7].grid(row=Ligne, column = Colonne, pady = 10)
        Ligne += 2
    Most_of_the_checkbuttons[-1].config(state = DISABLED)
    Ligne = 10
    Colonne = 1
    Most_of_the_stringvars.append(StringVar(Win_choice, False))
    Most_of_the_checkbuttons.append(Checkbutton(Win_choice, text=Most_of_the_checkbuttons_text[-1], variable = Most_of_the_stringvars[-1], onvalue=True, offvalue=False, command=Most_of_the_fonctions[-1], background = Most_of_the_backgrounds[-1], foreground = "white"))
    Most_of_the_checkbuttons[-1].grid(row=Ligne, column = Colonne, pady = 10)
    Obstacle_choice = Spinbox(Win_choice, width = 20, values=["Spinning obstacle", "Vertical obstacle", "Horizontal obstacle", "Static obstacle"], state = DISABLED, command = un_active_collisions, background = "turquoise1", foreground = "black", disabledbackground = "turquoise4")
    Obstacle_choice.grid(row = 8, column = 2, pady = 10)
    Bonuses = Label(Win_choice, width = 20, text = "← Bonuses corners →", background = "Light slate blue")
    Bonuses.grid(row = 9, column = 1, pady = 10)
    Purple_Bonus = Scale(Win_choice, from_=0, to=5, showvalue=True, variable=PurpleSuperScale, tickinterval=1, orient='h', command = scale_that_purple_scale, background = "#eba6ff", foreground = "purple")
    Purple_Bonus.grid(row = 9, column=0)
    Blue_Bonus = Scale(Win_choice, from_=0, to=5, showvalue=True, variable=BlueSuperScale, tickinterval=1, orient='h', command = scale_that_blue_scale, background = "#66ffff", foreground = "blue")
    Blue_Bonus.grid(row = 9, column=2)
    def color_changing_initialisation():
        global Talking_a_bit_before_changing_the_color
        if croissant:
            label_text = ["Je m'attendais pas à te voir ici", "Comment tu m'as trouvé(e)?", "", "Je vois", "Eh bien, vu que tu m'as trouvé(e), je vais te donner quelque chose", "Laisse-moi juste...", "Voilà!", "Comment-ça, ça ne marche pas?", "Attends, je devrais pouvoir le réparer", "En théorie, j'ai juste à faire cela", "faire ceci", "Ajouter ce truc ici, qu'importe ce que c'est", "Et ça devrait être bon", "À la prochaine!"]
            button_text = ["Moi non plus", "Eh bien, je...", "", "", "Qu'est-ce que c'est?", "Prend ton temps", "Merci!", "", "", "", "", "", "Merci!²", "o/"]
            entry_text = ["Ces entrées", "servent à changer", "la couleur", "des fenêtres"]
            if croissant == "croissant":
                entry_text[-1] = "des gâteaux"
        else:
            label_text = ["I didn't expected to see you there", "How did you find me?", "", "I see", "Well, since you found me, I'll give you a little something", "Let me just...", "Here you go!", "What do you mean, this doesn't work?", "Wait, I should be able to fix this", "In theory, I just have to do that", "Do this", "Add that thing here, whatever it is", "And that should be good", "See you next time!"]
            button_text = ["Me neither", "Well, I...", "", "", "What is it?", "Take your time", "Thanks!", "", "", "", "", "", "Thanks!²", "o/"]
            entry_text = ["These entries", "are used to", "change the", "windows colors"]
        if Talking_a_bit_before_changing_the_color < len(label_text):
            Slowly_changing_color.config(text = label_text[Talking_a_bit_before_changing_the_color])
            Button_to_change_the_color.config(text = button_text[Talking_a_bit_before_changing_the_color])
            Talking_a_bit_before_changing_the_color += 1
        if Talking_a_bit_before_changing_the_color == 7:
            Row = 2
            Column = 3
            for i in range(4):
                Color_changing_stringvars.append(StringVar(Win_choice))
                Color_changing_entries.append(Entry(Win_choice, width = 20, textvariable = Color_changing_stringvars[i], state = DISABLED, background = "gray60"))
                Color_changing_entries[i].grid(row = Row, column = Column, pady = 10)
                Row += 1
                if Row == 4:
                    Row = 2
                    Column += 1
            Row = 5
            Column = 3
            if croissant:
                This_list_is_not_working = ["Ça", "fonctionne", "ne", "pas"]
            else:
                This_list_is_not_working = ["This", "not", "is", "working"]
            for i in range(4):
                Color_changing_labels.append(Label(Win_choice, width = 20, text = This_list_is_not_working[i]))
                Color_changing_labels[i].grid(row = Row, column = Column, pady = 10)
                Row += 1
                if Row == 7:
                    Row = 5
                    Column += 1
            if croissant == "croissant":
                Color_changing_button.append(Button(Win_choice, width = 22, text = "Galette des rois", command = color_changing, background = "gray40"))
            elif croissant:
                Color_changing_button.append(Button(Win_choice, width = 22, text = "Bouton de test", command = color_changing, background = "gray40"))
            else:
                Color_changing_button.append(Button(Win_choice, width = 22, text = "Test button", command = color_changing, background = "gray40"))
            Color_changing_button[0].grid(row = 4, column = 4, pady = 10)
            if croissant:
                R = "Réinitialiser"
            else:
                R = "Reset"
            Color_changing_button.append(Button(Win_choice, width = 20, text = R, command = color_changing, state = DISABLED))#, background="Light slate blue", foreground="black"))
            Color_changing_button[1].grid(row = 0, column = 3, pady = 10)
            Slowly_changing_color.config(state = DISABLED)
            Button_to_change_the_color.config(state = DISABLED)
            tabulation[0].config(width = 20, background = "white", foreground = "black")
            tabulation[1].config(background = "white", foreground = "black")
            Win_choice.update()
        elif Talking_a_bit_before_changing_the_color == 10:
            Color_changing_labels[0].config(text = entry_text[0])
            Color_changing_button[1].config(background="Light slate blue", foreground="black", state = NORMAL)
            Color_changing_entries[0].config(state = NORMAL, background = "white")
        elif Talking_a_bit_before_changing_the_color == 11:
            Color_changing_labels[2].config(text = entry_text[1])
            tabulation[0].config(background = bg1, foreground=fg1)
            Color_changing_entries[2].config(state = NORMAL, background = "white")
        elif Talking_a_bit_before_changing_the_color == 12:
            Color_changing_labels[1].config(text = entry_text[2])
            tabulation[1].config(background = bg2, foreground=fg2)
            Color_changing_entries[1].config(state = NORMAL, background = "white")
        elif Talking_a_bit_before_changing_the_color == 13:
            Color_changing_labels[3].config(text = entry_text[3])
            if croissant == "croissant":
                Color_changing_button[0].config(background="Light slate blue", foreground="black", text = "Manger la couleur des gâteaux", width = 22)
            elif croissant:
                Color_changing_button[0].config(background="Light slate blue", foreground="black", text = "Vérifier la couleur des fenêtres", width = 22)
            else:
                Color_changing_button[0].config(background="Light slate blue", foreground="black", text = "Checking windows colors", width = 22)
            Color_changing_entries[3].config(state = NORMAL, background = "white")
        elif Talking_a_bit_before_changing_the_color == 14:
            Color_changing_button[0].config(state = NORMAL)
            Slowly_changing_color.config(width = 20)
            
    def color_changing():
        global bg1, fg1, bg2, fg2, B, P
        if Talking_a_bit_before_changing_the_color < 14:
            Color_changing_button[0].config(state = DISABLED)
            Slowly_changing_color.config(state = NORMAL, text = "")
            if croissant == "croissant":
                Button_to_change_the_color.config(state = NORMAL, text = "Ça ne se mange pas")
            elif croissant:
                Button_to_change_the_color.config(state = NORMAL, text = "Ça ne marche pas")
            else:
                Button_to_change_the_color.config(state = NORMAL, text = "This doesn't work")
        else:
            if bg1 != "#eba6ff":
                Color_changing_labels[1].config(background = bg1)
            if fg1 != "purple":
                Color_changing_labels[1].config(foreground = fg1)
            if bg2 != "#66ffff":
                Color_changing_labels[3].config(background = bg2)
            if fg2 != "blue":
                Color_changing_labels[3].config(foreground = fg2)
            
            try:
                Color_changing_labels[0].config(background = Color_changing_entries[0].get())
                bg1 = Color_changing_entries[0].get()
                P = bg1
            except TclError:
                Color_changing_labels[0].config(background = fg_color)
            try:
                Color_changing_labels[0].config(foreground = Color_changing_entries[1].get())
                fg1 = Color_changing_entries[1].get()
            except TclError:
                Color_changing_labels[0].config(foreground = bg_color)
            
            try:
                Color_changing_labels[2].config(background = Color_changing_entries[2].get())
                bg2 = Color_changing_entries[2].get()
                B = bg2
            except TclError:
                Color_changing_labels[2].config(background = fg_color)
            try:
                Color_changing_labels[2].config(foreground = Color_changing_entries[3].get())
                fg2 = Color_changing_entries[3].get()
            except TclError:
                Color_changing_labels[2].config(foreground = bg_color)
            '''bg1 = "#eba6ff"
            P = ""
            fg1 = "purple"
            bg2 = "#66ffff"
            B = ""
            fg2 = "blue"'''
    
    Talking_a_bit_before_changing_the_color = 0
    tabulation = []
    tabulation.append(Label(Win_choice, width = 50, text = "↓ Background color ↘", background = bg_color, foreground = bg_color))
    tabulation[0].grid(row = 1, column = 3, pady = 10)
    tabulation.append(Label(Win_choice, width = 20, text = "↑ Foreground color ↗", background = bg_color, foreground = bg_color))
    tabulation[1].grid(row = 4, column = 3, pady = 10)
    Slowly_changing_color = Label(Win_choice, width = 50, text = "Oh, hey!", background="gold")
    Slowly_changing_color.grid(row = 0, column = 4, pady = 10)
    Button_to_change_the_color = Button(Win_choice, width = 20, text = "Hey!", command = color_changing_initialisation, background="gold2")
    Button_to_change_the_color.grid(row = 1, column = 4, pady = 10)
    Color_changing_stringvars = []
    Color_changing_entries = []
    Color_changing_labels = []
    Color_changing_button = []
    Ending_button = Button(Win_choice, width = 18, text="Create the windows", foreground="black", background="IndianRed1", command = finished_choice)
    Ending_button.grid(row = 10, column = 0, pady = 10)
    Cancel_button = Button(Win_choice, width = 18, text="Cancel the creation", foreground="black", background="IndianRed1", command = canceled_choice)
    Cancel_button.grid(row = 10, column = 2, pady = 10)

Win_choice.protocol("WM_DELETE_WINDOW", canceled_choice)
Win_choice.update()
Win_choice.mainloop()

if Cancel is False:
    if source_width < initial_size:
        source_width = initial_size
        source_height = initial_size
    if source_width2 < initial_size:
        source_width2 = initial_size
        source_height2 = initial_size
    if obstacle:
        source_width2 *= base_size_multiplier
        source_height2 *= base_size_multiplier
    if vitesse <= 0:
        vitesse = 1
    if vitesse2 <= 0:
        vitesse2 = 1
    if override_redirect:
        taskbar -= 30
    if vitesse_progressive:
        speed_cap = 20
        limiteur_prise_de_vitesse = 10
    if variation_taille:
        size_change = 50
    if collisions:
        difference = "vitesse"
    if obstacle_tournoyant:
        inverse = 0
    if glitchy:
        number_of_labels = 7
        number_of_letters = 15
        taille = 30
        vitesse *= 2
        vitesse2 *= 2
        letter_str = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz 1234567890œ&é'([{#~-|è`_\ç^à@ù%*µ)]}=ê$£ë¥Ù⁴³²¹¬ß®©»«ÔÎÛðæ±ÊøÂ¶ôîûýþ€åâ¡÷×¿§/.?ºẞ‘><ÖÏÜÐÆªËÄöïüÝÞÇ¢Åä¦†‡ඞƒñÑšžŸ¤™☺☻♣♠♥♦⌂♂♀♪♫☼·•◘○◙↑↓←→↖↗↘↙⮐⮑⇦⇧⇨⇩↺↻↕↔↨▲▼◄►︿‹–—˜„‼…½¼¾‰║╣╗╝╚╔╠╦═╬┐└┴┬├─┼┤│∟¯┌┘ı█▄▀▬■░▒▓✔"
    if croissant == "croissant":
        C = "croissants"
        F_Win = "Premier gâteau : "
        S_Win = "Second gâteau : "
    elif croissant:
        C = "coins"
        F_Win = "Première fenêtre : "
        S_Win = "Seconde fenêtre : "
    else:
        C = "corners"
        F_Win = "First window : "
        S_Win = "Second window : "
    #---------------------------------Initialisation---------------------------------
    
    finish_everything = Tk()
    finish_everything.title("Game over")
    finish_everything.geometry(f"227x50+{finish_everything.winfo_screenwidth()-235}+{finish_everything.winfo_screenheight()-50-70}")
    finish_everything.config(background = "black")
    def ending_everything():
        global loop
        print("Game over!")
        loop = False
    def pausing_everything():
        print("WHY IS IT NOT WORKING AAAAAAAAAAAAA")
        '''global Pause
        global pause_timer
        Pause = 1 - Pause
        if Pause:
            if timer:
                pause_timer = int(time.time())'''
    if croissant:
        D_E_text = "Fermer les fenêtres"
        S_E_text = "Stopper les fenêtres"
    else:
        D_E_text = "Closing the windows"
        S_E_text = "Pausing the windows"
    destroy_everything = Button(finish_everything, width = 31, text = D_E_text, command = ending_everything, background = "IndianRed3", foreground = "black")
    destroy_everything.grid(row = 0, column = 0, pady = 10)
    stop_everything = Button(finish_everything, width = 31, text = S_E_text, command = pausing_everything, background = "IndianRed3", foreground = "black")
    #stop_everything.grid(row = 1, column = 0, pady = 10)
    finish_everything.update()
    
    loop = True
    Pause = 0
    size = source_width // 8
    size2 = source_width2 // 8
    x = 500
    y = 500
    x2 = 500
    y2 = 500

    if fond_colore:
        BG = Tk()
        BG.title("Background")
        BG.geometry(f"{BG.winfo_screenwidth()}x{BG.winfo_screenheight()}+0+0")
        BG.configure(background=couleur)
        BG.update()

    fenetre2 = Tk() 
    fenetre2.title("Corner game 2")
    fenetre2.geometry(f"{source_width2}x{source_height2}+{x2}+{y2}")
    if on_top:
        fenetre2.attributes("-topmost", True)
    if override_redirect:
        fenetre2.overrideredirect(True)
    if positions_en_direct:
        CORNER2 = Label(fenetre2, width=10, text=("NB " + C + " : " + str(NB_Corner2)), font=('Times New Roman', size, 'bold'), foreground=fg2, background=bg2)
        CORNER_X2 = Label(fenetre2, width=10, text=str(x2), font=('Times New Roman', size, 'bold'), foreground=fg2, background=bg2)
        CORNER_Y2 = Label(fenetre2, width=10, text=str(y2), font=('Times New Roman', size, 'bold'), foreground=fg2, background=bg2)
        CORNER2.grid(row=0, column=0, pady=10)
        CORNER_X2.grid(row=1, column=0, pady=10)
        CORNER_Y2.grid(row=2, column=0, pady=10)
    elif glitchy:
        fenetre2.configure(background=bg2)
        labels1 = []
        for i in range(number_of_labels):
            labels1.append(Label(fenetre2, text = 'a', font=("Helvetica", taille), foreground = fg2, background = bg2))
            labels1[i].pack(expand=True)
    else:
        fenetre2.configure(background=bg2)
        CORNER2 = Label(fenetre2, text=str(NB_Corner2), font=('Times New Roman', size2*3, 'bold'), foreground=fg2, background=bg2)
        CORNER2.pack(expand=True)

    fenetre = Tk() 
    fenetre.title("Corner game 1")
    fenetre.geometry(f"{source_width}x{source_height}+{x}+{y}")
    if on_top:
        fenetre.attributes("-topmost", True)
    if override_redirect:
        fenetre.overrideredirect(True)
    if positions_en_direct:
        CORNER = Label(fenetre, width=10, text=("NB " + C + " : " + str(NB_Corner1)), font=('Times New Roman', size2, 'bold'), foreground=fg1, background=bg1)
        CORNER_X = Label(fenetre, width=10, text=str(x), font=('Times New Roman', size2, 'bold'), foreground=fg1, background=bg1)
        CORNER_Y = Label(fenetre, width=10, text=str(y), font=('Times New Roman', size2, 'bold'), foreground=fg1, background=bg1)
        CORNER.grid(row=0, column=0, pady=10)
        CORNER_X.grid(row=1, column=0, pady=10)
        CORNER_Y.grid(row=2, column=0, pady=10)
    elif glitchy:
        fenetre.configure(background=bg1)
        labels2 = []
        for i in range(number_of_labels):
            labels2.append(Label(fenetre, text = 'a', font=("Helvetica", taille), foreground =fg1, background=bg1))
            labels2[i].pack(expand=True)
    else:
        fenetre.configure(background=bg1)
        CORNER = Label(fenetre, text=str(NB_Corner1), font=('Times New Roman', size*3, 'bold'), foreground=fg1, background=bg1)
        CORNER.pack(expand=True)

    screen_width = fenetre.winfo_screenwidth() - source_width
    screen_height = fenetre.winfo_screenheight() - source_height - taskbar
    screen_width2 = fenetre.winfo_screenwidth() - source_width2
    screen_height2 = fenetre.winfo_screenheight() - source_height2 - taskbar
    x_random1 = 1
    x_random2 = screen_width - 1
    y_random1 = 1
    y_random2 = screen_height - 1

    def corner1_random():
        global x
        global y
        x = random.randint(x_random1, x_random2)
        y = random.randint(y_random1, y_random2)
        if collisions:
            if (x < x2 + source_width2 - vitesse and x + source_width - vitesse > x2) or (y < y2 + source_height2 and y + source_height > y2):
                corner1_random()

    def corner2_random():
        global x2
        global y2
        x2 = random.randint(x_random1, x_random2)
        y2 = random.randint(y_random1, y_random2)
        if collisions:
            if (x < x2 + source_width2 - vitesse and x + source_width - vitesse > x2) or (y < y2 + source_height2 and y + source_height > y2):
                corner2_random()

    def positions():
        CORNER_X.config(text=("X : " + str(x)))
        CORNER_Y.config(text=("Y : " + str(y)))
        CORNER_X2.config(text=("X : " + str(x2)))
        CORNER_Y2.config(text=("Y : " + str(y2)))

    def speed_up(D):
        if random.randint(1, limiteur_prise_de_vitesse) == 1:
            if D < 0:
                if D > (speed_cap * -1):
                    D -= 1
            else:
                if D < speed_cap:
                    D += 1
        return D

    def screen_size_change():
        global screen_width
        global screen_height
        global screen_width2
        global screen_height2
        screen_width = fenetre.winfo_screenwidth() - source_width
        screen_height = fenetre.winfo_screenheight() - source_height - taskbar
        screen_width2 = fenetre.winfo_screenwidth() - source_width2
        screen_height2 = fenetre.winfo_screenheight() - source_height2 - taskbar

    def collisions_sans_probleme():
        global deplacement_X
        global deplacement_Y
        global deplacement_Y2
        global deplacement_X2
        if obstacle_tournoyant:
            global inverse
        if (x < (x2 + source_width2 - (vitesse + difference))) and ((x + source_width - (vitesse + difference)) > x2):
            if (y >= y2 and y <= y2 + source_height2) or (y + source_height >= y2 and y + source_height <= y2 + source_height2):
                deplacement_Y *= -1
                deplacement_Y2 *= -1
                if vitesse_progressive:
                    deplacement_Y = speed_up(deplacement_Y)
                    if not obstacle_V and not obstacle_tournoyant:
                        deplacement_Y2 = speed_up(deplacement_Y2)
                if obstacle_tournoyant and deplacement_Y2 != 0:
                    inverse = 1 - inverse
        elif (y < (y2 + source_height2)) and ((y + source_height) > y2):
            if (x >= x2 and x <= x2 + source_width2) or (x + source_width >= x2 and x + source_width <= x2 + source_width2):
                deplacement_X *= -1
                deplacement_X2 *= -1
                if vitesse_progressive:
                    deplacement_X = speed_up(deplacement_X)
                    if not obstacle_H and not obstacle_tournoyant:
                        deplacement_X2 = speed_up(deplacement_X2)
                if obstacle_tournoyant and deplacement_X2 != 0:
                    inverse = 1 - inverse

    def chrono(T):
        if T >= 3600:
            t = T // 3600
            t2 = (T / 3600) - t
            t2 *= 60
            return str(t) + H + add + str(int(t2)) + " minutes"
        elif T >= 60:
            t = T // 60
            return str(t) + " minutes" + add + str(T % 60) + S
        else:
            return str(T) + S

    def letters():
        for i in range(number_of_labels):
            s = ''.join([choice(letter_str) for k in range(number_of_letters)])
            labels1[i].config(text = s)
            fenetre.update()
        for i in range(number_of_labels):
            s = ''.join([choice(letter_str) for k in range(number_of_letters)])
            labels2[i].config(text = s)
            fenetre2.update()

    corner1_random()
    if obstacle_tournoyant:
        x2 = 0
        y2 = 0
    else:
        corner2_random()

    deplacement_X = vitesse * choice([-1, 1])
    deplacement_Y = vitesse * choice([-1, 1])
    if obstacle:
        deplacement_X2 = 0
        deplacement_Y2 = 0
    elif obstacle_V:
        deplacement_X2 = 0
        deplacement_Y2 = vitesse2 * base_speed_multiplier * choice([-1, 1])
    elif obstacle_H:
        deplacement_X2 = vitesse2 * base_speed_multiplier * choice([-1, 1])
        deplacement_Y2 = 0
    else:
        deplacement_X2 = vitesse2 * choice([-1, 1])
        deplacement_Y2 = vitesse2 * choice([-1, 1])
    if collisions:
        if difference == "vitesse":
            difference = vitesse

    def move_window():
        if True:
            global source_width
            global source_height
            global source_width2
            global source_height2
            
            global screen_width
            global screen_height
            global screen_width2
            global screen_height2
            
            global x
            global y
            global deplacement_X
            global deplacement_Y
            global NB_Corner1
            
            global x2
            global y2
            global deplacement_X2
            global deplacement_Y2
            global NB_Corner2
        
        #---------------------------------Première fenêtre---------------------------------
        
        direction = 0
        x += deplacement_X
        y += deplacement_Y
        fenetre.geometry(f"{source_width}x{source_height}+{x}+{y}")
        fenetre.update()
        
        if x >= screen_width or x <= (x_random1 - 1):
            deplacement_X *= -1
            direction += 1
            if vitesse_progressive:
                deplacement_X = speed_up(deplacement_X)
        
        if y >= screen_height or y <= (y_random1 - 1):
            deplacement_Y *= -1
            direction += 1
            if vitesse_progressive:
                deplacement_Y = speed_up(deplacement_Y)
        
        if collisions:
            collisions_sans_probleme()
        
        if direction == 2:
            NB_Corner1 += 1
            print(F_Win + str(NB_Corner1) + " " + C)
            if not glitchy:
                if positions_en_direct:
                    CORNER.config(text="NB " + C + " : " + str(NB_Corner1))
                else:
                    CORNER.config(text=str(NB_Corner1))
            if vitesse_progressive:
                deplacement_X = vitesse
                deplacement_Y = vitesse
            if variation_vitesse and not obstacle_H and not obstacle_V:
                deplacement_X2 *= 2
                deplacement_Y2 *= 2
                if deplacement_X < -1 or deplacement_X > 1:
                    deplacement_X = deplacement_X // 2
                    deplacement_Y = deplacement_Y // 2
            if variation_taille:
                if source_width > size_change:
                    source_width -= size_change
                    source_height -= size_change
                source_width2 += size_change
                source_height2 += size_change
                screen_size_change()
            corner1_random()
        
        if random.randint(1, r) == 1:
            if deplacement_X > 0:
                for i in range(deplacement_X):
                    a = random.randint(0, 5)
                    x += a
                    a = random.randint(0, 5)
                    y += a
            elif deplacement_X < 0:
                for i in range(0, deplacement_X, -1):
                    a = random.randint(0, 5)
                    x += a
                    a = random.randint(0, 5)
                    y += a
        
        #---------------------------------Deuxième fenêtre---------------------------------
        if not obstacle_tournoyant:
            direction2 = 0
            x2 += deplacement_X2
            y2 += deplacement_Y2
            fenetre2.geometry(f"{source_width2}x{source_height2}+{x2}+{y2}")
            fenetre2.update()
            
            if x2 >= screen_width2 or x2 <= (x_random1 - 1):
                deplacement_X2 *= -1
                direction2 += 1
                if vitesse_progressive:
                    deplacement_X2 = speed_up(deplacement_X2)
            
            if y2 >= screen_height2 or y2 <= (y_random1 - 1):
                deplacement_Y2 *= -1
                direction2 += 1
                if vitesse_progressive:
                    deplacement_Y2 = speed_up(deplacement_Y2)
            
            if direction2 == 2:
                NB_Corner2 += 1
                print(S_Win + str(NB_Corner2) + " " + C)
                if not glitchy:
                    if positions_en_direct:
                        CORNER2.config(text="NB " + C + " : " + str(NB_Corner2))
                    else:
                        CORNER2.config(text=str(NB_Corner2))
                if vitesse_progressive:
                    deplacement_X2 = vitesse
                    deplacement_Y2 = vitesse
                if variation_vitesse:
                    deplacement_X *= 2
                    deplacement_Y *= 2
                    if deplacement_X2 < -1 or deplacement_X2 > 1:
                        deplacement_X2 = deplacement_X2 // 2
                        deplacement_Y2 = deplacement_Y2 // 2
                if variation_taille:
                    if source_width2 > size_change:
                        source_width2 -= size_change
                        source_height2 -= size_change
                    source_width += size_change
                    source_height += size_change
                    screen_size_change()
                corner2_random()
            
            if random.randint(1, r) == 1:
                if deplacement_X2 > 0:
                    for i in range(deplacement_X2):
                        a = random.randint(0, 5)
                        x2 += a
                        a = random.randint(0, 5)
                        y2 += a
                elif deplacement_X2 < 0:
                    for i in range(0, deplacement_X2, -1):
                        a = random.randint(0, 5)
                        x2 += a
                        a = random.randint(0, 5)
                        y2 += a
        else:
            if not inverse:
                if x2 == 0 and y2 == 0:
                    deplacement_X2 = vitesse
                    deplacement_Y2 = 0
                elif x2 == screen_width2 and y2 == 0:
                    deplacement_X2 = 0
                    deplacement_Y2 = vitesse
                elif x2 == screen_width2 and y2 == screen_height2:
                    deplacement_X2 = vitesse * -1
                    deplacement_Y2 = 0
                elif x2 == 0 and y2 == screen_height2:
                    deplacement_X2 = 0
                    deplacement_Y2 = vitesse * -1
            else:
                if x2 == 0 and y2 == 0:
                    deplacement_X2 = 0
                    deplacement_Y2 = vitesse
                elif x2 == screen_width2 and y2 == 0:
                    deplacement_X2 = vitesse * -1
                    deplacement_Y2 = 0
                elif x2 == screen_width2 and y2 == screen_height2:
                    deplacement_X2 = 0
                    deplacement_Y2 = vitesse * -1
                elif x2 == 0 and y2 == screen_height2:
                    deplacement_X2 = vitesse
                    deplacement_Y2 = 0
            x2 += deplacement_X2
            y2 += deplacement_Y2
            fenetre2.geometry(f"{source_width2}x{source_height2}+{x2}+{y2}")
        
        if positions_en_direct:
            positions()
        if glitchy:
            letters()
                    
    if timer:
        current_time = int(time.time())
        compteur = 0
        pause_timer = 0
        if croissant:
            half_of_the_sentence = "Il reste donc "
            quarter_of_the_sentence = "!"
            H = " heures"
            add = " et "
            Time_is_down_hehe_you_got_the_joke_question_mark = " du temps est écoulé!"
            one = "Un quart"
            two = "La moitié"
            three = "Trois quarts"
        else:
            half_of_the_sentence = "So there are "
            quarter_of_the_sentence = " left!"
            H = " hours"
            add = " and "
            Time_is_down_hehe_you_got_the_joke_question_mark = " of the time is up!"
            one = "A quarter"
            two = "Half"
            three = "Three quarters"
            
    if croissant:
        S = " secondes"
        win2 = ") gagne!"
        After_3_minutes = "Égalité!"
        Add_obstacle = "Et l'"
        What = ", d'un manière ou d'une autre, a fait "
        I_did_it = "a fait "
        if croissant == "croissant":
            beginning = "Le"
            win = " gâteau ("
            first_one = " premier"
            if not B:
                B = "bleu"
            if not P:
                P = "violet"
        else:
            beginning = "La"
            win = " fenêtre ("
            first_one = " première"
            if not B:
                B = "bleue"
            if not P:
                P = "violette"
    else:
        S = " seconds"
        beginning = "The"
        win = " window ("
        win2 = ") win!"
        first_one = " first"
        if not B:
            B = "blue"
        if not P:
            P = "purple"
        After_3_minutes = "Tie!"
        Add_obstacle = "And the "
        What = " somehow did "
        I_did_it = "did "
    
    while loop:
        if not Pause:
            move_window()
            if timer > 0:
                if int(time.time()) >= current_time + (timer // 4) and compteur == 0:
                    print(one + Time_is_down_hehe_you_got_the_joke_question_mark)
                    print(half_of_the_sentence + chrono((timer // 4) * 3) + quarter_of_the_sentence)
                    compteur += 1
                elif int(time.time()) >= current_time + (timer // 2) and compteur == 1:
                    print(two + Time_is_down_hehe_you_got_the_joke_question_mark)
                    print(half_of_the_sentence + chrono(timer // 2) + quarter_of_the_sentence)
                    compteur += 1
                elif int(time.time()) >= current_time + ((timer // 4) * 3) and compteur == 2:
                    print(three + Time_is_down_hehe_you_got_the_joke_question_mark)
                    print(half_of_the_sentence + chrono((timer // 4)) + quarter_of_the_sentence)
                    compteur += 1
                elif int(time.time()) >= (current_time + timer):
                    loop = False
        else:
            if timer and int(time.time()) >= pause_timer + 1:
                current_time += 1
                print(current_time)
                pause_timer = int(time.time())
    
    fenetre.destroy()
    fenetre2.destroy()
    finish_everything.destroy()
    if not obstacle and not obstacle_H and not obstacle_V and not obstacle_tournoyant:
        if NB_Corner1 > NB_Corner2:
            print(beginning + first_one + win + P + win2)
        elif NB_Corner1 < NB_Corner2:
            minus = -1
            if croissant == "croissant":
                minus -= 1
            print(beginning + S[:minus] + win + B + win2)
        else:
            print(After_3_minutes)
    else:
        print(beginning + win[:-1] + I_did_it + str(NB_Corner1) + " " + C)
        if NB_Corner2 > 0:
            print(Add_obstacle + "obstacle" + What + str(NB_Corner2) + " " + C)

#1150 lines!
