import ex1
import ex2
import ex3
import ex4

print("1. Exercici 1"
      "\n2.Exercici 2"
      "\n3. Exercici 3"
      "\n4.Exercici 4")

ex = int(input("Escriu la tasca que vols executar (1,2,3,4): "))

if ex == 1:
    ex1.cut()
elif ex == 2:
    ex2.histogram()
elif ex == 3:
    ex3.resize()
elif ex == 4:
    ex4.mono_stereo()
