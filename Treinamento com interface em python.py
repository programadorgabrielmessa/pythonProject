import tkinter as tk
from tkinter import messagebox


# Função para calcular o valor total com desconto
def calcular():
    try:
        valor_unitario = float(entry_valor_unitario.get())
        quantidades = int(entry_quantidade.get())

        valor_total_sem_desconto = valor_unitario * quantidades

        if quantidades < 200:
            desconto_percentual = 0
        elif quantidades < 1000:
            desconto_percentual = 0.05
        elif quantidades < 2000:
            desconto_percentual = 0.1
        else:
            desconto_percentual = 0.15

        valor_desconto = valor_total_sem_desconto * desconto_percentual
        valor_total_com_desconto = valor_total_sem_desconto - valor_desconto

        label_resultado.config(text=f"Valor total sem desconto: R${valor_total_sem_desconto:.2f}\n"
                                    f"Desconto aplicado: {desconto_percentual * 100:.0f}%\n"
                                    f"Valor total com desconto: R${valor_total_com_desconto:.2f}\n"
                                    f"Pedido: {quantidades} unidades\n"
                                    f"Desconto aplicado: {desconto_percentual * 100:.0f}%")
    except ValueError:
        messagebox.showerror("Erro", "Por favor, insira valores válidos.")


# Configuração da janela principal
root = tk.Tk()
root.title("Calculadora de Desconto")

# Enunciado do problema
enunciado = """
Enunciado: Imagina-se que você é um dos programadores responsáveis pela construção de um app de vendas para uma determinada empresa X que vende em atacado. 
Uma das estratégias de vendas dessa empresa X é dar descontos maiores por unidade conforme as informações abaixo:

• Se quantidade for menor que 200 o desconto será de 0%;
• Se quantidade for igual ou maior que 200 e menor que 1000 o desconto será de 5%;
• Se quantidade for igual ou maior que 1000 e menor que 2000 o desconto será de 10%;
• Se quantidade for igual ou maior que 2000 o desconto será de 15%;


"""

label_enunciado = tk.Label(root, text=enunciado, justify=tk.LEFT, wraplength=600)
label_enunciado.pack(padx=10, pady=10)

# Labels e entradas para o valor unitário e quantidade
label_nome = tk.Label(root, text="Bem-vindo, Gabriel Rodrigues de Almeida Messa!")
label_nome.pack()

label_valor_unitario = tk.Label(root, text="Digite o valor unitário do produto:")
label_valor_unitario.pack()
entry_valor_unitario = tk.Entry(root)
entry_valor_unitario.pack()

label_quantidade = tk.Label(root, text="Digite a quantidade do produto:")
label_quantidade.pack()
entry_quantidade = tk.Entry(root)
entry_quantidade.pack()

# Botão para calcular o desconto
botao_calcular = tk.Button(root, text="Calcular", command=calcular)
botao_calcular.pack()

# Label para exibir os resultados
label_resultado = tk.Label(root, text="")
label_resultado.pack(pady=10)

# Executa o loop principal da interface gráfica
root.mainloop()

'''
Elabore um programa em Python que:
A. Realizar o print de uma mensagem de boas-vindas que apareça o seu nome;
B. Deve-se entrar com o valor unitário e quantidade do produto;
C. Deve-se retornar o valor total sem desconto e o valor total com desconto;
D. Deve-se utilizar as estruturas if, elif e else (todas elas);
E. Deve-se fazer comentários no código;
F. Deve-se colocar na apresentação de saída de console um pedido recebendo desconto.

EXEMPLO DE SAÍDA DE CONSOLE:
[Exemplo de saída de console que o aluno deve fazer, em que se pergunta o valor do produto (pode ser qualquer valor), a quantidade (deve ser maior que 200) e apresenta o valor final sem o desconto e com o desconto.]
'''
