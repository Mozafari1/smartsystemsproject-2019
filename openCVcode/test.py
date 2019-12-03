import cv2

# lager en variable med 2 
# imread leser bildet
# 1 - laster en farge bildet
# 0  - laster bildet i gråskall 
# -1 laster bildet som inkluderer alpha channel ( unchanged) 
img = cv2.imread('1.png',-1) # Denne funksjonen gir ikke noe feil selv om  man gir feil navn
# Variablen tar inn to verdi 1- bildet navn. 2 flags som er 1, 0 -1
print(img) # skriver ut matrisen til bildet
cv2.imshow("Lena", img) # viser bildet i ny vendu 
wk = cv2.waitKey(0) # venter 5ms
# Når brukeren presser ESC buttom avlsuttes all vinduene

if wk == 27: 
    cv2.destroyAllWindows()

# Dersom man presser S buttom da lager man en kopi av bildet så avsluttes vinduene
elif wk == ord('s'):

    cv2.imwrite("Lena_copy.png",img) # kopierer bildet
    cv2.destroyAllWindows() # Avlsutter alle vinduene


