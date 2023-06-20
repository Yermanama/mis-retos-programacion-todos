""" 
     *
    ***
   *****
  *     *
 ***   ***
***** *****
"""

def imprimir_trifuerza(rows:int):
   for row in range(0,rows):
      asteriscos = "*" * ((2*(row+1) - 1))
      start_space = " " * (((2*(rows + 1) - 1)) - row)
      print(start_space + asteriscos)
   for row in range(0,rows):
      asteriscos = "*" * ((2*(row+1) - 1))
      start_space = " " *((rows - row) + 1)
      middle_space = " " * (2*(rows - row) -1)
      print(start_space + asteriscos + middle_space + asteriscos)
  
if __name__ == "__main__":
   imprimir_trifuerza(1)
   imprimir_trifuerza(2)
   imprimir_trifuerza(3)
   imprimir_trifuerza(5)
   imprimir_trifuerza(20)
