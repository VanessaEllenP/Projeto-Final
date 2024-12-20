#Equipe: Vanessa Ellen Paixão, Aislan Silva de Jesus, Icaro Dantas e Kaique Conceição

import tkinter as tk
from tkinter import ttk, messagebox

# Lista para armazenar os dados de sensoriamento
sensores = []

def abrir_tela_sensoriamento():
    # Configuração da interface
    janela = tk.Tk()
    janela.title("Gerenciamento de Sensoriamento")
    janela.geometry("900x800")
    janela.configure(bg="#121212")
    janela.resizable(False, False)

    # Título no topo
    titulo = tk.Label(janela, text="Gerenciamento de Sensoriamento", font=("Arial", 20, "bold"), fg="white", bg="#121212")
    titulo.pack(pady=20)

    # Funções do CRUD
    def adicionar_sensoriamento():
        try:
            sensor = {
                "temperatura": float(entry_temperatura.get()),
                "luminosidade": float(entry_luminosidade.get()),
                "gases": float(entry_gases.get()),
                "presenca": var_presenca.get()  # Obtém o valor da presença (True ou False)
            }
        except ValueError:
            messagebox.showwarning("Erro", "Por favor, insira valores numéricos válidos para Temperatura, Luminosidade e Gases!")
            return

        if not sensor["temperatura"] or not sensor["luminosidade"]:
            messagebox.showwarning("Erro", "Os campos Temperatura e Luminosidade são obrigatórios!")
            return
        sensores.append(sensor)
        limpar_campos()
        messagebox.showinfo("Sucesso", "Sensoriamento adicionado com sucesso!")

    def atualizar_sensoriamento():
        selecionado = tabela_detalhes.selection()
        if selecionado:
            index = tabela_detalhes.index(selecionado)
            sensores[index] = {
                "temperatura": float(entry_temperatura.get()),
                "luminosidade": float(entry_luminosidade.get()),
                "gases": float(entry_gases.get()),
                "presenca": var_presenca.get()
            }
            limpar_campos()
            messagebox.showinfo("Sucesso", "Sensoriamento atualizado com sucesso!")
            visualizar_sensores()
        else:
            messagebox.showwarning("Erro", "Nenhum sensoriamento selecionado!")

    def excluir_sensoriamento():
        selecionado = tabela_detalhes.selection()
        if selecionado:
            index = tabela_detalhes.index(selecionado)
            del sensores[index]
            limpar_campos()
            messagebox.showinfo("Sucesso", "Sensoriamento excluído com sucesso!")
            visualizar_sensores()
        else:
            messagebox.showwarning("Erro", "Nenhum sensoriamento selecionado!")

    def visualizar_sensores():
        # Limpa a tabela antes de adicionar os dados
        tabela_detalhes.delete(*tabela_detalhes.get_children())
        for sensor in sensores:
            tabela_detalhes.insert("", tk.END, values=(
                sensor["temperatura"], sensor["luminosidade"], sensor["gases"], sensor["presenca"]
            ))

    def preencher_campos(event):
        selecionado = tabela_detalhes.selection()
        if selecionado:
            # Obtém o identificador do item selecionado
            item_id = selecionado[0]
            # Descobre o índice do item selecionado na tabela
            index = tabela_detalhes.index(item_id)
            sensor = sensores[index]

            # Preenchendo os campos de entrada
            entry_temperatura.delete(0, tk.END)
            entry_temperatura.insert(0, sensor["temperatura"])

            entry_luminosidade.delete(0, tk.END)
            entry_luminosidade.insert(0, sensor["luminosidade"])

            entry_gases.delete(0, tk.END)
            entry_gases.insert(0, sensor["gases"])

            # Atualizando o Checkbutton
            var_presenca.set(sensor["presenca"])



    def limpar_campos():
        for entry in entries:
            entry.delete(0, tk.END)
        var_presenca.set(False)  # Resetando o campo booleano de presença

    # Função para exibir tooltip
    def mostrar_tooltip(event, texto):
        tooltip = tk.Label(janela, text=texto, fg="white", bg="#333333", font=("Arial", 10), relief="solid", padx=5, pady=5)
        tooltip.place(x=400, y=350)  # Coordenadas fixas (ajuste os valores conforme necessário)
        return tooltip


    def esconder_tooltip(tooltip):
        tooltip.destroy()


    # Centralizar os elementos
    def centralizar(frame):
        for widget in frame.winfo_children():
            widget.grid_configure(padx=5, pady=5, sticky="w")

    # Campos de entrada
    campos = [
        ("Temperatura:", "entry_temperatura"), ("Luminosidade:", "entry_luminosidade"), 
        ("Gases:", "entry_gases"), ("Presença:", "var_presenca")
    ]

    entries = []
    frame_campos = tk.Frame(janela, bg="#121212")
    frame_campos.pack(pady=20)

    # Variável para o campo Presença (booleano)
    var_presenca = tk.BooleanVar()

    for i, (label_text, entry_var) in enumerate(campos):
        label = tk.Label(frame_campos, text=label_text, fg="white", bg="#121212", font=("Arial", 12))
        label.grid(row=i, column=0, padx=5, pady=5, sticky="e")
        
        if entry_var == "var_presenca":
            checkbox = tk.Checkbutton(frame_campos, variable=var_presenca, bg="#121212", fg="white", font=("Arial", 12))
            checkbox.grid(row=i, column=1, padx=5, pady=5, sticky="w")
        else:
            entry = tk.Entry(frame_campos, width=30, bg="#1F1F1F", fg="white", font=("Arial", 12))
            entry.grid(row=i, column=1, padx=5, pady=5, sticky="w")
            entries.append(entry)
            globals()[entry_var] = entry

    # Botões
    frame_botoes = tk.Frame(janela, bg="#121212")
    frame_botoes.pack(pady=20)

    botoes = [
        ("Adicionar", adicionar_sensoriamento, "#6A0DAD", "Clique aqui para adicionar um novo sensoriamento"),
        ("Atualizar", atualizar_sensoriamento, "#FFA500", "Clique aqui para atualizar os dados de um sensoriamento"),
        ("Excluir", excluir_sensoriamento, "#FF1744", "Clique aqui para excluir um sensoriamento"),
        ("Visualizar", visualizar_sensores, "#00C853", "Clique aqui para visualizar os dados de sensoriamento")
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

    # Tabela para exibir os sensoriamentos
    frame_tabela = tk.Frame(janela, bg="#121212")
    frame_tabela.pack(pady=20, fill=tk.BOTH, expand=True)

    colunas = ["Temperatura", "Luminosidade", "Gases", "Presença"]
    tabela_detalhes = ttk.Treeview(frame_tabela, columns=colunas, show="headings", height=8)

    for coluna in colunas:
        tabela_detalhes.heading(coluna, text=coluna)
        tabela_detalhes.column(coluna, width=30, anchor="center", stretch=True) # Consegue alterar a largura das colunas

    tabela_detalhes.pack(fill=tk.BOTH, expand=True)

    tabela_detalhes.bind("<ButtonRelease-1>", preencher_campos)

    # Executar a interface
    janela.mainloop()
