import tkinter as tk
import os

# função para obter a tabela ARP usando o comando "arp -a"
def get_arp_table():
    arp_table = os.popen("arp -a").read()
    return arp_table

# cria a janela principal
root = tk.Tk()
root.title("Tabela ARP")

# cria o botão que atualiza a tabela ARP
button = tk.Button(root, text="Atualizar", command=lambda: arp_text.config(state="normal") or arp_text.delete(1.0, tk.END) or arp_text.insert(tk.END, get_arp_table()) or arp_text.config(state="disabled"))
button.pack()

# cria a área de texto para exibir a tabela ARP
arp_text = tk.Text(root, height=20, width=80)
arp_text.insert(tk.END, get_arp_table())
arp_text.config(state="disabled")
arp_text.pack()

# inicia o loop principal da aplicação
root.mainloop()
