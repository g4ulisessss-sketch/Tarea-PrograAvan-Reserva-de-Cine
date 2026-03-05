

class Persona:
    def __init__(self, id_persona, nombre, email, telefono):
        self.id_persona = id_persona
        self.nombre = nombre
        self.email = email
        self.telefono = telefono

    def login(self):
        return f"{self.nombre} ha iniciado sesion en el sistema."

    def logout(self):
        return f"{self.nombre} ha cerrado sesion."

    def actualizar_datos(self, nuevo_email):
        self.email = nuevo_email
        return f"Datos actualizados. Nuevo email: {self.email}"


class Usuario(Persona):
    def __init__(self, id_persona, nombre, email, telefono, puntos_fidelidad):

        super().__init__(id_persona, nombre, email, telefono)
        self.puntos_fidelidad = puntos_fidelidad
        self.historial_reservas = [] 

    def crear_reserva(self, reserva):
        self.historial_reservas.append(reserva)
        return f"Reserva creada con éxito para {self.nombre}."

    def consultar_promociones(self):
        return "Consultando promociones disponibles..."

    def cancelar_reserva(self):
        return "Reserva cancelada."

class Empleado(Persona):
    def __init__ (self, id_persona, nombre, email, telefono, id_empleado, rol, horario):
        super().__init__(id_persona, nombre, email, telefono)
        self.id_empleado=id_empleado
        self.rol=rol
        self.horario=horario

    def marcar_entrada(self):
        return f"El empleado {self.nombre} ({self.rol}) ha marcado su entrada."

    def gestionar_funciones(self):
    
        if self.rol == "ADMIN":
            return f"Acceso concedido: {self.nombre} está gestionando la cartelera."
        else:
            return "Acceso denegado: Solo el ADMIN puede gestionar funciones."

class Pelicula:

    def __init__(self, titulo, duracion, clasificacion, genero):
        self.titulo = titulo
        self.duracion = duracion
        self.clasificacion = clasificacion
        self.genero = genero

    def obtener_sinopsis(self):
            return f"[{self.titulo}]: Una increíble cinta de {self.genero} con duración de {self.duracion} min."


    def es_apta_para_todo_publico(self):

        if self.clasificacion == "A":
            return f"Es apta para todo publico"
        else:
            return f"No es apta para todo publico"
         
class Promocion:
    def __init__(self,codigo, descripcion, porcentajeDescuento, fechaExpiracion):
        self.codigo=codigo
        self.descripcion=descripcion
        self.porcentajeDescuento=porcentajeDescuento
        self.fechaExpiracion=fechaExpiracion

    def esValida(self,usuario):
            return f"La promoción '{self.codigo}' es válida para el usuario."
 
    def aplicar_descuento(self,monto):
        descuento = monto * self.porcentajeDescuento
        monto_final = monto - descuento
        return monto_final

class Funcion:
    def __init__(self,idFuncion, horarioInicio, precioBase):
        self.idFuncion=idFuncion
        self.horarioInicio=horarioInicio
        self.precioBase=precioBase

    def calcular_asientos_libres(self):

        return f"Calculando disponibilidad para la función {self.idFuncion}..."

    def obtener_detalles_funcion(self):
        return f"Función {self.idFuncion} | Inicio: {self.horarioInicio} | Precio: ${self.precioBase}"


class Espacio:
    def __init__ (self,idEspacio,nombre, ubicacion):
        self.idEspacio=idEspacio
        self.nombre=nombre
        self.ubicacion=ubicacion

    def verificar_disponibilidad(self):
        return f"Verificando: El espacio '{self.nombre}' se encuentra disponible."

    def limpiar_espacio(self):
        return f"El espacio '{self.nombre}' en {self.ubicacion} ha sido limpiado y está listo."
 
class Sala(Espacio):
    def __init__ (self,idEspacio,nombre, ubicacion, capacidad, tipo, esVip):
        super().__init__(idEspacio,nombre, ubicacion)
        self.capacidadTotal=capacidad
        self.tipo=tipo
        self.esVip=esVip


    def ajustar_aforo(self, nueva_capacidad):
        self.capacidadTotal = nueva_capacidad
        return f"El aforo de la sala '{self.nombre}' se ajustó a {self.capacidadTotal} personas."

    def obtener_tipo_sala(self):
        estado_vip = "VIP" if self.esVip else "Estándar"
        return f"La sala '{self.nombre}' es de tipo {self.tipo} ({estado_vip})."

class ZonaComida(Espacio):
    def __init__(self, idEspacio, nombre, ubicacion,listaproductos,stockactual):
        super().__init__(idEspacio, nombre, ubicacion)
        self.listaproductos=listaproductos
        self.stockactual=stockactual

    def vender_producto(self, producto):
        return f"Se ha registrado la venta de: {producto} en {self.nombre}."
    
    def actualizar_inventario(self, cantidad):
        return f"El inventario de {self.nombre} se ha actualizado con {cantidad} unidades nuevas."


class Reserva:
    def __init__ (self,idreserva,asientos,montototal,estado):
        self.idreserva=idreserva
        self.asientos=asientos
        self.montototal=montototal
        self.estado=estado

    def confirmar_pago(self):
        self.estado = "PAGADA" 
        return f"El pago se realizó con éxito"
    
    def generar_ticket(self):
        
        return f"La reserva {self.idreserva} con los asientos {self.asientos} tiene un monto total de ${self.montototal}, gracias por su preferencia"
    
    def aplicar_promocion(self, promo):
        self.montototal = promo.aplicar_descuento(self.montototal)
        return f"Promoción '{promo.codigo}' aplicada con éxito. Nuevo total: ${self.montototal}"