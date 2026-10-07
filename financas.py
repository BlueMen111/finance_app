def mostrar_extrato(transacoes):
    print("=== EXTRATO FINANCEIRO ===")
    for numero, transacao in enumerate(transacoes, start=1):
        print(f"{numero}. {transacao['descricao']} - R${transacao['valor']:.2f} ({transacao['tipo']})")
        print("-----------------------------")   
        
def calcular_total(transacoes):
    total_receita = 0
    total_despesa = 0

    for transacao in transacoes:
        if transacao['tipo'] == 'receita':
            total_receita += transacao['valor']

        elif transacao['tipo'] == 'despesa':
            total_despesa += transacao['valor']

    saldo = total_receita - total_despesa

    return saldo, total_receita, total_despesa

def maior_despesa_receita(transacoes):
    maior_despesa = 0
    descricao_maior = ""
    maior_receita = 0
    descricao_receita = ""
    for transacao in transacoes:
        if transacao['tipo'] == 'despesa':
            if transacao['valor'] > maior_despesa:
                maior_despesa = transacao['valor']
                descricao_maior = transacao['descricao']
                
        elif transacao['tipo'] == 'receita':
            if transacao['valor'] > maior_receita:
                maior_receita = transacao['valor']
                descricao_receita = transacao['descricao']          
    return maior_despesa, descricao_maior, maior_receita, descricao_receita

def registrar_transacao(transacoes, descricao, valor, tipo):
    if valor <= 0:
        print("Insira um valor válido.")
    elif tipo not in ["receita", "despesa"]:
        print("Tipo invalido, use receita ou despesa")
    else:
        nova_transacao = {"descricao": descricao, "valor": valor, "tipo": tipo}
        transacoes.append(nova_transacao)
        print("Transação registrada!")
        


