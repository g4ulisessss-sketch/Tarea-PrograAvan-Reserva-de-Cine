
class Persona:
    def __init__(self, idPersona, nombre, email):
        self.idPersona = idPersona
        self.nombre = nombre
        self.email = email

    def login(self):
        return f"{self.nombre} ha iniciado sesión en el sistema de la cafetería."

    def actualizarPerfil(self, nuevo_email):
        self.email = nuevo_email
        return f"Perfil actualizado. Nuevo email: {self.email}"

class Cliente(Persona):
    def __init__(self, idPersona, nombre, email, puntosFidelidad):
        super().__init__(idPersona, nombre, email)
        self.puntosFidelidad = puntosFidelidad
        self.historialPedidos = []

    def realizarPedido(self, pedido):
        self.historialPedidos.append(pedido)
        return f"El cliente {self.nombre} ha realizado un nuevo pedido."

    def consultarHistorial(self):
        return f"Consultando el historial de {self.nombre}... Total de pedidos: {len(self.historialPedidos)}"

    def canjearPuntos(self, puntos_a_usar):
        if self.puntosFidelidad >= puntos_a_usar:
            self.puntosFidelidad -= puntos_a_usar
            return f"Se han canjeado {puntos_a_usar} puntos. Puntos restantes: {self.puntosFidelidad}"
        return "Puntos insuficientes para el canje."

    def mostrar_detalle(self):
        return f"ID: {self.idPersona} | {self.nombre} | Puntos: {self.puntosFidelidad}"

class Empleado(Persona):
    def __init__(self, idPersona, nombre, email, idEmpleado, rol):
        super().__init__(idPersona, nombre, email)
        self.idEmpleado = idEmpleado
        self.rol = rol 

    def actualizarInventario(self):
        if self.rol == "GERENTE":
            return f"[{self.rol}] {self.nombre} está actualizando el inventario maestro."
        return f"Acceso denegado: {self.nombre} no tiene permisos de GERENTE."

    def cambiarEstadoPedido(self, nuevo_estado):
        return f"El empleado {self.nombre} cambió el estado del pedido a: {nuevo_estado}"

    def mostrar_detalle(self):
        return f"ID: {self.idEmpleado} | {self.nombre} | Rol: {self.rol}"

class ProductoBase:
    def __init__(self, idProducto, nombre, precioBase):
        self.idProducto = idProducto
        self.nombre = nombre
        self.precioBase = precioBase

class Bebida(ProductoBase):
    def __init__(self, idProducto, nombre, precioBase, tamaño, temperatura, modificadores):
        super().__init__(idProducto, nombre, precioBase)
        self.tamaño = tamaño
        self.temperatura = temperatura 
        self.modificadores = modificadores 

    def agregarExtra(self, extra):
        self.modificadores.append(extra)
        return f"Extra '{extra}' agregado a la bebida {self.nombre}."

    def calcularPrecioFinal(self):
        
        costo_extras = len(self.modificadores) * 5.0
        precio_final = self.precioBase + costo_extras
        return precio_final

    def mostrar_detalle(self):
        return f"ID: {self.idProducto} | {self.nombre} (${self.precioBase}) | Cat: Bebida {self.temperatura}"

class Postre(ProductoBase):
    def __init__(self, idProducto, nombre, precioBase, esVegano, sinGluten):
        super().__init__(idProducto, nombre, precioBase)
        self.esVegano = esVegano
        self.sinGluten = sinGluten
        
    def mostrar_detalle(self):
        return f"ID: {self.idProducto} | {self.nombre} (${self.precioBase}) | Cat: Postre"


class Inventario:
    def __init__(self, ingredientes):
        
        self.ingredientes = ingredientes

    def reducirStock(self, ingrediente, cantidad):
        if ingrediente in self.ingredientes and self.ingredientes[ingrediente] >= cantidad:
            self.ingredientes[ingrediente] -= cantidad
            return f"Stock de {ingrediente} reducido. Restante: {self.ingredientes[ingrediente]}"
        return f"Error: No hay suficiente stock de {ingrediente}."

    def notificarFaltante(self, ingrediente):
        return f"¡ALERTA DE INVENTARIO! El ingrediente '{ingrediente}' está por agotarse."

class Pedido:
    def __init__(self, idPedido, productos, estado, total):
        self.idPedido = idPedido
        self.productos = productos 
        self.estado = estado 
        self.total = total

    def calcularTotal(self):
        suma = 0
        for producto in self.productos:
           
            if isinstance(producto, Bebida):
                suma += producto.calcularPrecioFinal()
            else:
                suma += producto.precioBase
        self.total = suma
        return f"El total del pedido #{self.idPedido} ha sido recalculado: ${self.total:.2f}"

    def validarStock(self, inventario_actual):

        return f"Verificando disponibilidad de ingredientes para el pedido #{self.idPedido}... ¡Stock confirmado!"