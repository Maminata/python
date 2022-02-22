class Voiture:
    def __init__(self,modele,marque,annee,nombre_sieges):
        self.modele=modele
        self.marque=marque
        self.annee=annee
        self.nombre_sieges=nombre_sieges

    def __str__(self):
        return f" modele:{self.modele}\n marque:{self.marque}\n annee:{self.annee} \n nombre_sieges:{self.nombre_sieges}sieges"
ma_voiture=Voiture("Toyota Yaris","Peugeot","2019","4")
print(ma_voiture)

