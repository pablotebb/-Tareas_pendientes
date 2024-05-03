class Tareas_pendientes:
  def __init__(self, tareas_pendientes):
    self.tareas_pendientes = tareas_pendientes
  
  def agregar_tarea(self, *tarea):
    for self.tarea in tarea:
      try:
        
        # Controlo que la lista sólo reciba cadenas
        if not isinstance(self.tarea, str):
          raise TypeError("Error!, solo se permiten cadenas")
        
        self.tareas_pendientes.append(self.tarea)
        
      except TypeError as e:
        print(e)
  
  def marcar_tarea(self):
    pass
  
  def mostar_todas_tareas(self):
    print(f"{self.tareas_pendientes}")
  
  def eliminar_tarea(self):
    pass


tareas = ["Desayunar", "Fregar", "Hacer la comida"]

mis_tareas = Tareas_pendientes(tareas)
mis_tareas.mostar_todas_tareas()
mis_tareas.agregar_tarea("Ir a hacer la compra")
mis_tareas.mostar_todas_tareas()
mis_tareas.agregar_tarea("Ir a pasear", "comer", "estudiar")
mis_tareas.mostar_todas_tareas()

mis_tareas.agregar_tarea("comer", 1, "estudiar")
mis_tareas.mostar_todas_tareas()

