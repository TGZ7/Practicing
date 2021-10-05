def squares(n)
  # A function that prints concentric black and whites squares from a matrix made from a n variable, with a centered square
  import numpy
  import matplotlib.pyplot as plt
  
  matriz=np.ones([n,n])
  bi=0 
  signo=1
  for i in range(n//3):                       #creo un i que irá agrandandose
      for j in range(i,matriz.shape[0]-i):     # Voy recorriendo un fragmento cada vez
          for k in range(i,matriz.shape[1]-i): # más pequeño de la matriz original
              matriz[j][k]=bi                  # Sustituyendo sus valores por 1 y 0 alternando

      bi+=signo
      signo=signo*-1
  print(matriz)
  
  
  plt.figure(figsize=(5,5)) 
  plt.imshow(matriz, cmap="gray")
  plt.show()
