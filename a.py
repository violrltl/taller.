class Motocicleta:
    estado = "nueva"
    motor= False

    def __init__(self,color, matricula, combustible_litros, numero_ruedas, marca, modelo, fecha_fabricacion, velocidad_punta, peso, combustible_maximo):
        self.color = color
        self.matricula = matricula
        self.combustible_litros = combustible_litros
        self.numero_ruedas = numero_ruedas
        self.marca = marca
        self.modelo = modelo
        self.fecha_fabricacion=fecha_fabricacion
        self.velocidad_punta= velocidad_punta
        self.peso= peso
        self.combustible_maximo= combustible_maximo

    def arrancar(self):
        if self.motor == False:
            self.motor =True
            print(f"el motor de {self.marca} {self.modelo} ha arrancado")
        else:
            print(f"el motor de {self.marca} {self.modelo} ya estaba en marcha")
    def detener(self):
        if self.motor == True:
            self.motor = False
            print(f"el motor de {self.marca} {self.modelo}  se ha detenido")
        else:
            print(f"el motor de  {self.marca} {self.modelo} ya esta detenido")

    def consultaPrice(self):
        print(f"el precio de  {self.marca} {self.modelo} es de ${self.precio}")

    def deposito(self):
        print(f"reporte del deposito de {self.marca} {self.modelo} ")
        print(f"el deposito tiene {self.combustible_litros} litro de combustible ")
        print(f"la capacidad maxima del tanque es {self.combustible_maximo} litros ")
        print(f" los litros que faltan para llenar el deposito son {self.combustible_maximo - self.combustible_litros} litros")
        print("fin del reposrte, feli dia :D :\n")


    def repostar(self):
        while True:
            self.repostar_litros = float(input(f"¿cuantos litros desea repostar en su {self.marca}{self.modelo}?:\n"))
            if self.combustible_litros + self.repostar_litros <= self.combustible_maximo:
                self.combustible_litros += self.repostar_litros
                print(f"la motocicleta {self.marca} {self.modelo} tiene {self.combustible_litros} litros de combustible")
                break
            else:
                print("lo sentimos, esta cantidad supera la capacdad maxima")






laloopsi = Motocicleta("tromposita" ,"nigwe4", 4, 2, "lalaloopsi", 3000, "12/2/2", 57000, "200kg", 12)
SuperKorris = Motocicleta(
    color= "korra",
    combustible_maximo = 30,
    matricula= "jife52",
    combustible_litros=0,
    numero_ruedas=1,
    fecha_fabricacion="2/3/11",
    velocidad_punta= 90000,
    peso= "90kg",
    marca= "LOK",
    modelo= "avatar",)

laloopsi.arrancar()
SuperKorris.detener()

SuperKorris.precio= 13000000
laloopsi.precio= 5000000

print(f" El precio de la motocicleta {SuperKorris.marca} {SuperKorris.modelo} es de ${SuperKorris.precio}  ")
print(f" El precio de la motocicleta {laloopsi.marca} {laloopsi.modelo} es de ${laloopsi.precio}  ")



print(laloopsi.consultaPrice())
print(SuperKorris.consultaPrice())

print(laloopsi.deposito())
print(SuperKorris.deposito())

print(laloopsi.repostar())
print(SuperKorris.repostar())

