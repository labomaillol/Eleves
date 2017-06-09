from tkinter import *
import random

def change_suite_easy():
    suite = random.sample(CLR_POSSIBLE, 3)
    print(suite)
    return suite

def change_suite_normal():
    suite = random.sample(CLR_POSSIBLE, 4)
    print(suite)
    return suite

def change_suite_hard():
    suite = random.sample(CLR_POSSIBLE, 5)
    print(suite)
    return suite

def verifier ():
    global bon, bienPlace,choixJoueur, NB_RENDU
    bon=0
    bienPlace=0

     
    for i, j in zip(choixJoueur,suite):
            if i==j :
                bienPlace+=1;
            elif i in suite :
                bon+=1
    if bienPlace == 3:
        ## On appele parti_fini, et ajouter 'Gagné', au texte
        parti_fini('WIN')
    else:
        print('VERIFY_NB_RENDU:', NB_RENDU)
        ## Si NB_RENDU n'Est pas égal à la limite maximum
        if MAX_LIMIT != NB_RENDU:
            ## Sinon, on créer les textes
            can.create_text(400,positiony,text=("BONNE : {0} ".format(bienPlace)), font="Arial",fill='blue')
            can.create_text(515,positiony,text=("MAL PLACE : {0} ".format(bon)), font="Arial",fill='blue')
            ## Reset la liste vide
            choixJoueur=[]
            ## On ajoute +1 au nombre d'essais
            NB_RENDU += 1
             
        else:
            # Si la limite est atteinte, il a perdu
            print('FAILURE')
            ## On appele part_fini, et ajouter 'Perdu' au texte
            parti_fini('LOSE')

def verifier2 ():
    global bon, bienPlace,choixJoueur, NB_RENDU
    bon=0
    bienPlace=0

     
    for i, j in zip(choixJoueur,suite):
            if i==j :
                bienPlace+=1;
            elif i in suite :
                bon+=1
    if bienPlace == 4:
        ## On appele parti_fini, et ajouter 'Gagné', au texte
        parti_fini2('WIN')
    else:
        print('VERIFY_NB_RENDU:', NB_RENDU)
        ## Si NB_RENDU n'Est pas égal à la limite maximum
        if MAX_LIMIT != NB_RENDU:
            ## Sinon, on créer les textes
            can.create_text(400,positiony,text=("BONNE : {0} ".format(bienPlace)), font="Arial",fill='blue')
            can.create_text(515,positiony,text=("MAL PLACE : {0} ".format(bon)), font="Arial",fill='blue')
            ## Reset la liste vide
            choixJoueur=[]
            ## On ajoute +1 au nombre d'essais
            NB_RENDU += 1
             
        else:
            # Si la limite est atteinte, il a perdu
            print('FAILURE')
            ## On appele part_fini, et ajouter 'Perdu' au texte
            parti_fini2('LOSE')

def verifier3 ():
    global bon, bienPlace,choixJoueur, NB_RENDU
    bon=0
    bienPlace=0

     
    for i, j in zip(choixJoueur,suite):
            if i==j :
                bienPlace+=1;
            elif i in suite :
                bon+=1
    if bienPlace == 5:
        ## On appele parti_fini, et ajouter 'Gagné', au texte
        parti_fini3('WIN')
    else:
        print('VERIFY_NB_RENDU:', NB_RENDU)
        ## Si NB_RENDU n'Est pas égal à la limite maximum
        if MAX_LIMIT != NB_RENDU:
            ## Sinon, on créer les textes
            can.create_text(400,positiony,text=("BONNE : {0} ".format(bienPlace)), font="Arial",fill='blue')
            can.create_text(515,positiony,text=("MAL PLACE : {0} ".format(bon)), font="Arial",fill='blue')
            ## Reset la liste vide
            choixJoueur=[]
            ## On ajoute +1 au nombre d'essais
            NB_RENDU += 1
             
        else:
            # Si la limite est atteinte, il a perdu
            print('FAILURE')
            ## On appele part_fini, et ajouter 'Perdu' au texte
            parti_fini3('LOSE')

def reconnaitre(event):
    global positionx, positiony
    positionx += 59
     
    if positionx>176:
        positionx=26
        positiony += 55
         
    x1=event.x
    y1=event.y
    print(x1, y1)
    ## Trouvé le ID du cercle le plus proche du clique (tuple)
    the_closest_can = event.widget.find_closest(x1,y1)[0] #Premier élément
    ## Avec le ID, on peut trouver la couleur du cercle dans le canva
    the_color_name = event.widget.itemcget(the_closest_can, 'fill')
    ## position curseur et objet sélectionner
    the_tags_can = event.widget.gettags(the_closest_can)
    print('CLOSEST:', the_closest_can)
    print('COLOR_NAME:', the_color_name)
    print('TAGS:', the_tags_can)
 
    if the_color_name == 'green':
        cJ = 'V' 
    elif the_color_name == 'yellow':
        cJ = 'J' 
    else: ## Sinon, prendre la première lettre et la mettre en majuscule
        cJ = the_color_name[0].upper()
 
    if cJ not in choixJoueur:
        choixJoueur.append(cJ)
        can.create_oval(positionx-15, positiony-15, positionx+15, positiony+15,fill=the_color_name)
    else: ## déjà à l'intérieur.
        print('Already inside:', cJ, the_color_name)
        ## On recule la position du X, qu'on a additioné au début
        positionx -= 58
 
    print('LIST_CHOIXJOUEUR:', choixJoueur)
    if len(choixJoueur) >=3:
        verifier()
         
    print() #Espacer les prints, par block

def reconnaitre2(event):
    global positionx, positiony
    positionx += 59
     
    if positionx>230:
        positionx=26
        positiony += 55
         
    x1=event.x
    y1=event.y
    print(x1, y1)
    ## Trouvé le ID du cercle le plus proche du clique (tuple)
    the_closest_can = event.widget.find_closest(x1,y1)[0] #Premier élément
    ## Avec le ID, on peut trouver la couleur du cercle dans le canva
    the_color_name = event.widget.itemcget(the_closest_can, 'fill')
    ## position curseur et objet sélectionner
    the_tags_can = event.widget.gettags(the_closest_can)
    print('CLOSEST:', the_closest_can)
    print('COLOR_NAME:', the_color_name)
    print('TAGS:', the_tags_can)
 
    if the_color_name == 'green':
        cJ = 'V' 
    elif the_color_name == 'yellow':
        cJ = 'J' 
    else: ## Sinon, prendre la première lettre et la mettre en majuscule
        cJ = the_color_name[0].upper()
 
    if cJ not in choixJoueur:
        choixJoueur.append(cJ)
        can.create_oval(positionx-15, positiony-15, positionx+15, positiony+15,fill=the_color_name)
    else: ## déjà à l'intérieur.
        print('Already inside:', cJ, the_color_name)
        ## On recule la position du X, qu'on a additioné au début
        positionx -= 58
 
    print('LIST_CHOIXJOUEUR:', choixJoueur)
    if len(choixJoueur) >= 4:
        verifier2()
         
    print() #Espacer les prints, par block

def reconnaitre3(event):
    global positionx, positiony
    positionx += 59
     
    if positionx>283:
        positionx=26
        positiony += 55
         
    x1=event.x
    y1=event.y
    print(x1, y1)
    ## Trouvé le ID du cercle le plus proche du clique (tuple)
    the_closest_can = event.widget.find_closest(x1,y1)[0] #Premier élément
    ## Avec le ID, on peut trouver la couleur du cercle dans le canva
    the_color_name = event.widget.itemcget(the_closest_can, 'fill')
    ## position curseur et objet sélectionner
    the_tags_can = event.widget.gettags(the_closest_can)
    print('CLOSEST:', the_closest_can)
    print('COLOR_NAME:', the_color_name)
    print('TAGS:', the_tags_can)
 
    if the_color_name == 'green':
        cJ = 'V' 
    elif the_color_name == 'yellow':
        cJ = 'J' 
    else: ## Sinon, prendre la première lettre et la mettre en majuscule
        cJ = the_color_name[0].upper()
 
    if cJ not in choixJoueur:
        choixJoueur.append(cJ)
        can.create_oval(positionx-15, positiony-15, positionx+15, positiony+15,fill=the_color_name)
    else: ## déjà à l'intérieur.
        print('Already inside:', cJ, the_color_name)
        ## On recule la position du X, qu'on a additioné au début
        positionx -= 58
 
    print('LIST_CHOIXJOUEUR:', choixJoueur)
    if len(choixJoueur) >= 5:
        verifier3()
         
    print() #Espacer les prints, par block

def main():

    #traits verticaux
    can.create_line(0,0,0,320,fill='gold')
    can.create_line(60,0,60,320,fill='red')
    can.create_line(120,0,120,320,fill='blue')
    can.create_line(180,0,180,320,fill='yellow')
      
    #traits horizontaux
    can.create_line(0,0,180,0,fill='gold')
    can.create_line(0,53,180,53,fill='red')
    can.create_line(0,106,180,106,fill='blue')
    can.create_line(0,160,180,160,fill='white')
    can.create_line(0,213,180,213,fill='yellow')
    can.create_line(0,266,180,266,fill='green')
    can.create_line(0,320,180,320,fill='gray')
      
    can.create_oval(220-15, 26-15, 220+15, 26+15, fill='red')
    can.create_oval(220-15, 79-15, 220+15, 79+15, fill='yellow')
    can.create_oval(220-15, 133-15, 220+15, 133+15, fill='blue')
    can.create_oval(220-15, 186-15, 220+15, 186+15, fill='orange')
    can.create_oval(220-15, 240-15, 220+15, 240+15, fill='green')
    can.create_oval(220-15, 293-15, 220+15, 293+15, fill='gray')

 
    can.bind("<Button-1>",reconnaitre)

def main2():

    can.create_line(0,0,0,320,fill='gold')
    can.create_line(60,0,60,320,fill='red')
    can.create_line(120,0,120,320,fill='blue')
    can.create_line(180,0,180,320,fill='yellow')
    can.create_line(240,0,240,320,fill='green')

    can.create_line(0,0,240,0,fill='gold')
    can.create_line(0,53,240,53,fill='red')
    can.create_line(0,106,240,106,fill='blue')
    can.create_line(0,160,240,160,fill='white')
    can.create_line(0,213,240,213,fill='yellow')
    can.create_line(0,266,240,266,fill='green')
    can.create_line(0,320,240,320,fill='gray')
      
    can.create_oval(280-15, 26-15, 280+15, 26+15, fill='red')
    can.create_oval(280-15, 79-15, 280+15, 79+15, fill='yellow')
    can.create_oval(280-15, 133-15, 280+15, 133+15, fill='blue')
    can.create_oval(280-15, 186-15, 280+15, 186+15, fill='orange')
    can.create_oval(280-15, 240-15, 280+15, 240+15, fill='green')
    can.create_oval(280-15, 293-15, 280+15, 293+15, fill='gray')

    can.bind("<Button-1>",reconnaitre2)
    
def main3():
    #cadre du mastermind

    #traits verticaux
    can.create_line(0,0,0,320,fill='gold')
    can.create_line(60,0,60,320,fill='red')
    can.create_line(120,0,120,320,fill='blue')
    can.create_line(180,0,180,320,fill='yellow')
    can.create_line(240,0,240,320,fill='green')
    can.create_line(300,0,300,320,fill='gray')
      
    #traits horizontaux
    can.create_line(0,0,300,0,fill='gold')
    can.create_line(0,53,300,53,fill='red')
    can.create_line(0,106,300,106,fill='blue')
    can.create_line(0,160,300,160,fill='white')
    can.create_line(0,213,300,213,fill='yellow')
    can.create_line(0,266,300,266,fill='green')
    can.create_line(0,320,300,320,fill='gray')
    
      
    can.create_oval(340-15, 26-15, 340+15, 26+15, fill='red')
    can.create_oval(340-15, 79-15, 340+15, 79+15, fill='yellow')
    can.create_oval(340-15, 133-15, 340+15, 133+15, fill='blue')
    can.create_oval(340-15, 186-15, 340+15, 186+15, fill='orange')
    can.create_oval(340-15, 240-15, 340+15, 240+15, fill='green')
    can.create_oval(340-15, 293-15, 340+15, 293+15, fill='gray')

    can.bind("<Button-1>",reconnaitre3)

def parti_fini(the_text, suffix_to_say='YOU '):
    """Lorsque la parti est fini"""
    can.delete('all')
    rect = can.create_rectangle(0,0,1001,501)
    txt = can.create_text(500,250, text=suffix_to_say+the_text,font="Arial 70")
 
    btn_quit = Button(can, text="QUIT", command=base)
    ## On place le nouveau bouton dans le canva principale,
    ## en créant une fenêtre juste pour lui
    ## canva.create_window(axeX, axeY, anchor=NW, window=le_widget_a_attacher)
    btn_quit_window = can.create_window(250,350, anchor=NW, window=btn_quit)
     
    btn_retry = Button(can, text="TRY AGAIN", command=restarting)
    ## On place le nouveau bouton dans le canva principale
    ## canva.create_window(axeX, axeY, anchor=NW, window=le_widget_a_attacher)
    btn_retry_window = can.create_window(750,350, anchor=NW, window=btn_retry)

    btn_solution = Button(can, text="SOLUTION", command=solution)
    btn_solution_window = can.create_window(480,350, anchor = NW, window=btn_solution)
 
    ## Ensuite on peut appeler notre fonction, qui MODIFIERA,
    ## La configuration des dessins (rect, txt) dans le canva (can)
    change_color(can, rect, txt)

def parti_fini2(the_text, suffix_to_say='YOU '):
    can.delete('all')
    rect = can.create_rectangle(0,0,1001,501)
    txt = can.create_text(500,250, text=suffix_to_say+the_text,font="Arial 70")
 
    btn_quit = Button(can, text="QUIT", command=base)
    btn_quit_window = can.create_window(250,350, anchor=NW, window=btn_quit)
    btn_retry = Button(can, text="TRY AGAIN", command=restarting2)
    btn_retry_window = can.create_window(750,350, anchor=NW, window=btn_retry)
    btn_solution = Button(can, text="SOLUTION", command=solution)
    btn_solution_window = can.create_window(480,350, anchor = NW, window=btn_solution)
 
    change_color(can, rect, txt)

def parti_fini3(the_text, suffix_to_say='YOU '):
    can.delete('all')
    rect = can.create_rectangle(0,0,1001,501)
    txt = can.create_text(500,250, text=suffix_to_say+the_text,font="Arial 70")
 
    btn_quit = Button(can, text="QUIT", command=base)
    btn_quit_window = can.create_window(250,350, anchor=NW, window=btn_quit)
    btn_retry = Button(can, text="TRY AGAIN", command=restarting3)
    btn_retry_window = can.create_window(750,350, anchor=NW, window=btn_retry)   
    btn_solution = Button(can, text="SOLUTION", command=solution)
    btn_solution_window = can.create_window(480,350, anchor = NW, window=btn_solution)
    change_color(can, rect, txt)

def change_color(widget, rect, txt):
    """Changer la couleur, à partir d'un widget"""
    ## itemconfigure(nom_du_dessin, fill="")
    widget.itemconfigure(rect, fill=random.choice(BG_GAGNANT))
    widget.itemconfigure(txt, fill=random.choice(TEXT_GAGNANT))
    ## On callback, à chaque 2 secondes, en appelant change_color,
    ## avec ses arguments, widget, rect, txt
    widget.after(2000, change_color, widget, rect, txt)

def solution():
    can.delete('all')
    can.create_rectangle(200,200,800,400, outline='red', fill='turquoise')
    can.create_text(500,100, text='LA SOLUTION ETAIT : ', font='Arial 30', fill='blue')
    can.create_text(500,300, text=suite, font='Arial 50', fill='gold')
    btn_quit = Button(can, text="QUIT", command=base)
    btn_quit_window = can.create_window(470,450, anchor = NW, window=btn_quit)
     
def restarting():
    """Fonction recommancer"""
    print('Restarting..')
    ## On appele les variable à modifier (global)
    global NB_RENDU, choixJoueur, positionx, positiony
    ## On supprime les dessins
    can.delete('all')
    ## On reset tous les variables de départ..
    NB_RENDU = 0
    choixJoueur=[]
    positionx=-30
    positiony=26
 
    #On recall main(), pour redessiner les dessins..
    main()

def restarting2():
    print('Restarting..')
    global NB_RENDU, choixJoueur, positionx, positiony
    can.delete('all')
    NB_RENDU = 0
    choixJoueur=[]
    positionx=-30
    positiony=26
    main2()

def restarting3():
    print('Restarting..')
    global NB_RENDU, choixJoueur, positionx, positiony
    can.delete('all')
    NB_RENDU = 0
    choixJoueur=[]
    positionx=-30
    positiony=26
    main3()

def solo():
    can.delete('all')
    global choixJoueur, NB_RENDU,positionx,positiony
    NB_RENDU = 0
    choixJoueur=[]
    positionx = -30
    positiony = 26
    ecranSolo ()

        
def ecranSolo ():
    can.create_text(500, 70, text="LEVELS", font='Arial 70', fill='blue')
#ligne1
    can.create_oval(250-100,270-100,250+100,270+100, fill='blue')
    btn_1= Button(can, text='EASY', command=level1)
    btn_1_window = can.create_window(230,260, anchor=NW, window=btn_1)
    can.create_oval(500-100,270-100,500+100,270+100, fill='white')
    btn_2= Button(can, text='NORMAL', command=level2)
    btn_2_window = can.create_window(465,260, anchor=NW, window=btn_2)
    can.create_oval(750-100,270-100,750+100,270+100, fill='red')
    btn_3= Button(can, text='HARD', command=level3)
    btn_3_window = can.create_window(730,260, anchor=NW, window=btn_3)

def level1():
    can.delete('all')
    global suite
    suite = change_suite_easy()
    main()

def level2():
    can.delete('all')
    global suite
    suite = change_suite_normal()
    main2()

def level3():
    can.delete('all')
    global suite
    suite = change_suite_hard()
    main3()

def multi():
    global suite, positiona, positionb, choixJoueur, NB_RENDU, positionx,positiony
    can.delete('all')
    can.create_text(500, 60, text='VOTRE SUITE', font='Arial 20', fill='blue')
    can.create_rectangle(200,100,800,300, outline='red', fill='turquoise') 
    can.create_text(500,350, text='COULEURS POSSIBLES', font='Arial 20', fill='blue')
    can.create_oval(127-50, 430-50, 127+50, 430+50, fill='red')
    can.create_oval(277-50, 430-50, 277+50, 430+50, fill='yellow')
    can.create_oval(427-50, 430-50, 427+50, 430+50, fill='blue')
    can.create_oval(577-50, 430-50, 577+50, 430+50, fill='orange')
    can.create_oval(727-50, 430-50, 727+50, 430+50, fill='green')
    can.create_oval(877-50, 430-50, 877+50, 430+50, fill='grey')
    positiona=130
    positionb=200
    suite= []
    NB_RENDU = 0
    choixJoueur=[]
    positionx = -30
    positiony = 26
    can.bind("<Button-1>",couleurmulti)

def couleurmulti(event):
    global positiona, positionb
    positiona += 150
    x1=event.x
    y1=event.y
    print(x1, y1)
    the_closest_can = event.widget.find_closest(x1,y1)[0]
    the_color_name = event.widget.itemcget(the_closest_can, 'fill')
    the_tags_can = event.widget.gettags(the_closest_can)
    print('CLOSEST:', the_closest_can)
    print('COLOR_NAME:', the_color_name)
    print('TAGS:', the_tags_can)

    if the_color_name == 'green':
        s = 'V' 
    elif the_color_name == 'yellow':
        s = 'J' 
    else:
        s = the_color_name[0].upper()

    if s not in suite:
        suite.append(s)
        can.create_oval(positiona-50, positionb-50, positiona+50, positionb+50,fill=the_color_name)
    else:
        print('Already inside:', s, the_color_name)
        
        positiona -= 150

    print('LIST_SUITE_CHOISI:', suite)
    if len(suite) >= 4:
        btn_valider = Button(can, text="VALIDER", command=valider)
        btn_valider = can.create_window(900,250, anchor=NW, window=btn_valider)
       
    print() #Espacer les prints, par block

def valider():
    can.delete('all')
    main2()

def base():
    global can
    global fenetre
#ECRAN DE DEMARRAGE et choix du mode 
    can.delete('all')
    can.create_text(500,80, text='Mastermind', font='Razing 70', fill='red')
    can.create_rectangle(250,155,750,235,outline='blue', fill='red')
    can.create_text(500,195, text= 'UN JOUEUR', font='Arial 20', fill='blue')
    can.create_rectangle(250,295,750,375,outline='blue', fill='red')
    can.create_text(500,335, text='DEUX JOUEURS', font='Arial 20', fill='blue')

    btn_solo= Button(can, text='START', command=solo)
    btn_solo_window = can.create_window(700,182, anchor=NW, window=btn_solo)

    btn_multi= Button(can, text='START', command=multi)
    btn_multi_window = can.create_window(700,322, anchor=NW, window=btn_multi)

    can.bind("<Button-1>",solo, multi)

CLR_POSSIBLE = ['R','O','V','J','B','G'] 
NB_RENDU = 0 #nombre d'essais
MAX_LIMIT = 5 # 6 lignes (0 à 5)
choixJoueur=[]
positionx=-30
positiony=26
positiona=130
positionb=200
suite=[]
BG_GAGNANT = ['red', 'orange', 'blue', 'green', 'grey']
TEXT_GAGNANT = ['black', 'white']
fenetre=Tk()
can = Canvas(fenetre,bg='black', height=500, width=1000)
can.pack()
fenetre.mainloop
base()
         
fenetre.mainloop
