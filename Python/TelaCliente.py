#Equipe: Vanessa Ellen Paixão, Aislan Silva de Jesus, Icaro Dantas e Kaique Conceição

import tkinter as tk
from tkinter import ttk, messagebox

# Lista para armazenar os dados dos clientes
clientes = []

def abrir_tela_cliente():
    # Configuração da interface
    janela = tk.Toplevel()
    janela.title("Gerenciamento de Clientes")
    janela.geometry("900x800")
    janela.configure(bg="#121212")
    janela.resizable(False, False)

    # Título no topo
    titulo = tk.Label(janela, text="Gerenciamento de Clientes", font=("Arial", 20, "bold"), fg="white", bg="#121212")
    titulo.pack(pady=20)

    # Funções do CRUD
    def adicionar_cliente():
        cliente = {
            "nome": entry_nome.get(),
            "cpf": entry_cpf.get(),
            "email": entry_email.get(),
            "telefone": entry_telefone.get(),
            "celular": entry_celular.get(),
            "cep": entry_cep.get(),
            "logradouro": entry_logradouro.get(),
            "numero": entry_numero.get(),
            "bairro": entry_bairro.get(),
            "cidade": entry_cidade.get(),
            "uf": entry_uf.get(),
            "complemento": entry_complemento.get()
        }
        if not cliente["nome"] or not cliente["cpf"]:
            messagebox.showwarning("Erro", "Os campos Nome e CPF são obrigatórios!")
            return
        clientes.append(cliente)
        limpar_campos()
        messagebox.showinfo("Sucesso", "Cliente adicionado com sucesso!")

    def atualizar_cliente():
        selecionado = tabela_detalhes.selection()
        if selecionado:
            index = tabela_detalhes.index(selecionado)
            clientes[index] = {
                "nome": entry_nome.get(),
                "cpf": entry_cpf.get(),
                "email": entry_email.get(),
                "telefone": entry_telefone.get(),
                "celular": entry_celular.get(),
                "cep": entry_cep.get(),
                "logradouro": entry_logradouro.get(),
                "numero": entry_numero.get(),
                "bairro": entry_bairro.get(),
                "cidade": entry_cidade.get(),
                "uf": entry_uf.get(),
                "complemento": entry_complemento.get()
            }
            limpar_campos()
            messagebox.showinfo("Sucesso", "Cliente atualizado com sucesso!")
            visualizar_clientes()
        else:
            messagebox.showwarning("Erro", "Nenhum cliente selecionado!")

    def excluir_cliente():
        selecionado = tabela_detalhes.selection()
        if selecionado:
            index = tabela_detalhes.index(selecionado)
            del clientes[index]
            limpar_campos()
            messagebox.showinfo("Sucesso", "Cliente excluído com sucesso!")
            visualizar_clientes()
        else:
            messagebox.showwarning("Erro", "Nenhum cliente selecionado!")

    def visualizar_clientes():
        # Limpa a tabela antes de adicionar os dados
        tabela_detalhes.delete(*tabela_detalhes.get_children())
        for cliente in clientes:
            tabela_detalhes.insert("", tk.END, values=(
                cliente["nome"], cliente["cpf"], cliente["email"], cliente["telefone"],
                cliente["celular"], cliente["cep"], cliente["logradouro"], cliente["numero"], 
                cliente["bairro"], cliente["cidade"], cliente["uf"], cliente["complemento"]
            ))

    def preencher_campos(event):
        selecionado = tabela_detalhes.selection()
        if selecionado:
            index = tabela_detalhes.index(selecionado)
            cliente = clientes[index]
            entry_nome.delete(0, tk.END)
            entry_nome.insert(0, cliente["nome"])
            entry_cpf.delete(0, tk.END)
            entry_cpf.insert(0, cliente["cpf"])
            entry_email.delete(0, tk.END)
            entry_email.insert(0, cliente["email"])
            entry_telefone.delete(0, tk.END)
            entry_telefone.insert(0, cliente["telefone"])
            entry_celular.delete(0, tk.END)
            entry_celular.insert(0, cliente["celular"])
            entry_cep.delete(0, tk.END)
            entry_cep.insert(0, cliente["cep"])
            entry_logradouro.delete(0, tk.END)
            entry_logradouro.insert(0, cliente["logradouro"])
            entry_numero.delete(0, tk.END)
            entry_numero.insert(0, cliente["numero"])
            entry_bairro.delete(0, tk.END)
            entry_bairro.insert(0, cliente["bairro"])
            entry_cidade.delete(0, tk.END)
            entry_cidade.insert(0, cliente["cidade"])
            entry_uf.delete(0, tk.END)
            entry_uf.insert(0, cliente["uf"])
            entry_complemento.delete(0, tk.END)
            entry_complemento.insert(0, cliente["complemento"])

    def limpar_campos():
        for entry in entries:
            entry.delete(0, tk.END)

    # Função para exibir tooltip
    def mostrar_tooltip(event, texto):
        tooltip = tk.Label(janela, text=texto, fg="white", bg="#333333", font=("Arial", 10), relief="solid", padx=5, pady=5)
        tooltip.place(x=400, y=370)  # Coordenadas fixas (ajuste os valores conforme necessário)
        return tooltip


    def esconder_tooltip(tooltip):
        tooltip.destroy()

    # Campos de entrada
    campos = [
        ("Nome:", "entry_nome"),
        ("CPF:", "entry_cpf"),
        ("Email:", "entry_email"),
        ("Telefone:", "entry_telefone"),
        ("Celular:", "entry_celular"),
        ("CEP:", "entry_cep"),
        ("Logradouro:", "entry_logradouro"),
        ("Número:", "entry_numero"),
        ("Bairro:", "entry_bairro"),
        ("Cidade:", "entry_cidade"),
        ("UF:", "entry_uf"),
        ("Complemento:", "entry_complemento")
    ]

    entries = []
    frame_campos = tk.Frame(janela, bg="#121212")
    frame_campos.pack(pady=20)

    for i, (label_text, entry_var) in enumerate(campos):
        label = tk.Label(frame_campos, text=label_text, fg="white", bg="#121212", font=("Arial", 12))
        label.grid(row=i, column=0, padx=5, pady=5, sticky="e")
        entry = tk.Entry(frame_campos, width=30, bg="#1F1F1F", fg="white", font=("Arial", 12))
        entry.grid(row=i, column=1, padx=5, pady=5, sticky="w")
        entries.append(entry)
        globals()[entry_var] = entry

    # Botões
    frame_botoes = tk.Frame(janela, bg="#121212")
    frame_botoes.pack(pady=20)

    botoes = [
        ("Adicionar", adicionar_cliente, "#6A0DAD", "Clique aqui para adicionar um novo cliente"),
        ("Atualizar", atualizar_cliente, "#FFA500", "Clique aqui para atualizar os dados do cliente"),
        ("Excluir", excluir_cliente, "#FF1744", "Clique aqui para excluir um cliente"),
        ("Visualizar", visualizar_clientes, "#00C853", "Clique aqui para visualizar os clientes")
    ]

    tooltips = {}

    for i, (text, command, color, tooltip_text) in enumerate(botoes):
        btn = tk.Button(frame_botoes, text=text, command=command, bg=color, fg="white",
                        font=("Arial", 12), width=12, cursor="hand2", activebackground=color)
        btn.grid(row=0, column=i, padx=10, pady=10)

        # Adiciona evento para mostrar e esconder o tooltip
        def on_enter(event, texto=tooltip_text):
            tooltip = mostrar_tooltip(event, texto)
            tooltips[btn] = tooltip

        def on_leave(event):
            if btn in tooltips:
                esconder_tooltip(tooltips[btn])
                del tooltips[btn]

        btn.bind("<Enter>", on_enter)
        btn.bind("<Leave>", on_leave)

    # Tabela para exibir os clientes
    frame_tabela = tk.Frame(janela, bg="#121212")
    frame_tabela.pack(pady=20, fill=tk.BOTH, expand=True)

    colunas = ["Nome", "CPF", "Email", "Telefone", "Celular", "CEP", "Logradouro", "Número", "Bairro", "Cidade", "UF", "Complemento"]
    tabela_detalhes = ttk.Treeview(frame_tabela, columns=colunas, show="headings", height=8)

    for coluna in colunas:
        tabela_detalhes.heading(coluna, text=coluna)
        tabela_detalhes.column(coluna, width=30, anchor="center", stretch=True) # Consegue alterar a largura das colunas

    tabela_detalhes.pack(fill=tk.BOTH, expand=True)

    tabela_detalhes.bind("<ButtonRelease-1>", preencher_campos)

    visualizar_clientes()

    janela.mainloop()
