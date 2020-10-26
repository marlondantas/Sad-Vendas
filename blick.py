#Beep Beep im a sheep ♫
#P

from datetime import datetime
import os


class Clientes:
    def Cadastrar(dados):
        print("Iniciando Cadastro do Cliente")
        #montado a string do dados
        novo=""
        for x in dados:
            novo+=x+"/o/"

        #checar se o usuario(user) existe
        dados.clear()
        dados.append(novo.split("/o/")[3])
        dados.append(novo.split("/o/")[4])
        r=Clientes.Consultar(dados)[0]
        if r == "Sucesso" or r =="Senha Errada":
            print("User já cadastrado")
            return "User já cadastrado"

        #jogando para o txt: Clientes.txt
        file=open("Clientes.txt","r").read().split("\n")

        #salvando o txt:
        exitF=open("Clientes.txt","w")
        for f in file:
             exitF.write(f+"\n")
        exitF.write(novo)
        exitF.close()
        print("Cadastrado")
        return "Cadastrado"
    #Dados[] = user,senha
    def Consultar(dados):
        # Abrir o BD.txt:
        print("iniciando a Consulta")
        file = open("Clientes.txt", "r").read().split("\n")
        dadosC = []
        for x in range(3, len(file)):
            dadosC.append(file[x].split("/o/"))
        for y in range(len(dadosC)):
            # lembra de retonar os dados do clientes apos o login.
            if dadosC[y][3] == dados[0]:
                if dadosC[y][4] == dados[1]:
                    return "Sucesso",dadosC[y]
                else:
                    return "Senha Errada"
        return "Cadastro não cadastrado"

    def Editar(self):
        # sem tempo para isso
        pass

        # checar se ja existe um banco de dados presente.
    def Checarpasta(self):
        sublocal = os.listdir()
        p = False

        for x in sublocal:
            if x == "Clientes.txt":
                p = True

        if p == False:
            txt = open("Clientes.txt", "w")
            txt.write("Banco de Dados.txt\n")
            txt.write("Sad Codes®\n")
            txt.write("Dados: Nome/ CPF/ E-mail/ User/ Senha/ Data de nascimento/ Telefone")
            txt.close()
            p = True

class Produtos:
    # dados 0 ID,1 nome,2 preco,3 categoria
    def Cadastrar(dados):
        print("iniciando Cadastro")

        # montador a strin do novo produto
        novo = ""
        for x in dados:
            novo += x + "/o/"

        # checar se o produto existe
        id = dados[0]
        dados.clear
        dados.append(id)
        r = Produtos.Consultar(dados)
        print(r)
        if r[0] == "Produto Já cadastrado":
            return "Produto Já cadastrado"

        # abrindo o txt: Produtos.txt
        file = open("Produtos.txt", "r").read().split("\n")

        # salvando o arquivo txt
        exitF = open("Produtos.txt", "w")
        for f in file:
            exitF.write(f + "\n")
        exitF.write(novo)
        exitF.close()
        print("Produto Registrado")
        return "Produto Registrado"
    # dados ID
    def Consultar(dados):
        print("iniciando consulta")
        # abri o banco de dados
        file = open("Produtos.txt", "r").read().split("\n")
        dadosC = []
        # carrega os dados para a comparação
        for x in range(4, len(file)):
            dadosC.append(file[x].split("/o/"))

        # analisa a lista para buscar semelhantes
        for y in range(len(dadosC)):
            if dadosC[y][0] == dados:
                return "Produto Já cadastrado", dadosC[y]
        return "Produto novo", dadosC

    def Editar(self):
        print("Em manutanção")
        # Sem tempo para terminar isso
        pass

    def ChecarPasta(self):
        # checar se ja existe um banco de dados presente.
        sublocal = os.listdir()
        p = False

        for x in sublocal:
            if x == "Produtos.txt":
                p = True

        if p == False:
            txt = open("Produtos.txt", "w")
            txt.write("Banco de Dados.txt\n")
            txt.write("Sad Codes®\n")
            txt.write("Produtos Cadastrados\n")
            txt.write("Dados:C. de Barra/ Nome/ Preco/ Categoria")
            txt.close()
            p = True

class vendas:
    def criarPasta (self):
        g= os.listdir()

        for x in g:
            if x == "Recibos":
                print("Ops")
                return
            else:
                os.makedirs("/Recibos",exist_ok=True)

    def checarVendas(self):
        g=os.listdir()

        for x in g:
            if x == "RelatorioVendas.txt":
                h=open("RelatorioVendas.txt","r").read().split("\n")
                if len(h)> 5:
                    return h[len(h)-1]
                else:
                    return "Sem Vendas Registrada"

        h=open("RelatorioVendas.txt","w")
        h.write("Banco de Dados.txt\n")
        h.write("Sad Codes®\n")
        h.write("Relatorio de Vendas\n")
        h.write("Numero da venda/Login/Cpf/Codigo do produto/Produto e Quatidade/Valor Total/Dia e Hora\n")
        h.close()

    def relatorio(totalP,ddp,ddq,ddC):
        #totap = numero de produtos:
        #ddv: ID,
        # quatidade
        #ddc: login, cpf

        Un=vendas.checarVendas(0)
        if Un == "Sem Vendas Registrada" or Un == None:
            Un="0/o/000"
        Un.split("/o/")

        NAtual=int(Un[0])+1

        Dproduto=[]

        for x in range(int(totalP)):
            Dproduto.append(Produtos.Consultar(ddp)[1])

        produtos=""

        valorT=0

        for x in range(len(Dproduto)):
            linhap=Dproduto[x]
            produtos=produtos+"ID:"+str(linhap[0])+" Produto:"+str(linhap[1])+" X "+str(ddq[x]) + " ="+str(float(int(ddq[x])*float(linhap[2])))+"\n"

            valorT=+ float(int(ddq[x])*float(linhap[2]))

        time="Dia:"+str(datetime.now().day)+"/"+str(datetime.now().month)+" Hora:"+str(datetime.now().hour)+":"+str(datetime.now().minute)+"."
                                                                    #Aqui muda.....................(ja arrumei)..........................................##
        linha=str(NAtual)+"/o/"+ddC[0]+"/o/"+ddC[1]+"/o/"+produtos.replace("\n","/")+"/O/"+time

        Relatorio=open("RelatorioVendas.txt","r").read().split("\n")

        RelatorioN=open("RelatorioVendas.txt","w")
        for x in Relatorio:
            RelatorioN.write(x+"\n")
        RelatorioN.write(linha)
        RelatorioN.close()

        saida=open("Venda"+str(NAtual)+".txt","w")
        saida.write("Sad Vendas:\n")
        saida.write("Sad Codes®\n")
        saida.write("Venda Número: "+str(NAtual)+"\n")
        saida.write("Nome: "+ddC[0])
        saida.write(" Cpf: "+ddC[1]+"\n")
        #produto
        #saida.write("Codigo: "+ddV[0]+" "+Dproduto[1][1]+" X "+ddV[1]+"\n")
        saida.write(produtos)
        saida.write("Valor total: R$"+str(round(valorT,2))+"\n")
        saida.write("Data: "+ time+"\n")
        saida.write("Obrigado pela compra\n")
        saida.write("-------------------------------------------------------------------------------------------------")
        saida.close()

'''
d=input("Digite 1 para continuar")
if d == "1":
    produto=["789654","Maça","2.65","Fruta"]
    Produtos.ChecarPasta(None)
    Produtos.Cadastrar(produto)

    print("Agora sim o bixo vai ....")

    vendas.checarVendas(None)
    d=["789654","50"]
    f=["Marlon","123456789-5"]
    vendas.relatorio(d,f)


### Aqui para baixo, nao conta
print("teste muito bom e estruturado")
f=input("Digite 1 para clientes e 2 para produtos")
if f =="1":
    g=input("Digite 1 para Cadastro e 2 para consulta")
    if g =="1":
        dados=[]
        for x in range(7):
            dados.append(input("Digite um valor referente a :"+str(x)))
        print(dados)
        Clientes.Cadastrar(dados)
    elif g =="2":
        dados=[]
        dados.append(input("Digite o User:"))
        dados.append(input("Digite a Senha:"))
        print(Clientes.Consultar(dados))
elif f == "2":
    g=input("Digite 1 para Cadastro e 2 para consulta")
    if g =="1":
        dados=[]
        for x in range(4):
            dados.append(input("Digite um valor referente a :"+str(x)))
        Produtos.Cadastrar(dados)
    elif g =="2":
        dados=[]
        dados.append(input("Digite o id:"))
        print(Produtos.Consultar(dados))
        
'''
## Versao 1.8
