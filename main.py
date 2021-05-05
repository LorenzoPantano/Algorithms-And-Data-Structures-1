import B
from ListaConcatenataDictionary import LinkedListDictionary
import ListAVL

"""Main del progetto, B.py contiene l'inizializzazione dei sottoinsiemi B(i) che formano una partizione di Z"""

if __name__=='__main__':
    # Variabili globali

    r = 6  # Per 0<i<d-1 B(i) contiene gli elementi n di Z tali che n>=min + i*b o
    min = int(input("Inserisci min: "))  # n<min +(i+1)*b; Per i = d contiene tutti gli elementi minori del min
    max = int(input("Inserisci max: "))  # Per i = d+1 contiene tutti gli elementi maggiori del massimo
    b = int(input("Inserisci b: "))
    d = ((max - min) // b)

    B = B.B(r, b, min, max)
    v = []   # Array v
    vc = []   # contatore per v
    for i in range(0, d+2):
        liste = LinkedListDictionary()
        v.append(liste)
        vc.append(0)
    run = 1
    while run:
        print("Qaule operazione vuoi eseguire? \n1. Inserisci (key,value)\n2. Delete (key)\n3. Search (key)")
        print("4.Stampa e info su una cella del vettore")
        print("Per un valore diverso da 1,2,3,4 termina il programma...\n")
        choice = int(input())
        if choice == 1:
            # INSERT
            key = int(input("Key: "))  # Per l'inserimento, si valuta a quale sottoinsieme B(i)
            value = input("Value: ")  # di Z appartiene key, e si inserisce nella posizione i dell'array
            for k in range(0, d):
                first_elem = B[k][0]
                last_elem = B[k][len(B[k])-1]
                if (key >= first_elem) and (key <= last_elem):
                    exist = v[k].search(key)
                    if exist != None:
                        v[k].cambiaValore(key, value)
                        break
                    v[k].insert(key, value)
                    vc[k] += 1
                    if vc[k] >= 6:
                        if vc[k] - 1 == 5:
                            v[k] = ListAVL.listaToAVL(v[k])
                else:
                    continue
            if key >= B[d + 1][0]:
                exist = v[d + 1].search(key)
                if exist != None:
                    v[d + 1].cambiaValore(key, value)
                else:
                    v[d + 1].insert(key, value)
                    vc[d +1] += 1
                    if vc[d +1] >= 6:
                        if vc[d + 1] - 1 == 5:
                            v[d + 1] = ListAVL.listaToAVL(v[d + 1])
            if key < B[0][0]:
                exist = v[d].search(key)
                if exist != None:
                    v[d].cambiaValore(key, value)
                else:
                    v[d].insert(key, value)
                    vc[d] += 1
                    if vc[d] >= 6:
                        if vc[d] - 1 == 5:
                            v[d] = ListAVL.listaToAVL(v[d])

        elif choice == 2:
            # DELETE
            key = int(input("Key: "))
            for k in range(0, d):
                first_elem = B[k][0]
                last_elem = B[k][len(B[k]) - 1]
                if (key >= first_elem) and (key <= last_elem):
                    exist = v[k].search(key)
                    if exist is None:
                        print("Elemento non trovato")
                        break
                    v[k].delete(key)
                    vc[k] -= 1
                    if vc[k] < 6:
                        if vc[k] + 1 == 6:
                            v[k] = ListAVL.avlToLista(v[k])
                else:
                    continue
            if key >= B[d + 1][0]:
                exist = v[d + 1].search(key)
                if exist is None:
                    print("Elemento non trovato")
                else:
                    v[d + 1].delete(key)
                    vc[d + 1] -= 1
                    if vc[d + 1] < 6:
                        if vc[d + 1] + 1 == 6:
                            v[d + 1] = ListAVL.avlToLista(v[d + 1])
            if key < B[0][0]:
                exist = v[d].search(key)
                if exist is None:
                    print("Elemento non trovato")
                else:
                    v[d].delete(key)
                    vc[d] -= 1
                    if vc[d] < 6:
                        if vc[d] + 1 == 6:
                            v[d] = ListAVL.avlToLista(v[d])

        elif choice == 3:
            # SEARCH
            key = int(input("Key: "))
            t = None
            for k in range(0, d):
                first_elem = B[k][0]
                last_elem = B[k][len(B[k]) - 1]
                if (key >= first_elem) and (key <= last_elem):
                    t = v[k].search(key)
                    if t is not None:
                        struttura = k
                else:
                    continue
            if key >= B[d + 1][0]:
                t = v[d + 1].search(key)
                if t is not None:
                    struttura = d + 1
            if key < B[0][0]:
                t = v[d].search(key)
                if t is not None:
                    struttura = d
            if t is not None:
                print(f"Alla chiave {key} corrisponde il valore {t} e si trova nella struttura puntata da v[{struttura}]")
            else:
                print("Nessun valore corrispondente")

        elif choice == 4:
            # INFO
            cell = int(input("Di quale cella vuoi visualizzare il contenuto?"))
            for k in range(0, d + 2):
                if cell == k:
                    n = vc[k]
                    if n >= 6:
                        tipo = "Albero AVL"
                    else:
                        tipo = "Lista Collegata"
                    print(f"V[{k}] ha {n} elementi -> {tipo}")
                    v[k].print()
        else:
            # END
            print("Termino il programma...")
            run = 0