from django.db import models

class Cliente(models.Model):
    identificacion = models.CharField(max_length=20, unique=True, verbose_name="Identificación")
    nombre = models.CharField(max_length=100, verbose_name="Nombre")
    apellido = models.CharField(max_length=100, verbose_name="Apellido")
    correo = models.EmailField(verbose_name="Correo Electrónico")
    telefono = models.CharField(max_length=15, verbose_name="Teléfono")
    direccion = models.TextField(verbose_name="Dirección")

    def __str__(self):
        return f"{self.nombre} {self.apellido}"


class HistorialCliente(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name='historiales', verbose_name="Cliente")
    fecha = models.DateField(auto_now_add=True, verbose_name="Fecha")
    descripcion = models.TextField(verbose_name="Descripción")

    def __str__(self):
        return f"Historial de {self.cliente.nombre} {self.cliente.apellido} el {self.fecha}"


class SolicitudServicio(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name='solicitudes', verbose_name="Cliente")
    fecha_solicitud = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de Solicitud")
    tipo_servicio = models.CharField(max_length=100, verbose_name="Tipo de Servicio")
    descripcion = models.TextField(verbose_name="Descripción")

    def __str__(self):
        return f"Solicitud de {self.tipo_servicio} por {self.cliente.nombre} {self.cliente.apellido} el {self.fecha_solicitud}"


class Tecnico(models.Model):
    nombre = models.CharField(max_length=100, verbose_name="Nombre")
    apellido = models.CharField(max_length=100, verbose_name="Apellido")
    especialidad = models.CharField(max_length=100, verbose_name="Especialidad")
    correo = models.EmailField(verbose_name="Correo Electrónico")
    telefono = models.CharField(max_length=15, verbose_name="Teléfono")

    def __str__(self):
        return f"{self.nombre} {self.apellido} - {self.especialidad}"


class OrdenTrabajo(models.Model):
    solicitud = models.ForeignKey(SolicitudServicio, on_delete=models.CASCADE, related_name='ordenes', verbose_name="Solicitud de Servicio")
    tecnico = models.ForeignKey(Tecnico, on_delete=models.CASCADE, related_name='ordenes', verbose_name="Técnico Asignado")
    fecha_asignacion = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de Asignación")
    estado = models.CharField(max_length=50, choices=[('Pendiente', 'Pendiente'), ('En Proceso', 'En Proceso'), ('Completada', 'Completada')], default='Pendiente', verbose_name="Estado")
    descripcion = models.TextField(verbose_name="Descripción de la Orden")

    def __str__(self):
        return f"Orden {self.id} - {self.estado}"

class Equipo(models.Model):
    nombre = models.CharField(max_length=100, verbose_name="Nombre del Equipo")
    modelo = models.CharField(max_length=100, verbose_name="Modelo")
    numero_serie = models.CharField(max_length=100, unique=True, verbose_name="Número de Serie")
    fabricante = models.CharField(max_length=100, verbose_name="Fabricante")
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name='equipos', verbose_name="Cliente")
    fecha_adquisicion = models.DateField(verbose_name="Fecha de Adquisición")

    def __str__(self):
        return f"{self.nombre} - {self.modelo} ({self.numero_serie})"
    

class Presupuesto(models.Model):
    solicitud = models.ForeignKey(SolicitudServicio, on_delete=models.CASCADE, related_name='presupuestos', verbose_name="Solicitud de Servicio")
    fecha_creacion = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de Creación")
    total_estimado = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Total Estimado")
    descripcion = models.TextField(verbose_name="Descripción")

    def __str__(self):
        return f"Presupuesto {self.id} - {self.total_estimado} CL"
    
class Diagnostico(models.Model):
    solicitud = models.ForeignKey(SolicitudServicio, on_delete=models.CASCADE, related_name='diagnosticos', verbose_name="Solicitud de Servicio")
    tecnico = models.ForeignKey(Tecnico, on_delete=models.CASCADE, related_name='diagnosticos', verbose_name="Técnico")
    fecha = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de Diagnóstico")
    descripcion = models.TextField(verbose_name="Descripción")

    def __str__(self):
        return f"Diagnóstico {self.id} - {self.solicitud.cliente.nombre} {self.solicitud.cliente.apellido}"
    
class Pago(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name='pagos', verbose_name="Cliente")
    fecha = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de Pago")
    monto = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Monto")
    descripcion = models.TextField(verbose_name="Descripción")

    def __str__(self):
        return f"Pago {self.id} - {self.monto} CL"

class PruebaDiagnostico(models.Model):
    diagnostico = models.ForeignKey(Diagnostico, on_delete=models.CASCADE, related_name='pruebas', verbose_name="Diagnóstico")
    prueba = models.CharField(max_length=100, verbose_name="Prueba")
    resultado = models.CharField(max_length=100, verbose_name="Resultado")
    fecha = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de la Prueba")

    def __str__(self):
        return f"Prueba {self.prueba} - Resultado: {self.resultado}"

class SolicitudRepuesto(models.Model):
    orden_trabajo = models.ForeignKey(OrdenTrabajo, on_delete=models.CASCADE, related_name='solicitudes_repuesto', verbose_name="Orden de Trabajo")
    repuesto = models.CharField(max_length=100, verbose_name="Repuesto Solicitado")
    cantidad = models.IntegerField(verbose_name="Cantidad")
    fecha_solicitud = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de Solicitud")
    estado = models.CharField(max_length=50, choices=[('Pendiente', 'Pendiente'), ('Aprobado', 'Aprobado'), ('Rechazado', 'Rechazado')], default='Pendiente', verbose_name="Estado")

    def __str__(self):
        return f"Solicitud de {self.repuesto} - {self.estado}"

class OrdenCompra(models.Model):
    solicitud_repuesto = models.ForeignKey(SolicitudRepuesto, on_delete=models.CASCADE, related_name='ordenes_compra', verbose_name="Solicitud de Repuesto")
    fecha_creacion = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de Creación")
    proveedor = models.CharField(max_length=100, verbose_name="Proveedor")
    monto = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Monto")

    def __str__(self):
        return f"Orden de Compra {self.id} - {self.proveedor}"

class HistorialOrdenTrabajo(models.Model):
    orden_trabajo = models.ForeignKey(OrdenTrabajo, on_delete=models.CASCADE, related_name='historiales', verbose_name="Orden de Trabajo")
    fecha = models.DateTimeField(auto_now_add=True, verbose_name="Fecha")
    descripcion = models.TextField(verbose_name="Descripción")

    def __str__(self):
        return f"Historial de Orden {self.orden_trabajo.id} el {self.fecha}"

class ServicioRealizado(models.Model):
    orden_trabajo = models.ForeignKey(OrdenTrabajo, on_delete=models.CASCADE, related_name='servicios_realizados', verbose_name="Orden de Trabajo")
    fecha_realizacion = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de Realización")
    descripcion = models.TextField(verbose_name="Descripción del Servicio")

    def __str__(self):
        return f"Servicio Realizado {self.id} - {self.orden_trabajo.id}"

class RegistroFotografico(models.Model):
    orden_trabajo = models.ForeignKey(OrdenTrabajo, on_delete=models.CASCADE, related_name='registros_fotograficos', verbose_name="Orden de Trabajo")
    imagen = models.ImageField(upload_to='fotos/', verbose_name="Imagen")
    descripcion = models.TextField(verbose_name="Descripción")
    fecha = models.DateTimeField(auto_now_add=True, verbose_name="Fecha")

    def __str__(self):
        return f"Registro Fotográfico {self.id} - {self.orden_trabajo.id}"

