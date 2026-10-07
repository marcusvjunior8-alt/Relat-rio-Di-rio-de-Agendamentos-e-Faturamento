pets = []
valores = []
servicos = []


option = input("Deseja cadastrar um pet? (s/n)\n")
while option.lower() == 's':
    name_pet = input('Digite nome do pet:\n')
    service = input('Digite o serviço: (banho, tosa ou consulta)\n')
    value_pay = float(input('Digite o valor pago:(R$)'))

    pets.append(name_pet)
    servicos.append(service.lower())
    valores.append(value_pay)


    option = input("Deseja cadastrar um pet? (s/n)\n")

total_pets = len(pets)

if total_pets > 0:
    faturamento_total = sum(valores)
    media_atendimento = faturamento_total/total_pets
    atendimento_banho = servicos.count('banho')
    atendimento_tosa = servicos.count('tosa')
    atendimento_consulta = servicos.count('consulta')
    print('=========================================')
    print('--- RESUMO DO DIA - PATAS & CUIDADOS ---')
    print('=========================================')
    print('Pets atentidos:',total_pets)
    print('Faturamento total do dia:',faturamento_total)
    print('Média por atendimento:',media_atendimento)
    print('--- Atendimentos: ---\nBanho:',atendimento_banho, '\nTosa:',atendimento_tosa , '\nConsulta:',atendimento_consulta)
    print('========================================')
else:
    print('Nenhum pet foi cadastrado hoje.')