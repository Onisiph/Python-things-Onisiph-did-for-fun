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
Win_choice.geometry("540x468+50+50")
Win_choice.config(background = bg_color)

if True: #All variables
    source_width = 0
    source_height = 0
    source_width2 = 0
    source_height2 = 0
    vitesse = 0
    vitesse2 = 0

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

    taskbar = 70
    base_speed_multiplier = 1
    base_size_multiplier = 2

Timing = StringVar(Win_choice)
Coloring = StringVar(Win_choice)
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
        txt += "Size successfully changed\n"
    except ValueError:
        source_width = 0
        source_height = 0
        txt += "Not size successfully changed\n"
    try:
        vitesse = int(String_and_Var[1].get())
        txt += "Speed successfully changed"
    except ValueError:
        vitesse = 0
        txt += "Not speed successfully changed"
    Text_and_Check[1].config(text = txt, background = "Light slate blue")
    txt = ""
    try:
        source_width2 = int(String_and_Var[2].get())
        source_height2 = source_width2
        txt += "Size successfully changed\n"
    except ValueError:
        source_width2 = 0
        source_height2 = 0
        txt += "Not size successfully changed\n"
    try:
        vitesse2 = int(String_and_Var[3].get())
        txt += "Speed successfully changed"
    except ValueError:
        vitesse2 = 0
        txt += "Not speed successfully changed"
    Text_and_Check[3].config(text = txt, background = "Light slate blue")

def Timer_check():
    global timer
    try:
        timer = int(Timing.get())
        Timed_label.config(text = "Timer successfully changed")
    except ValueError:
        timer = 0
        Timed_label.config(text = "Not timer successfully changed")

def Color_check():
    global fond_colore
    global couleur
    if couleur != "":
        Text_Fonction_and_Button[-1].config(background = couleur)
    couleur = Coloring.get()
    try:
        Colored_label.config(background = couleur, text = "Color successfully changed")
        fond_colore = 1
    except TclError:
        couleur = ""
        Colored_label.config(text = "Not color successfully changed", background = bg_color, foreground = fg_color)
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
    if Most_of_the_stringvars[8].get() == "1":
        Obstacle_choice.config(state=NORMAL)
        obstacle_type = Obstacle_choice.get()
        obstacle = 0
        obstacle_H = 0
        obstacle_V = 0
        obstacle_tournoyant = 0
        if obstacle_type == "Classic obstacle":
            obstacle = 1
        elif obstacle_type == "Horizontal obstacle":
            obstacle_H = 1
        elif obstacle_type == "Vertical obstacle":
            obstacle_V = 1
        elif obstacle_type == "Spinning obstacle":
            obstacle_tournoyant = 1
    else:
        Obstacle_choice.config(state=DISABLED)

def finished_choice():
    global on_top
    global override_redirect
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
    Timed_label = Label(Win_choice, text = "", width = 25, background = "white", foreground = "black")
    Timed_label.grid(row = 3, column = 2, pady = 10)
    Colored_entry = Entry(Win_choice, width = 20, textvariable = Coloring)
    Colored_entry.grid(row = 4, column = 0, pady = 10)
    Colored_label = Label(Win_choice, text = "", width = 25, background = bg_color, foreground = fg_color)
    Colored_label.grid(row = 4, column = 2, pady = 10)
    Ligne = 2
    Colonne = 1
    Text_Fonction_and_Button = ["Checking size/speed", "Checking time", "Checking color", S_and_S_check, Timer_check, Color_check, "Light slate blue", "white", bg_color, "black", "black", fg_color]
    for i in range(12, 15):
        Text_Fonction_and_Button.append(Button(Win_choice, width = 20, text = Text_Fonction_and_Button[i-12], command = Text_Fonction_and_Button[i-9], background = Text_Fonction_and_Button[i-6], foreground = Text_Fonction_and_Button[i-3]))
        Text_Fonction_and_Button[i].grid(row = Ligne, column = Colonne, pady = 10)
        Ligne += 1
    Colonne = 0
    Most_of_the_stringvars = []
    Most_of_the_checkbuttons = []
    Most_of_the_checkbuttons_text = ["Windows on top", "Live positions", "Progressive speed", "Collisions", "Override redirect", "Size variation", "Speed variation", "Glitchy effect", "Obstacle window"]
    Most_of_the_fonctions = [tour_de_pass_pass, Sixth_row, Seventh_row, un_active_collisions, tour_de_pass_pass, Sixth_row, Seventh_row, Sixth_row, un_active_collisions]
    Most_of_the_backgrounds = ["gold", "spring green", "MediumOrchid1", "turquoise1", "gold", "spring green", "MediumOrchid1", "spring green", "turquoise4"]
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
    Obstacle_choice = Spinbox(Win_choice, width = 20, values=["Spinning obstacle", "Vertical obstacle", "Horizontal obstacle", "Classic obstacle"], state = DISABLED, command = un_active_collisions, background = "turquoise1", foreground = "black", disabledbackground = "turquoise4")
    Obstacle_choice.grid(row = 8, column = 2, pady = 10)
    Ending_button = Button(Win_choice, width = 18, text="Create the windows", foreground="black", background="IndianRed1", command = finished_choice)
    Ending_button.grid(row = 9, column = 0, pady = 10)
    Cancel_button = Button(Win_choice, width = 18, text="Cancel the creation", foreground="black", background="IndianRed1", command = canceled_choice)
    Cancel_button.grid(row = 9, column = 2, pady = 10)

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

    #---------------------------------Initialisation---------------------------------
    
    NB_Corner1 = 0
    NB_Corner2 = 0
    size = source_width // 8
    size2 = source_width2 // 8
    x = 500
    y = 500
    x2 = 500
    y2 = 500

    if fond_colore:
        BG = Tk()
        BG.title("Background")
        xf = BG.winfo_screenwidth()
        yf = BG.winfo_screenheight()
        BG.geometry(f"{xf}x{yf}+0+0")
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
        CORNER2 = Label(fenetre2, width=10, text=("NB corners : " + str(NB_Corner2)), font=('Times New Roman', size, 'bold'), foreground="blue", background="#66ffff")
        CORNER_X2 = Label(fenetre2, width=10, text=str(x2), font=('Times New Roman', size, 'bold'), foreground="blue", background="#66ffff")
        CORNER_Y2 = Label(fenetre2, width=10, text=str(y2), font=('Times New Roman', size, 'bold'), foreground="blue", background="#66ffff")
        CORNER2.grid(row=0, column=0, pady=10)
        CORNER_X2.grid(row=1, column=0, pady=10)
        CORNER_Y2.grid(row=2, column=0, pady=10)
    elif glitchy:
        fenetre2.configure(background="#66ffff")
        labels1 = []
        for i in range(number_of_labels):
            labels1.append(Label(fenetre2, text = 'a', font=("Helvetica", taille), foreground = "blue", background = "#66ffff"))
            labels1[i].pack(expand=True)
    else:
        fenetre2.configure(background="#66ffff")
        CORNER2 = Label(fenetre2, text=str(NB_Corner2), font=('Times New Roman', size*3, 'bold'), foreground="blue", background="#66ffff")
        CORNER2.pack(expand=True)

    fenetre = Tk() 
    fenetre.title("Corner game 1")
    fenetre.geometry(f"{source_width}x{source_height}+{x}+{y}")
    if on_top:
        fenetre.attributes("-topmost", True)
    if override_redirect:
        fenetre.overrideredirect(True)
    if positions_en_direct:
        CORNER = Label(fenetre, width=10, text=("NB corners : " + str(NB_Corner1)), font=('Times New Roman', size2, 'bold'), foreground="purple", background="#eba6ff")
        CORNER_X = Label(fenetre, width=10, text=str(x), font=('Times New Roman', size2, 'bold'), foreground="purple", background="#eba6ff")
        CORNER_Y = Label(fenetre, width=10, text=str(y), font=('Times New Roman', size2, 'bold'), foreground="purple", background="#eba6ff")
        CORNER.grid(row=0, column=0, pady=10)
        CORNER_X.grid(row=1, column=0, pady=10)
        CORNER_Y.grid(row=2, column=0, pady=10)
    elif glitchy:
        fenetre.configure(background="#eba6ff")
        labels2 = []
        for i in range(number_of_labels):
            labels2.append(Label(fenetre, text = 'a', font=("Helvetica", taille), foreground ="purple", background="#eba6ff"))
            labels2[i].pack(expand=True)
    else:
        fenetre.configure(background="#eba6ff")
        CORNER = Label(fenetre, text=str(NB_Corner1), font=('Times New Roman', size2*3, 'bold'), foreground="purple", background="#eba6ff")
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
            return str(t) + " hours and " + str(int(t2)) + " minutes"
        elif T >= 60:
            t = T // 60
            return str(t) + " minutes and " + str(T % 60) + " seconds"
        else:
            return str(T) + " seconds"

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
            print("First window :", NB_Corner1, "corners")
            if not glitchy:
                if positions_en_direct:
                    CORNER.config(text="NB corners : " + str(NB_Corner1))
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
                print("Second window :", NB_Corner2, "corners")
                if not glitchy:
                    if positions_en_direct:
                        CORNER2.config(text="NB corners : " + str(NB_Corner2))
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
    while True:
        move_window()
        if timer > 0:
            half_of_the_sentence = "So there are "
            quarter_of_the_sentence = " left!"
            if int(time.time()) >= current_time + (timer // 4) and compteur == 0:
                print("A quarter of the time is up!")
                print(half_of_the_sentence + chrono((timer // 4) * 3) + quarter_of_the_sentence)
                compteur += 1
            elif int(time.time()) >= current_time + (timer // 2) and compteur == 1:
                print("Half of the time is up!")
                print(half_of_the_sentence + chrono(timer // 2) + quarter_of_the_sentence)
                compteur += 1
            elif int(time.time()) >= current_time + ((timer // 4) * 3) and compteur == 2:
                print("Three quarters of the time is up!")
                print(half_of_the_sentence + chrono((timer // 4)) + quarter_of_the_sentence)
                compteur += 1
            elif int(time.time()) >= (current_time + timer):
                break

    if not obstacle and not obstacle_H and not obstacle_V and not obstacle_tournoyant:
        if NB_Corner1 > NB_Corner2:
            print("The first window (purple) win!")
        elif NB_Corner2 < NB_Corner1:
            print("The second window (blue) win!")
        else:
            print("Tie!")
    else:
        print("The window did", NB_Corner1, "corners!")
        if NB_Corner2 > 0:
            print("And the obstacle somehow did", NB_Corner2, "corners")
