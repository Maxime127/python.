Le nombre à deviner 
secret = 7

Variable pur stocker la réponse de l'utilisateur
devine = 0

Tant que l'utilisateur n'a pas deviné le bon nombre 
while devine != secret:
      Demander un nombre à l'utilisateur
	  devine = int(input("Devine un nombre entre 1 et 10 : "à))
	  
	  
	  vérifie si c'est le bon nombre 
	  if devine < secret:
	     print("trop petit !")
      elif devine > secret:
         print("trop grand !")
	  else:
	     print("Bravo ! tu as trouvé le nombre.")
		 
		 