
def B(r, b, min, max):
    """Inizializzazione dei sottoinsiemi B(i), a partire dai parametri inserite nel main (b,min,max, r = 6)
     :param r,b,min,max interi
     :return B lista"""
    if b <= r:
         print(f"Errore, b non puo' essere minore di r ({r})")   # Condizione per cui b deve essere > r
         return
    if (((max - min) % b)!=0):      # Condizione per cui max - min deve essere multiplo di b
         print("Errore, (max - min) deve essere multiplo di b")
         return
    d = ((max - min) // b)
    if d < 0:
        d = -d
    B = []
    i = 0
    while i < d:                                 # Stampa tutti i sottoinsimi B(i)
       B.append([])
       for n in range(min,max+1):
            if (n >= min + i*b) and (n < min + (i+1)*b):
                B[i].append(n)
       print(f"B[{i}]: {B[i]}")
       i = i+1
    B.append([])       # B[d] contiene tutti gli elementi n < min (min escluso)
    B.append([])       # B[d+1] contiene tutti gli elemeni n >= max
    B[d+1].append(max)
    print(f"B[{d}]: (-inf,{min})")   # Stampo anche B(d) e B(d+1)
    print(f"B[{d+1}]: [{max},+inf)")
    return B
