'''
Crear un programa que permita crear objetos de la clase CuentaBancaria, cuyos atributos son: numeroCta, nombreCliente, saldoCta, fechaApertura, ultimoRetiro, ultimaConsignacion.
Aplicar encapsulamiento y definir los métodos apropiados para controlar y gestionar los atributos de los objetos creados.
Utilizar un menu para las diferentes opciones, tales como aperturaCta, consignar, retirar y transferencia entre otros.
'''

'''
Kevin Estiven Quiñones Quiñones
ingenieria de sistemas 
unimonserrate-nocturna

'''

class CuentaBancaria
|   def __init__(self, numeroCta, nombreCliente, saldoCta, fechaApertura, ultimoRetiro, ultimaConsignacion):
        self.__nombreCliente = nonbreCliente
        self.__saldoCta = saldoCta 
        self.__fechaApertura = fechaApertura
        self.__ultimoRetiro = ultimoRetiro
        self.__ultimaCopnsignacion = ultimaConsignacion 
        
    def set_numeroCta(self, x):
        self.__numeroCta = x 
    
    def set_nombreCliente(self, x):
        self.__nombreCliente = x
    
    def set_saldoCta(self, x):
        self.__saldoCta = x
        
    def set_fechaApertura(self, x):
        self.__fechaApertura = x
        
    def  set_ultimoRetiro(self, x):
        self.__ultimoRetiro = x

    def set_ultimaConsignacion(self, x):
        self.__ultimaConsignacion = x

   
    def get_numeroCta(self):
        return self.__numeroCta

    def get_nombreCliente(self):
        return self.__nombreCliente

    def get_saldoCta(self):
        return self.__saldoCta

    def get_fechaApertura(self):
        return self.__fechaApertura

    def get_ultimoRetiro(self):
        return self.__ultimoRetiro

    def get_ultimaConsignacion(self):
        return self.__ultimaConsignacion

    
    def consignar(self, monto):
        self.__saldoCta += monto
        self.__ultimaConsignacion = monto

    def retirar(self, monto):
        if monto > self.__saldoCta:
            print("Fondos insuficientes.")
        else:
            self.__saldoCta -= monto
            self.__ultimoRetiro = monto

    def transferir(self, otraCuenta, monto):
        if monto > self.__saldoCta:
            print("Fondos insuficientes para la transferencia.")
        else:
            self.__saldoCta -= monto
            otraCuenta.consignar(monto)
            print(f"Se han transferido {monto} a la cuenta {otraCuenta.get_numeroCta()}.")
def mostrar_menu():
    print("\n--- Menu de Opciones ---")
    print("1. Apertura de Cuenta")
    print("2. Consignar")
    print("3. Retirar")
    print("4. Transferir")
    print("5. Mostrar Detalles de la Cuenta")
    print("6. Salir")

def crear_cuenta():
    numeroCta = input("Ingrese el numero de la cuenta: ")
    nombreCliente = input("Ingrese el nombre del cliente: ")
    saldoCta = float(input("Ingrese el saldo inicial: "))
    fechaApertura = input("Ingrese la fecha de apertura (DD/MM/AAAA): ")
    return CuentaBancaria(numeroCta, nombreCliente, saldoCta, fechaApertura, 0, 0)

def main():
    cuentas = {}  
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opcion: ")

        if opcion == "1":
            nueva_cuenta = crear_cuenta()
            cuentas[nueva_cuenta.get_numeroCta()] = nueva_cuenta
            print("Cuenta creada exitosamente.")

        elif opcion == "2":
            numeroCta = input("Ingrese el numero de la cuenta: ")
            monto = float(input("Ingrese el monto a consignar: "))
            if numeroCta in cuentas:
                cuentas[numeroCta].consignar(monto)
                print(f"{monto} consignados a la cuenta {numeroCta}.")
            else:
                print("Cuenta no encontrada.")

        elif opcion == "3":
            numeroCta = input("Ingrese el numero de la cuenta: ")
            monto = float(input("Ingrese el monto a retirar: "))
            if numeroCta in cuentas:
                cuentas[numeroCta].retirar(monto)
            else:
                print("Cuenta no encontrada.")

        elif opcion == "4":
            numeroCta_origen = input("Ingrese el numero de la cuenta de origen: ")
            numeroCta_destino = input("Ingrese el numero de la cuenta de destino: ")
            monto = float(input("Ingrese el monto a transferir: "))
            if numeroCta_origen in cuentas and numeroCta_destino in cuentas:
                cuentas[numeroCta_origen].transferir(cuentas[numeroCta_destino], monto)
            else:
                print("Una o ambas cuentas no fueron encontradas.")

        elif opcion == "5":
            numeroCta = input("Ingrese el numero de la cuenta: ")
            if numeroCta in cuentas:
                cuenta = cuentas[numeroCta]
                print(f"Detalles de la Cuenta {numeroCta}:")
                print(f"Nombre del Cliente: {cuenta.get_nombreCliente()}")
                print(f"Saldo: {cuenta.get_saldoCta()}")
                print(f"Fecha de Apertura: {cuenta.get_fechaApertura()}")
                print(f"Ultimo Retiro: {cuenta.get_ultimoRetiro()}")
                print(f"ultima Consignación: {cuenta.get_ultimaConsignacion()}")
            else:
                print("Cuenta no encontrada.")

        elif opcion == "6":
            print("Saliendo del programa.")
            break

        else:
            print("Opcion no valida.")

if __name__ == "__main__":
    main()

