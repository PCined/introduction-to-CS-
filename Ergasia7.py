import random
P1=input('Καλωσήρθατε στην Τριλιζα!Επλεξτε συμβολο (X ή Ο): ')
while P1!="X" and P1!="O":
    P1=input("Επιλεξτε Χ ή Ο (προσοχή: Αγγλικά και κεφαλάια): ")
if P1=="X":
    C="O"
else:
    C="X"

replay=1
while replay==1:    
    draw=0
    square=[[" "," "," "],[" "," "," "],[" "," "," "]]
    print('Ο ακόλουθος πίνακας δειχνει τις ονομασιες των θεσεων, συμβουλευτειτε τον για να παιξετε')
    print('1 ] 2 [ 3')
    print('4 ] 5 [ 6')
    print('7 ] 8 [ 9')
    print("Ας ξεκινήσουμε")
    choice=int(input("Αν θελετε να παιξετε πρωτος πατηστε 1, αλλιως πατηστε 2: "))
    while choice!=1 and choice!=2 :
        choice=int(input("1 ή 2 ... Παμε το χεις .. δεν ειναι δυσκολο: "))
    if choice==2:
        i=random.randrange(0,3)
        j=random.randrange(0,3)
        square[i][j]=C
        draw=draw+1
        #emfanish ths partidas meta apo epilogh
        print(square[0][0],' ] ',square[0][1],' [ ',square[0][2])
        print(square[1][0],' ] ',square[1][1],' [ ',square[1][2])
        print(square[2][0],' ] ',square[2][1],' [ ',square[2][2])
   

    
    won=0
    choice=int(input("Είναι σειρά σας. Διαλέξτε εναν αριθμο απο αυτους που εμφανίζονται πανω για να παιξετε στην αντίστοιχη θέση "))
  
    while won==0 and draw<9:
        Played=0
        while Played==0:
            if choice==1:     
                if square[0][0]==" ":
                    square[0][0]=P1
                    Played=1
                else:
                    choice=int(input("Επιλεξτε μια άδεια θέση"))
            if choice==2:
                if square[0][1]==" ":    
                    square[0][1]=P1
                    Played=1
                else:
                    choice=int(input("Επιλεξτε μια άδεια θέση"))
            if choice==3:
                if square[0][2]==" ":
                    square[0][2]=P1
                    Played=1
                else:
                    choice=int(input("Επιλεξτε μια άδεια θέση"))
            if choice==4:
                if square[1][0]==" ":
                    square[1][0]=P1
                    Played=1
                else:
                    choice=int(input("Επιλεξτε μια άδεια θέση"))
            if choice==5:
                if square[1][1]==" ":
                    square[1][1]=P1
                    Played=1
                else:
                    choice=int(input("Επιλεξτε μια άδεια θέση"))
            if choice==6:
                if square[1][2]==" ":
                    square[1][2]=P1
                    Played=1
                else:
                    choice=int(input("Επιλεξτε μια άδεια θέση"))
            if choice==7:
                if square[2][0]==" ":
                    square[2][0]=P1
                    Played=1
                else:
                    choice=int(input("Επιλεξτε μια άδεια θέση"))
            if choice==8:
                if square[2][1]==" ":
                    square[2][1]=P1
                    Played=1
                else:
                    choice=int(input("Επιλεξτε μια άδεια θέση"))
            if choice==9:
                if square[2][2]==" ":
                    square[2][2]=P1
                    Played=1
                else:
                    choice=int(input("Επιλεξτε μια άδεια θέση"))
        draw=draw+1
        print(" ")
        print(square[0][0],' ] ',square[0][1],' [ ',square[0][2])
        print(square[1][0],' ] ',square[1][1],' [ ',square[1][2])
        print(square[2][0],' ] ',square[2][1],' [ ',square[2][2])
        print(" ")
        #Elegxos gia nikhth se peiptwsh orizontias trilizas
        if square[0][0]==square[0][1] and square[0][1]==square[0][2] and square[0][0]!=" ":
            won=1
        if square[1][0]==square[1][1] and square[1][1]==square[1][2] and square[1][2]!=" ":
            won=1
        if square[2][0]==square[2][1] and square[2][1]==square[2][2] and square[2][2]!=" ":
            won=1
        #Elegxos gia nikhth se periptwsh katheths trilizas
        if square[0][0]==square[1][0] and square[1][0]==square[2][0] and square[2][0]!=" ":
            won=1
        if square[0][1]==square[1][1] and square[1][1]==square[2][1] and square[2][1]!=" ":
            won=1
        if square[0][2]==square[1][2] and square[1][2]==square[2][2] and square[2][2]!=" ":
            won=1
        #Elegxos gia nikhth me diagwnia triliza
        if square[0][0]==square[1][1] and square[1][1]==square[2][2] and square[2][2]!=" ":
            won=1
        if square[0][2]==square[1][1] and square[1][1]==square[2][0] and square[2][0]!=" ":
            won=1
        if won==0:
            #kinhsh tou upologisth
            i=random.randrange(0,3)
            j=random.randrange(0,3)
            Played=0
            while Played==0:    
                if square[i][j]==" ":
                    square[i][j]=C
                    Played=1
                else:
                    i=random.randrange(0,3)
                    j=random.randrange(0,3)
            draw=draw+1
            print(" ")
            print(square[0][0],' ] ',square[0][1],' [ ',square[0][2])
            print(square[1][0],' ] ',square[1][1],' [ ',square[1][2])
            print(square[2][0],' ] ',square[2][1],' [ ',square[2][2])
            print(" ")
            #Elegxos gia nikhth se peiptwsh orizontias trilizas
            if square[0][0]==square[0][1] and square[0][1]==square[0][2] and square[0][0]!=" ":
                won=2
            if square[1][0]==square[1][1] and square[1][1]==square[1][2] and square[1][2]!=" ":
                won=2
            if square[2][0]==square[2][1] and square[2][1]==square[2][2] and square[2][2]!=" ":
                won=2
            #Elegxos gia nikhth se periptwsh katheths trilizas
            if square[0][0]==square[1][0] and square[1][0]==square[2][0] and square[2][0]!=" ":
                won=2
            if square[0][1]==square[1][1] and square[1][1]==square[2][1] and square[2][1]!=" ":
                won=2
            if square[0][2]==square[1][2] and square[1][2]==square[2][2] and square[2][2]!=" ":
                won=2
            #Elegxos gia nikhth me diagwnia triliza
            if square[0][0]==square[1][1] and square[1][1]==square[2][2] and square[2][2]!=" ":
                won=2
            if square[0][2]==square[1][1] and square[1][1]==square[2][0] and square[2][0]!=" ":
                won=2
            if won==0:
                choice=int(input("Σειρά σας: "))

    if won==1:
        print("Συγχαρητήρια! Κερδίσατε")
    elif won==2:
        print("Δυστυχώς χάσατε :(")
    else:
        print:("Ισοπαλία")
    replay=int(input("Αν θελετε να ξαναπαιξετε επιλεξτε 1"))
    



        
            
        

