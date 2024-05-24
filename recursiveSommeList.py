
def recursiveSommeList(tab):
    if(len(tab) == 0):
        return 0
    else : return tab[0] + recursiveSommeList(tab[1:])

tabs = [1, 2, 7, 8, 9,58,69,254]
print(recursiveSommeList(tabs))