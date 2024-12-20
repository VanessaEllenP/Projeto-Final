# Equipe: Vanessa Ellen Paixão, Aislan Silva de Jesus, Icaro Dantas e Kaique Conceição

import tkinter as tk
from tkinter import ttk, messagebox

# Lista para armazenar os fluxos de caminhões
fluxos_caminhoes = []

def abrir_tela_fluxo_caminhoes():
    # Configuração da interface
    janela = tk.Toplevel()
    janela.title("Fluxo de Caminhões")
    janela.geometry("900x800")
    janela.configure(bg="#121212")
    janela.resizable(False, False)

    # Título no topo
    titulo = tk.Label(janela, text="Fluxo de Caminhões", font=("Arial", 20, "bold"), fg="white", bg="#121212")
    titulo.pack(pady=20)

    # Funções do CRUD
    def adicionar_fluxo():
        fluxo = {
            "carga": entry_carga.get(),
            "hora_saida": entry_hora_saida.get(),
            "hora_retorno": entry_hora_retorno.get(),
            "data_saida": entry_data_saida.get(),
            "data_retorno": entry_data_retorno.get(),
            "destino": entry_destino.get(),
            "roteiro": entry_roteiro.get(),
            "km_saida": entry_km_saida.get(),
            "km_chegada": entry_km_chegada.get(),
            "caminhao": entry_caminhao.get(),
            "cliente": entry_cliente.get(),
            "motorista": entry_motorista.get()
        }
        if not fluxo["carga"] or not fluxo["hora_saida"] or not fluxo["caminhao"]:
            messagebox.showwarning("Erro", "Os campos Carga, Hora de Saída e Caminhão são obrigatórios!")
            return
        fluxos_caminhoes.append(fluxo)
        limpar_campos()
        messagebox.showinfo("Sucesso", "Fluxo adicionado com sucesso!")

    def atualizar_fluxo():
        selecionado = tabela_detalhes.selection()
        if selecionado:
            index = tabela_detalhes.index(selecionado)
            fluxos_caminhoes[index] = {
                "carga": entry_carga.get(),
                "hora_saida": entry_hora_saida.get(),
                "hora_retorno": entry_hora_retorno.get(),
                "data_saida": entry_data_saida.get(),
                "data_retorno": entry_data_retorno.get(),
                "destino": entry_destino.get(),
                "roteiro": entry_roteiro.get(),
                "km_saida": entry_km_saida.get(),
                "km_chegada": entry_km_chegada.get(),
                "caminhao": entry_caminhao.get(),
                "cliente": entry_cliente.get(),
                "motorista": entry_motorista.get()
            }
            limpar_campos()
            messagebox.showinfo("Sucesso", "Fluxo atualizado com sucesso!")
            visualizar_fluxos()
        else:
            messagebox.showwarning("Erro", "Nenhum fluxo selecionado!")

    def excluir_fluxo():
        selecionado = tabela_detalhes.selection()
        if selecionado:
            index = tabela_detalhes.index(selecionado)
            del fluxos_caminhoes[index]
            limpar_campos()
            messagebox.showinfo("Sucesso", "Fluxo excluído com sucesso!")
            visualizar_fluxos()
        else:
            messagebox.showwarning("Erro", "Nenhum fluxo selecionado!")

    def visualizar_fluxos():
        # Limpa a tabela antes de adicionar os dados
        tabela_detalhes.delete(*tabela_detalhes.get_children())
        for fluxo in fluxos_caminhoes:
            tabela_detalhes.insert("", tk.END, values=(
                fluxo["carga"], fluxo["hora_saida"], fluxo["hora_retorno"], fluxo["data_saida"],
                fluxo["data_retorno"], fluxo["destino"], fluxo["roteiro"], fluxo["km_saida"],
                fluxo["km_chegada"], fluxo["caminhao"], fluxo["cliente"], fluxo["motorista"]
            ))

    def preencher_campos(event):
        selecionado = tabela_detalhes.selection()
        if selecionado:
            index = tabela_detalhes.index(selecionado)
            fluxo = fluxos_caminhoes[index]
            entry_carga.delete(0, tk.END)
            entry_carga.insert(0, fluxo["carga"])
            entry_hora_saida.delete(0, tk.END)
            entry_hora_saida.insert(0, fluxo["hora_saida"])
            entry_hora_retorno.delete(0, tk.END)
            entry_hora_retorno.insert(0, fluxo["hora_retorno"])
            entry_data_saida.delete(0, tk.END)
            entry_data_saida.insert(0, fluxo["data_saida"])
            entry_data_retorno.delete(0, tk.END)
            entry_data_retorno.insert(0, fluxo["data_retorno"])
            entry_destino.delete(0, tk.END)
            entry_destino.insert(0, fluxo["destino"])
            entry_roteiro.delete(0, tk.END)
            entry_roteiro.insert(0, fluxo["roteiro"])
            entry_km_saida.delete(0, tk.END)
            entry_km_saida.insert(0, fluxo["km_saida"])
            entry_km_chegada.delete(0, tk.END)
            entry_km_chegada.insert(0, fluxo["km_chegada"])
            entry_caminhao.delete(0, tk.END)
            entry_caminhao.insert(0, fluxo["caminhao"])
            entry_cliente.delete(0, tk.END)
            entry_cliente.insert(0, fluxo["cliente"])
            entry_motorista.delete(0, tk.END)
            entry_motorista.insert(0, fluxo["motorista"])

    def limpar_campos():
        for entry in entries:
            entry.delete(0, tk.END)

    # Campos de entrada
    campos = [
        ("Carga:", "entry_carga"),
        ("Hora de Saída:", "entry_hora_saida"),
        ("Hora de Retorno:", "entry_hora_retorno"),
        ("Data de Saída:", "entry_data_saida"),
        ("Data de Retorno:", "entry_data_retorno"),
        ("Destino:", "entry_destino"),
        ("Roteiro:", "entry_roteiro"),
        ("Km de Saída:", "entry_km_saida"),
        ("Km de Chegada:", "entry_km_chegada"),
        ("Caminhão:", "entry_caminhao"),
        ("Cliente:", "entry_cliente"),
        ("Motorista:", "entry_motorista")
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
        ("Adicionar", adicionar_fluxo, "#6A0DAD"),
        ("Atualizar", atualizar_fluxo, "#FFA500"),
        ("Excluir", excluir_fluxo, "#FF1744"),
        ("Visualizar", visualizar_fluxos, "#00C853")
    ]

    for i, (text, command, color) in enumerate(botoes):
        btn = tk.Button(frame_botoes, text=text, command=command, bg=color, fg="white",
                        font=("Arial", 12), width=12, cursor="hand2", activebackground=color)
        btn.grid(row=0, column=i, padx=10, pady=10)

    # Tabela para exibir os fluxos
    frame_tabela = tk.Frame(janela, bg="#121212")
    frame_tabela.pack(pady=20, fill=tk.BOTH, expand=True)

    colunas = [
        "Carga", "Hora Saída", "Hora Retorno", "Data Saída", "Data Retorno", 
        "Destino", "Roteiro", "Km Saída", "Km Chegada", "Caminhão", "Cliente", "Motorista"
    ]
    tabela_detalhes = ttk.Treeview(frame_tabela, columns=colunas, show="headings", height=8)

    for coluna in colunas:
        tabela_detalhes.heading(coluna, text=coluna)
        tabela_detalhes.column(coluna, width=30, anchor="center", stretch=True)

    tabela_detalhes.pack(fill=tk.BOTH, expand=True)

    tabela_detalhes.bind("<ButtonRelease-1>", preencher_campos)

    janela.mainloop()

