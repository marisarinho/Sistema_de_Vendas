from pprint import pprint

print('Bem vindo ao nosso sistema de vendas! Aqui você poderá cadastrar produtos e fazer pedidos.')
print()

dados = {"produtos": [],
         "pedidos": []}

def cadastrado():
    desc = input('Descrição do produto: ')  
    valor = float(input('Valor unitário: ')) 
    return desc, valor
def listar_produtos():
    print("Produtos cadastrados:")
    if not dados['produtos']:
        print("Nenhum produto cadastrado.")
    else:
        for produto in dados['produtos']:
            print(f"ID: {produto['id']}, Nome: {produto['nome']}, Descrição: {produto['descricao']}, Valor: {produto['valor']:.2f}")
    print('--------')
while True:
    print('--------')
    opcao = int(input('''Selecione uma das opções abaixo:
1 - Cadastrar produto.
2 - Listar produtos.  
3 - Fazer pedido.
4 - Pesquisar produtos.                     
5 - Sair.
'''))
    print('--------')
    if opcao == 1:

        produto = input("Digite o produto que você quer adicionar: ")
        
        descricao, valor = cadastrado()

        dados['produtos'].append({
            'id': len(dados['produtos']) + 1,
            'nome': produto,
            'descricao': descricao,
            'valor': valor,
        })
            
        print("Produto cadastrado!")
        print('--------')
    
    elif opcao==2:
        listar_produtos()
    elif opcao ==3:
        carrinho=[]
        total_compras=0
        while True:
            listar_produtos()
            pedido=input('Digite o Id para escolher um pedido ou digite 0(numero zero)para finalizar compra.')
            print('--------')
            
            if pedido=='0':
                print('Os produtos que voce comprou:')
                for prod in carrinho:
                    print(f'{prod['nome']},R${prod['valor']:.2f}')
                print(f'Valor total das suas comprinhas:{total_compras:.2f}')
                print('--------')
                break
            else:
                  for produto in dados['produtos']:
                      if produto['id']==int(pedido):
                          quant = int(input('Digite quantos produtos desse ID você deseja: '))
                          print('--------')
                          carrinho.append(produto)
                          total_compras+=produto['valor']*quant

                          carrinho.append({
                                    'nome': produto['nome'],
                                    'valor': produto['valor'],
                                    'quantidade': quant
                                    })
                          print(f"{quant}x {produto['nome']} adicionado ao carrinho.")
                          print('--------')

    elif opcao==4:
        print('No momento não é possivel pesquisar produtos.')
    elif opcao==5:
        print("Fim do programa.")
        print('--------')
        break