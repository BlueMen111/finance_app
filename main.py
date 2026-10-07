import os
os.system ("cls")
from data.armazenamento import salvar_transacao_do_app, carregar_transacoes
from financas import mostrar_extrato, calcular_total, maior_despesa_receita, registrar_transacao

transacoes = carregar_transacoes()

def pausar():
    input("\nPressione Enter para continuar...")   
   
def finance_app():

    while True:
        os.system ("cls")
        saldo_atual, total_receitas, total_despesas = calcular_total(transacoes)
        maior_despensa, descricao_maior, maior_receita, descricao_receita = maior_despesa_receita(transacoes)
    
        
        print("=== FINANCE APP ===")
        print("1- Ver Saldo")
        print("2- Despesas")
        print("3- Receitas")
        print("4- Ver Extrato")
        print("5- Registrar nova transação")
        print("6- Fechar...")
        options = input("Digite a sua opção: ")
        
        if options == "1":
            print(f"Seu saldo é de: R${saldo_atual:.2f}")
            
            pausar()
                
        elif options == "2":
            print("1- Para ver despesas totais")
            print("2- Para ver a maior despesa")
            options_despesa = input("Selecione a opção de despesa: ")
            
            if options_despesa == "1":
                print(f"A sua despesa total é de: R${total_despesas:.2f}")
                pausar()
                
            elif options_despesa == "2":
                print(f"A sua maior despesa é: {descricao_maior} R${maior_despensa:.2f}")
                pausar()
                        
            else:
                print("Insira uma opção válida!")    
                pausar()
                
        elif options == "3":
            print("1- Para ver receitas totais")
            print("2- Para ver a maior receita")     
            options_receita = input("Selecione a opção de receita: ")  
            
            if options_receita == "1":
                print(f"A sua receita total é de: R${total_receitas:.2f}")
                pausar()
                       
            elif options_receita == "2":
                print(f"A sua maior receita é {descricao_receita} R${maior_receita:.2f}")
                pausar()
                
            else:
                print("Insira uma opção válida!")        
                pausar()
                
        elif options == "4":
            mostrar_extrato(transacoes)  
            
            pausar()
        elif options == "5":
            descricao = input("Digite uma descrição: ")
            
            valor_texto = input("Digite um novo valor: ").strip()
            
            valor_texto_tratado = valor_texto.replace(",", ".")
            
            tipo = input("Digite um tipo (receita/despesa): ").strip().lower()

            try:
                valor = float(valor_texto_tratado)
                if tipo not in ['receita', 'despesa']:
                    raise KeyError
                    
                registrar_transacao(transacoes, descricao, valor, tipo)
                salvar_transacao_do_app(transacoes)

            except ValueError:
                print(f"Erro: O texto '{valor_texto}' não é um número válido. Por favor, use apenas números.")   

            except KeyError:
                print(f"Erro: O tipo '{tipo}' não existe. Por favor, use apenas 'receita' ou 'despesa'.")
            pausar()
            
        elif options == "6":
            print("Parando o programa....")
            break
        else:
            print("Insira uma opção válida!")
                

finance_app()         
          


        