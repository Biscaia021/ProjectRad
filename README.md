import tkinter as tk

#janela = tk.Tk()

# frame1 =tk.Frame(master=janela,width=100,height=100,bg="red")
# frame1.pack()
# frame2 =tk.Frame(master=janela,width=50,height=50,bg="green")
# frame2.pack()
# frame3 =tk.Frame(master=janela,width=25,height=25,bg="blue")
# frame3.pack()




# frame1=tk.Frame(master=janela,height=100,bg="red")
# frame1.pack(fill=tk.X)
#
# frame2=tk.Frame(master=janela,height=50,bg="green")
# frame2.pack(fill=tk.X)
#
# frame3=tk.Frame(master=janela,height=25,bg="blue")
# frame3.pack(fill=tk.X)




# frame1=tk.Frame(master=janela,width=200,height=100,bg="red")
# frame1.pack(fill=tk.BOTH,side=tk.LEFT,expand=True)
#
# frame2=tk.Frame(master=janela,width=100,bg="green")
# frame2.pack(fill=tk.BOTH,side=tk.LEFT,expand=True)
#
# frame3=tk.Frame(master=janela,width=50,bg="blue")
# frame3.pack(fill=tk.BOTH,side=tk.LEFT,expand=True)



# frame=tk.Frame(master=janela,width=210,height=210)
# frame.pack()
#
# label1=tk.Label(master=frame,text="Estou na posição (0,0)",bg="red")
# label1.place(x=0,y=0)
#
# label2=tk.Label(master=frame,text="Estou na posição (75,75)",bg="blue")
# label2.place(x=75,y=75)


# for i in range (3):
#     for j in range(3):
#         frame = tk.Frame(
#             master=janela,
#             relief=tk.RAISED,
#             borderwidth=1
#         )
#         frame.grid(row=i, column=j,padx=5,pady=5)
#         label = tk.Label(master=frame,text=f"linha {i}\nColuna{j}")
#         label.pack()



# for i in range(3):
#     janela.columnconfigure(i,weight=1,minsize=75)
#     janela.rowconfigure(i,weight=1,minsize=50)
#     for j in range(3):
#         frame = tk.Frame(
#             master=janela,
#             relief=tk.RAISED,
#             borderwidth=1
#         )
#         frame.grid(row=i,column=j,padx=5,pady=5)
#     label=tk.Label(master=frame,text=f"Linha {i}\nColuna {j}")
#     label.pack()



# janela.columnconfigure(0,minsize=250)
# janela.rowconfigure([0,1],minsize=100)
#
# label1=tk.Label(text="A")
# label1.grid(row=0,column=0,sticky="ne")
#
# label2=tk.Label(text="B")
# label2.grid(row=1,column=0,sticky="sw")



# def clicado():
#     label.config(text="botão clicado")
#
# janela=tk.Tk()
# janela.title("exemplo tkinter")
#
# label=tk.Label(janela,text=("ola, tkinter"))
# label.pack()
#
# botao = tk.Button(janela,text="clique em mim",command=clicado)
# botao.pack()





# def sair():
#     janela.quit()
#
# def sobre():
#     segunda_janela = tk.Toplevel(janela)
#     segunda_janela.title("sobre")
#     segunda_janela.geometry("200x100")
#
# janela=tk.Tk()
# janela.geometry("320x150")
# menubar=tk.Menu(janela)
# janela.config(menu=menubar)
#
#
# menu_arquivo = tk.Menu(menubar,tearoff=0)
# menu_arquivo.add_command(label="abrir")
# menu_arquivo.add_command(label="fechar")
# menu_arquivo.add_separator()
# menu_arquivo.add_command(label="sair",command=sair)
# menubar.add_cascade(label="arquivo",menu=menu_arquivo)
#
#
# menu_ajuda = tk.Menu(menubar,tearoff=0)
# menu_ajuda.add_command(label="bem-vindo")
# menu_ajuda.add_command(label="sobre",command=sobre)
# menubar.add_cascade(label="ajuda",menu=menu_ajuda)


# import tkinter as tk
# from tkinter import ttk
#
# def selecionar_mes (event):
#     selecionar_month = combo.get()
#     print(f"voce selecionou:{selecionar_month}")
#
#
# janela = tk.Tk()
# janela.geometry("200x100")
# labeltop = tk.Label(janela,text="meses")
# labeltop.grid(column=0,row=0)
# meses=["janeiro","fevereiro","março","abril"]
# combo = ttk.Combobox(janela,values=meses)
# combo.grid(column=0,row=1)
# combo.current(1)
# combo.bind("<<comboboxselected>>",selecionar_mes)


# janela = tk.Tk()
# janela.title("nos love python")
#
# janela.geometry("600x250")
# janela.eval("tk::PlaceWindow . center")

root= tk.Tk()
width = 600
height= 300

screen_width=root.winfo_screenwidth()
screen_height=root.winfo_screenheight()

x=(screen_width/2)-(width/2)
y=(screen_height/2)-(height/2)

root.geometry("%dx%d+%d+%d" % (width,height,x,y))




root.mainloop()
