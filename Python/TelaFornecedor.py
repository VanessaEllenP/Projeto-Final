#Equipe: Vanessa Ellen Paixão, Aislan Silva de Jesus, Icaro Dantas e Kaique Conceição

import tkinter as tk
from tkinter import ttk, messagebox

# Lista para armazenar os dados dos fornecedores
fornecedores = []

def abrir_tela_fornecedor():
    # Configuração da interface
    janela = tk.Toplevel()
    janela.title("Gerenciamento de Fornecedores")
    janela.geometry("900x900")
    janela.configure(bg="#121212")
    janela.resizable(False, False)

    # Título no topo
    titulo = tk.Label(janela, text="Gerenciamento de Fornecedores", font=("Arial", 20, "bold"), fg="white", bg="#121212")
    titulo.pack(pady=20)

    # Funções do CRUD
    def adicionar_fornecedor():
        fornecedor = {
            "nome": entry_nome.get(),
            "cnpj": entry_cnpj.get(),
            "razao_social": entry_razao_social.get(),
            "segmento": entry_segmento.get(),
            "email": entry_email.get(),
            "telefone": entry_telefone.get(),
            "celular": entry_celular.get(),
            "logradouro": entry_logradouro.get(),
            "numero": entry_numero.get(),
            "bairro": entry_bairro.get(),
            "cidade": entry_cidade.get(),
            "uf": entry_uf.get(),
            "cep": entry_cep.get(),
            "complemento": entry_complemento.get()
        }
        if not fornecedor["nome"] or not fornecedor["cnpj"]:
            messagebox.showwarning("Erro", "Os campos Nome e CNPJ são obrigatórios!")
            return
        fornecedores.append(fornecedor)
        limpar_campos()
        messagebox.showinfo("Sucesso", "Fornecedor adicionado com sucesso!")

    def atualizar_fornecedor():
        selecionado = tabela_detalhes.selection()
        if selecionado:
            index = tabela_detalhes.index(selecionado)
            fornecedores[index] = {
                "nome": entry_nome.get(),
                "cnpj": entry_cnpj.get(),
                "razao_social": entry_razao_social.get(),
                "segmento": entry_segmento.get(),
                "email": entry_email.get(),
                "telefone": entry_telefone.get(),
                "celular": entry_celular.get(),
                "logradouro": entry_logradouro.get(),
                "numero": entry_numero.get(),
                "bairro": entry_bairro.get(),
                "cidade": entry_cidade.get(),
                "uf": entry_uf.get(),
                "cep": entry_cep.get(),
                "complemento": entry_complemento.get()
            }
            limpar_campos()
            messagebox.showinfo("Sucesso", "Fornecedor atualizado com sucesso!")
            visualizar_fornecedores()
        else:
            messagebox.showwarning("Erro", "Nenhum fornecedor selecionado!")

    def excluir_fornecedor():
        selecionado = tabela_detalhes.selection()
        if selecionado:
            index = tabela_detalhes.index(selecionado)
            del fornecedores[index]
            limpar_campos()
            messagebox.showinfo("Sucesso", "Fornecedor excluído com sucesso!")
            visualizar_fornecedores()
        else:
            messagebox.showwarning("Erro", "Nenhum fornecedor selecionado!")

    def visualizar_fornecedores():
        # Limpa a tabela antes de adicionar os dados
        tabela_detalhes.delete(*tabela_detalhes.get_children())
        for fornecedor in fornecedores:
            tabela_detalhes.insert("", tk.END, values=(
                fornecedor["nome"], fornecedor["cnpj"], fornecedor["razao_social"], fornecedor["segmento"],
                fornecedor["email"], fornecedor["telefone"], fornecedor["celular"],
                fornecedor["logradouro"], fornecedor["numero"], fornecedor["bairro"], fornecedor["cidade"],
                fornecedor["uf"], fornecedor["cep"], fornecedor["complemento"]
            ))

    def preencher_campos(event):
        selecionado = tabela_detalhes.selection()
        if selecionado:
            index = tabela_detalhes.index(selecionado)
            fornecedor = fornecedores[index]
            entry_nome.delete(0, tk.END)
            entry_nome.insert(0, fornecedor["nome"])
            entry_cnpj.delete(0, tk.END)
            entry_cnpj.insert(0, fornecedor["cnpj"])
            entry_razao_social.delete(0, tk.END)
            entry_razao_social.insert(0, fornecedor["razao_social"])
            entry_segmento.delete(0, tk.END)
            entry_segmento.insert(0, fornecedor["segmento"])
            entry_email.delete(0, tk.END)
            entry_email.insert(0, fornecedor["email"])
            entry_telefone.delete(0, tk.END)
            entry_telefone.insert(0, fornecedor["telefone"])
            entry_celular.delete(0, tk.END)
            entry_celular.insert(0, fornecedor["celular"])
            entry_logradouro.delete(0, tk.END)
            entry_logradouro.insert(0, fornecedor["logradouro"])
            entry_numero.delete(0, tk.END)
            entry_numero.insert(0, fornecedor["numero"])
            entry_bairro.delete(0, tk.END)
            entry_bairro.insert(0, fornecedor["bairro"])
            entry_cidade.delete(0, tk.END)
            entry_cidade.insert(0, fornecedor["cidade"])
            entry_uf.delete(0, tk.END)
            entry_uf.insert(0, fornecedor["uf"])
            entry_cep.delete(0, tk.END)
            entry_cep.insert(0, fornecedor["cep"])
            entry_complemento.delete(0, tk.END)
            entry_complemento.insert(0, fornecedor["complemento"])

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

    # Centralizar os elementos
    def centralizar(frame):
        for widget in frame.winfo_children():
            widget.grid_configure(padx=5, pady=5, sticky="w")

    # Campos de entrada
    campos = [
        ("Nome:", "entry_nome"), 
        ("CNPJ:", "entry_cnpj"),
        ("Razão Social:", "entry_razao_social"),
        ("Segmento:", "entry_segmento"),
        ("Email:", "entry_email"),
        ("Telefone:", "entry_telefone"),
        ("Celular:", "entry_celular"),
        ("Logradouro:", "entry_logradouro"),
        ("Número:", "entry_numero"),
        ("Bairro:", "entry_bairro"),
        ("Cidade:", "entry_cidade"),
        ("UF:", "entry_uf"),
        ("CEP:", "entry_cep"),
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
        ("Adicionar", adicionar_fornecedor, "#6A0DAD", "Clique aqui para adicionar um novo fornecedor"),
        ("Atualizar", atualizar_fornecedor, "#FFA500", "Clique aqui para atualizar os dados do fornecedor"),
        ("Excluir", excluir_fornecedor, "#FF1744", "Clique aqui para excluir um fornecedor"),
        ("Visualizar", visualizar_fornecedores, "#00C853", "Clique aqui para visualizar os fornecedores")
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

    # Tabela para exibir os fornecedores
    frame_tabela = tk.Frame(janela, bg="#121212")
    frame_tabela.pack(pady=20, fill=tk.BOTH, expand=True)

    colunas = ["Nome", "CNPJ", "Razão Social", "Segmento", "Email", "Telefone", "Celular",
               "Logradouro", "Número", "Bairro", "Cidade", "UF", "CEP", "Complemento"]

    tabela_detalhes = ttk.Treeview(frame_tabela, columns=colunas, show="headings", height=10)
    tabela_detalhes.pack(fill=tk.BOTH, expand=True)

    for coluna in colunas:
        tabela_detalhes.heading(coluna, text=coluna)
        tabela_detalhes.column(coluna, width=30, anchor="center", stretch=True) # Consegue alterar a largura das colunas

    tabela_detalhes.bind("<ButtonRelease-1>", preencher_campos)

    visualizar_fornecedores()

    janela.mainloop()
