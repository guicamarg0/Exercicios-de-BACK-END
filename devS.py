class Escola():
    def __init__(self, nome,sobrenome,funcao):
      self.nome = nome
      self.sobrenome = sobrenome
      self.funcao = funcao
#Somente a secretaria pode executar 
    def mostrarMsg(self):
        if self.funcao == "Secretaria":
            print("Bem vindo ao sistema de cadastro de alunos")
        else:
            print("Vocẽ não tem acesso.")
#Somente os estudantes pode ver os avisos
    def avisosAlunos(self):
        if self.funcao == "Estudante":
            print("Não haverá aula hoje!")

    def informacao(self):
      print("Nome: {} ".format(self.nome))
      print("Sobrenome: {} ".format(self.sobrenome))
      print("Função: {} ".format(self.funcao))

#Diretor não pode calcular a media
    def calcularMedia(self):
        if self.funcao == "Diretor":     
            print("Vocẽ não tem acesso.")
        else:
            nota = 0
            media = 60
            nome = input("Informe o nome: ")
            n1 = int(input("Informe a 1° nota: "))
            n2 = int(input("Informe a 2° nota: "))
            n3 = int(input("Informe a 3° nota: "))
            nota = (n1 + n2 +n3)/3


            if nota >= media:
                print("aluno aprovado")
            else:
                print("aluno reprovado")  
     
       
     
# classes que herdam da classe pai
class Diretor(Escola):
  def __init__(self, nome, sobrenome, funcao):
    super().__init__(nome, sobrenome, funcao)
    


class Professor(Escola):
  def __init__(self, nome, sobrenome, funcao):
    super().__init__(nome, sobrenome, funcao)
   
class Aluno(Escola):
  def __init__(self, nome, sobrenome, funcao):
    super().__init__(nome, sobrenome, funcao)

class Rh(Escola):
    def __init__(self, nome, sobrenome, funcao):
      super().__init__(nome, sobrenome, funcao)
      
#criar objetos
#DIRETORES DO COLEGIO
direManha = Diretor("Angela", "Santos", "Diretor")
direTarde = Diretor("Andrey", "Silva", "Diretor")
direNoite = Diretor("João", "Fontana", "Diretor")
#PROFESSORES DO 3DA1M
profDS = Professor("Elias","Silva","Professor")
profJD = Professor("Elias","Silva","Professor")
profCG = Professor("Elias","Silva","Professor")
profAPs = Professor("Jurandir","Santos","Professor")
profBCE = Professor("Fábio","Dias","Professor")
#Recursos Humannos - RH
rhSecretaria = Rh("Silvana","Lima", "Secretaria")

