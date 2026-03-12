from cafeteria import *

print(" REGISTRO MANUAL DE INVENTARIO Y USUARIOS")



print(">>> CARGANDO MENÚ DE BEBIDAS (10 OBJETOS)")
b1 = Bebida(101, "Cold Brew", 55.0, "Grande", "FRIA", ["Hielo extra"])
b2 = Bebida(102, "Americano Helado", 45.0, "Mediano", "FRIA", ["Sin azúcar"])
b3 = Bebida(103, "Espresso Doble", 40.0, "Chico", "CALIENTE", [])
b4 = Bebida(104, "Latte Deslactosado", 60.0, "Grande", "CALIENTE", ["Leche deslactosada"])
b5 = Bebida(105, "Té Verde Helado", 50.0, "Mediano", "FRIA", [])
b6 = Bebida(106, "Frappé Caramel", 75.0, "Grande", "FRIA", ["Crema batida", "Extra caramelo"])
b7 = Bebida(107, "Agua Mineral Preparada", 35.0, "Grande", "FRIA", ["Limón", "Sal"])
b8 = Bebida(108, "Mocha Blanco", 70.0, "Mediano", "CALIENTE", [])
b9 = Bebida(109, "Tisana Frutal", 55.0, "Grande", "FRIA", ["Doble carga"])
b10 = Bebida(110, "Café de Olla Helado", 50.0, "Mediano", "FRIA", ["Sin canela"])

print(b1.mostrar_detalle())
print(b2.mostrar_detalle())
print(b3.mostrar_detalle())
print(b4.mostrar_detalle())
print(b5.mostrar_detalle())
print(b6.mostrar_detalle())
print(b7.mostrar_detalle())
print(b8.mostrar_detalle())
print(b9.mostrar_detalle())
print(b10.mostrar_detalle())


print("\n>>> CARGANDO MENÚ DE POSTRES (10 OBJETOS)")
p1 = Postre(201, "Bagel Salado", 65.0, False, False)
p2 = Postre(202, "Galleta de Avena", 30.0, False, True)
p3 = Postre(203, "Croissant", 45.0, False, False)
p4 = Postre(204, "Brownie Vegano", 55.0, True, False)
p5 = Postre(205, "Muffin de Arándano", 40.0, False, False)
p6 = Postre(206, "Panqué de Elote", 50.0, False, True)
p7 = Postre(207, "Tarta de Manzana", 60.0, False, False)
p8 = Postre(208, "Rol de Canela", 55.0, False, False)
p9 = Postre(209, "Empanada de Espinaca", 45.0, True, False)
p10 = Postre(210, "Cheesecake Clásico", 70.0, False, False)

print(p1.mostrar_detalle())
print(p2.mostrar_detalle())
print(p3.mostrar_detalle())
print(p4.mostrar_detalle())
print(p5.mostrar_detalle())
print(p6.mostrar_detalle())
print(p7.mostrar_detalle())
print(p8.mostrar_detalle())
print(p9.mostrar_detalle())
print(p10.mostrar_detalle())


print("\n>>> DANDO DE ALTA CLIENTES (10 OBJETOS)")
c1 = Cliente(301, "Gerardo Gonzalez", "gerardo@email.com", 150)
c2 = Cliente(302, "Carlos Romero", "carlos@email.com", 50)
c3 = Cliente(303, "Ana Sanchez", "ana@email.com", 300)
c4 = Cliente(304, "Monkey D. Luffy", "luffy@pirates.com", 500)
c5 = Cliente(305, "Roronoa Zoro", "zoro@pirates.com", 20)
c6 = Cliente(306, "Michael Scott", "michael@dunder.com", 100)
c7 = Cliente(307, "Dwight Schrute", "dwight@dunder.com", 80)
c8 = Cliente(308, "Shohei Ohtani", "shohei@dodgers.com", 250)
c9 = Cliente(309, "Aaron Judge", "judge@yankees.com", 180)
c10 = Cliente(310, "Laura Gomez", "laura@email.com", 10)

print(c1.mostrar_detalle())
print(c2.mostrar_detalle())
print(c3.mostrar_detalle())
print(c4.mostrar_detalle())
print(c5.mostrar_detalle())
print(c6.mostrar_detalle())
print(c7.mostrar_detalle())
print(c8.mostrar_detalle())
print(c9.mostrar_detalle())
print(c10.mostrar_detalle())


print("\n>>> DANDO DE ALTA EMPLEADOS (10 OBJETOS)")
e1 = Empleado(401, "Pam Beesly", "pam@cafeteria.com", "EMP01", "GERENTE")
e2 = Empleado(402, "Jim Halpert", "jim@cafeteria.com", "EMP02", "BARISTA")
e3 = Empleado(403, "Kevin Malone", "kevin@cafeteria.com", "EMP03", "MESERO")
e4 = Empleado(404, "Oscar Martinez", "oscar@cafeteria.com", "EMP04", "BARISTA")
e5 = Empleado(405, "Angela Martin", "angela@cafeteria.com", "EMP05", "MESERO")
e6 = Empleado(406, "Sanji Vinsmoke", "sanji@cafeteria.com", "EMP06", "BARISTA")
e7 = Empleado(407, "Nami", "nami@cafeteria.com", "EMP07", "GERENTE")
e8 = Empleado(408, "Usopp", "usopp@cafeteria.com", "EMP08", "MESERO")
e9 = Empleado(409, "Stanley Hudson", "stanley@cafeteria.com", "EMP09", "BARISTA")
e10 = Empleado(410, "Kelly Kapoor", "kelly@cafeteria.com", "EMP10", "MESERO")

print(e1.mostrar_detalle())
print(e2.mostrar_detalle())
print(e3.mostrar_detalle())
print(e4.mostrar_detalle())
print(e5.mostrar_detalle())
print(e6.mostrar_detalle())
print(e7.mostrar_detalle())
print(e8.mostrar_detalle())
print(e9.mostrar_detalle())
print(e10.mostrar_detalle())

print("\n--- VALIDACIÓN DE DATOS FINALIZADA ---\n")


print(">>> INICIANDO PROCESO DE PEDIDO...")

inventario_hoy = Inventario({"Café": 1000, "Leche": 500, "Azúcar": 200, "Hielo": 300})


print(f"Empleado en caja: {e2.nombre} ({e2.rol})")
print(f"Cliente: {c1.nombre} (Puntos: {c1.puntosFidelidad})")


print("\n[SISTEMA]: Seleccionando productos...")
productos_pedido = [b1, b6, p3]
for prod in productos_pedido:
    print(f" - Agregado: {prod.nombre}")


nuevo_pedido = Pedido(995, productos_pedido, "PENDIENTE", 0.0)
print(nuevo_pedido.validarStock(inventario_hoy))


print("\n>>> APLICANDO GESTIÓN COMERCIAL...")
print(nuevo_pedido.calcularTotal())
print("¿Desea canjear puntos de fidelidad?: SI (Canjeando 50 puntos = $50 de descuento)")
c1.canjearPuntos(50)
total_con_descuento = nuevo_pedido.total - 50.0
print(f"[SISTEMA]: ¡ÉXITO! Descuento aplicado.")


print(f"\n[COCINA]: {e6.cambiarEstadoPedido('PREPARANDO')}")
print(f"[COCINA]: {e6.cambiarEstadoPedido('ENTREGADO')}")

print(f"\nResumen de Pedido #{nuevo_pedido.idPedido}:")
print(f"Cliente: {c1.nombre}")
print(f"Atendió: {e2.nombre}")
print(f"Artículos: {[p.nombre for p in nuevo_pedido.productos]}")
print(f"Total Final: ${total_con_descuento:.2f}")
print(f"Estado: PAGADO. Ticket generado en PDF.")