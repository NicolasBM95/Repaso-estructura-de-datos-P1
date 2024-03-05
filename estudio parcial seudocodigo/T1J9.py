#Un centro de salud requiere un sistema de información para administrar la agenda de citas por semana. Para cada
#cita, se debe permitir almacenar la información del médico y del paciente, hora y fecha, tipo de atención (general,
#especializado, odontología) y el valor de la factura del servicio. La información personal de los usuarios, así como de
#los médicos, almacenada en el sistema debe incluir el nombre completo, cedula, fecha de nacimiento, y teléfono de
#contacto. 

class persona:
    def __init__(self, nombre, cedula, fecha_nacimiento, telefono):
        self.nombre = nombre
        self.cedula = cedula
        self.fecha_nacimiento = fecha_nacimiento
        self.telefono = telefono

class paciente(persona):
    def __init__(self, nombre, cedula, fecha_nacimiento, telefono):
        super().__init__(nombre, cedula, fecha_nacimiento, telefono)

class medico(persona):
    def __init__(self, nombre, cedula, fecha_nacimiento, telefono):
        super().__init__(nombre, cedula, fecha_nacimiento, telefono)

class cita:
    def __init__(self, medico, paciente, fecha, hora, tipo_atencion, valor_factura, tipo_aten):
        self.medico = medico
        self.paciente = paciente
        self.fecha = fecha
        self.hora = hora
        self.tipo_atencion = tipo_atencion
        self.valor_factura = valor_factura
        self.tipo_aten = tipo_aten

paciente1 = paciente("Juan Perez", "123456789", "1990-01-01", "1234567890")
medico1 = medico("Dr. Maria Rodriguez", "987654321", "1975-05-05", "0987654321")
cita1 = cita(medico1, paciente1, "2024-03-15", "09:00", "General", 50000, "Pediatría")

print("Información de la cita:")
print("Médico:", cita1.medico.nombre)
print("Paciente:", cita1.paciente.nombre)
print("Fecha:", cita1.fecha)
print("Hora:", cita1.hora)
print("Tipo de atención:", cita1.tipo_atencion)
print("Valor de la factura:", cita1.valor_factura)
print("Tipo de atención:", cita1.tipo_aten)