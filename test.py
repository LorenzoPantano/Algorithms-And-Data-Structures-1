import B
from ListaConcatenataDictionary import LinkedListDictionary
import ListAVL

"""
Cartella di progetto identica alla precedente, il main e' modificato per eseguire inserimenti e cancellazioni
successive per calcolarne i tempi di esecuzione e paragonarli ad dictionary di Python (Dictionary Test)
"""

if __name__=='__main__':
    # Variabili globali

    r = 6
    min = -1000
    max = 1000
    b = 100
    d = ((max - min) // b)

    B = B.B(r, b, min, max)
    v = []   # Array v
    vc = []   # contatore per v
    for i in range(0,d+2):
        liste = LinkedListDictionary()
        v.append(liste)
        vc.append(0)


def insert(key, value):   # INSERT PRIMO METODO
    """Insert operation del dictionary"""
    global r
    global v
    global vc
    global B
    global d
    for k in range(0, d):
        if key in B[k]:
            exist = v[k].search(key)
            if exist != None:
                v[k].delete(key)
                vc[k] -= 1
            v[k].insert(key, value)
            vc[k] += 1
            if vc[k] >= 6:
                if vc[k] -1 == 5:
                    v[k] = ListAVL.listaToAVL(v[k])
    if key > B[d + 1][0]:
        exist = v[d + 1].search(key)
        if exist != None:
            v[d + 1].delete(key)
            vc[d +1] -= 1
        v[d + 1].insert(key, value)
        vc[d +1] += 1
        if vc[d +1] >= 6:
            if vc[d + 1] - 1 == 5:
                v[d + 1] = ListAVL.listaToAVL(v[d + 1])
    if key < B[0][0]:
        exist = v[d].search(key)
        if exist != None:
            v[d].delete(key)
            vc[d] -= 1
        v[d].insert(key, value)
        vc[d] += 1
        if vc[d] >= 6:
            if vc[d] - 1 == 5:
                v[d] = ListAVL.listaToAVL(v[d])


def delete(key):   # DELETE PRIMO METODO
    global r
    global v
    global vc
    global B
    global d
    """DELETE operation"""
    for k in range(0, d):
        if key in B[k]:
            v[k].delete(key)
            vc[k] -= 1
            if vc[k] < 6:
                if vc[k] + 1 == 6:
                    v[k] = ListAVL.avlToLista(v[k])
    if key > B[d + 1][0]:
        v[d + 1].delete(key)
        vc[d + 1] -= 1
        if vc[d + 1] < 6:
            if vc[d + 1] + 1 == 6:
                v[d + 1] = ListAVL.avlToLista(v[d + 1])
    if key < B[0][0]:
        v[d].delete(key)
        vc[k] -= 1
        if vc[d] < 6:
            if vc[d] + 1 == 6:
                v[d] = ListAVL.avlToLista(v[d])


def search(key):    # SEARCH PRIMO METODO
    global r
    global v
    global vc
    global B
    global d
    """Search operation del dictionary"""
    t = None
    for k in range(0, d):
        if key in B[k]:
            t = v[k].search(key)
    if key > B[d + 1][0]:
        t = v[d + 1].search(key)
    if key < B[0][0]:
        t = v[d].search(key)
    if t != None:
        print(f"Alla chiave {key} corrisponde il valore {t}")
    else:
        print("Nessun valore corrispondente")


def insertBinary(key,value):  # INSERT CON RICERCA BINARIA
    for k in range(0,d):
        t = binarySearch(B[k], key)
        if t is True:
            exist = v[k].search(key)
            if exist is not None:
                v[k].delete(key)
                vc[k] -= 1
            v[k].insert(key, value)
            vc[k] += 1
            if vc[k] >= 6:
                if vc[k] - 1 == 5:
                    v[k] = ListAVL.listaToAVL(v[k])
        else:
            continue
    if key > B[d + 1][0]:
        exist = v[d + 1].search(key)
        if exist != None:
            v[d + 1].delete(key)
            vc[d +1] -= 1
        v[d + 1].insert(key, value)
        vc[d +1] += 1
        if vc[d +1] >= 6:
            if vc[d + 1] - 1 == 5:
                v[d + 1] = ListAVL.listaToAVL(v[d + 1])
    if key < B[0][0]:
        exist = v[d].search(key)
        if exist != None:
            v[d].delete(key)
            vc[d] -= 1
        v[d].insert(key, value)
        vc[d] += 1
        if vc[d] >= 6:
            if vc[d] - 1 == 5:
                v[d] = ListAVL.listaToAVL(v[d])

def searchBinary(key):
    for k in range(0,d):
        t = binarySearch(B[k], key)
        if t is True:
            exist = v[k].search(key)
            if exist is not None:
                print(f"Trovata, valore {exist}")
        else:
            continue
    if key > B[d + 1][0]:
        exist = v[d + 1].search(key)
        if exist != None:
            print(f"Trovata, valore {exist}")
    if key < B[0][0]:
        exist = v[d].search(key)
        if exist != None:
            print(f"Trovata, valore {exist}")

def deleteBinary(key):
    for k in range(0, d):
        t = binarySearch(B[k], key)
        if t is True:
            v[k].delete(key)
            vc[k] -= 1
            if vc[k] >= 6:
                if vc[k] - 1 == 5:
                    v[k] = ListAVL.avlToLista(v[k])
        else:
            continue
    if key > B[d + 1][0]:
        v[d + 1].delete(key)
        vc[d + 1] -= 1
        if vc[d + 1] < 6:
            if vc[d + 1] + 1 == 6:
                v[d + 1] = ListAVL.avlToLista(v[d + 1])
    if key < B[0][0]:
        v[d].delete(key)
        vc[d] -= 1
        if vc[d] < 6:
            if vc[d] + 1 == 6:
                v[d] = ListAVL.avlToLista(v[d])


def insert2(key, value): # INSERT ULTIMO METODO
    for k in range(0,d):
        first_elem = B[k][0]
        size = len(B[k])
        last_elem = B[k][size-1]
        if (key >= first_elem) and (key <= last_elem):
                exist = v[k].search(key)
                if exist is not None:
                    v[k].delete(key)
                    vc[k] -= 1
                v[k].insert(key, value)
                vc[k] += 1
                if vc[k] >= 6:
                    if vc[k] - 1 == 5:
                        v[k] = ListAVL.listaToAVL(v[k])
        else:
            continue
    if key > B[d + 1][0]:
        exist = v[d + 1].search(key)
        if exist != None:
            v[d + 1].delete(key)
            vc[d +1] -= 1
        v[d + 1].insert(key, value)
        vc[d +1] += 1
        if vc[d +1] >= 6:
            if vc[d + 1] - 1 == 5:
                v[d + 1] = ListAVL.listaToAVL(v[d + 1])
    if key < B[0][0]:
        exist = v[d].search(key)
        if exist != None:
            v[d].delete(key)
            vc[d] -= 1
        v[d].insert(key, value)
        vc[d] += 1
        if vc[d] >= 6:
            if vc[d] - 1 == 5:
                v[d] = ListAVL.listaToAVL(v[d])


def delete2(key):   # DELETE ULTIMO METODO
    global r
    global v
    global vc
    global B
    global d
    for k in range(0,d):
        first_elem = B[k][0]
        size = len(B[k])
        last_elem = B[k][size-1]
        if (key >= first_elem) and (key <= last_elem):
                v[k].delete(key)
                vc[k] -= 1
                if vc[k] >= 6:
                    if vc[k] - 1 == 5:
                        v[k] = ListAVL.avlToLista(v[k])
        else:
            continue
    if key > B[d + 1][0]:
        v[d + 1].delete(key)
        vc[d + 1] -= 1
        if vc[d + 1] < 6:
            if vc[d + 1] + 1 == 6:
                v[d + 1] = ListAVL.avlToLista(v[d + 1])
    if key < B[0][0]:
        v[d].delete(key)
        vc[d] -= 1
        if vc[d] < 6:
            if vc[d] + 1 == 6:
                v[d] = ListAVL.avlToLista(v[d])


def search2(key):   # SEARCH ULTIMO METODO
    global r
    global v
    global vc
    global B
    global d
    """Search operation del dictionary
    SearchBinary e' implementata usando il metodo di ricerca binaria nell'insieme B(i)
    dove B(i) viene scelto come per la funzione insertBinary2"""
    t = None
    for k in range(0, d):
        first_elem = B[k][0]
        size = len(B[k])
        last_elem = B[k][size-1]
        if (key >= first_elem) and (key <= last_elem):
                t = v[k].search(key)
        else:
            continue
    if key > B[d + 1][0]:
        t = v[d + 1].search(key)
    if key < B[0][0]:
        t = v[d].search(key)
    if t is not None:
        print(f"Alla chiave {key} corrisponde il valore {t}")
    else:
        print("Nessun valore corrispondente")


def binarySearch(array, x):
    """Binary Search"""
    mid = (len(array)) // 2
    if len(array) == 1:
        if x == mid:
            return True
        return False
    else:
        if x == mid:
            return True
        else:
            if x < mid:
                return binarySearch(array[0:mid],x)
            else:
                return binarySearch(array[mid +1: len(array)],x)

def test1():
    for i in range(0, 5000):
        insert(i,f"prova{i}")
    for i in range(0, 5000):
        search(i)
    for i in range(0, 5000):
        delete(i)

def test2():
    for i in range(0, 5000):
        insertBinary(i,f"prova{i}")
    for i in range(0,5000):
        searchBinary(i)
    for i in range(0,5000):
        deleteBinary(i)

def test3():
    for i in range(0, 1500):
        insert2(i,f"prova{i}")
    for i in range(0, 1500):
        search2(i)
    for i in range(0, 1500):
        delete2(i)


test1()