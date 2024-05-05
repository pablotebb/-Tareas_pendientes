import os

def limpiar_consola():
    if os.name == 'posix': # Para sistemas basados en Unix/Linux/Mac
        _ = os.system('clear')
    elif os.name == 'nt': # Para sistemas Windows
        _ = os.system('cls')
        
def solo_letras(cadena):
    palabras = cadena.split()  # Dividir la cadena en palabras
    for palabra in palabras:
        if not palabra.isalpha():
            raise ValueError("La cadena solo debe contener letras")
    return True

class Tarea:
  def __init__(self, nombre="-------"):
    self.nombre = nombre
    self.marca = False
  
  def set_marca(self, opcion_marca):
    self.marca = opcion_marca
    
  def get_marca(self):
    return self.marca

class Tareas_pendientes:
  def __init__(self):
    self.tareas = []
    
  def agregar(self, descripcion):
    self.tarea = Tarea(descripcion) 
    self.tareas.append(self.tarea)
  
  
  def marcar(self, opcion_marcado):
    
    # self.tarea.set_marca(opcion_marcado)
    if not self.tareas:
      print("No hay tareas pendientes!")
    else:
      try:
        if self.tareas[opcion_marcado].get_marca():
          self.tareas[opcion_marcado].set_marca(False)
        else:
          self.tareas[opcion_marcado].set_marca(True)
      except IndexError:     
        print("")
        print("Error: Indice no encontrado")   
  
  def mostrar(self):
    # self.tarea = Tarea()
    if not self.tareas:
      print("")
      print("--------------------------")
      print("")
      print("No hay tareas pendientes!")
      print("")
      print("--------------------------")
    else:
      for i, tarea in enumerate(self.tareas, start=1):
        if tarea.get_marca() == False:
          print("")
          print(f"{i}) [ ] {tarea.nombre}")
          print("")
        else: 
          print("")
          print(f"{i}) [X] {tarea.nombre}")
          print("")
         
           
  
  def eliminar(self, opcion):
    try: 
      self.tareas.pop(opcion-1)
      
    except IndexError:
      print("")
      print("Error: Indice no encontrado")
    except ValueError:
      print("")
      print("Error: No introduzca letras")

def main():
  tareas = Tareas_pendientes()
  
  while True:
    limpiar_consola()  
    # MENU
    print("""
    -------------------------------------
      T A R E A S  P E N D I E N T E S:
           
         1) Agregar tarea 
         
         2) Marcar o desmarcar tarea 
         
         3) Mostrar todas tareas
         
         4) Eliminar tarea 
         
         5) Salir
         
    -------------------------------------
          """)
    opcion = input("Entra una opción: ")
    
    if opcion == "1":     # AGREGAR 
      print("")
      try:
        tarea = input("Por favor, introduce una tarea: ")
        solo_letras(tarea)
        tareas.agregar(tarea)
      except ValueError as error:
        print("")
        print("Error: ", error)
        
    elif opcion == "2":   # MARCAR
      try:
        print("")
        opcion_marca = int(input("Por favor, introduce la opcion a marcar o desmarcar: (ej: 2) "))
        tareas.marcar(opcion_marca - 1)
      except ValueError:
        print("")
        print("No debes introducir letras")
    elif opcion == "3":   # MOSTRAR TODAS
      tareas.mostrar()
    elif opcion == "4":   # ELIMINAR
      print("")
      try:
        opcion_numero = int(input("Por favor, introduce la opcion a eliminar: (ej: 2) "))
        tareas.eliminar(opcion_numero)
      except ValueError:
        print("")
        print("Error: No introduzca letras")

    elif opcion == "5":   # SALIR
      print("")
      break 
    else:
      print("")
      print("Opcion no correcta")
    
    print("")
    input("Presione Enter para continuar...")
      
      


if __name__ == "__main__":
  main()



