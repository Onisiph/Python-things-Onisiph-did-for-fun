from tkinter import *
from random import choice
import random
import time

#background and foregound/text color
bg = "black"
fg = "green"
#All characters it can randomely choose
letter_str = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz 1234567890œ&é'([{#~-|è`_\ç^à@ù%*µ}])=ê$£ë¥Ù³²¹¬ß®©»«ÔÎÛðæ±ÊøÂ¶ôîûýþ€åâ¡÷×¿§/.?ºẞ‘><ÖÏÜÐÆªËÄöïüÝÞÇ¢Åä¦†‡ඞƒñÑšžŸ¤™☺☻♣♠♥♦⌂♂♀⚧♪♫☼·•◘○◙↑↓←→↕↔↨▲▼◄►︿‹–—˜„‼…½¼¾‰║╣╗╝╚╔╠╦═╬┐└┴┬├─┼┤│∟¯┌┘ı█▄▀▬■░▒▓✔༒㋡☣"
#A list of texts it can generate
word_list_universal = ["Hello world", "ඞ︿ඞ", "I will conquer the world", "     ", ":3", "MOUAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHA", "Test message", "Hellow world", "owo", "MAJUSCULES", "💖🌸👩‍💻", "🌟🌙🌠☄🌌", "Be gay do crimes", "Reject humanity become dragon", "Be neurodivergent"]
word_list_french = ["Joyeux non-anniversaire!", "Mini jeu! Trouve le plus long!", "Mini jeu! Retiens la bonne combinaison!", "Je t'ai menti, j'ai installé un virus sur ton PC", "Je crois que ça a bugué, attend", "Ceci est un easter egg", "Félicitations", "Pas de chance", "J'ai pas envie", "PANIQUE", "AAAAAAAAAAA quel hasard", "Insérer prénom", "Quelle horreur", "Femboy ou fille trans?", "ÛÏ_îfIẞý<Vâ=Ô/0TH`Kôþ» oui ceci est voulu"]
word_list_english = ["Happy non-anniversary!", "Minigame! Find the longest!", "Minigame! Remember the password!", "I lied, I put a virus on your computer", "Wait, I think there is a problem", "This is an easter egg", "Congratulations", "No luck", "I don't want to", "PANIC", "AAAAAAAAAAA what a coincidence", "Insert name", "How horrible", "Femboy or trans girl?", "ÛÏ_îfIẞý<Vâ=Ô/0TH`Kôþ» Yup, this is wanted"]
word_list = []

opti_choice = 8
if opti_choice:
    #An attempt to optimize the way it choose the characters (I have no idea if it works or not)
    N_letter = len(letter_str)
    N_letter = N_letter // opti_choice
    letter_list = [letter_str[:N_letter]]
    for o in range(1, opti_choice-1):
        letter_list.append(letter_str[N_letter*o:N_letter*(o+1)])
    letter_list.append(letter_str[N_letter*(opti_choice-1):])

def Stopping_everything(b):
    if b:
        randomizer.config(state=NORMAL)
        not_really_randomizer.config(state=NORMAL)
        real_randomizer.config(state=NORMAL)
    else:
        randomizer.config(state=DISABLED)
        not_really_randomizer.config(state=DISABLED)
        real_randomizer.config(state=DISABLED)

def language():
    '''Set up the language of the labels and texts (default to English)'''
    global word_list
    def make_it_english():
        first_thing.config(text = "How many characters do you want to generate?")
        randomizer.config(text = "randomizing")
        second_thing.config(text = "What text do you want to generate?")
        not_really_randomizer.config(text = "generate text")
        real_randomizer.config(text = "real randomizing")
        last_thing.config(text = "How much waiting between each character")
        MemoryCheck.config(text = "Memory")
        PastMemoryCheck.config(text = "Past Memory")
        if Now_you_can_change_colors:
            Now_you_can_change_colors[0].config(text = "Change the colors (Backgroud color and text color)")
            Now_you_can_change_colors[3].config(text = "changing colors")
        English_language.config(text = "English")
        French_language.config(text = "French")
    def make_it_french():
        first_thing.config(text = "Combien ce charactères voulez-vous générer?")
        randomizer.config(text = "randomizer")
        second_thing.config(text = "Quel texte voulez-vous générer?")
        not_really_randomizer.config(text = "générer texte")
        real_randomizer.config(text = "randomizer pour de vrai")
        last_thing.config(text = "Quel temps d'attente entre chaque charactères?")
        MemoryCheck.config(text = "Mémoire")
        PastMemoryCheck.config(text = "Mémoire passée")
        if Now_you_can_change_colors:
            Now_you_can_change_colors[0].config(text = "Changer les couleurs (couleur de fond et couleur de texte)")
            Now_you_can_change_colors[3].config(text = "changer les couleurs")
        English_language.config(text = "Anglais")
        French_language.config(text = "Français")
    FR = French.get()
    EN = English.get()
    word_list = []
    for i in word_list_universal:
        word_list.append(i)
    if SUPREMACY:
        word_list.append(SUPREMACY)
    if EN == "Fake True" and FR == "Fake True":
        for i in word_list_english:
            if not i in word_list:
                word_list.append(i)
        for i in word_list_french:
            if not i in word_list:
                word_list.append(i)
        make_it_english()
    elif FR == "Fake True":
        for i in word_list_french:
            if not i in word_list:
                word_list.append(i)
        make_it_french()
    else:
        for i in word_list_english:
            if not i in word_list:
                word_list.append(i)
        make_it_english()

def find_len(l):
    '''It find every text that have the right length'''
    a = []
    for i in word_list:
        if len(i) == l:
            a.append(i)
    return a

def remove_last(txt):
    '''Used to remove the last character of a string
    I guess I didn't found any easier way'''
    if not txt == "":
        t = ""
        for i in range(len(txt)-1):
            t += txt[i]
        return t
    else:
        return ""

def wait_is_50():
    '''A fonction for the fisrt way of generating characters
    If the user type something else than a number, it default to 30'''
    try:
        you_will_wait = int(number_of_waiting.get())
    except ValueError:
        you_will_wait = 30
    if you_will_wait <= 0:
        you_will_wait = 30
    return you_will_wait

def optimized_choice():
    '''An attempt to optimize the way it choose the characters
    (I have no idea if it works or not)'''
    if not opti_choice:
        return choice(letter_str)
    else:
        return choice(choice(letter_list))

def different_number(n, f=5, s=25):
    '''Enter a number and it will give you a different number
    Hopefully'''
    nb = random.randint(f, s)
    if type(n) is int:
        if nb != n:
            return nb
        else:
            return different_number(n, f, s)
    elif type(n) is list:
        if not nb in n:
            return nb
        else:
            return different_number(n, f, s)
    else:
        return None

def randomely_generated_text(length = None, affichage = True):
    '''Write a text of a length that you can decide (if there is no length, it take the number in the first entry)
    You can also decide if it will be printed in the shell'''
    I_hope_there_will_be_a_lot_of_things_there()
    r = ""
    temp_var = None
    if length is None:
        try:
            rnb = int(random_number.get()) -1
        except ValueError:
            if French.get() == "Fake True" and English.get() == "Fake False":
                Stopping_everything(True)
                raise ValueError("Le nombre de caractères doit être un nombre, crétin")
            else:
                Stopping_everything(True)
                raise ValueError("The number of characters must be a number, dumbass")
    else:
        rnb = length - 1
        if not type(rnb) is int:
            if French.get() == "Fake True" and English.get() == "Fake False":
                Stopping_everything(True)
                raise ValueError("Le nombre de caractères doit être un nombre, crétin")
            else:
                Stopping_everything(True)
                raise ValueError("The number of characters must be a number, dumbass")
    short_list = find_len(rnb+1)
    if short_list != []:
        if random.randint(1, 5) == 1:
            testing = choice(short_list)
            randomely_choosen_text(testing)
        else:
            temp_var = "This is a str"
    else:
        temp_var = "None"
    if temp_var is not None:
        for i in range(rnb):
            r += optimized_choice()
            for j in range(wait_is_50()):
                s = ''.join([optimized_choice() for k in range(rnb - i)])
                random_text.config(text = (r+s))
                fenetre.update()
            if affichage:
                print(r)
            if now_you_can_see_the_length:
                word_length[0].config(text = str(len(r)+1))
    Stopping_everything(True)

def really_randomely_generated_text():
    '''A truly randomely generated text
    Yes, I know, it's logic'''
    I_hope_there_will_be_a_lot_of_things_there()
    if random.randint(1, 5) == 1:
        randomely_choosen_text()
    else:
        x = random.randint(1, 50)
        r = ""
        for i in range(x):
            r += optimized_choice()
            for j in range(wait_is_50()):
                s = ''.join([optimized_choice() for k in range(x - i)])
                random_text.config(text = (r+s))
                fenetre.update()
            print(r)
            if now_you_can_see_the_length:
                word_length[0].config(text = str(len(r)+1))
    Stopping_everything(True)

def not_really_randomized_text():
    '''This one just write the text you want to write
    But only if you write it in the second entry'''
    I_hope_there_will_be_a_lot_of_things_there()
    final_text = not_random_text.get()
    M = Memory.get()
    PM = PastMemory.get()
    if PM == "Fake True" and final_text not in word_list:
        word_list_universal.append(final_text)
        word_list.append(final_text)
        save(final_text)
    elif M == "Fake True" and final_text not in word_list:
        word_list_universal.append(final_text)
        word_list.append(final_text)
    N_txt = len(final_text)
    r = ""
    for i in range(N_txt):
        r += final_text[i]
        for j in range(wait_is_50()):
            s = ''.join([optimized_choice() for k in range(N_txt - i - 1)])
            random_text.config(text = (r+s))
            fenetre.update()
        if now_you_can_see_the_length:
            word_length[0].config(text = str(len(r)))
    Stopping_everything(True)

def randomely_choosen_text(txt = None, affichage = True):
    '''This one choose a text in the word_list
    You can also write what you want with it'''
    global Stop_everything
    global n
    global Virus
    global Virus_T
    global memory_password
    global memory_game_windows
    global memory_game_labels
    global memory_game_buttons
    I_hope_there_will_be_a_lot_of_things_there()
    if txt is None:
        final_text = choice(word_list)
    else:
        final_text = txt
        if (type(final_text) is str) is False:
            final_text = str(final_text)
    N_txt = len(final_text)
    r = ""
    for i in range(N_txt):
        r += final_text[i]
        for j in range(wait_is_50()):
            s = ''.join([optimized_choice() for k in range(N_txt - i - 1)])
            random_text.config(text = (r+s))
            fenetre.update()
        if affichage:
            print(r)
        if now_you_can_see_the_length:
            word_length[0].config(text = str(len(r)))
        if r == "Je crois que ça a bugué, attend" or r == "Wait, I think there is a problem":
            Stop_everything = True
            time.sleep(5)
            if r == "Je crois que ça a bugué, attend":#French.get() == "Fake True":
                write("Ouep, je confirme")
            else:
                write("Yup, I confirm")
            time.sleep(0.5)
            fenetre.destroy()
        elif r == "Femboy or trans girl?" or r == "Femboy ou fille trans?":
            Stop_everything = True
            def F_or_F(choice):
                global Stop_everything
                global SUPREMACY
                SUPREMACY = choice + " SUPREMACY"
                if not SUPREMACY in word_list:
                    word_list.append(SUPREMACY)
                F_choice_window.destroy()
                Stop_everything = False
                Stopping_everything(True)
            F_choice_window = Tk()
            F_choice_window.title(r)
            f_X = fenetre.winfo_x()
            f_Y = fenetre.winfo_y()
            f_H = fenetre.winfo_height()
            f_W = fenetre.winfo_width()
            size_X = f_W // 2
            size_Y = f_H // 2
            F_choice_window.geometry(f"{size_X}x{size_Y}+{f_X + f_W - size_X}+{f_Y + f_H - size_Y}")
            F_choice_window.config(background = bg)
            F_choice_window.attributes("-topmost", True)
            F_choice_window.protocol("WM_DELETE_WINDOW", disable_event)
            Femboy_button = Button(F_choice_window, width = size_X//55, height=size_Y//800, font=("Helvetica", size_X//10), text="femboy!", command=lambda t = "FEMBOY": F_or_F(t), foreground=fg, background=bg)
            Femboy_button.grid(row = 0, column = 0, pady = 10)
            Trans_girl_button = Button(F_choice_window, width = size_X//55, height=size_Y//800, font=("Helvetica", size_X//10), text=r[10:-1]+"!", command=lambda t = "TRANS GIRL": F_or_F(t), foreground=fg, background=bg)
            Trans_girl_button.grid(row = 2, column = 0, pady = 10)
        elif r == "Insert name" or r == "Insérer prénom":
            Stop_everything = True
            def your_name():
                global Stop_everything
                name = str(entry_name.get())
                word_list_universal.append("Hello " + name)
                word_list.append("Hello " + name)
                name_window.destroy()
                Stop_everything = False
                Stopping_everything(True)
            name_window = Tk()
            name_window.title(r)
            f_X = fenetre.winfo_x()
            f_Y = fenetre.winfo_y()
            f_H = fenetre.winfo_height()
            f_W = fenetre.winfo_width()
            size_X = f_W // 2
            size_Y = f_H // 2
            name_window.geometry(f"{size_X}x{size_Y}+{f_X + f_W - size_X}+{f_Y + f_H - size_Y}")
            name_window.config(background = bg)
            name_window.attributes("-topmost", True)
            name_window.protocol("WM_DELETE_WINDOW", disable_event)
            entry_name = StringVar(fenetre, 'Fake True')
            name_entry = Entry(name_window, width = size_X//55, font=("Helvetica", size_X//10), textvariable=entry_name)
            name_entry.pack(expand=True)
            name_button = Button(name_window, width = size_X//55, height=size_Y//800, font=("Helvetica", size_X//10), text=r, command=your_name, foreground=fg, background=bg)
            name_button.pack(expand=True)
        elif r == "Je t'ai menti, j'ai installé un virus sur ton PC" or r == "I lied, I put a virus on your computer":
            n += 1
            Virus = True
            Virus_T = int(time.time())
        elif (r == "Mini jeu! Retiens la bonne combinaison!" or r == "Minigame! Remember the password!") and memory_password == "Not_defined_yet":
            Stop_everything = True
            time.sleep(0.5)
            #nine_characters = "☼♣♪♠☺♥♫♦⌂"
            nine_characters = ""
            def add_a_character(txt):
                new_cha = optimized_choice()
                if not new_cha in txt:
                    return txt + new_cha
                else:
                    return add_a_character(txt)
            for i in range(9):
                nine_characters = add_a_character(nine_characters)
            memory_password = choice(nine_characters) + choice(nine_characters) + choice(nine_characters)
            memory_color = ["red", "orange", "yellow", "green", "cyan", "purple", "magenta", "white", "black"]
            def if_black_white():
                if memory_color[nb_w] == "black":
                    return "white"
                else:
                    return "black"
            write(memory_password, False)
            f_X = fenetre.winfo_x()
            f_Y = fenetre.winfo_y()
            f_H = fenetre.winfo_height()
            f_W = fenetre.winfo_width()
            print(f_X, f_Y, f_W, f_H)
            size_X = f_W // 4
            size_Y = f_H // 4
            nb_w = 0
            def define_pos(f, size, h):
                return (f+(size*(h-1)))+((size//2)*(h-1))
            for i in range(1, 4):
                for j in range(1, 4):
                    memory_game_windows.append(Tk())
                    if nb_w != 0:
                        memory_game_windows[nb_w].geometry(f"{size_X}x{size_Y}+{define_pos(f_X, size_X, j)}+{define_pos(f_Y, size_Y, i)}")
                    else:
                        memory_game_windows[nb_w].geometry("1x1+-500+-500")
                    memory_game_windows[nb_w].title(nine_characters[nb_w])
                    memory_game_windows[nb_w].configure(background=if_black_white())
                    memory_game_windows[nb_w].attributes("-topmost", True)
                    memory_game_windows[nb_w].protocol("WM_DELETE_WINDOW", disable_event)
                    memory_game_labels.append(Label(memory_game_windows[nb_w], text = nine_characters[nb_w], font=("Helvetica", 50), foreground = memory_color[nb_w], background = if_black_white()))
                    memory_game_labels[nb_w].pack(expand=True)
                    memory_game_buttons.append(Button(memory_game_windows[nb_w], text = nine_characters[nb_w], font=("Helvetica", 50), foreground = if_black_white(), background = memory_color[nb_w], command=lambda k=nine_characters[nb_w]: memory_minigame(k)))
                    memory_game_buttons[nb_w].pack(expand=True)
                    memory_game_buttons[nb_w].update()
                    nb_w += 1
            time.sleep(1.5)
            write("   ", False)
            time.sleep(0.2)
            memory_game_windows[0].geometry(f"{size_X}x{size_Y}+{define_pos(f_X, size_X, 1)}+{define_pos(f_Y, size_Y, 1)}")
            memory_game_buttons[0].update()
        elif (r == "Mini jeu! Trouve le plus long!" or r == "Minigame! Find the longest!") and now_you_can_see_the_length is False:
            Stop_everything = True
            first = random.randint(5, 25)
            second = different_number(first)
            time.sleep(1.5)
            count(first, False)
            time.sleep(1.5)
            count(second, False)
            time.sleep(1.5)
            write("     ", False)
            f_X = fenetre.winfo_x()
            f_Y = fenetre.winfo_y()
            f_H = fenetre.winfo_height()
            f_W = fenetre.winfo_width()
            print(f_X, f_Y, f_W, f_H)
            size_X = f_W // 3
            size_Y = (f_H // 4) * 2
            first_word.append(Tk())
            first_word[0].config(background = bg)
            first_word[0].geometry(f"{size_X}x{size_Y}+{f_X}+{f_Y + (f_H // 4)}")
            first_word[0].attributes("-topmost", True)
            first_word[0].protocol("WM_DELETE_WINDOW", disable_event)
            first_word_button = Button(first_word[0], text = "1", font=("Helvetica", 45), foreground = fg, background = bg, command = lambda a=(first>second): longest_minigame(a))
            first_word_button.pack(expand=True)
            second_word.append(Tk())
            second_word[0].config(background = bg)
            second_word[0].geometry(f"{size_X}x{size_Y}+{f_X+f_W-size_X}+{f_Y + (f_H // 4)}")
            second_word[0].attributes("-topmost", True)
            second_word[0].protocol("WM_DELETE_WINDOW", disable_event)
            second_word_button = Button(second_word[0], text = "2", font=("Helvetica", 45), foreground = fg, background = bg, command = lambda a=(first<second): longest_minigame(a))
            second_word_button.pack(expand=True)
            if r == "Mini jeu! Trouve le plus long!":#French.get() == "Fake True":
                first_word[0].title("Le premier!")
                first_word_label = Label(first_word[0], text = "Le premier!", font=("Helvetica", 45), foreground = fg, background = bg)
                first_word_label.pack(expand=True)
                second_word[0].title("Le second!")
                second_word_label = Label(second_word[0], text = "Le second!", font=("Helvetica", 45), foreground = fg, background = bg)
                second_word_label.pack(expand=True)
            else:
                first_word[0].title("The first one!")
                first_word_label = Label(first_word[0], text = "The first one!", font=("Helvetica", 45), foreground = fg, background = bg)
                first_word_label.pack(expand=True)
                second_word[0].title("The second one!")
                second_word_label = Label(second_word[0], text = "The second one!", font=("Helvetica", 45), foreground = fg, background = bg)
                second_word_label.pack(expand=True)
            first_word[0].update()
            second_word[0].update()
    if Stop_everything is False:
        Stopping_everything(True)

def write(txt = None, affichage = True):
    '''This one's purpose is to use the randomely_choosen_text fonction without having a super long name
    It also bypass the Stop_everything feature (which stop button from working is it is at True)'''
    randomely_choosen_text(txt, affichage)

def count(length = None, affichage = True):
    '''This one's purpose is to use the randomely_generated_text fonction without having a super long name
    It also bypass the Stop_everything feature (which stop button from working is it is at True)'''
    randomely_generated_text(length, affichage)

def wait(fl):
    '''The only use of this fonction is because sometime I type "wait" instead of "time.sleep"
    Yes I have some lazyness issues'''
    time.sleep(fl)

Nostalgique = False
def Nostalgia():
    '''That fonction is just to activate the "Past memory", which is to add old user-writed texts to the word_list
    It uses a .txt file to save the texts (if the file doesn't exist, it create it)
    Also, you can only use it once'''
    global Nostalgique
    if Nostalgique is False:
        Nostalgique = True
        try:
            f = open("Lots of different texts.txt", "r")
        except FileNotFoundError:
            f = open("Lots of different texts.txt", "w")
            f.write("I definitely remember you now\nTest Mémoire Passée (TMP)\n")
            f.close()
            f = open("Lots of different texts.txt", "r")
        text = remove_last(f.readline())
        while text != "":
            word_list_universal.append(text)
            word_list.append(text)
            text = remove_last(f.readline())
        f.close()

def save(txt):
    '''This one is linked to the nostalgia function, it's used to save the user-writed texts in the .txt file'''
    f = open("Lots of different texts.txt", "r")
    text = f.readline()
    l = []
    while text != "":
        l.append(text)
        text = f.readline()
    f.close()
    f = open("Lots of different texts.txt", "w")
    for i in l:
        f.write(i)
    f.write(txt + "\n")
    f.close()

def letters(n):
    '''This one is to do the glitchy effect in the "virus" windows'''
    for j in range(6):
        for _ in range(80 * (j+1)):
            for i in range(j, 6):
                s = ''.join([optimized_choice() for k in range(15)])
                #print(s)
                labels[n][i].config(text = s)
                list_w[n].update()
    
def disable_event():
    '''This function is used to block the user from closing the windows'''
    print("MOUAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHA")#pass

def you_got_a_virus():
    '''Used to create and use the "virus" windows'''
    global n
    global Virus
    global Virus_T
    global Virus_launched
    if Virus:
        if Virus_T != False:
            list_w.append(Tk())
            list_w[n].title(f"Virus {n}")
            x = random.randint(250, 500)
            y = random.randint(250, 500)
            list_w[n].geometry(f"{x}x{y}+{random.randint(0, list_w[n].winfo_screenwidth()-x)}+{random.randint(0, list_w[n].winfo_screenheight()-y)}")
            list_w[n].configure(background=bg)
            list_w[n].attributes("-topmost", True)
            list_w[n].protocol("WM_DELETE_WINDOW", disable_event)
            Virus_launched = True
            Virus_T = False
            labels.append([])
            assert labels[n] == []
            for i in range(6):
                labels[n].append(Label(list_w[n], text = ''.join([optimized_choice() for k in range(15)]), font=("Helvetica", 50), foreground = fg, background = bg))
                labels[n][i].pack(expand=True)
            list_w[n].update()
        if Virus_launched is True:
            for i in range(n+1):
                #for _ in range(50*(i+3)):
                letters(i)

def memory_minigame(cha):
    '''I could have put this function in the randomely_choosen_text one but that's okay
    It's used to play the memory/password minigame'''
    global memory_password
    global Stop_everything
    global Ligne
    def destroy_everything():
        for i in memory_game_windows:
            i.destroy()
    if memory_password[0] == cha:
        memory_password = memory_password[1:]
    else:
        destroy_everything()
        write(memory_password)
        time.sleep(1.5)
        fenetre.destroy()
    if memory_password == "":
        destroy_everything()
        Stop_everything = False
        Stopping_everything(True)
        add_four_changing_color_mechanics = 0
        Now_you_can_change_colors.append(Label(fenetre, width=50, text = "Change the colors (Backgroud color and text color)", foreground=fg, background=bg))
        Now_you_can_change_colors[add_four_changing_color_mechanics].grid(row=Ligne, column=0,pady=10)
        add_four_changing_color_mechanics += 1
        Ligne += 1
        Now_you_can_change_colors.append(Entry(fenetre, width = 13, textvariable=background_color))
        Now_you_can_change_colors[add_four_changing_color_mechanics].grid(row=Ligne, column=0,pady=10)
        add_four_changing_color_mechanics += 1
        Ligne += 1
        Now_you_can_change_colors.append(Entry(fenetre, width = 13, textvariable=foregound_color))
        Now_you_can_change_colors[add_four_changing_color_mechanics].grid(row=Ligne, column=0,pady=10)
        add_four_changing_color_mechanics += 1
        Ligne += 1
        Now_you_can_change_colors.append(Button(fenetre, text="changing colors", width=20, command=changing_the_color, foreground=fg, background=bg))
        Now_you_can_change_colors[add_four_changing_color_mechanics].grid(row=Ligne, column=0,pady=10)
        add_four_changing_color_mechanics += 1
        Ligne += 1
        language()
        
def changing_the_color(b = None, f = None):
    '''Ever wanted to change the color of everything on the windows? Use that function!
    You can each use the entries added by the memory minigame or enter the colors manually by calling the function'''
    global bg
    global fg
    if b is None:
        bg = background_color.get()
    else:
        bg = b
    if f is None:
        fg = foregound_color.get()
    else:
        fg = f
    try:
        fenetre.config(background = bg)
        random_text.config(foreground = fg, background = bg)
        first_thing.config(foreground = fg, background = bg)
        randomizer.config(foreground = fg, background = bg)
        second_thing.config(foreground = fg, background = bg)
        not_really_randomizer.config(foreground = fg, background = bg)
        real_randomizer.config(foreground = fg, background = bg)
        last_thing.config(foreground = fg, background = bg)
        MemoryCheck.config(foreground = fg, background = bg)
        PastMemoryCheck.config(foreground = fg, background = bg)
        for i in Now_you_can_change_colors:
            i.config(background = bg, foreground = fg)
        English_language.config(foreground = fg, background = bg)
        French_language.config(foreground = fg, background = bg)
        if now_you_can_see_the_length:
            word_length[0].config(background = bg, foreground = fg)
    except TclError:
        if French.get() == "Fake True" and English.get() == "Fake False":
            raise TclError("Ce ne sont pas des couleurs")
        else:
            raise TclError("These are not colors")

def longest_minigame(a):
    '''I could have put this function in the randomely_choosen_text one but that's okay
    It's used to play the "guess the longest text" minigame'''
    global now_you_can_see_the_length
    global Stop_everything
    global Ligne
    def destroy_everything():
        first_word[0].destroy()
        second_word[0].destroy()
    if a is True:
        destroy_everything()
        now_you_can_see_the_length = True
        word_length.append(Label(fenetre, text = "0", font=("Helvetica", 30), foreground=fg, background=bg))
        word_length[0].grid(row=Ligne, column = 0, pady = 10)
        Ligne += 1
        fenetre.update()
        Stop_everything = False
        Stopping_everything(True)
    else:
        destroy_everything()
        if English.get():
            write("Too bad!")
        elif French.get():
            write("Raté!")
        else:
            write("Too bad!")
        time.sleep(1.5)
        fenetre.destroy()

def I_hope_there_will_be_a_lot_of_things_there():
    '''I guess there's not a lot of things there
    This function was supposed to be used to put all the functions that I want to use everytime a button is clicked'''
    Stopping_everything(False)
    you_got_a_virus()

if True: #Every events variables
    #Those "if True" is only so it takes less place
    Stop_everything = False
    Virus = False
    Virus_T = False
    Virus_launched = False
    n = -1
    labels = []
    list_w = []
    memory_password = "Not_defined_yet"
    memory_game_windows = []
    memory_game_labels = []
    memory_game_buttons = []
    Now_you_can_change_colors = []
    word_length = []
    now_you_can_see_the_length = False
    first_word = []
    second_word = []
    SUPREMACY = ""

if True: #Window initialisation
    fenetre = Tk()
    fenetre.geometry("1500x750+100+100")
    fenetre.configure(background=bg)
    fenetre.title("Generate text with a cool animation")

if True: #All stringVar
    random_number = StringVar(fenetre)
    not_random_text = StringVar(fenetre)
    number_of_waiting = StringVar(fenetre)
    Memory = StringVar(fenetre, 'Fake False')
    PastMemory = StringVar(fenetre, 'Fake False')
    background_color = StringVar(fenetre)
    foregound_color = StringVar(fenetre)
    French = StringVar(fenetre, 'Fake False')
    English = StringVar(fenetre, 'Fake True')

if True: #Base widgets
    Ligne = 0
    random_text = Label(fenetre, text = "", font=("Helvetica", 60), foreground=fg, background=bg)
    random_text.grid(row=Ligne, column=0,pady=10)
    Ligne += 1
    
    first_thing = Label(fenetre, width=40, text="How many characters do you want to generate?", foreground=fg, background=bg)
    first_thing.grid(row=Ligne, column=0, pady=10)
    Ligne += 1
    
    how_randomized = Entry(fenetre, width=13, textvariable=random_number)#, foreground="red", background="#000000")
    how_randomized.grid(row=Ligne, column=0, pady=10)
    Ligne += 1
    
    randomizer = Button(fenetre, text="randomizing", width=20, command=randomely_generated_text, foreground=fg, background=bg)
    randomizer.grid(row=Ligne, column=0, pady=10)
    Ligne += 1
    
    second_thing = Label(fenetre, width=40, text="What text do you want to generate?", foreground=fg, background=bg)
    second_thing.grid(row=Ligne, column=0, pady=10)
    Ligne += 1
    
    what_final_text = Entry(fenetre, width = 13, textvariable=not_random_text)
    what_final_text.grid(row = Ligne, column = 0, pady = 10)
    Ligne += 1
    
    not_really_randomizer = Button(fenetre, text="generate text",width = 20, command=not_really_randomized_text, foreground=fg, background=bg)
    not_really_randomizer.grid(row = Ligne, column = 0, pady = 10)
    Ligne += 1
    
    real_randomizer = Button(fenetre, text="real randomizing", width=20, command=really_randomely_generated_text, foreground=fg, background=bg)
    real_randomizer.grid(row=Ligne, column=0, pady=10)
    Ligne += 1
    
    last_thing = Label(fenetre, width=40, text="How much waiting between each character", foreground=fg, background=bg)
    last_thing.grid(row = Ligne, column = 0, pady = 10)
    Ligne += 1
    
    how_much_waiting = Entry(fenetre, width = 13, textvariable=number_of_waiting)
    how_much_waiting.grid(row = Ligne, column = 0, pady = 10)
    Ligne += 1
    
    MemoryCheck = Checkbutton(fenetre, text="Memory", variable = Memory, onvalue='Fake True', offvalue='Fake False', foreground=fg, background=bg)
    MemoryCheck.grid(row=Ligne, column = 0)
    Ligne += 1
    
    PastMemoryCheck = Checkbutton(fenetre, text="Past Memory", variable = PastMemory, onvalue='Fake True', offvalue='Fake False', foreground=fg, background=bg, command=Nostalgia)
    PastMemoryCheck.grid(row=Ligne, column = 0)
    Ligne += 1
    
    English_language = Checkbutton(fenetre, text="English", variable=English, onvalue="Fake True", offvalue="Fake False", foreground=fg, background=bg, command=language)
    English_language.grid(row=Ligne, column = 0)
    Ligne += 1
    
    French_language = Checkbutton(fenetre, text="French", variable=French, onvalue="Fake True", offvalue="Fake False", foreground=fg, background=bg, command=language)
    French_language.grid(row=Ligne, column = 0)
    Ligne += 1
    
    fenetre.update()

language()

fenetre.mainloop()
