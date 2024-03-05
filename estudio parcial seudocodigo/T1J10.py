#Una empresa de bienes raíces requiere un sistema que le permita administrar los inmuebles que dispone para
#alquiler. El sistema debe permitir almacenar la información de los usuarios, así como permitirles alquilar hasta dos
#inmuebles y pagar la renta. Cada inmueble se identifica por un código de identificación con letras y números, la
#dirección completa, el valor de la renta mensual, la información del dueño del inmueble; cada inmueble solo se puede
#rentar a único usuario. Tanto la información personal de los usuarios como dueños de inmueble debe incluir el nombre
#completo, cedula, fecha de nacimiento, dirección completa, teléfono de contacto y correo electrónico. La dirección
#debe incluir tipo de vía (calle, carrera, etc.), número o nombre de la vía, número y letra con la nomenclatura del
#inmueble, número de apto si aplica, ciudad, y barrio.

class persona():
    def __init__(self, nombre, cedula, fecha_nacimiento, direccion, telefono, correo):
        self.nombre = nombre
        self.cedula = cedula
        self.fecha_nacimiento = fecha_nacimiento
        self.direccion = direccion
        self.telefono = telefono
        self.correo = correo

class usuario(persona):
    def __init__(self, nombre, cedula, fecha_nacimiento, direccion, telefono, correo):
        super().__init__(nombre, cedula, fecha_nacimiento, direccion, telefono, correo)
        self.inmuebles_alquilados = []
    
class duenioInmueble(persona):
    def __init__(self, nombre, cedula, fecha_nacimiento, direccion, telefono, correo):
        super().__init__(nombre, cedula, fecha_nacimiento, direccion, telefono, correo)

class inmueble():
    def __init__(self, codigo, direccion, valor_renta_mensual, duenio):
        self.codigo = codigo
        self.direccion = direccion
        self.valor_renta_mensual = valor_renta_mensual
        self.duenio = duenio
        self.usuario_actual = None

    def alquilar(self, usuario):
        if len(usuario.inmuebles_alquilados) >= 2:
            print("El usuario ya ha alquilado el máximo de inmuebles permitidos.")
            return False
        if self.usuario_actual:
            print("El inmueble ya está alquilado.")
            return False
        self.usuario_actual = usuario
        usuario.inmuebles_alquilados.append(self)
        print(f"El inmueble con código {self.codigo} ha sido alquilado por {usuario.nombre}.")
        return True
    
    def pagar_renta(self):
        if not self.usuario_actual:
            print("El inmueble no está alquilado.")
            return False
        print(f"Se ha recibido el pago de renta mensual por el inmueble con código {self.codigo}.")
        return True
    
duenio1 = duenioInmueble("Juan Perez", "123456789", "1980-01-01", "Calle 123 # 45-67", "1234567", "juan@example.com")
usuario1 = usuario("Maria Rodriguez", "987654321", "1990-01-01", "Carrera 45 # 67-89", "9876543", "maria@example.com")

inmueble1 = inmueble("A123", "Calle 67 # 89-10", 1000000, duenio1)
inmueble2 = inmueble("B456", "Carrera 12 # 34-56", 1500000, duenio1)

inmueble1.alquilar(usuario1)
inmueble2.alquilar(usuario1)

inmueble1.pagar_renta()
inmueble2.pagar_renta()