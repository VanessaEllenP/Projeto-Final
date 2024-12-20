#Equipe: Vanessa Ellen Paixão, Aislan Silva de Jesus, Icaro Dantas e Kaique Conceição

import tkinter as tk
from TelaCliente import abrir_tela_cliente
from TelaFornecedor import abrir_tela_fornecedor
from TelaCaminhao import abrir_tela_caminhao
from TelaProduto import abrir_tela_produto
from TelaFluxo_Caminhoes import abrir_tela_fluxo_caminhoes
from TelaManutenção import abrir_tela_manutencao
from TelaSensoriamento import abrir_tela_sensoriamento
from TelaFuncionario import abrir_tela_funcionario

def criar_menu_principal():
    
    janela_principal = tk.Tk()
    janela_principal.title("Menu Principal")
    janela_principal.geometry("400x700")
    janela_principal.configure(bg="#121212")
    janela_principal.resizable(False, False)

    titulo = tk.Label(janela_principal, text="Menu Principal", font=("Arial", 20, "bold"), fg="white", bg="#121212")
    titulo.pack(pady=20)

    # Função para criar botões do menu
    def criar_botao(texto, comando):
        return tk.Button(
            janela_principal,
            text=texto,
            command=lambda: [janela_principal.withdraw(), comando()],
            bg="#6A0DAD",
            fg="white",
            font=("Arial", 12),
            width=20,
            height=2,
            cursor="hand2",
            activebackground="#8A2BE2"
        )

    # Botões para abrir cada tela
    botoes = [
        ("Tela Cliente", abrir_tela_cliente),
        ("Tela Fornecedor", abrir_tela_fornecedor),
        ("Tela Funcionário", abrir_tela_funcionario),                                    
        ("Tela Caminhão", abrir_tela_caminhao),
        ("Tela Produto", abrir_tela_produto),
        ("Tela Fluxo de Caminhões", abrir_tela_fluxo_caminhoes),
        ("Tela Manutenção", abrir_tela_manutencao),
        ("Tela Sensoriamento", abrir_tela_sensoriamento)
    ]

    for texto, comando in botoes:
        botao = criar_botao(texto, comando)
        botao.pack(pady=10)

    # Rodar o menu principal
    janela_principal.mainloop()

if __name__ == "__main__":
    criar_menu_principal()
