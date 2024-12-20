#Equipe: Vanessa Ellen Paixão, Aislan Silva de Jesus, Icaro Dantas e Kaique Conceição

import tkinter as tk
from tkinter import ttk, messagebox

# Lista para armazenar os dados dos funcionários
funcionarios = []

def abrir_tela_funcionario():
    # Configuração da interface
    janela = tk.Tk()
    janela.title("Gerenciamento de Funcionários")
    janela.geometry("900x800")
    janela.configure(bg="#121212")
    janela.resizable(False, False)

    # Título no topo
    titulo = tk.Label(janela, text="Gerenciamento de Funcionários", font=("Arial", 20, "bold"), fg="white", bg="#121212")
    titulo.pack(pady=20)

    # Funções do CRUD
    def adicionar_funcionario():
        funcionario = {
            "nome": entry_nome.get(),
            "cpf": entry_cpf.get(),
            "cargo": entry_cargo.get(),
            "telefone": entry_telefone.get(),
            "celular": entry_celular.get(),
            "email": entry_email.get(),
            "rua": entry_rua.get(),
            "numero": entry_numero.get(),
            "bairro": entry_bairro.get(),
            "cidade": entry_cidade.get(),
            "estado": entry_estado.get(),
            "cep": entry_cep.get(),
            "complemento": entry_complemento.get()
        }
        if not funcionario["nome"] or not funcionario["cpf"]:
            messagebox.showwarning("Erro", "Os campos Nome e CPF são obrigatórios!")
            return
        funcionarios.append(funcionario)
        limpar_campos()
        messagebox.showinfo("Sucesso", "Funcionário adicionado com sucesso!")

    def atualizar_funcionario():
        selecionado = tabela_detalhes.selection()
        if selecionado:
            index = tabela_detalhes.index(selecionado)
            funcionarios[index] = {
                "nome": entry_nome.get(),
                "cpf": entry_cpf.get(),
                "cargo": entry_cargo.get(),
                "telefone": entry_telefone.get(),
                "celular": entry_celular.get(),
                "email": entry_email.get(),
                "rua": entry_rua.get(),
                "numero": entry_numero.get(),
                "bairro": entry_bairro.get(),
                "cidade": entry_cidade.get(),
                "estado": entry_estado.get(),
                "cep": entry_cep.get(),
                "complemento": entry_complemento.get()
            }
            limpar_campos()
            messagebox.showinfo("Sucesso", "Funcionário atualizado com sucesso!")
            visualizar_funcionarios()
        else:
            messagebox.showwarning("Erro", "Nenhum funcionário selecionado!")

    def excluir_funcionario():
        selecionado = tabela_detalhes.selection()
        if selecionado:
            index = tabela_detalhes.index(selecionado)
            del funcionarios[index]
            limpar_campos()
            messagebox.showinfo("Sucesso", "Funcionário excluído com sucesso!")
            visualizar_funcionarios()
        else:
            messagebox.showwarning("Erro", "Nenhum funcionário selecionado!")

    def visualizar_funcionarios():
        # Limpa a tabela antes de adicionar os dados
        tabela_detalhes.delete(*tabela_detalhes.get_children())
        for funcionario in funcionarios:
            tabela_detalhes.insert("", tk.END, values=(
                funcionario["nome"], funcionario["cpf"], funcionario["email"],
                funcionario["telefone"], funcionario["celular"], funcionario["cep"],
                funcionario["rua"], funcionario["numero"], funcionario["bairro"],
                funcionario["cidade"], funcionario["estado"], funcionario["complemento"]
            ))

    def preencher_campos(event):
        selecionado = tabela_detalhes.selection()
        if selecionado:
            index = tabela_detalhes.index(selecionado)
            funcionario = funcionarios[index]
            entry_nome.delete(0, tk.END)
            entry_nome.insert(0, funcionario["nome"])
            entry_cpf.delete(0, tk.END)
            entry_cpf.insert(0, funcionario["cpf"])
            entry_cargo.delete(0, tk.END)
            entry_cargo.insert(0, funcionario["cargo"])
            entry_telefone.delete(0, tk.END)
            entry_telefone.insert(0, funcionario["telefone"])
            entry_celular.delete(0, tk.END)
            entry_celular.insert(0, funcionario["celular"])
            entry_email.delete(0, tk.END)
            entry_email.insert(0, funcionario["email"])
            entry_rua.delete(0, tk.END)
            entry_rua.insert(0, funcionario["rua"])
            entry_numero.delete(0, tk.END)
            entry_numero.insert(0, funcionario["numero"])
            entry_bairro.delete(0, tk.END)
            entry_bairro.insert(0, funcionario["bairro"])
            entry_cidade.delete(0, tk.END)
            entry_cidade.insert(0, funcionario["cidade"])
            entry_estado.delete(0, tk.END)
            entry_estado.insert(0, funcionario["estado"])
            entry_cep.delete(0, tk.END)
            entry_cep.insert(0, funcionario["cep"])
            entry_complemento.delete(0, tk.END)
            entry_complemento.insert(0, funcionario["complemento"])

    def limpar_campos():
        for entry in entries:
            entry.delete(0, tk.END)

    # Função para exibir tooltip
    def mostrar_tooltip(event, texto):
        tooltip = tk.Label(janela, text=texto, fg="white", bg="#333333", font=("Arial", 10), relief="solid", padx=5, pady=5)
        tooltip.place(x=400, y=580)  # Coordenadas fixas (ajuste os valores conforme necessário)
        return tooltip


    def esconder_tooltip(tooltip):
        tooltip.destroy()

    # Centralizar os elementos
    def centralizar(frame):
        for widget in frame.winfo_children():
            widget.grid_configure(padx=5, pady=5, sticky="w")

    # Campos de entrada
    campos = [
        ("Nome:", "entry_nome"), ("CPF:", "entry_cpf"),
        ("Cargo:", "entry_cargo"), ("Telefone:", "entry_telefone"),
        ("Celular:", "entry_celular"), ("Email:", "entry_email"),
        ("Rua:", "entry_rua"), ("Número:", "entry_numero"),
        ("Bairro:", "entry_bairro"),  # Adicionando campo Bairro
        ("Cidade:", "entry_cidade"), ("Estado:", "entry_estado"),
        ("CEP:", "entry_cep"), ("Complemento:", "entry_complemento")  # Adicionando campo Complemento
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
        ("Adicionar", adicionar_funcionario, "#6A0DAD", "Clique aqui para adicionar um novo funcionário"),
        ("Atualizar", atualizar_funcionario, "#FFA500", "Clique aqui para atualizar os dados de um funcionário"),
        ("Excluir", excluir_funcionario, "#FF1744", "Clique aqui para excluir um funcionário"),
        ("Visualizar", visualizar_funcionarios, "#00C853", "Clique aqui para visualizar os dados dos funcionários")
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

    # Tabela para exibição dos funcionários
    frame_tabela = tk.Frame(janela, bg="#121212")
    frame_tabela.pack(pady=20, fill=tk.BOTH, expand=True)

    colunas = ["Nome", "CPF", "Email", "Telefone", "Celular", "CEP", "Logradouro", "Número", "Bairro", "Cidade", "UF", "Complemento"]
    tabela_detalhes = ttk.Treeview(frame_tabela, columns=colunas, show="headings", height=8)

    for coluna in colunas:
        tabela_detalhes.heading(coluna, text=coluna)
        tabela_detalhes.column(coluna, width=30, anchor="center", stretch=True) # Consegue alterar a largura das colunas

    tabela_detalhes.pack(fill=tk.BOTH, expand=True)

    tabela_detalhes.bind("<ButtonRelease-1>", preencher_campos)

    # Executar a interface
    janela.mainloop()


