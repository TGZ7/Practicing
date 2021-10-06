def drawcircle(n,r):     # Given a n size for the canvas and a r radius for the circle, draw a black circle in a white canvas
  n=50
  r=20
  matriz=np.ones([n,n])
  '''     Ecuación cicunferencia
          (x-a)**2 + (y-b)**2 = r**2

          En nuestro caso a=b=matriz.shape[0]/2
  '''
  a=n//2
  b=a
  print(a)
  print(b)

  for y in range(n):
      for x in range(n):
          cir=(x-a)**2+(y-b)**2
          if cir-r<=r**2<=cir+r:
              matriz[x][y]=0

  print(matriz)

  import matplotlib.pyplot as plt
  plt.figure(figsize=(5,5)) 
  plt.imshow(matriz, cmap="gray")
  plt.show()
