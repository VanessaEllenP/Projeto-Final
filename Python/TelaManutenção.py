#Equipe: Vanessa Ellen Paixão, Aislan Silva de Jesus, Icaro Dantas e Kaique Conceição

import tkinter as tk
from tkinter import ttk, messagebox

# Lista para armazenar os dados das manutenções
manutencoes = []

def abrir_tela_manutencao():
    # Configuração da interface
    janela = tk.Tk()
    janela.title("Gerenciamento de Manutenção")
    janela.geometry("900x800")
    janela.configure(bg="#121212")
    janela.resizable(False, False)

    # Título no topo
    titulo = tk.Label(janela, text="Gerenciamento de Manutenção", font=("Arial", 20, "bold"), fg="white", bg="#121212")
    titulo.pack(pady=20)

    # Funções do CRUD
    def adicionar_manutencao():
        manutencao = {
            "data": entry_data.get(),
            "servico": entry_servico.get(),
            "mecanico": entry_mecanico.get(),
            "pecas": entry_pecas.get(),
            "caminhao": entry_caminhao.get()
        }
        if not manutencao["data"] or not manutencao["servico"]:
            messagebox.showwarning("Erro", "Os campos Data e Serviço são obrigatórios!")
            return
        manutencoes.append(manutencao)
        limpar_campos()
        messagebox.showinfo("Sucesso", "Manutenção adicionada com sucesso!")

    def atualizar_manutencao():
        selecionado = tabela_detalhes.selection()
        if selecionado:
            index = tabela_detalhes.index(selecionado)
            manutencoes[index] = {
                "data": entry_data.get(),
                "servico": entry_servico.get(),
                "mecanico": entry_mecanico.get(),
                "pecas": entry_pecas.get(),
                "caminhao": entry_caminhao.get()
            }
            limpar_campos()
            messagebox.showinfo("Sucesso", "Manutenção atualizada com sucesso!")
            visualizar_manutencoes()
        else:
            messagebox.showwarning("Erro", "Nenhuma manutenção selecionada!")

    def excluir_manutencao():
        selecionado = tabela_detalhes.selection()
        if selecionado:
            index = tabela_detalhes.index(selecionado)
            del manutencoes[index]
            limpar_campos()
            messagebox.showinfo("Sucesso", "Manutenção excluída com sucesso!")
            visualizar_manutencoes()
        else:
            messagebox.showwarning("Erro", "Nenhuma manutenção selecionada!")

    def visualizar_manutencoes():
        # Limpa a tabela antes de adicionar os dados
        tabela_detalhes.delete(*tabela_detalhes.get_children())
        for manutencao in manutencoes:
            tabela_detalhes.insert("", tk.END, values=(
                manutencao["data"], manutencao["servico"],
                manutencao["mecanico"], manutencao["pecas"], manutencao["caminhao"]
            ))

    def preencher_campos(event):
        selecionado = tabela_detalhes.selection()
        if selecionado:
            index = tabela_detalhes.index(selecionado)
            manutencao = manutencoes[index]
            entry_data.delete(0, tk.END)
            entry_data.insert(0, manutencao["data"])
            entry_servico.delete(0, tk.END)
            entry_servico.insert(0, manutencao["servico"])
            entry_mecanico.delete(0, tk.END)
            entry_mecanico.insert(0, manutencao["mecanico"])
            entry_pecas.delete(0, tk.END)
            entry_pecas.insert(0, manutencao["pecas"])
            entry_caminhao.delete(0, tk.END)
            entry_caminhao.insert(0, manutencao["caminhao"])

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
        ("Data:", "entry_data"), 
        ("Serviço:", "entry_servico"), ("Mecânico:", "entry_mecanico"),
        ("Peças:", "entry_pecas"), ("Caminhão:", "entry_caminhao")
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
        ("Adicionar", adicionar_manutencao, "#6A0DAD", "Clique aqui para adicionar uma nova manutenção"),
        ("Atualizar", atualizar_manutencao, "#FFA500", "Clique aqui para atualizar os dados de uma manutenção"),
        ("Excluir", excluir_manutencao, "#FF1744", "Clique aqui para excluir uma manutenção"),
        ("Visualizar", visualizar_manutencoes, "#00C853", "Clique aqui para visualizar as manutenções")
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

    # Tabela para exibir as manutenções
    frame_tabela = tk.Frame(janela, bg="#121212")
    frame_tabela.pack(pady=20, fill=tk.BOTH, expand=True)

    colunas = ["Data", "Serviço", "Mecânico", "Peças", "Caminhão"]
    tabela_detalhes = ttk.Treeview(frame_tabela, columns=colunas, show="headings", height=8)

    for coluna in colunas:
        tabela_detalhes.heading(coluna, text=coluna)
        tabela_detalhes.column(coluna, width=30, anchor="center", stretch=True) # Consegue alterar a largura das colunas

    tabela_detalhes.pack(fill=tk.BOTH, expand=True)

    tabela_detalhes.bind("<ButtonRelease-1>", preencher_campos)

    # Executar a interface
    janela.mainloop()
