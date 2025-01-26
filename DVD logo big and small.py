from tkinter import *
import random
import time

r = 10000
ajustement = 0

#---------------------------------User choice---------------------------------

Win_choice = Tk()
Win_choice.title("Windows configuration")
Win_choice.geometry("570x510+50+50")
bg_color = "black"
Win_choice.config(background = bg_color)

bg_colonne0 = "#eba6ff"
fg_colonne0 = "purple"
bg_colonne1 = "Light slate blue"
fg_colonne1 = "black"
bg_colonne2 = "#66ffff"
fg_colonne2 = "blue"

source_width = 0
source_height = 0
source_width2 = 0
source_height2 = 0
deplacement_X = 0
deplacement_Y = 0
deplacement_X2 = 0
deplacement_Y2 = 0
NB_Corner1 = 0
NB_Corner2 = 0
on_top = 0
position_en_direct = 0
croissant = 0
timer = 0

BIG_STRINGVAR_WIDTH = StringVar(Win_choice)
BIG_STRINGVAR_HEIGHT = StringVar(Win_choice)
BIG_STRINGVAR_SPEED_X = StringVar(Win_choice)
BIG_STRINGVAR_SPEED_Y = StringVar(Win_choice)
small_stringvar_width = StringVar(Win_choice)
small_stringvar_height = StringVar(Win_choice)
small_stringvar_speed_x = StringVar(Win_choice)
small_stringvar_speed_y = StringVar(Win_choice)
Where_are_the_windows = StringVar(Win_choice, False)
I_like_croissants = StringVar(Win_choice, False)
where_is_the_window = StringVar(Win_choice, False)
PurpleSuperScale = IntVar(Win_choice)
BlueSuperScale = IntVar(Win_choice)
Timing = StringVar(Win_choice)
Cancel = False

def big_window_size():
    global source_width
    global source_height
    TXT = ""
    if croissant:
        try:
            BIG_WIDTH = int(BIG_STRINGVAR_WIDTH.get())
            TXT += "Largeur modifiée avec succès\n"
        except ValueError:
            BIG_WIDTH = 0
            TXT += "Largeur non modifiée avec succès\n"
        try:
            BIG_HEIGHT = int(BIG_STRINGVAR_HEIGHT.get())
            TXT += "Hauteur modifiée avec succès"
        except ValueError:
            BIG_HEIGHT = 0
            TXT += "Hauteur non modifiée avec succès"
    else:
        try:
            BIG_WIDTH = int(BIG_STRINGVAR_WIDTH.get())
            TXT += "Width successfully changed\n"
        except ValueError:
            BIG_WIDTH = 0
            TXT += "Width not successfully changed\n"
        try:
            BIG_HEIGHT = int(BIG_STRINGVAR_HEIGHT.get())
            TXT += "Height successfully changed"
        except ValueError:
            BIG_HEIGHT = 0
            TXT += "Height not successfully changed"
    source_width = BIG_WIDTH
    source_height = BIG_HEIGHT
    BIG_LABEL_CHECK_SIZE.config(text=TXT, background=bg_colonne0)
    small_window_size()

def big_window_speed():
    global deplacement_X
    global deplacement_Y
    TXT = ""
    if croissant:
        try:
            BIG_X = int(BIG_STRINGVAR_SPEED_X.get())
            TXT += "Vitesse X modifiée avec succès\n"
        except ValueError:
            BIG_X = 0
            TXT += "Vitesse X non modifiée avec succès\n"
        try:
            BIG_Y = int(BIG_STRINGVAR_SPEED_Y.get())
            TXT += "Vitesse Y modifiée avec succès"
        except ValueError:
            BIG_Y = 0
            TXT += "Vitesse Y non modifiée avec succès"
    else:
        try:
            BIG_X = int(BIG_STRINGVAR_SPEED_X.get())
            TXT += "Vitesse X successfully changed\n"
        except ValueError:
            BIG_X = 0
            TXT += "Vitesse X not successfully changed\n"
        try:
            BIG_Y = int(BIG_STRINGVAR_SPEED_Y.get())
            TXT += "Vitesse Y successfully changed"
        except ValueError:
            BIG_Y = 0
            TXT += "Vitesse Y not successfully changed"
    deplacement_X = BIG_X
    deplacement_Y = BIG_Y
    BIG_LABEL_CHECK_SPEED.config(text=TXT, background=bg_colonne0)
    small_window_speed()

def small_window_speed():
    global deplacement_X2
    global deplacement_Y2
    TXT = ""
    if croissant:
        try:
            small_x = int(small_stringvar_speed_x.get())
            TXT += "Vitesse X modifiée avec succès\n"
        except ValueError:
            small_x = 0
            TXT += "Vitesse X non modifiée avec succès\n"
        try:
            small_y = int(small_stringvar_speed_y.get())
            TXT += "Vitesse Y modifiée avec succès"
        except ValueError:
            small_y = 0
            TXT += "Vitesse Y non modifiée avec succès"
    else:
        try:
            small_x = int(small_stringvar_speed_x.get())
            TXT += "Vitesse X successfully changed\n"
        except ValueError:
            small_x = 0
            TXT += "Vitesse X not successfully changed\n"
        try:
            small_y = int(small_stringvar_speed_y.get())
            TXT += "Vitesse Y successfully changed"
        except ValueError:
            small_y = 0
            TXT += "Vitesse Y not successfully changed"
    deplacement_X2 = small_x
    deplacement_Y2 = small_y
    small_label_check_speed.config(text=TXT, background=bg_colonne2)
    Win_choice.update()

def small_window_size():
    global source_width2
    global source_height2
    txt = ""
    if croissant:
        try:
            small_width = int(small_stringvar_width.get())
            txt += "Largeur modifiée avec succès\n"
        except ValueError:
            small_width = 0
            txt += "Largeur non modifiée avec succès\n"
        try:
            small_height = int(small_stringvar_height.get())
            txt += "Hauteur modifiée avec succès"
        except ValueError:
            small_height = 0
            txt += "Hauteur non modifiée avec succès"
    else:
        try:
            small_width = int(small_stringvar_width.get())
            txt += "Widht successfully changed\n"
        except ValueError:
            small_width = 0
            txt += "Width not successfully changed\n"
        try:
            small_height = int(small_stringvar_height.get())
            txt += "Height successfully changed"
        except ValueError:
            small_height = 0
            txt += "Height not successfully changed"
    source_width2 = small_width
    source_height2 = small_height
    small_label_check_size.config(text=txt, background=bg_colonne2)
    Win_choice.update()

T = "Timer"
N = "not"
C = "successfully changed"
def Timer_check():
    global timer
    try:
        timer = int(Timing.get())
        Timed_label.config(text = f"{T} {C}", background = "white")
    except ValueError:
        timer = 0
        Timed_label.config(text = f"{T} {N} {C}", background = "white")

def this_language_is_terrible_help():
    global Clarification_texts, Im_so_lazy_help, croissant
    global T, N, C
    croissant = int(I_like_croissants.get())
    if croissant:
        BIG_LABEL.config(text = "Grande fenêtre")
        small_label.config(text = "Petite fenêtre")
        Clarification_texts = ["← Largeur des fenêtres →", "← Heuteur des fenêtres →", "← Vitesse X des fenêtres →", "← Vitesse Y des fenêtres →"]
        for i in range(4):
            Clarification_labels[i].config(text = Clarification_texts[i])
        Im_so_lazy_help[0] = "Vérification taille"
        Im_so_lazy_help[1] = "Vérification vitesse"
        Im_so_lazy_help[-2].config(text = Im_so_lazy_help[0])
        Im_so_lazy_help[-1].config(text = Im_so_lazy_help[1])
        Timed_button.config(text = "Vérifier le chrono")
        Please_dont_click_on_this_this_is_terrible.config(text = "Croissant")
        Live_positions.config(text = "Positions en direct")
        Top_positions.config(text = 'Fenêtres sur le dessus')
        Bonuses.config(text = "← Coins bonus →")
        EnDiNg_BuTtOn.config(text = "Créer les fenêtres")
        CaNcEl_BuTtOn.config(text = "Annuler la création")
        N = "non"
        C = "modifié avec succès"
        T = "Chrono"
    else:
        BIG_LABEL.config(text = "Big window")
        small_label.config(text = "Small window")
        Clarification_texts = ["← Windows width →", "← Windows height →", "← Windows X speed →", "← Windows Y speed →"]
        for i in range(4):
            Clarification_labels[i].config(text = Clarification_texts[i])
        Im_so_lazy_help[0] = "Check size"
        Im_so_lazy_help[1] = "Check speed"
        Im_so_lazy_help[-2].config(text = Im_so_lazy_help[0])
        Im_so_lazy_help[-1].config(text = Im_so_lazy_help[1])
        Timed_button.config(text = "Checking time")
        Please_dont_click_on_this_this_is_terrible.config(text = "French")
        Live_positions.config(text = "Live positions")
        Top_positions.config(text = 'Windows on top')
        Bonuses.config(text = "← Bonuses corners →")
        EnDiNg_BuTtOn.config(text = "Create the windows")
        CaNcEl_BuTtOn.config(text = "Cancel the creation")
        T = "Timer"
        N = "not"
        C = "successfully changed"

def scale_that_purple_scale(n):
    Purple_Bonus.config(background = ["#eba6ff", "#e074ff", "#d64afe", "#d02cff", "#c600ff", "#a800d8"][int(n)], foreground = ["purple", "purple2", "purple3", "purple4", "gray12", "black"][int(n)])

def scale_that_blue_scale(n):
    Blue_Bonus.config(background = ["#66ffff", "#36ffff", "#14ffff", "#00eded", "#00cece", "#00b1b1"][int(n)], foreground = ["blue", "blue2", "blue3", "blue4", "navy", "black"][int(n)])

def finished_choice():
    global position_en_direct
    global croissant
    global on_top
    global NB_Corner1
    global NB_Corner2
    NB_Corner1 = PurpleSuperScale.get()
    NB_Corner2 = BlueSuperScale.get()
    croissant = int(I_like_croissants.get())
    position_en_direct = int(Where_are_the_windows.get())
    on_top = int(where_is_the_window.get())
    Timer_check()
    big_window_size()
    big_window_speed()
    Win_choice.destroy()

def canceled_choice():
    global Cancel
    Cancel = True
    Win_choice.destroy()

if True:
    Colonne = 0
    Ligne = 0
    BIG_LABEL = Label(Win_choice, width = 29, text="Big window", foreground=fg_colonne0, background=bg_colonne0)
    BIG_LABEL.grid(row = Ligne, column = Colonne, pady = 10)
    Ligne += 1
    BIG_ENTRY_WIDTH = Entry(Win_choice, width = 20, textvariable=BIG_STRINGVAR_WIDTH)#, foreground="blue", background="#66ffff")
    BIG_ENTRY_WIDTH.grid(row = Ligne, column = Colonne, pady = 10)
    Ligne += 1
    BIG_ENTRY_HEIGHT = Entry(Win_choice, width = 20, textvariable=BIG_STRINGVAR_HEIGHT)#, foreground="blue", background="#66ffff")
    BIG_ENTRY_HEIGHT.grid(row = Ligne, column = Colonne, pady = 10)
    Ligne += 1
    BIG_LABEL_CHECK_SIZE = Label(Win_choice, width = 27, text="", foreground=fg_colonne0, background=bg_color)
    BIG_LABEL_CHECK_SIZE.grid(row = Ligne, column = Colonne, pady = 10)
    Ligne += 1
    BIG_ENTRY_SPEED_X = Entry(Win_choice, width = 20, textvariable=BIG_STRINGVAR_SPEED_X)#, foreground="blue", background="#66ffff")
    BIG_ENTRY_SPEED_X.grid(row = Ligne, column = Colonne, pady = 10)
    Ligne += 1
    BIG_ENTRY_SPEED_Y = Entry(Win_choice, width = 20, textvariable=BIG_STRINGVAR_SPEED_Y)#, foreground="blue", background="#66ffff")
    BIG_ENTRY_SPEED_Y.grid(row = Ligne, column = Colonne, pady = 10)
    Ligne += 1
    BIG_LABEL_CHECK_SPEED = Label(Win_choice, width = 27, text="", foreground=fg_colonne0, background=bg_color)
    BIG_LABEL_CHECK_SPEED.grid(row = Ligne, column = Colonne, pady = 10)
    Top_positions = Checkbutton(Win_choice, text="Windows on top", variable = where_is_the_window, onvalue=True, offvalue=False, background = "gold", foreground = fg_colonne1)
    Top_positions.grid(row=8, column = Colonne, pady = 10)

    Ligne = 1
    Colonne += 1
    Clarification_labels = []
    Clarification_texts = ["← Windows width →", "← Windows height →", "← Windows X speed →", "← Windows Y speed →"]
    for i in range(4):
        Clarification_labels.append(Label(Win_choice, width = 20, text = Clarification_texts[i], foreground = fg_colonne1, background = bg_colonne1))
        Clarification_labels[i].grid(row = Ligne, column = Colonne, pady = 10)
        Ligne += 1
        if Ligne == 3:
            Ligne += 1
    Ligne = 3
    Im_so_lazy_help = ["Check size", "Check speed", big_window_size, big_window_speed]
    for i in range(4, 6):
        Im_so_lazy_help.append(Button(Win_choice, width = 20, text = Im_so_lazy_help[i-4], command = Im_so_lazy_help[i-2], foreground = fg_colonne1, background = bg_colonne1))
        Im_so_lazy_help[i].grid(row = Ligne, column = Colonne, pady = 10)
        Ligne += 3
    Live_positions = Checkbutton(Win_choice, text="Live positions", variable = Where_are_the_windows, onvalue=True, offvalue=False, background = "spring green", foreground = fg_colonne1)
    Live_positions.grid(row=8, column = Colonne, pady = 10)

    Ligne = 0
    Colonne += 1
    small_label = Label(Win_choice, width = 29, text="Small window", foreground=fg_colonne2, background=bg_colonne2)
    small_label.grid(row = Ligne, column = Colonne, pady = 10)
    Ligne += 1
    small_entry_width = Entry(Win_choice, width = 20, textvariable=small_stringvar_width)#, foreground="purple", background="#eba6ff")
    small_entry_width.grid(row = Ligne, column = Colonne, pady = 10)
    Ligne += 1
    small_entry_height = Entry(Win_choice, width = 20, textvariable=small_stringvar_height)#, foreground="purple", background="#eba6ff")
    small_entry_height.grid(row = Ligne, column = Colonne, pady = 10)
    Ligne += 1
    small_label_check_size = Label(Win_choice, width = 27, text="", foreground=fg_colonne2, background=bg_color)
    small_label_check_size.grid(row = Ligne, column = Colonne, pady = 10)
    Ligne += 1
    small_entry_speed_x = Entry(Win_choice, width = 20, textvariable=small_stringvar_speed_x)#, foreground="purple", background="#eba6ff")
    small_entry_speed_x.grid(row = Ligne, column = Colonne, pady = 10)
    Ligne += 1
    small_entry_speed_y = Entry(Win_choice, width = 20, textvariable=small_stringvar_speed_y)#, foreground="purple", background="#eba6ff")
    small_entry_speed_y.grid(row = Ligne, column = Colonne, pady = 10)
    Ligne += 1
    small_label_check_speed = Label(Win_choice, width = 27, text="", foreground=fg_colonne2, background=bg_color)
    small_label_check_speed.grid(row = Ligne, column = Colonne, pady = 10)
    Please_dont_click_on_this_this_is_terrible = Checkbutton(Win_choice, text="French", variable = I_like_croissants, onvalue=True, offvalue=False, command=this_language_is_terrible_help, background = "blue", foreground = "white")
    Please_dont_click_on_this_this_is_terrible.grid(row=8, column = Colonne, pady = 10)
    
    Timed_entry = Entry(Win_choice, width = 20, textvariable = Timing)
    Timed_entry.grid(row = 7, column = 0, pady = 10)
    Timed_button = Button(Win_choice, width = 20, text = "Checking time", command = Timer_check)
    Timed_button.grid(row = 7, column = 1, pady = 10)
    Timed_label = Label(Win_choice, text = "", width = 25, background = bg_color, foreground = "black")
    Timed_label.grid(row = 7, column = 2, pady = 10)
    Bonuses = Label(Win_choice, width = 20, text = "← Bonuses corners →", background = "Light slate blue")
    Bonuses.grid(row = 9, column = 1, pady = 10)
    Purple_Bonus = Scale(Win_choice, from_=0, to=5, showvalue=True, variable=PurpleSuperScale, tickinterval=1, orient='h', command = scale_that_purple_scale, background = "#eba6ff", foreground = "purple")
    Purple_Bonus.grid(row = 9, column=0)
    Blue_Bonus = Scale(Win_choice, from_=0, to=5, showvalue=True, variable=BlueSuperScale, tickinterval=1, orient='h', command = scale_that_blue_scale, background = "#66ffff", foreground = "blue")
    Blue_Bonus.grid(row = 9, column=2)

    EnDiNg_BuTtOn = Button(Win_choice, width = 18, text="Create the windows", foreground="black", background="white", command = finished_choice)
    EnDiNg_BuTtOn.grid(row = 10, column = 0, pady = 10)
    Ligne += 1
    CaNcEl_BuTtOn = Button(Win_choice, width = 18, text="Cancel the creation", foreground="black", background="white", command = canceled_choice)
    CaNcEl_BuTtOn.grid(row = 10, column = 2, pady = 10)

Win_choice.protocol("WM_DELETE_WINDOW", canceled_choice)
Win_choice.update()
Win_choice.mainloop()

if Cancel is False:
    #---------------------------------Initialisation---------------------------------

    if True: #size and speed checks
        if source_width < 300:
            source_width = 400
        if source_height < 300:
            source_height = 400
        if source_width2 < 200:
            source_width2 = 200
        if source_height2 < 200:
            source_height2 = 200
        if source_width < source_width2:
            source_width, source_width2 = source_width2, source_width
        if source_height < source_height2:
            source_height, source_height2 = source_height2, source_height
        if source_width == source_width2:
            source_width2 = source_width - 100
        if source_height == source_height2:
            source_height2 = source_height - 100
        if deplacement_X <= 0:
            deplacement_X = 1
        if deplacement_Y <= 0:
            deplacement_Y = 1
        if deplacement_X2 <= 1:
            deplacement_X2 = 2
        if deplacement_Y2 <= 1:
            deplacement_Y2 = 2

    finish_everything = Tk()
    finish_everything.title("Game over")
    finish_everything.geometry(f"227x50+{finish_everything.winfo_screenwidth()-235}+{finish_everything.winfo_screenheight()-50-70}")
    finish_everything.config(background = "black")
    def ending_everything():
        global loop
        print("Game over!")
        loop = False
    if croissant:
        D_E_text = "Fermer les fenêtres"
    else:
        D_E_text = "Closing the windows"
    destroy_everything = Button(finish_everything, width = 31, text = D_E_text, command = ending_everything, background = "IndianRed3", foreground = "black")
    destroy_everything.grid(row = 0, column = 0, pady = 10)
    finish_everything.update()
    
    loop = True
    
    text_size = source_width//20
    text_size2 = source_width2//20
    size = source_width // 8
    size2 = source_width2 // 8
    
    if croissant:
        C = "coins"
        B_W = "Grande fenêtre"
        S_W = "Petite fenêtre"
    else:
        C = "corners"
        B_W = "Big window"
        S_W = "Small window"
    
    x = 500
    y = 500
    x2 = 700
    y2 = 700

    fenetre2 = Tk() 
    fenetre2.title("Corner game small")
    fenetre2.geometry(f"{source_width2}x{source_height2}+{x2}+{y2}")
    if on_top:
        fenetre2.attributes("-topmost", True)
    if position_en_direct:
        CORNER2 = Label(fenetre2, width=text_size2, text=(f"NB {C} : {NB_Corner2}"), font=('Times New Roman', 25, 'bold'), foreground="blue", background="#66ffff")
        CORNER_X2 = Label(fenetre2, width=text_size2, text=str(x2), font=('Times New Roman', 25, 'bold'), foreground="blue", background="#66ffff")
        CORNER_Y2 = Label(fenetre2, width=text_size2, text=str(y2), font=('Times New Roman', 25, 'bold'), foreground="blue", background="#66ffff")
        CORNER2.grid(row=0, column=0, pady=10)
        CORNER_X2.grid(row=1, column=0, pady=10)
        CORNER_Y2.grid(row=2, column=0, pady=10)
    else:
        fenetre2.configure(background="#66ffff")
        CORNER2 = Label(fenetre2, text=str(NB_Corner2), font=('Times New Roman', size2*3, 'bold'), foreground="blue", background="#66ffff")
        CORNER2.pack(expand=True)

    fenetre = Tk() 
    fenetre.title("Corner game big")
    fenetre.geometry(f"{source_width}x{source_height}+{x}+{y}")
    if on_top:
        fenetre.attributes("-topmost", True)
    if position_en_direct:
        CORNER = Label(fenetre, width=text_size, text=(f"NB {C} : {NB_Corner1}"), font=('Times New Roman', 25, 'bold'), foreground="purple", background="#eba6ff")
        CORNER_X = Label(fenetre, width=text_size, text=str(x), font=('Times New Roman', 25, 'bold'), foreground="purple", background="#eba6ff")
        CORNER_Y = Label(fenetre, width=text_size, text=str(y), font=('Times New Roman', 25, 'bold'), foreground="purple", background="#eba6ff")
        CORNER.grid(row=0, column=0, pady=10)
        CORNER_X.grid(row=1, column=0, pady=10)
        CORNER_Y.grid(row=2, column=0, pady=10)
    else:
        fenetre.configure(background="#eba6ff")
        CORNER = Label(fenetre, text=str(NB_Corner1), font=('Times New Roman', size*3, 'bold'), foreground="purple", background="#eba6ff")
        CORNER.pack(expand=True)

    screen_width = fenetre.winfo_screenwidth() - source_width
    screen_height = fenetre.winfo_screenheight() - source_height - 70
    x_random1 = 1
    x_random2 = screen_width - 1
    y_random1 = 1
    y_random2 = screen_height - 1
            
    def corner1_random():
        global x
        global y
        x = random.randint(x_random1, x_random2)
        y = random.randint(y_random1, y_random2)
        bordure_fenetre_2()
        corner2_random()

    def corner2_random():
        global x2
        global y2
        x2 = random.randint(x2_random1, x2_random2)
        y2 = random.randint(y2_random1, y2_random2)

    def positions():
        CORNER_X.config(text=("X : " + str(x)))
        CORNER_Y.config(text=("Y : " + str(y)))
        CORNER_X2.config(text=("X : " + str(x2)))
        CORNER_Y2.config(text=("Y : " + str(y2)))
        
    def bordure_fenetre_2():
        global screen_width2
        global screen_height2
        global x2_random1
        global x2_random2
        global y2_random1
        global y2_random2
        
        screen_width2 = x + source_width - source_width2
        screen_height2 = y + source_height - source_height2
        x2_random1 = x + 1
        x2_random2 = screen_width2 - 1
        y2_random1 = y + 1
        y2_random2 = screen_height2 - 1
    
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
    
    corner1_random()

    def move_window():
        global source_width
        global source_height
        
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
        
        if y >= screen_height or y <= (y_random1 - 1):
            deplacement_Y *= -1
            direction += 1
        
        if direction == 2:
            NB_Corner1 += 1
            print(B_W + " : " + str(NB_Corner1))
            if position_en_direct:
                CORNER.config(text=f"NB {C} : {NB_Corner1}")
            else:
                CORNER.config(text=str(NB_Corner1))
            corner1_random()
        
        if random.randint(1, r) == 1:
            #print("Changement")
            if deplacement_X > 0:
                for i in range(deplacement_X):
                    x += random.randint(0, 5)
                    y += random.randint(0, 5)
            elif deplacement_X < 0:
                for i in range(0, deplacement_X, -1):
                    x += random.randint(0, 5)
                    y += random.randint(0, 5)
        
        #---------------------------------Deuxième fenêtre---------------------------------
        
        direction2 = 0
        x2 += deplacement_X2
        y2 += deplacement_Y2
        fenetre2.geometry(f"{source_width2}x{source_height2}+{x2}+{y2}")
        fenetre2.update()
        
        if x2 == screen_width2 or x2 == x:
            deplacement_X2 *= -1
            direction2 += 1
        elif x2 < x:
            deplacement_X2 *= -1
            direction2 += 1
            x2 = x + ajustement
        elif x2 > screen_width2:
            deplacement_X2 *= -1
            direction2 += 1
            x2 = screen_width2 - ajustement
        
        if y2 == screen_height2 or y2 == y:
            deplacement_Y2 *= -1
            direction2 += 1
        elif y2 < y:
            deplacement_Y2 *= -1
            direction2 += 1
            y2 = y + ajustement
        elif y2 > screen_height2:
            deplacement_Y2 *= -1
            direction2 += 1
            y2 = screen_height2 - ajustement
        
        if direction2 == 2:
            NB_Corner2 += 1
            print(S_W + " : " + str(NB_Corner2))
            if position_en_direct:
                CORNER2.config(text=f"NB {C} : {NB_Corner2}")
            else:
                CORNER2.config(text=str(NB_Corner2))
            corner2_random()
        
        if random.randint(1, r) == 1:
            #print("Changement2")
            if deplacement_X2 > 0:
                for i in range(deplacement_X2):
                    x2 += random.randint(0, 5)
                    y2 += random.randint(0, 5)
            elif deplacement_X2 < 0:
                for i in range(0, deplacement_X2, -1):
                    x2 += random.randint(0, 5)
                    y2 += random.randint(0, 5)
        
        if position_en_direct:
            positions()
        bordure_fenetre_2()
             
    if timer:
        current_time = int(time.time())
        compteur = 0
        pause_timer = 0
        if croissant:
            S = " secondes"
            half_of_the_sentence = "Il reste donc "
            quarter_of_the_sentence = "!"
            H = " heures"
            add = " et "
            Time_is_down_hehe_you_got_the_joke_question_mark = " du temps est écoulé!"
            one = "Un quart"
            two = "La moitié"
            three = "Trois quarts"
        else:
            S = " seconds"
            half_of_the_sentence = "So there are "
            quarter_of_the_sentence = " left!"
            H = " hours"
            add = " and "
            Time_is_down_hehe_you_got_the_joke_question_mark = " of the time is up!"
            one = "A quarter"
            two = "Half"
            three = "Three quarters"
           
    if croissant:
        After_3_minutes = "Égalité!"
        beginning = "La"
        win = " fenêtre gagne!"
        first_one = " grande"
        second_one = " petite"
    else:
        beginning = "The"
        win = " window win!"
        first_one = " big"
        second_one = " small"
        After_3_minutes = "Tie!"

    while loop:
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
    
    fenetre.destroy()
    fenetre2.destroy()
    finish_everything.destroy()
    if NB_Corner1 > NB_Corner2:
        print(beginning + first_one + win)
    elif NB_Corner1 < NB_Corner2:
        print(beginning + second_one + win)
    else:
        print(After_3_minutes)
