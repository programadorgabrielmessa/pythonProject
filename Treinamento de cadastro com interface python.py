import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

# Funções para manipulação de dados
def cadastrar_colaborador():
    nome = nome_entry.get()
    setor = setor_entry.get()
    try:
        pagamento = float(pagamento_entry.get())
    except ValueError:
        messagebox.showerror("Erro", "Digite um número válido para o pagamento.")
        return

    colaborador = {
        "id": id_global.get(),
        "nome": nome,
        "setor": setor,
        "pagamento": pagamento
    }
    lista_colaboradores.append(colaborador)
    id_global.set(id_global.get() + 1)
    messagebox.showinfo("Sucesso", "Colaborador cadastrado com sucesso!")
    limpar_campos()

def limpar_campos():
    nome_entry.delete(0, tk.END)
    setor_entry.delete(0, tk.END)
    pagamento_entry.delete(0, tk.END)

# Inicializa a aplicação e a janela principal
app = tk.Tk()
app.title("Sistema de Cadastro")
app.geometry("800x600")

# Variáveis globais
id_global = tk.IntVar(value=0)
lista_colaboradores = []

# Criação dos frames
frame_dados_pessoais = tk.LabelFrame(app, text="Dados Pessoais")
frame_dados_pessoais.pack(fill="both", expand="yes", padx=10, pady=10)

# Campos de entrada de dados pessoais
tk.Label(frame_dados_pessoais, text="Nome:").grid(row=0, column=0, sticky=tk.W, padx=5, pady=5)
nome_entry = tk.Entry(frame_dados_pessoais, width=30)
nome_entry.grid(row=0, column=1, padx=5, pady=5)

tk.Label(frame_dados_pessoais, text="Setor:").grid(row=1, column=0, sticky=tk.W, padx=5, pady=5)
setor_entry = tk.Entry(frame_dados_pessoais, width=30)
setor_entry.grid(row=1, column=1, padx=5, pady=5)

tk.Label(frame_dados_pessoais, text="Pagamento:").grid(row=2, column=0, sticky=tk.W, padx=5, pady=5)
pagamento_entry = tk.Entry(frame_dados_pessoais, width=30)
pagamento_entry.grid(row=2, column=1, padx=5, pady=5)

# Botões de ação
frame_acoes = tk.Frame(app)
frame_acoes.pack(fill="both", expand="yes", padx=10, pady=10)

tk.Button(frame_acoes, text="Cadastrar", command=cadastrar_colaborador).pack(side=tk.LEFT, padx=5, pady=5)
tk.Button(frame_acoes, text="Limpar", command=limpar_campos).pack(side=tk.LEFT, padx=5, pady=5)
tk.Button(frame_acoes, text="Sair", command=app.quit).pack(side=tk.LEFT, padx=5, pady=5)

# Inicializa o loop da aplicação
app.mainloop()
