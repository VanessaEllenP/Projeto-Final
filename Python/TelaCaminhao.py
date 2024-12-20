#Equipe: Vanessa Ellen Paixão, Aislan Silva de Jesus, Icaro Dantas e Kaique Conceição

import tkinter as tk
from tkinter import ttk, messagebox

# Lista para armazenar os dados dos caminhões
caminhoes = []

def abrir_tela_caminhao():
    # Configuração da interface
    janela = tk.Toplevel()
    janela.title("Gerenciamento de Caminhões")
    janela.geometry("900x800")
    janela.configure(bg="#121212")
    janela.resizable(False, False)

    # Título no topo
    titulo = tk.Label(janela, text="Gerenciamento de Caminhões", font=("Arial", 20, "bold"), fg="white", bg="#121212")
    titulo.pack(pady=20)

    # Funções do CRUD
    def adicionar_caminhao():
        caminhao = {
            "marca": entry_marca.get(),
            "modelo": entry_modelo.get(),
            "placa": entry_placa.get(),
            "renavan": entry_renavan.get(),
            "chassi": entry_chassi.get(),
            "capacidade": entry_capacidade.get()
        }
        if not caminhao["placa"] or not caminhao["modelo"]:
            messagebox.showwarning("Erro", "Os campos Placa e Modelo são obrigatórios!")
            return
        caminhoes.append(caminhao)
        limpar_campos()
        messagebox.showinfo("Sucesso", "Caminhão adicionado com sucesso!")

    def atualizar_caminhao():
        selecionado = tabela_detalhes.selection()
        if selecionado:
            index = tabela_detalhes.index(selecionado)
            caminhoes[index] = {
                "marca": entry_marca.get(),
                "modelo": entry_modelo.get(),
                "placa": entry_placa.get(),
                "renavan": entry_renavan.get(),
                "chassi": entry_chassi.get(),
                "capacidade": entry_capacidade.get()
            }
            limpar_campos()
            messagebox.showinfo("Sucesso", "Caminhão atualizado com sucesso!")
            visualizar_caminhoes()
        else:
            messagebox.showwarning("Erro", "Nenhum caminhão selecionado!")

    def excluir_caminhao():
        selecionado = tabela_detalhes.selection()
        if selecionado:
            index = tabela_detalhes.index(selecionado)
            del caminhoes[index]
            limpar_campos()
            messagebox.showinfo("Sucesso", "Caminhão excluído com sucesso!")
            visualizar_caminhoes()
        else:
            messagebox.showwarning("Erro", "Nenhum caminhão selecionado!")

    def visualizar_caminhoes():
        # Limpa a tabela antes de adicionar os dados
        tabela_detalhes.delete(*tabela_detalhes.get_children())
        for caminhao in caminhoes:
            tabela_detalhes.insert("", tk.END, values=(
                caminhao["marca"], caminhao["modelo"], caminhao["placa"], caminhao["renavan"], 
                caminhao["chassi"], caminhao["capacidade"]
            ))

    def preencher_campos(event):
        selecionado = tabela_detalhes.selection()
        if selecionado:
            index = tabela_detalhes.index(selecionado)
            caminhao = caminhoes[index]
            entry_marca.delete(0, tk.END)
            entry_marca.insert(0, caminhao["marca"])
            entry_modelo.delete(0, tk.END)
            entry_modelo.insert(0, caminhao["modelo"])
            entry_placa.delete(0, tk.END)
            entry_placa.insert(0, caminhao["placa"])
            entry_renavan.delete(0, tk.END)
            entry_renavan.insert(0, caminhao["renavan"])
            entry_chassi.delete(0, tk.END)
            entry_chassi.insert(0, caminhao["chassi"])
            entry_capacidade.delete(0, tk.END)
            entry_capacidade.insert(0, caminhao["capacidade"])

    def limpar_campos():
        for entry in entries:
            entry.delete(0, tk.END)

    # Funções para tooltips
    def mostrar_tooltip(event, texto):
        tooltip = tk.Label(janela, text=texto, fg="white", bg="#333333", font=("Arial", 10), relief="solid", padx=5, pady=5)
        tooltip.place(x=event.x_root - janela.winfo_rootx() + 20, y=event.y_root - janela.winfo_rooty() + 20)
        return tooltip

    def esconder_tooltip(tooltip):
        tooltip.destroy()

    # Campos de entrada
    campos = [
        ("Marca:", "entry_marca"),
        ("Modelo:", "entry_modelo"),
        ("Placa:", "entry_placa"),
        ("Renavan:", "entry_renavan"),
        ("Chassi:", "entry_chassi"),
        ("Capacidade:", "entry_capacidade")
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
        ("Adicionar", adicionar_caminhao, "#6A0DAD", "Clique aqui para adicionar um novo caminhão"),
        ("Atualizar", atualizar_caminhao, "#FFA500", "Clique aqui para atualizar os dados de um caminhão"),
        ("Excluir", excluir_caminhao, "#FF1744", "Clique aqui para excluir um caminhão"),
        ("Visualizar", visualizar_caminhoes, "#00C853", "Clique aqui para visualizar os caminhões")
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

    # Tabela para exibir os caminhões
    frame_tabela = tk.Frame(janela, bg="#121212")
    frame_tabela.pack(pady=20, fill=tk.BOTH, expand=True)

    colunas = ["Marca", "Modelo", "Placa", "Renavan", "Chassi", "Capacidade"]
    tabela_detalhes = ttk.Treeview(frame_tabela, columns=colunas, show="headings", height=8)

    for coluna in colunas:
        tabela_detalhes.heading(coluna, text=coluna)
        tabela_detalhes.column(coluna, width=30, anchor="center", stretch=True) # Consegue alterar a largura das colunas

    tabela_detalhes.pack(fill=tk.BOTH, expand=True)

    tabela_detalhes.bind("<ButtonRelease-1>", preencher_campos)

    janela.mainloop()
