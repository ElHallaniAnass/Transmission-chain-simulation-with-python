from random import randint

class Gestion_data:
    def __init__(self):
        pass

   # convert int_list to str_list
    # def convert(list):    
    #     s = [str(i) for i in list]       
    #     res = str("".join(s))    
    #     return(res)
        

    def ecrir(file, text):              #pour cree ou supprimer et ajouter text
        with open(file, "w") as file:
            file.write(text)
            file.close()

    def ajouter(file, text):            #pour ajouter au fichier
        with open(file, "a") as file:
            file.seek(text)
            file.close()

    def lire(file):                     #lire le fichier
        with open(file, "r") as file:
            return file.read()

    def create_vecteur(text):           #cree vecteur pour simplifier le traitement
        return [int(text[i]) for i in range(len(text))]

    def rand_data(lengh):               #cree vecteur avec des 0,1
        return [randint(0,1) for _ in range(lengh)]

    def rand_data_file(file, lengh):    #cree fichier avec random data
        a = Gestion_data.rand_data(lengh)
        r = ""
        for i in range(len(a)):
            r = r + str(a[i])
        Gestion_data.ecrir(file, r)





































