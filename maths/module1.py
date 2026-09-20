# Créé par h.gibert, le 07/09/2026 en Python 3.7
def complement(b):

  a = [1 - x for x in b]


  c = 1
  result = list(a)
  for i in range(len(result) - 1, -1, -1):
    total = result[i] + c
    result[i] = total % 2
    c = total // 2

  return result



if __name__ == "__main__":
  user_input = input("Entrez un nombre binaire (ex: 0101) : ")


  b = [int(char) for char in user_input if char in "01"]

  if len(b) > 0:
    resultat = complement(b)
    print("Tableau d'origine :", b)
    print("Complément à 2    :", resultat)
  else:
    print("Erreur : Veuillez entrer uniquement des 0 et des 1.")