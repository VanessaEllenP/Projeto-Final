#Equipe: Vanessa Ellen Paixão, Aislan Silva de Jesus, Icaro Dantas e Kaique Conceição

import tkinter as tk
from tkinter import ttk, messagebox

# Lista para armazenar os dados dos produtos
produtos = []

def abrir_tela_produto():
    # Configuração da interface
    janela = tk.Tk()
    janela.title("Gerenciamento de Produto")
    janela.geometry("900x800")
    janela.configure(bg="#121212")
    janela.resizable(False, False)

    # Título no topo
    titulo = tk.Label(janela, text="Gerenciamento de Produtos", font=("Arial", 20, "bold"), fg="white", bg="#121212")
    titulo.pack(pady=20)

    # Funções do CRUD
    def adicionar_produto():
        produto = {
            "descricao": entry_descricao.get(),
            "validade": entry_validade.get(),
            "segmento": entry_segmento.get(),
            "lote": entry_lote.get(),
            "armazenamento": entry_armazenamento.get(),
            "quantidade": entry_quantidade.get(),
            "fornecedor": entry_fornecedor.get()  # Adicionado id_fornecedor com o nome "fornecedor"
        }
        if not produto["descricao"] or not produto["validade"]:
            messagebox.showwarning("Erro", "Os campos Descrição e Validade são obrigatórios!")
            return
        produtos.append(produto)
        limpar_campos()
        messagebox.showinfo("Sucesso", "Produto adicionado com sucesso!")

    def atualizar_produto():
        selecionado = tabela_detalhes.selection()
        if selecionado:
            index = tabela_detalhes.index(selecionado)
            produtos[index] = {
                "descricao": entry_descricao.get(),
                "validade": entry_validade.get(),
                "segmento": entry_segmento.get(),
                "lote": entry_lote.get(),
                "armazenamento": entry_armazenamento.get(),
                "quantidade": entry_quantidade.get(),
                "fornecedor": entry_fornecedor.get()
            }
            limpar_campos()
            messagebox.showinfo("Sucesso", "Produto atualizado com sucesso!")
            visualizar_produtos()
        else:
            messagebox.showwarning("Erro", "Nenhum produto selecionado!")

    def excluir_produto():
        selecionado = tabela_detalhes.selection()
        if selecionado:
            index = tabela_detalhes.index(selecionado)
            del produtos[index]
            limpar_campos()
            messagebox.showinfo("Sucesso", "Produto excluído com sucesso!")
            visualizar_produtos()
        else:
            messagebox.showwarning("Erro", "Nenhum produto selecionado!")

    def visualizar_produtos():
        # Limpa a tabela antes de adicionar os dados
        tabela_detalhes.delete(*tabela_detalhes.get_children())
        for produto in produtos:
            tabela_detalhes.insert("", tk.END, values=(
                produto["descricao"], produto["validade"], produto["segmento"],
                produto["lote"], produto["armazenamento"], produto["quantidade"],
                produto["fornecedor"]
            ))

    def preencher_campos(event):
        selecionado = tabela_detalhes.selection()
        if selecionado:
            index = tabela_detalhes.index(selecionado)
            produto = produtos[index]
            entry_descricao.delete(0, tk.END)
            entry_descricao.insert(0, produto["descricao"])
            entry_validade.delete(0, tk.END)
            entry_validade.insert(0, produto["validade"])
            entry_segmento.delete(0, tk.END)
            entry_segmento.insert(0, produto["segmento"])
            entry_lote.delete(0, tk.END)
            entry_lote.insert(0, produto["lote"])
            entry_armazenamento.delete(0, tk.END)
            entry_armazenamento.insert(0, produto["armazenamento"])
            entry_quantidade.delete(0, tk.END)
            entry_quantidade.insert(0, produto["quantidade"])
            entry_fornecedor.delete(0, tk.END)
            entry_fornecedor.insert(0, produto["fornecedor"])

    def limpar_campos():
        for entry in entries:
            entry.delete(0, tk.END)

    # Função para exibir tooltip
    def mostrar_tooltip(event, texto):
        tooltip = tk.Label(janela, text=texto, fg="white", bg="#333333", font=("Arial", 10), relief="solid", padx=5, pady=5)
        tooltip.place(x=400, y=450)  # Coordenadas fixas (ajuste os valores conforme necessário)
        return tooltip

    def esconder_tooltip(tooltip):
        tooltip.destroy()


    # Centralizar os elementos
    def centralizar(frame):
        for widget in frame.winfo_children():
            widget.grid_configure(padx=5, pady=5, sticky="w")

    # Campos de entrada
    campos = [
        ("Descrição:", "entry_descricao"), ("Validade:", "entry_validade"),
        ("Segmento:", "entry_segmento"), ("Lote:", "entry_lote"),
        ("Armazenamento:", "entry_armazenamento"), ("Quantidade:", "entry_quantidade"),
        ("Fornecedor:", "entry_fornecedor")
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
        ("Adicionar", adicionar_produto, "#6A0DAD", "Clique aqui para adicionar um novo produto"),
        ("Atualizar", atualizar_produto, "#FFA500", "Clique aqui para atualizar os dados de um produto"),
        ("Excluir", excluir_produto, "#FF1744", "Clique aqui para excluir um produto"),
        ("Visualizar", visualizar_produtos, "#00C853", "Clique aqui para visualizar os dados dos produtos")
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

    # Tabela para exibir os produtos
    frame_tabela = tk.Frame(janela, bg="#121212")
    frame_tabela.pack(pady=20, fill=tk.BOTH, expand=True)

    colunas = ["Descrição", "Validade", "Segmento", "Lote", "Armazenamento", "Quantidade", "Fornecedor"]
    tabela_detalhes = ttk.Treeview(frame_tabela, columns=colunas, show="headings", height=8)

    for coluna in colunas:
        tabela_detalhes.heading(coluna, text=coluna)
        tabela_detalhes.column(coluna, width=30, anchor="center", stretch=True) # Consegue alterar a largura das colunas

    tabela_detalhes.pack(fill=tk.BOTH, expand=True)

    tabela_detalhes.bind("<ButtonRelease-1>", preencher_campos)

    # Executar a interface
    janela.mainloop()
