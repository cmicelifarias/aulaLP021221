#classe é automavel
#nrodas e placa são atributos
#métodos da classe são dirigir, __init__, get_placas

class Automovel:
    # aqui são os argumentos da função
    def __init__(self,valor_placa,valor_nrodas):
        # atributo privado -> só colocar na frente __
        self.__placa = valor_placa
        #atributo público
        self.nrodas = valor_nrodas

    #função para pegar o valor de uma placa
    def get_placa(self):
        return self.__placa
    
    #função para mudar o valor de um atributo privado
    def set_placa(self,a):
        self.__placa == a

    def dirigir(self):
        print("Estou dirigindo")

# a é o objeto
a = Automovel("xxx-1234", 4) #aqui eu executo o __init__(a, "xxx-1234",4)
print(a.get_placa()) #get_placa(a)
a.dirigir()
a.nrodas = 5
a.__placa = "YYY-5678"
print(a.nrodas)
print(a.__placa)
