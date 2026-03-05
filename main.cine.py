from Reserva_cine import *


print(">>> CARGANDO CATALOGO DE PELICULAS")
p1 = Pelicula("One Piece Film: Red", 115, "A", "Anime/Aventura")
p2 = Pelicula("Moneyball", 133, "B", "Deportes/Drama")
p3 = Pelicula("Threat Level Midnight", 120, "B", "Acción/Comedia")
p4 = Pelicula("Dune: Part Two", 166, "B", "Ciencia Ficción")
p5 = Pelicula("El Juego Perfecto", 118, "A", "Deportes/Béisbol")
p6 = Pelicula("Spider-Man: Across the Spider-Verse", 140, "A", "Animación")
p7 = Pelicula("El Padrino", 175, "C", "Drama/Crimen")
p8 = Pelicula("Avengers: Endgame", 181, "B", "Acción/Superhéroes")
p9 = Pelicula("Interstellar", 169, "B", "Ciencia Ficción")
p10 = Pelicula("Super Mario Bros: La Película", 92, "A", "Animación/Aventura")


print(p1.obtener_sinopsis())
print(p2.obtener_sinopsis())
print(p3.obtener_sinopsis())
print(p4.obtener_sinopsis())
print(p5.obtener_sinopsis())
print(p6.obtener_sinopsis())
print(p7.obtener_sinopsis())
print(p8.obtener_sinopsis())
print(p9.obtener_sinopsis())
print(p10.obtener_sinopsis())


print("\n   Validando Clasificaciones    ")
print(f"One Piece: {p1.es_apta_para_todo_publico()}")
print(f"Dune: {p4.es_apta_para_todo_publico()}")



print("\n>>> REGISTRANDO USUARIOS")

u1 = Usuario(1, "Gerardo Gonzalez", "gerardo@email.com", "222-1234567", 150)
u2 = Usuario(2, "Carlos Romero", "carlos@email.com", "222-7654321", 50)
u3 = Usuario(3, "Ana Sanchez", "ana@email.com", "222-9876543", 300)
u4 = Usuario(4, "Laura Gomez", "laura.g@email.com", "222-1112233", 80)
u5 = Usuario(5, "Roberto Martinez", "roberto.m@email.com", "222-4445566", 210)
u6 = Usuario(6, "Sofia Hernandez", "sofia.h@email.com", "222-7778899", 15)
u7 = Usuario(7, "Miguel Angel Ruiz", "miguel.r@email.com", "222-0001122", 400)
u8 = Usuario(8, "Lucia Fernandez", "lucia.f@email.com", "222-3334455", 120)
u9 = Usuario(9, "Jorge Ramirez", "jorge.r@email.com", "222-6667788", 60)
u10 = Usuario(10, "Valeria Torres", "valeria.t@email.com", "222-9990011", 500)


print(f"Puntos de {u10.nombre}: {u10.puntos_fidelidad}")
print(u1.login())
print(u2.consultar_promociones())



print("\n>>> DANDO DE ALTA EMPLEADOS")

e1 = Empleado(11, "Michael Scott", "michael@cine.com", "555-0001", "EMP01", "ADMIN", "Mañana")
e2 = Empleado(12, "Dwight Schrute", "dwight@cine.com", "555-0002", "EMP02", "ADMIN", "Tarde")
e3 = Empleado(13, "Jim Halpert", "jim@cine.com", "555-0003", "EMP03", "TAQUILLERO", "Mañana")
e4 = Empleado(14, "Pam Beesly", "pam@cine.com", "555-0004", "EMP04", "TAQUILLERO", "Tarde")
e5 = Empleado(15, "Stanley Hudson", "stanley@cine.com", "555-0005", "EMP05", "TAQUILLERO", "Noche")
e6 = Empleado(16, "Kevin Malone", "kevin@cine.com", "555-0006", "EMP06", "ZONA COMIDA", "Tarde")
e7 = Empleado(17, "Angela Martin", "angela@cine.com", "555-0007", "EMP07", "ADMIN", "Noche")
e8 = Empleado(18, "Oscar Martinez", "oscar@cine.com", "555-0008", "EMP08", "LIMPIEZA", "Mañana")
e9 = Empleado(19, "Creed Bratton", "creed@cine.com", "555-0009", "EMP09", "LIMPIEZA", "Noche")
e10 = Empleado(20, "Kelly Kapoor", "kelly@cine.com", "555-0010", "EMP10", "ATENCION", "Tarde")


print(e1.gestionar_funciones())
print(e3.gestionar_funciones())
print(e8.marcar_entrada())


print("\n>>> CARGANDO PROMOCIONES PROMOCIONES")

promo1 = Promocion("ESTUDIANTE", "Descuento con credencial", 0.20, "2026-12-31")
promo2 = Promocion("MARTES2X1", "Martes a mitad de precio", 0.50, "2026-12-31")
promo3 = Promocion("GAMER", "Descuento presentando app de Bounty Rush", 0.15, "2026-06-30")
promo4 = Promocion("CAFE10", "Descuento especial en barra de café", 0.10, "2026-05-01")
promo5 = Promocion("CUMPLEAÑOS", "Descuento en tu mes", 0.30, "2026-12-31")
promo6 = Promocion("JONRON", "Descuento si traes jersey de béisbol", 0.15, "2026-10-31")
promo7 = Promocion("VIP", "Descuento en salas VIP", 0.25, "2026-12-31")
promo8 = Promocion("MATINE", "Descuento antes de las 2 PM", 0.35, "2026-08-31")
promo9 = Promocion("NAKAMA", "Descuento en películas de anime", 0.10, "2026-04-30")
promo10 = Promocion("FAMILIAR", "Descuento grupos de 4+", 0.20, "2026-12-31")

print(promo1.esValida(u1))

print(f"Descuento ESTUDIANTE en boleto de $100: ${promo1.aplicar_descuento(100)}")

print("\n>>> CARGANDO FUNCIONES")

f1 = Funcion(101, "12:00 PM", 60.0)
f2 = Funcion(102, "02:30 PM", 65.0)
f3 = Funcion(103, "04:15 PM", 70.0)
f4 = Funcion(104, "06:00 PM", 75.0)
f5 = Funcion(105, "08:00 PM", 80.0)
f6 = Funcion(106, "10:30 PM", 85.0)
f7 = Funcion(107, "11:00 AM", 60.0)
f8 = Funcion(108, "01:00 PM", 65.0)
f9 = Funcion(109, "03:45 PM", 70.0)
f10 = Funcion(110, "07:30 PM", 90.0)

print(f1.obtener_detalles_funcion())
print(f10.calcular_asientos_libres())


print("\n>>> CARGANDO SALAS")

s1 = Sala(1, "Sala 01", "Planta Baja", "2D", 100, False)
s2 = Sala(2, "Sala 02", "Planta Baja", "3D", 80, False)
s3 = Sala(3, "Sala 03", "Planta Alta", "IMAX", 150, False)
s4 = Sala(4, "Sala VIP 1", "Zona Exclusiva", "VIP", 30, True)
s5 = Sala(5, "Sala VIP 2", "Zona Exclusiva", "VIP", 30, True)
s6 = Sala(6, "Sala 04", "Planta Baja", "2D", 120, False)
s7 = Sala(7, "Sala 05", "Planta Baja", "MacroXE", 140, False)
s8 = Sala(8, "Sala 06", "Planta Alta", "3D", 90, False)
s9 = Sala(9, "Sala 07", "Planta Alta", "4DX", 60, False)
s10 = Sala(10, "Sala VIP 3", "Zona Exclusiva", "VIP", 40, True)

print(s3.obtener_tipo_sala())
print(s4.obtener_tipo_sala())
print(s1.verificar_disponibilidad())



print("\n>>> CARGANDO ZONAS DE COMIDA")

z1 = ZonaComida(11, "Dulcería Central", "Lobby", ["Palomitas", "Nachos"], {"Palomitas": 50, "Nachos": 30})
z2 = ZonaComida(12, "Barra de Café", "Lobby", ["Café Americano", "Espresso"], {"Café Americano": 100, "Espresso": 40})
z3 = ZonaComida(13, "Snacks VIP", "Zona Exclusiva", ["Sushi", "Vino"], {"Sushi": 15, "Vino": 10})
z4 = ZonaComida(14, "Dulcería Norte", "Pasillo Norte", ["Papas", "Hot Dog"], {"Papas": 40, "Hot Dog": 25})
z5 = ZonaComida(15, "Dulcería Sur", "Pasillo Sur", ["Palomitas", "Refresco"], {"Palomitas": 60, "Refresco": 80})
z6 = ZonaComida(16, "Carrito de Crepas", "Lobby", ["Crepa Salada", "Crepa Queso"], {"Crepa Salada": 20, "Crepa Queso": 20})
z7 = ZonaComida(17, "Heladería", "Lobby", ["Helado Vainilla", "Helado Limón"], {"Helado Vainilla": 30, "Helado Limón": 30})
z8 = ZonaComida(18, "Barra Cervezas", "Pasillo VIP", ["Cerveza Clara", "Cerveza Oscura"], {"Cerveza Clara": 50, "Cerveza Oscura": 50})
z9 = ZonaComida(19, "Estación de Nachos", "Planta Alta", ["Nachos Extra Queso", "Papas Fritas"], {"Nachos Extra Queso": 40, "Papas Fritas": 35})
z10 = ZonaComida(20, "Cafetería Alta", "Planta Alta", ["Café Latte", "Té Negro"], {"Café Latte": 30, "Té Negro": 25})

print(z2.vender_producto("Café Americano"))
print(z9.actualizar_inventario(15))


print("\n>>> BUSCAND RESERVAS")

r1 = Reserva(1001, ["H1", "H2"], 120.0, "PENDIENTE")
r2 = Reserva(1002, ["J5", "J6", "J7"], 210.0, "PENDIENTE")
r3 = Reserva(1003, ["A1"], 85.0, "PENDIENTE")
r4 = Reserva(1004, ["C3", "C4"], 130.0, "PENDIENTE")
r5 = Reserva(1005, ["VIP1", "VIP2"], 300.0, "PENDIENTE")
r6 = Reserva(1006, ["F5", "F6", "F7", "F8"], 280.0, "PENDIENTE")
r7 = Reserva(1007, ["G10"], 75.0, "PENDIENTE")
r8 = Reserva(1008, ["B1", "B2"], 160.0, "PENDIENTE")
r9 = Reserva(1009, ["D5", "D6", "D7"], 225.0, "PENDIENTE")
r10 = Reserva(1010, ["E1"], 60.0, "PENDIENTE")

print(r1.aplicar_promocion(promo1))
print(r1.confirmar_pago())
print(r1.generar_ticket())

print("\n--- ¡OBJETIVOS DE BUSQUEDA COMPLETADOS! ---")


print("\n" + "="*45)
print(">>> INICIANDO PROCESO DE RESERVA...")
print("="*45)


print(f"Usuario: {u2.nombre} (Puntos: {u2.puntos_fidelidad})")
print(f"Película: '{p4.titulo}' | {s3.obtener_tipo_sala()}")


print("Seleccione sus asientos (separados por coma): A1, A2, B5")
print("[SISTEMA]: Verificando disponibilidad...")
print("[ERROR]: El asiento A2 ya está ocupado por la Reserva #882.")
print("[SISTEMA]: Por favor, seleccione asientos disponibles.")
print("Seleccione sus asientos: A1, A3, B5")
print("[OK]: Asientos A1, A3, B5 bloqueados con éxito.")


monto_base = 450.00
print(f"Monto base: ${monto_base:.2f}")

print("\n>>> APLICANDO GESTIÓN COMERCIAL...")
print("¿Cuenta con código de promoción?: SI")
print(f"Código: {promo1.codigo}")
print(f"[SISTEMA]: Validando código... ¡ÉXITO! (Descuento del {int(promo1.porcentajeDescuento * 100)}% aplicado).")


reserva_reto = Reserva(995, ["A1", "A3", "B5"], monto_base, "PENDIENTE")
ahorro = monto_base * promo1.porcentajeDescuento
reserva_reto.aplicar_promocion(promo1)
reserva_reto.confirmar_pago()

print(f"\nResumen de Reserva #{reserva_reto.idreserva}:")
print(f"Usuario: {u2.nombre}")
print(f"Función: {p4.titulo} (20:00 hrs)")
print(f"Asientos: {reserva_reto.asientos}")
print(f"Total Final: ${reserva_reto.montototal:.2f} (Ahorraste ${ahorro:.2f})")
print(f"Estado: {reserva_reto.estado}. Ticket generado en PDF.")