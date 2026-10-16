"""
Classe : Produit
Module : Produit.py
Description : Represente un produit vendu dans un rayon d'un magasin
"""
class Produit():
  """ Un produit est vendu a un prix donne et se trouve dans un seul rayon """
  def __init__(self, aNom, aReference, aPrix, aRayon=None):
    """Constructeur avec passage des valeurs pour les attributs"""
    self.nom = aNom
    self.reference = aReference
    self.prix = aPrix
    self.rayon = aRayon   # objet Rayon ou se trouve le produit

  def __str__(self):
    """ Methode pour l'affichage de la classe """
    chaine = "Produit" + "\n"
    chaine = chaine + "nom=" + str(self.nom) + "\n"
    chaine = chaine + "reference=" + str(self.reference) + "\n"
    chaine = chaine + "prix=" + str(self.prix) + " euros" + "\n"
    chaine = chaine + "rayon=" + str(self.rayon) + "\n"
    return chaine

  def getPrix(self):
    """ Renvoie le prix du produit """
    return self.prix

  def getRayon(self):
    """ Renvoie le rayon ou se trouve le produit """
    return self.rayon

  def setRayon(self, aRayon):
    """ Place le produit dans un rayon """
    self.rayon = aRayon

  def setPrix(self, aPrix):
    """ Modifie le prix du produit (le prix doit etre positif) """
    if aPrix < 0:
      print("Erreur : le prix ne peut pas etre negatif")
    else:
      self.prix = aPrix

if __name__ == '__main__':
  """ Permet d'executer le code localement """
  monProduit = Produit("Raquette de tennis", "RT-042", 89.90, "Tennis")
  print(monProduit)
  monProduit.setPrix(79.90)
  print("Nouveau prix : " + str(monProduit.getPrix()))
  print("Rayon : " + str(monProduit.getRayon()))
