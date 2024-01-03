import tkinter as tk
from tkinter import filedialog
import qrcode

def criar_qrcode():
    url = entry_url.get()
    nome_qrcode = entry_nome_qrcode.get()

    imagem = qrcode.make(url)

    nome_arquivo = nome_qrcode + ".png"
    caminho_absoluto = filedialog.askdirectory()  # Solicita ao usuário o diretório de destino
    caminho_completo = caminho_absoluto + "\\" + nome_arquivo

    imagem.save(caminho_completo)

    resultado_label.config(text=f"QR Code salvo em:\n{caminho_completo}")

# Criar a janela principal
janela = tk.Tk()
janela.title("Gerador de QR Code")

# Componentes da interface gráfica
label_url = tk.Label(janela, text="URL:")
label_nome_qrcode = tk.Label(janela, text="Nome do QRCode:")
entry_url = tk.Entry(janela)
entry_nome_qrcode = tk.Entry(janela)
botao_gerar = tk.Button(janela, text="Gerar QRCode", command=criar_qrcode)
resultado_label = tk.Label(janela, text="")

# Layout dos componentes
label_url.grid(row=0, column=0, sticky="E", padx=5, pady=5)
entry_url.grid(row=0, column=1, padx=5, pady=5)
label_nome_qrcode.grid(row=1, column=0, sticky="E", padx=5, pady=5)
entry_nome_qrcode.grid(row=1, column=1, padx=5, pady=5)
botao_gerar.grid(row=2, column=0, columnspan=2, pady=10)
resultado_label.grid(row=3, column=0, columnspan=2, pady=10)

# Iniciar a execução da interface gráfica
janela.mainloop()
