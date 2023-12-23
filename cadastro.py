try: # System developed by Claudir Santos
    selector = int(input("""
        \033[31m Cadastro de alunos - by Claudir\033[m
    \033[32m*Cadastre um aluno e tire a média de sua nota final*\033[m 
            Selecione uma das opções abaixo: \n
    1- Cadastrar alunos
    2- Encerrar programa\n
        """))
        
    def calculateAverageNotes():
        try:
            listValueNotes = []
            getAmontNotes = int(input(f"\nDigite a quantidade de notas para fazer a média de {getStudentName}: \n"))
            for i in range(getAmontNotes):
                valueNotes = int(input(f"\nDigite a {i+1}° Nota de {getStudentName}:"))
                listValueNotes.append(valueNotes)
            if listValueNotes:
                calculateAverage = sum(listValueNotes) / len(listValueNotes)
                formatAverageCalculatedToInt = int(calculateAverage)
                if formatMinimalAverageToAprovalToInt <= formatAverageCalculatedToInt:
                    studentStatus = "Aprovado(a)"
                else: studentStatus = "Reprovado(a)"
                formatedAverageCalculated = "{:.2f}".format(formatAverageCalculatedToInt)
                print(f"""
    \033[34mMédia Final\033[m    
    Aluno: {getStudentName}\n
    Idade: {getStudentAge}\n
    Média: {formatedAverageCalculated}\n
    Situação: {studentStatus}\n""")
        except ValueError:
            print("\n\033[31m|ERRO| Digite um número\033[m")
    if selector not in [1, 2]:
        raise ValueError("Selecione uma das opções!")
    if selector == 2:
        exit()
        
    getStudentName = input("\nDigite o nome do Aluno: \n")
    if getStudentName.replace(' ','').isalpha():
        getStudentAge = input(f"\nDigite a idade de {getStudentName}: \n")
        if getStudentAge.isdigit():
            convertStudentAgeToInt = int(getStudentAge)
            getAverageToAproval = input(f"\nDigite a média necessária para que {getStudentName} seja aprovado(a):\n")
            if getAverageToAproval.isdigit():
                formatMinimalAverageToAprovalToInt = int(getAverageToAproval)
                calculateAverageNotes()
        else:
            raise ValueError("Digite um número")
    else:
        raise ValueError("Digite o nome do Aluno! \n")

except ValueError as e:
    print("\033[31m|ERRO| ", e)
finally: print("\n\033[32mPrograma encerrado!\033[m")
# TODO: Requisitar média de aprovação e falar se o aluno foi aprovado ou não.
# TODO: Método Etec ou escola convencional