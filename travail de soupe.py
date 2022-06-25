def indice_max(liste):
    testeur=0
    index=0
    for i in range(len(liste)):
        if liste[i]>testeur:
            testeur=liste[i]
            index=i
    return index

