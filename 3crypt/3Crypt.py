#-------------- importation des differents modules --------------  

from tkinter import *
import tkinter.messagebox as tm 

#-------------- fonction pour interface du Login --------------

def Login():
 
    if Motdepasse.get() == '0518031212':
        Mafenetre.destroy()
        fen1 = Tk()
        fen1.title("•3Crypt V1•")
        fen1.geometry('1280x720')
        fen1.configure(bg="white")
        fen1.resizable(False, False)
        Label1 = Label(fen1,bg="blue",fg='white',text="Bienvenue sur 3Crypt votre logiciel de cryptage n°1",font='Helvetica') 
        Label1.place(x=500,y= 0)
        label3= Label(fen1,bg="white",text=" Notre programme a pour but de protéger vos données. Pour cela notre programme dispose de plusieurs algorithmes afin de crypter vos messages.",font="Times")
        label3.place(x=5,y=65)
        Label4 = Label(fen1,bg="white", text="Cependant il permet aussi de dechiffrer des messages dans plusieurs languages.",font="Times")
        Label4.place(x=5, y=90)
        Label5 = Label(fen1,bg="white", text="Pour cela nous mettons à votre dispositions plusieurs algorithme utilisant chacun des methodes differentes de cryptage.",font="Times")
        Label5.place(x=5, y=115)
        bouton1 = Button(fen1,bg="white",text="•Méthode Vigenère•",command=vigenere2,width=30,activebackground='blue')
        bouton1.place(x=40,y=370)
        bouton1 = Button(fen1,bg="white",text="•Méthode Vernam •",width=30,activebackground='red')
        bouton1.place(x=1015,y=370)
        bouton1 = Button(fen1,bg="white",text="•Méthode César•",command=crypt2,width=30,activebackground='green')
        bouton1.place(x=525,y=370)
        Label2 = Label(fen1,bg="white", text="Copyright © 2018 3Crypt WIG")
        Label2.place(x=554 ,y=695)
        photo2=PhotoImage(file='3Crypt.png')
        labelphoto=Label(fen1 ,bg="white", image=photo2).place(x=960,y=0)
        photo3=PhotoImage(file='cle.png')
        labelphoto=Label(fen1 ,bg="white", image=photo3).place(x=40,y=150)
        photo4=PhotoImage(file='super.png')
        labelphoto=Label(fen1 ,bg="white", image=photo4).place(x=470,y=400)
        photo5=PhotoImage(file='vigenere.png')
        labelphoto=Label(fen1 ,bg="white", image=photo5).place(x=10,y=410)
        photo6=PhotoImage(file='bientot.png')
        labelphoto=Label(fen1 ,bg="white", image=photo6).place(x=990,y=232)
        photo7=PhotoImage(file='vernam.png')
        labelphoto=Label(fen1 ,bg="white", image=photo7).place(x=960,y=410)
        fen1.mainloop()
   
    else:
        tm.showerror("Login erreur", "Identifiant Incorrect")
        
 

#-------------- fonction pour interface login  --------------

Mafenetre = Tk()
Mafenetre.title('•Identification requise•')
Mafenetre.geometry("300x80+850+400")
Mafenetre.resizable(False, False)
 
Label1 = Label(Mafenetre, text = 'Mot de passe ')
Label1.pack(side = LEFT, padx = 5, pady = 5)
 
Motdepasse= StringVar()
Champ = Entry(Mafenetre, textvariable= Motdepasse, show='*', bg ='red', fg='blue')
Champ.focus_set()
Champ.pack(side = LEFT, padx = 5, pady = 5)
 
Bouton = Button(Mafenetre, text ='Valider', command = Login)
 
Bouton.pack(side = LEFT, padx = 5, pady = 5)
 
#--------------fonction qui crypte(Méthode César)--------------

def crypt():
    global numb3,numb2,phrase
    phrase=entree.get()
    key= entree1.get()
    phrase= phrase.upper()
    alpha= "ABCDEFGHIJKLMNOPQRSTUVWXYZ "
    crypt= ""
    for let in phrase:
        if let in alpha:
            indice=alpha.find(let)
            num= indice +int(key)
            print(num)
            if(num==26):
                crypt=crypt+alpha[0]
            elif(indice==26):
                crypt=crypt+alpha[26]
            elif(num>=len(alpha)):
                #numb2=abs(num)
                numb3=num-(len(alpha)-1)
                crypt=crypt+alpha[numb3]
            if(num<len(alpha)-1 and num>0):
                crypt=crypt+alpha[num]
    print(crypt1.insert(0,crypt))
    print(phrase)
    print(crypt)
    
#--------------fonction qui decrypte( Méthode César )-------------- 

def décrypt():
    
    phrase2=entree2.get()
    key2= entree3.get()
    phrase2= phrase2.upper()
    
    alpha= "ABCDEFGHIJKLMNOPQRSTUVWXYZ "
    decrypt= ""
    for let in phrase2:
        if let in alpha:
            num= alpha.find(let)-int(key2)
            if(num==26-int(key2)):
                decrypt=decrypt+alpha[26]
            elif(num<0 and num!=(-26)):
                numb=26+num
                decrypt=decrypt+alpha[numb]
            else:
                decrypt=decrypt+alpha[num]
    print(Decrypt1.insert(0,decrypt))
    print(phrase2)
    print(decrypt)    
    

#--------------fonction pour interface ( Méthode César )--------------

def crypt2():
    global entree,entree1,entree2,entree3,Decrypt1,crypt1
    fen = Tk()
    fen.title("•Méthode César•")
    fen.focus_set()
    fen.geometry("265x210+850+400")
    fen.resizable(False, False)

 
    Label(fen,text=' CRYPTAGE ',fg ='black').grid(row =0,column=1)
    Label(fen,text='Texte à Crypter : ',fg ='blue').grid(row =1,sticky =W)
    Label(fen,text='Clé de cryptage : ',fg ='blue').grid(row =2,sticky =W)
    Label(fen, text='DECRYPTAGE', fg='black').grid(row =6, sticky =W)
    Label(fen, text='Texte à décrypter :', fg='blue').grid(row =7,sticky =W)
    Label(fen, text='Clé à décrypter :', fg='blue').grid(row =8,sticky =W)
    
    crypter = StringVar()
    crypt1 = Entry(fen,textvariable = crypter)
    crypt1.grid(row =3,column =1)
    crypter.set("Texte crypté")
    
    decrypter = StringVar()
    Decrypt1 = Entry(fen, textvariable = decrypter)
    Decrypt1.grid(row =9, column =1)
    decrypter.set("Texte crypté")

    
    entree = Entry(fen, fg='brown')
    entree.grid(row =1,column =1)
    
    entree1 = Entry(fen,  fg ='brown')
    entree1.grid(row =2,column =1)
    
    entree2= Entry(fen, fg ='brown')
    entree2.grid(row =7,column =1)
    
    entree3=Entry(fen, fg ='brown')
    entree3.grid(row =8, column =1)
    
    bou1 = Button(fen,text ='Crypter',fg ='blue',command =crypt)
    bou1.grid(row = 3)
    
    boutonDecry = Button(fen, text ='Décrypter', fg='blue', command =décrypt)
    boutonDecry.grid(row =9)
    
    
    bou3 = Button(fen,text ='Quitter',fg ='red',command =fen.destroy)
    bou3.place(x=123, y=180)
    
    fen.mainloop()

#--------------fonction qui crypte ( Méthode Vigenere )--------------

def vigenere():
    msg= entree4.get()
    key = entree5.get()
    key_index = 0
    vigenere = ""

    for cara in msg:
       
        carainscrit = ord(cara)
        carainscrit += ord(key[key_index]) - ord('a')
        if carainscrit > ord('z'):
            carainscrit -= ord('z') - ord('a')
       
        vigenere += str(chr(carainscrit))
       
        
        key_index += 1
        if key_index >= len(key):
            key_index = 0
    print(crypt1.insert(0,vigenere))
    print(vigenere)


#--------------fonction qui decrypte ( Méthode Vigenere )--------------

def vigeneredecrypt():
    msg2= entree6.get()
    key2 = entree7.get()
    key_index = 0
    vigeneredecrypt = ""

    for cara in msg2:
       
        carainscrit = ord(cara)
        carainscrit +=  ord('a')-ord(key2[key_index]) 
        if carainscrit > ord('z'):
            carainscrit -= ord('z') - ord('a')
       
        vigeneredecrypt += str(chr(carainscrit))
       
        
        key_index += 1
        if key_index >= len(key2):
            key_index = 0
    print(spcrypt1.insert(0,vigeneredecrypt))
    print(vigeneredecrypt)


#--------------fonction pour interface ( Méthode Vigenere )--------------

def vigenere2():
    global entree4,entree5,crypt1,entree6,entree7,spcrypt1
    sese=Tk()
    sese.title("•Méthode Vigenère•")
    sese.resizable(False, False)
    sese.focus_set()
    sese.geometry("265x210+850+400")
    
    Label(sese,text='CRYPTAGE',fg ='black').grid(row =0,column=1)
    Label(sese,text='Texte à Crypter : ',fg ='blue').grid(row =1,sticky =W)
    Label(sese,text='Clé de cryptage : ',fg ='blue').grid(row =2,sticky =W)
    Label(sese, text='DECRYPTAGE', fg='black').grid(row =6, sticky =W)
    Label(sese, text='Texte à décrypter :', fg='blue').grid(row =7,sticky =W)
    Label(sese, text='Clé à décrypter :', fg='blue').grid(row =8,sticky =W)
    
    crypter = StringVar()
    crypt1 = Entry(sese,textvariable = crypter)
    crypt1.grid(row =3,column =1)
    
    decrypter1 = StringVar()
    spcrypt1 = Entry(sese, textvariable = decrypter1)
    spcrypt1.grid(row =9, column =1)
    decrypter1.set("Texte crypté")
    
    entree4 = Entry(sese, fg='brown')
    entree4.grid(row =1,column =1)
        
    entree5 = Entry(sese,  fg ='brown')
    entree5.grid(row =2,column =1)
    
    entree6= Entry(sese, fg ='brown')
    entree6.grid(row =7,column =1)
    
    entree7=Entry(sese, fg ='brown')
    entree7.grid(row =8, column =1)
    
    boutonDecry2 = Button(sese, text ='Décrypter', fg='blue', command =vigeneredecrypt)
    boutonDecry2.grid(row =9)
    
    bou1 = Button(sese,text ='Crypter',fg ='blue',command =vigenere)
    bou1.grid(row = 3)
    
    bou3 = Button(sese,text ='Quitter',fg ='red',command =sese.destroy)
    bou3.place(x=123, y=180)
    
    sese.mainloop()
   
Mafenetre.mainloop()  

#----------------------------  FIN DU PROGRAMME ----------------------------#