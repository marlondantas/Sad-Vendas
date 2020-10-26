''' By: Sad Codes® '''

import tkinter
from tkinter import *
import tkinter as tk
from tkinter import ttk
import blick
import time

root = tk.Tk()

blick.Produtos.ChecarPasta(None)
blick.Clientes.Checarpasta(None)
blick.vendas.checarVendas(None)

T = "640x480"
t = "Sad Vendas"


class login(Frame):
    def __init__(self, master):
        Frame.fontePadrao = ("Arial", "10")
        Frame.d = Frame(master)
        root.iconbitmap('icon.ico')
        Frame.d.pack()

        Frame.e = Frame(master)
        Frame.e["pady"] = 5
        Frame.e.pack()

        Frame.f = Frame(master)
        Frame.f["pady"] = 5
        Frame.f.pack()

        Frame.g = Frame(master)
        Frame.g["pady"] = 5
        Frame.g.pack()

        Frame.titulo = Label(Frame.d, text="Faça Login")
        Frame.titulo["font"] = ("Arial", "12", "bold")
        Frame.titulo.pack()

        Frame.userLabel = Label(Frame.e, text="                  Usuário:", font=Frame.fontePadrao)
        Frame.userLabel.pack(side=LEFT)

        Frame.user = Entry(Frame.e)
        Frame.user["width"] = 25
        Frame.user["font"] = Frame.fontePadrao
        Frame.user.pack(side=LEFT)

        Frame.senhaLabel = Label(Frame.f, text="                    Senha:", font=Frame.fontePadrao)
        Frame.senhaLabel.pack(side=LEFT)

        Frame.senha = Entry(Frame.f)
        Frame.senha["width"] = 25
        Frame.senha["font"] = Frame.fontePadrao
        Frame.senha["show"] = "*"
        Frame.senha.pack(side=LEFT)

        Frame.esp = Label(Frame.g, text="                                            ")
        Frame.esp["font"] = ("Arial", "12", "bold")
        Frame.esp.pack(side=LEFT)

        Frame.autenticar = Button(Frame.g)
        Frame.autenticar["text"] = "Entrar"
        Frame.autenticar["font"] = ("Calibri", "10")
        Frame.autenticar["width"] = 12
        Frame.autenticar["bg"] = "black"
        Frame.autenticar["fg"] = "white"
        Frame.autenticar.bind("<Button-1>", self.Checar)
        Frame.autenticar.pack()

        Frame.__init__(self, master)
    def Checar(self, event):
        print("Checando....")
        D = hellocallback0()
        if D[0] == "" or D[1] == "":
            top = Toplevel()
            top.title("INFO")
            top.iconbitmap('icon.ico')
            top.geometry("200x100")

            msg = Message(top, text="Os campos estão em branco!")
            msg["font"] = ("Arial", 10, "bold")
            msg["fg"] = "red"
            msg.pack()

            button = Button(top, text="OK", command=top.destroy)
            button["bg"] = "black"
            button["fg"] = "white"
            button.pack()
            return

        d = (blick.Clientes.Consultar(list(D))[0])
        print(d)

        if d == "Sucesso":
            print("Button is pressed")
            self.newWindow = tk.Toplevel(self.master)
            self.app = abriropcao(self.newWindow)

            print(loginouregist())

            self.master.withdraw()
        else:
            top = Toplevel()
            top.title("INFO")
            top.iconbitmap('icon.ico')
            top.geometry("200x110")

            msg = Message(top, text="Usuário e/ou senha incorretos!")
            msg["font"] = ("Arial", 10, "bold")
            msg["fg"] = "red"
            msg.pack()

            button = Button(top, text="OK", command=top.destroy)
            button["bg"] = "black"
            button["fg"] = "white"
            button.pack()


class registar(Frame):
    def __init__(self, master):
        Frame.fontePadrao = ("Arial", "10")
        Frame.h = Frame(master)
        Frame.h["pady"] = 1
        Frame.h.pack()

        Frame.i = Frame(master)
        Frame.i["pady"] = 5
        Frame.i.pack()

        Frame.j = Frame(master)
        Frame.j["pady"] = 5
        Frame.j.pack()

        Frame.k = Frame(master)
        Frame.k["pady"] = 5
        Frame.k.pack()

        Frame.l = Frame(master)
        Frame.l["pady"] = 5
        Frame.l.pack()

        Frame.m = Frame(master)
        Frame.m["pady"] = 5
        Frame.m.pack()

        Frame.n = Frame(master)
        Frame.n["pady"] = 5
        Frame.n.pack()

        Frame.o = Frame(master)
        Frame.o["pady"] = 5
        Frame.o.pack()

        Frame.p = Frame(master)
        Frame.p["pady"] = 5
        Frame.p.pack()

        Frame.titulo2 = Label(Frame.h, text=" ○●○●○●○●○●○●○●○●○●○ ou cadastre-se ○●○●○●○●○●○●○●○●○●○ ")
        Frame.titulo2["font"] = ("Arial", "12", "bold")
        Frame.titulo2.pack()

        Frame.user2Label = Label(Frame.i, text="                  Usuário:", font=Frame.fontePadrao)
        Frame.user2Label.pack(side=LEFT)

        Frame.user2 = Entry(Frame.i)
        Frame.user2["width"] = 25
        Frame.user2["font"] = Frame.fontePadrao
        Frame.user2.pack(side=LEFT)

        Frame.senha2Label = Label(Frame.j, text="                    Senha:", font=Frame.fontePadrao)
        Frame.senha2Label.pack(side=LEFT)

        Frame.senha2 = Entry(Frame.j)
        Frame.senha2["width"] = 25
        Frame.senha2["font"] = Frame.fontePadrao
        Frame.senha2["show"] = "*"
        Frame.senha2.pack(side=LEFT)

        Frame.emailLabel = Label(Frame.k, text="                     Email:", font=Frame.fontePadrao)
        Frame.emailLabel.pack(side=LEFT)

        Frame.email = Entry(Frame.k)
        Frame.email["width"] = 25
        Frame.email["font"] = Frame.fontePadrao
        Frame.email.pack(side=LEFT)

        Frame.cpflabel = Label(Frame.l, text="                       CPF:", font=Frame.fontePadrao)
        Frame.cpflabel.pack(side=LEFT)

        Frame.cpf = Entry(Frame.l)
        Frame.cpf["width"] = 25
        Frame.cpf["font"] = Frame.fontePadrao
        Frame.cpf.pack(side=LEFT)

        Frame.nomelabel = Label(Frame.m, text="      Nome Completo:", font=Frame.fontePadrao)
        Frame.nomelabel.pack(side=LEFT)

        Frame.nome = Entry(Frame.m)
        Frame.nome["width"] = 25
        Frame.nome["font"] = Frame.fontePadrao
        Frame.nome.pack(side=LEFT)

        Frame.datalabel = Label(Frame.n, text="Data de Nascimento:", font=Frame.fontePadrao)
        Frame.datalabel.pack(side=LEFT)

        Frame.data = Entry(Frame.n)
        Frame.data["width"] = 25
        Frame.data["font"] = Frame.fontePadrao
        Frame.data.pack(side=LEFT)

        Frame.telefonelabel = Label(Frame.o, text="                 Telefone:", font=Frame.fontePadrao)
        Frame.telefonelabel.pack(side=LEFT)

        Frame.telefone = Entry(Frame.o)
        Frame.telefone["width"] = 25
        Frame.telefone["font"] = Frame.fontePadrao
        Frame.telefone.pack(side=LEFT)

        Frame.esp = Label(Frame.p, text="                                          ")
        Frame.esp["font"] = ("Arial", "12", "bold")
        Frame.esp.pack(side=LEFT)

        Frame.autenticar2 = Button(Frame.p)
        Frame.autenticar2["text"] = "Cadastrar"
        Frame.autenticar2["font"] = ("Calibri", "10")
        Frame.autenticar2["bg"] = "black"
        Frame.autenticar2["fg"] = "white"
        Frame.autenticar2["width"] = 12
        Frame.autenticar2.bind("<Button-1>", self.Cadastrar)
        Frame.autenticar2.pack(side=RIGHT)

        Frame.mensagem = Label(Frame.p, text="", font=Frame.fontePadrao)
        Frame.mensagem.pack()

        Frame.__init__(self, master)

    def Cadastrar(self, event):
        print("Cadastro...")
        D = hellocallback1()

        print(D)

        for x in D:
            if x == "":
                top = Toplevel()
                top.iconbitmap('icon.ico')
                top.geometry("200x100")
                top.title("INFO")

                msg = Message(top, text="Um campo está em branco!")
                msg["font"] = ("Arial", 10, "bold")
                msg["fg"] = "red"
                msg.pack()

                button = Button(top, text=" OK ", command=top.destroy)
                button["bg"] = "black"
                button["fg"] = "white"
                button.pack()
                return

        d = blick.Clientes.Cadastrar(list(D))
        if d == "Cadastrado":
            top = Toplevel()
            top.title("INFO")
            top.iconbitmap('icon.ico')
            top.geometry("200x100")

            msg = Message(top, text="Cadastrado com sucesso!")
            msg["font"] = ("Arial", 10, "bold")
            msg.pack()

            button = Button(top, text=" OK ", command=top.destroy)
            button["bg"] = "black"
            button["fg"] = "white"
            button.pack()
            print("Button is pressed")

            self.newWindow = tk.Toplevel(self.master)
            self.app = abriropcao(self.newWindow)

            print(loginouregist())

            self.master.withdraw()

class logiERig():
    def __init__(self, master):
        self.master = master
        self.frame = tk.Frame(master)

        master.title(t + " / Clientes")
        master.iconbitmap('icon.ico')

        login(master)
        registar(master)


def loginouregist():
    if Frame.user2.get() != "":
        print("register")
        return (Frame.user2.get(), Frame.senha2.get())
    elif Frame.user.get() != "":
        print("login")
        return (Frame.user.get(), Frame.senha.get())



def BB():
    print("Iniciando consulta")

    file = open("Produtos.txt", "r").read().split("\n")
    dadosC = []

    for x in range(4, len(file)):
        dadosC.append(file[x].split("/o/"))

    return dadosC


class VendasP(tkinter.Frame):
    def __init__(self, master=None, **kw):
        super().__init__(master, **kw)
        Frame.fontePadrao = ("Arial", "10")
        Frame.b = Frame(master)
        Frame.b["pady"] = 5
        Frame.b.pack()

        Frame.pd = Button(Frame.b)
        Frame.pd["text"] = "Comprar"
        Frame.pd["width"] = 10
        Frame.pd["fg"] = 'white'
        Frame.pd["bg"] = 'black'
        Frame.pd["font"] = Frame.fontePadrao
        Frame.pd["command"] = self.compra
        Frame.pd.pack(side=LEFT)

        Frame.esp = Label(Frame.b)
        Frame.esp["text"] = "           "
        Frame.esp["font"] = Frame.fontePadrao
        Frame.esp.pack(side=LEFT)

        Frame.pd2 = Button(Frame.b)
        Frame.pd2["text"] = "Voltar"
        Frame.pd2["width"] = 10
        Frame.pd2["fg"] = 'white'
        Frame.pd2["bg"] = 'black'
        Frame.pd2["font"] = Frame.fontePadrao
        Frame.pd2["command"] = self.voltar
        Frame.pd2.pack(side=LEFT)

        Frame.__init__(self, master)

        Frame.tree = ttk.Treeview(self.master)
        Frame.tree["columns"] = ["one", "two", "three"]
        Frame.tree.heading("#0", text="ID")
        Frame.tree.heading("#1", text="Produtos")
        Frame.tree.heading("#2", text="Categoria")
        Frame.tree.heading("#3", text="Preço")
        Frame.tree.column("one", width=146, stretch=tkinter.YES)
        Frame.tree.column("two", width=146, stretch=tkinter.YES)
        Frame.tree.column("three", width=146, stretch=tkinter.YES)
        Frame.tree.pack()

        D = BB()
        for x in D:
            Frame.tree.insert("", END, text=x[0], values=(x[1], x[3], x[2]))

    def voltar(self):
        print("Button is pressed, voltar")
        self.newWindow = tk.Toplevel(self.master)
        self.app = abriropcao(self.newWindow)

        self.master.withdraw()



    def compra(self):

        test = self.tree.item(self.tree.selection())
        print(test["text"], test["values"][0], test["values"][2])


        print("Button is pressed")
        self.newWindow = tk.Toplevel(self.master)
        self.app = abrirCarinho(self.newWindow)


class carrinho(Frame):
    def __init__(self, master=None, **kw):

        super().__init__(master, **kw)
        Frame.fontePadrao = ("Arial", "10", "bold")
        Frame.f = Frame(master)
        Frame.f["pady"] = 5
        Frame.f.pack()

        Frame.r = Frame(master)
        Frame.r["pady"] = 5
        Frame.r.pack()

        Frame.y = Frame(master)
        Frame.y["pady"] = 5
        Frame.y.pack()

        Frame.t = Frame(master)
        Frame.t["pady"] = 5
        Frame.t.pack()

        f = loginouregist()
        dezinho = blick.Clientes.Consultar(f)[1]
        print("Register .", dezinho)
        # ---()----

        Frame.nome = Label(Frame.f, text=("Nome: " + dezinho[0]), font=Frame.fontePadrao)
        Frame.nome.pack(side=LEFT)
        Frame.cpf = Label(Frame.f, text=("CPF: " + dezinho[1]), font=Frame.fontePadrao)
        Frame.cpf.pack(side=RIGHT)


        test = self.tree.item(self.tree.selection())
        jf = [test["text"], test["values"][0], test["values"][2]]
        print(jf)


        Frame.produto = Label(Frame.r, text=("Codigo: " + str(jf[0]) + " Produto:" + str(jf[1])), font=Frame.fontePadrao)
        Frame.produto.pack()

        Frame.txtQua = Label(Frame.y, text=("Quantidade:"), font=Frame.fontePadrao)
        Frame.txtQua.pack(side=LEFT)

        Frame.quantidae = Entry(Frame.y)
        Frame.quantidae["font"] = Frame.fontePadrao
        Frame.quantidae["width"] = 10
        Frame.quantidae.pack(side=RIGHT)

        Frame.pd = Button(Frame.t, text="Finalizar", font=Frame.fontePadrao)
        Frame.pd["width"] = 10
        Frame.pd["fg"] = 'white'
        Frame.pd["bg"] = 'black'
        Frame.pd["command"] = self.FinalizarC
        Frame.pd.pack(side=LEFT)

        Frame.__init__(self, master)

    def FinalizarC(self):
        print("Finalizar a Compra...")

        f = loginouregist()
        dezinho = blick.Clientes.Consultar(f)[1]

        blick.vendas.relatorio("1", str(self.tree.item(self.tree.selection())["text"]), str(Frame.quantidae.get()),
                               [dezinho[0], dezinho[1]])

        print("Sucesso.")

        self.master.withdraw()


class abrirvendasP():
    def __init__(self, master):
        self.master = master
        self.frame = tkinter.Frame(master)
        master.title("Sad Vendas / Lista de produtos")
        master.iconbitmap('icon.ico')

        VendasP(master)


class abrirCarinho():
    def __init__(self, master):
        self.master = master
        self.frame = tk.Frame(master)
        master.title("Sad Vendas / Carinho de compras")
        master.iconbitmap('icon.ico')

        carrinho(master)



class abriropcao():
    def __init__(self, master):
        self.master = master
        self.frame = tk.Frame(master)
        master.title(t + " /Opções")
        master.iconbitmap('icon.ico')

        Opecao(master)


class Opecao(Frame):
    def __init__(self, master, **kw):
        super().__init__(master, **kw)
        self.ent = None
        Frame.fontePadrao = ("Arial", "10")
        Frame.a = Frame(master)
        Frame.a["pady"] = 5
        Frame.a.pack()

        Frame.b = Frame(master)
        Frame.b["pady"] = 5
        Frame.b.pack()

        Frame.c = Frame(master)
        Frame.c["pady"] = 5
        Frame.c.pack()

        Frame.d = Frame(master)
        Frame.d["pady"] = 5
        Frame.d.pack()

        Frame.titulo = Label(Frame.a, text="Escolha uma opção:")
        Frame.titulo["font"] = ("Arial", "22", "bold")
        Frame.titulo.pack()

        Frame.prod = Button(Frame.b)
        Frame.prod["text"] = "Cadastrar Produtos"
        Frame.prod["font"] = ("Calibri", "10")
        Frame.prod["bg"] = "black"
        Frame.prod["fg"] = "white"
        Frame.prod["width"] = 20
        Frame.prod["command"] = self.Cadastro
        Frame.prod.pack()

        Frame.comp = Button(Frame.c)
        Frame.comp["text"] = "Comprar"
        Frame.comp["font"] = ("Calibri", "10")
        Frame.comp["bg"] = "black"
        Frame.comp["fg"] = "white"
        Frame.comp["width"] = 20
        Frame.comp["command"] = self.Compra
        Frame.comp.pack()

        Frame.sai = Button(Frame.d)
        Frame.sai["text"] = "Sair"
        Frame.sai["font"] = ("Calibri", "10")
        Frame.sai["bg"] = "black"
        Frame.sai["fg"] = "white"
        Frame.sai["width"] = 20
        Frame.sai["command"] = self.quit
        Frame.sai.pack()

    def Cadastro(self):
        print("Button is pressed, Cadastro")
        self.newWindow = tk.Toplevel(self.master)
        self.app = abrirCadastro(self.newWindow)

        self.master.withdraw()

    def Compra(self):
        print("Button is pressed B")
        self.newWindow = tk.Toplevel(self.master)
        self.app = abrirvendasP(self.newWindow)

        self.master.withdraw()



class abrirCadastro():
    def __init__(self, master):
        self.master = master
        self.frame = tk.Frame(master)
        master.title(t + " /Opções/ Cadastro")
        master.iconbitmap('icon.ico')
        master.geometry("400x250")

        CadastroP.Produtos(master)


class CadastroP(Frame):
    class Produtos(Frame):
        def __init__(self, master):
            Frame.fontePadrao = ("Arial", "10")
            Frame.a = Frame(master)
            Frame.a["pady"] = 5
            Frame.a.pack()

            Frame.b = Frame(master)
            Frame.b["pady"] = 5
            Frame.b.pack()

            Frame.c = Frame(master)
            Frame.c["pady"] = 5
            Frame.c.pack()

            Frame.d = Frame(master)
            Frame.d["pady"] = 5
            Frame.d.pack()

            Frame.e = Frame(master)
            Frame.e["pady"] = 5
            Frame.e.pack()

            Frame.f = Frame(master)
            Frame.f["pady"] = 5
            Frame.f.pack()

            Frame.titulo = Label(Frame.a, text="Cadastre seu Sad Produto")
            Frame.titulo["font"] = ("Arial", "12", "bold")
            Frame.titulo.pack()

            Frame.idLabel = Label(Frame.b, text="           ID:", font=Frame.fontePadrao)
            Frame.idLabel.pack(side=LEFT)

            Frame.id = Entry(Frame.b)
            Frame.id["width"] = 25
            Frame.id["font"] = Frame.fontePadrao
            Frame.id.pack(side=LEFT)

            Frame.produtoLabel = Label(Frame.c, text="   Produto:", font=Frame.fontePadrao)
            Frame.produtoLabel.pack(side=LEFT)

            Frame.produto = Entry(Frame.c)
            Frame.produto["width"] = 25
            Frame.produto["font"] = Frame.fontePadrao
            Frame.produto.pack(side=LEFT)

            Frame.categoriaLabel = Label(Frame.d, text="Categoria:", font=Frame.fontePadrao)
            Frame.categoriaLabel.pack(side=LEFT)

            Frame.categoria = Entry(Frame.d)
            Frame.categoria["width"] = 25
            Frame.categoria["font"] = Frame.fontePadrao
            Frame.categoria.pack(side=LEFT)

            Frame.precoLabel = Label(Frame.e, text="     Preço:", font=Frame.fontePadrao)
            Frame.precoLabel.pack(side=LEFT)

            Frame.preco = Entry(Frame.e)
            Frame.preco["width"] = 25
            Frame.preco["font"] = Frame.fontePadrao
            Frame.preco.pack(side=LEFT)

            Frame.precoLabel = Label(Frame.f, text="          ", font=Frame.fontePadrao)
            Frame.precoLabel.pack(side=LEFT)

            Frame.autenticar1 = Button(Frame.f)
            Frame.autenticar1["text"] = "Voltar"
            Frame.autenticar1["font"] = ("Calibri", "10")
            Frame.autenticar1["width"] = 12
            Frame.autenticar1["fg"] = "white"
            Frame.autenticar1["bg"] = "black"
            Frame.autenticar1["command"] = self.voltar2
            Frame.autenticar1.pack(side=RIGHT)

            Frame.precoLabel = Label(Frame.f, text="   ", font=Frame.fontePadrao)
            Frame.precoLabel.pack(side=RIGHT)

            Frame.autenticar = Button(Frame.f)
            Frame.autenticar["text"] = "Cadastrar"
            Frame.autenticar["font"] = ("Calibri", "10")
            Frame.autenticar["width"] = 12
            Frame.autenticar["fg"] = "white"
            Frame.autenticar["bg"] = "black"
            Frame.autenticar.bind("<Button-1>", self.cadastrarP)
            Frame.autenticar.pack(side=LEFT)

            Frame.__init__(self, master)

        def cadastrarP(self, event):
            D = helloback3()
            print(D)
            if D == 0:
                print("Erro na captação de dados,")
                return 0

            for x in D:
                if x == "" or x == " ":
                    print("Campo(S) em branco")
                    return 0

            d = blick.Produtos.Cadastrar(list(D))
            if d == "Produto Registrado":
                print("Button is pressed")
                self.newWindow = tk.Toplevel(self.master)
                self.app = abriropcao(self.newWindow)

                self.master.withdraw()

        def voltar2(self):
            print("Button is pressed, voltar")
            self.newWindow = tk.Toplevel(self.master)
            self.app = abriropcao(self.newWindow)

            self.master.withdraw()


def hellocallback0():
    print("Consultando....")
    usuario = Frame.user.get()
    senha = Frame.senha.get()

    return usuario, senha


def hellocallback1():
    usuario = Frame.user2.get()
    senha = Frame.senha2.get()
    email = Frame.email.get()
    cpf = Frame.cpf.get()
    nome = Frame.nome.get()
    data = Frame.data.get()
    telefone = Frame.telefone.get()

    return nome, cpf, email, usuario, senha, data, telefone


def helloback3():
    produto = Frame.produto.get()
    preco = Frame.preco.get()
    id = Frame.id.get()
    categoria = Frame.categoria.get()
    try:
        try:
            str(preco).replace(",", ".")
        except:
            pass

        preco = float(preco)
    except:
        print("preco não é int")
        return 0

    return id, produto, str(preco), categoria



class entradaC(Frame):
    imagem = PhotoImage(file="sad.png")
    w = Label(root, image=imagem)
    w.imagem = imagem
    w.pack()

    def __init__(self, master=None, **kw):
        super().__init__(master, **kw)
        self.ent = None
        Frame.fontePadrao = ("Arial", "10")
        Frame.a = Frame(master)
        Frame.a["pady"] = 5
        Frame.a.pack()

        Frame.b = Frame(master)
        Frame.b["pady"] = 5
        Frame.b.pack()

        Frame.c = Frame(master)
        Frame.c["pady"] = 5
        Frame.c.pack()

        Frame.titulo = Label(Frame.a, text="Bem-vindo a Sad Vendas!")
        Frame.titulo["font"] = ("Arial", "30", "bold")
        Frame.titulo.pack()

        Frame.desc = Label(Frame.b,
                           text="Sad Vendas é uma loja virtual onde os usuários podem vender\n e comprar produtos de forma rápida e 'segura'.",
                           font=Frame.fontePadrao)
        Frame.desc["font"] = ("Arial", "12", "italic")
        Frame.desc.pack()

        Frame.ent = Button(Frame.c)
        Frame.ent["text"] = "Entrar"
        Frame.ent["font"] = ("Calibri", "10")
        Frame.ent["command"] = self.Login
        Frame.ent["bg"] = "black"
        Frame.ent["fg"] = "white"
        Frame.ent["width"] = 12
        Frame.ent.pack(side=LEFT)

        Frame.esp = Label(Frame.c, text="      ")
        Frame.esp["font"] = ("Arial", "30", "bold")
        Frame.esp.pack(side=LEFT)

        Frame.sai = Button(Frame.c)
        Frame.sai["text"] = "Sair"
        Frame.sai["font"] = ("Calibri", "10")
        Frame.sai["bg"] = "black"
        Frame.sai["fg"] = "white"
        Frame.sai["width"] = 12
        Frame.sai["command"] = self.quit
        Frame.sai.pack(side=RIGHT)

    def Login(self):
        print('Button is pressed!')
        self.newWindow = tk.Toplevel(self.master)
        self.app = logiERig(self.newWindow)



root.title(t)
root.geometry(T)
root.iconbitmap('icon.ico')

cls = entradaC(root)

root.mainloop()

