class Professor:
    def __init__(self,nome):
        self.nome = nome

        
    def ministrar_aula(self,assunto):
        return f'O professor {self.nome} está ministrando uma aula sobre {assunto}'

        
class Aluno:
    def __init__(self,nome):
        self.nome = nome

        
    def presenca(self):
        return f'O aluno {self.nome} está presente!'

       
class Aula:
    def __init__(self,professor,assunto):
        self.professor = professor
        self.assunto = assunto
        self.alunos = []

        
    def adicionar_aluno(self,aluno):
        self.alunos.append(aluno)

    def listar_presenca(self):
        presenca = f"Presença na aula sobre {self.assunto}, ministrada pelo professor {self.professor.nome}:\n"
    
        for aluno in self.alunos:
        
            presenca = presenca + aluno.presenca() + '\n'
    
        return presenca


if __name__ == "__main__":
    
    #Criando Professor
    
    professor = Professor("Estevao da massa")


    #Criando Alunos

    aluno1 = Aluno("Pedro Vilas")
    aluno2 = Aluno("Thomas vitu")
    aluno3 = Aluno("Jm")       
    aluno4 = Aluno("Pedro Vilela")
    aluno5= Aluno("Nariz")

    
    #Criando Aula

    aula= Aula(professor,"Calculo 2")

    
    #Adicionando alunos na aula

    aula.adicionar_aluno(aluno1)
    aula.adicionar_aluno(aluno2)
    aula.adicionar_aluno(aluno3)
    aula.adicionar_aluno(aluno4)
    aula.adicionar_aluno(aluno5)

  

    print(aula.listar_presenca())

        
    

        
    

        
