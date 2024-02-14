"""
1. Defina las clases necesarias que permitan definir los atributos y métodos de los objetos involucrados.
    Defina las clases con la visibilidad de sus atributos y métodos.
2. Construya el código de una aplicación que dé solución al problema planteado por el docente.
    Escriba el código necesario para crear las clases definidas en el punto 1.
    Cree los constructores con los parámetros necesarios para definir el recurso en memoria de los atributos de la clase.
    Instancie la(s) clase(s) para que permita crear los objetos necesarios que permitan almacenar la información necesaria de cada objeto.
    Muestre la información almacenada por cada objeto.
    
Se debe de poder registrar un usuario con su identificación y su nombre
Una vez registrado el usuario se debe de crear una o varias cuentas (Ahorro, corriente, nómina, etc)
Una vez creada la cuenta se debe de hacer al menos una transacción(Consignación), esta debe de tener un monto
La actividad debe de ser individual y presentada en un documento (Con normas APA) y apoyada con un video explicativo de no mas de 5 minutos    
"""

class Cuenta:
    def __init__(self):
        self.balance = 0

    def deposito(self, cantidad):
        self.balance += cantidad
        return self.balance

class CuentaAhorros(Cuenta):
    def __init__(self):
        super().__init__()
        
class CuentaCorriente(Cuenta):
    def __init__(self):
        super().__init__()

class CuentaNomina(Cuenta):
    def __init__(self):
        super().__init__()
    
class Banco:
    def __init__(self):
        self.usuarios = []

    def crear_cuenta(self, usuario, tipo_cuenta):
        if tipo_cuenta == "ahorro":
            usuario.cuenta_ahorro = CuentaAhorros()
        elif tipo_cuenta == "corriente":
            usuario.cuenta_corriente == CuentaCorriente()
        elif tipo_cuenta == "nomina":
            usuario.cuenta_corriente == CuentaCorriente()
        raise ValueError("Tipo de cuenta no válido")

class User:
    def __init__(self, name, identification):
        self.name = name
        self.identification = identification
        self.cuenta_ahorro = None
        self.cuenta_corriente = None 
        self.cuenta_nomina = None

    def signup(self, banco):
        for user in banco.usuarios:
            if user.name == self.name:
                raise Exception('Usuario ya existe')
        banco.usuarios.append(self)
        return f"Usuario {self.name} registrado exitosamente"

    def guardar_dinero(self, cantidad):
        if not self.cuenta_ahorro:
            raise ValueError("No se encontró ninguna cuenta de guardado")
        return self.cuenta_ahorro.deposito(cantidad)


if __name__ == "__main__":
    banco = Banco()
    user1 = User("Jorgito", 12345)
    user2 = User("Andres", 67890)
    try:
        print(user1.signup(banco))
        print(user2.signup(banco))
    except Exception as e:
        print(e)

    banco.crear_cuenta(user1, "ahorro")
    banco.crear_cuenta(user2, "ahorro")

    print(user1.guardar_dinero(150))
    user2.guardar_dinero(200)
    