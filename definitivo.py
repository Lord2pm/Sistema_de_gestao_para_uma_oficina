from tkinter import *
from tkinter import messagebox
import sqlite3 as sql

database = sql.connect("base_dados.db")
cursor = database.cursor()

def atendidos():
	with open("atendidos.txt", "a") as x:
		x.write("1\n")

def show_atendidos():
	with open("atendidos.txt", "r") as x:
		y = []
		for i in x:
			y.append(i)
		qtd = len(y)
		messagebox.showinfo("Viaturas atendidas", f"Foram atendidas {qtd} viaturas.")

#Cadastro de viaturas @#$%&2001
def tela_cad_viat():
	def bt_cad_click():
		model = str(in_model.get())
		marca = str(in_marca.get())
		cor = str(in_cor.get())
		km = eval(in_km.get())

		nome = str(in_nome.get())
		morada = str(in_morada.get())
		num_BI = str(in_num_BI.get())
		num_tel = str(in_num_tel.get())
		ficha = eval(in_ficha.get())

		clicked = chosen.get()
		if clicked == "Reparação":
			cursor.execute("""CREATE TABLE IF NOT EXISTS Reparacao(Modelo text, Marca text, Cor text, Servico text, Quilometragem real, Nome_cond text, Morada text, N_BI text, N_tel text, Ficha integer)""")
			instrucao = f"INSERT INTO Reparacao VALUES('{model}', '{marca}', '{cor}', '{clicked}', {km}, '{nome}', '{morada}', '{num_BI}', '{num_tel}', {ficha})"
		else:
			cursor.execute("""CREATE TABLE IF NOT EXISTS Manutencao(Modelo text, Marca text, Cor text, Servico text, Quilometragem real, Nome_cond text, Morada text, N_BI text, N_tel text, Ficha integer)""")
			instrucao = f"INSERT INTO Manutencao VALUES('{model}', '{marca}', '{cor}', '{clicked}', {km}, '{nome}', '{morada}', '{num_BI}', '{num_tel}', {ficha})"
		cursor.execute(instrucao)
		database.commit()
		atendidos()

	def voltar():
		janela.destroy()
		main()

	janela = Tk()
	janela.title("Oficina Quase Perfeita - Cadastro de Viaturas")
	janela.config(bg="#006d68")
	janela.geometry("800x600+200+0")
	janela.resizable(False, False)

	barra_menu = Menu(janela)
	menu_ver = Menu(barra_menu, tearoff=0)
	menu_ver.add_command(label="Página anterior", command=voltar)
	barra_menu.add_cascade(label="Ver", menu=menu_ver)

	janela.config(menu=barra_menu)

	area2 = Frame(janela, bg="#000000", width="600", height="600")
	area2.place(x=200, y=0)

	lb_viat_data = Label(area2, text="Dados da Viatura", font=("Arial", 12), bg="#000000", fg="#c1c1c1")
	lb_viat_data.place(x=250, y=10)

	lb_label = Label(janela, text="Oficina Quase\nPerfeita", font=("Arial", 14), bg="#006d68", fg="#000000")
	lb_label.place(x=30, y=220)

	lb_model = Label(area2, text="Modelo da viatura", font=("Arial", 12), bg="#000000", fg="#c1c1c1")
	lb_model.place(x=25, y=50)

	in_model = Entry(area2, width="40", font=("Arial", 12))
	in_model.place(x=160, y=50)

	lb_marca = Label(area2, text="Marca da viatura", font=("Arial", 12), bg="#000000", fg="#c1c1c1")
	lb_marca.place(x=25, y=100)

	in_marca = Entry(area2, width="40", font=("Arial", 12))
	in_marca.place(x=160, y=100)

	lb_cor = Label(area2, text="Cor da viatura", font=("Arial", 12), bg="#000000", fg="#c1c1c1")
	lb_cor.place(x=25, y=150)

	in_cor = Entry(area2, width="40", font=("Arial", 12))
	in_cor.place(x=160, y=150)

	lb_km = Label(area2, text="Quilometragem", font=("Arial", 12), bg="#000000", fg="#c1c1c1")
	lb_km.place(x=25, y=200)

	in_km = Entry(area2, width="40", font=("Arial", 12))
	in_km.place(x=160, y=200)

	lb_service = Label(area2, text="Tipo de Serviço", font=("Arial", 12), bg="#000000", fg="#c1c1c1")
	lb_service.place(x=25, y=250)

	chosen = StringVar()

	rb_reparacao = Radiobutton(area2, text="Reparação", value="Reparação", variable=chosen)
	rb_reparacao.place(x=160, y=250)

	rb_manutencao = Radiobutton(area2, text="Manutenção", value="Manutenção", variable=chosen)
	rb_manutencao.place(x=250, y=250)

	lb_ficha = Label(area2, text="Ficha Número", font=("Arial", 12), bg="#000000", fg="#c1c1c1")
	lb_ficha.place(x=355, y=250)

	in_ficha = Entry(area2, width="6", font=("Arial", 12))
	in_ficha.place(x=465, y=250)

	lb_cond_data = Label(area2, text="Dados do Condutor", font=("Arial", 12), bg="#000000", fg="#c1c1c1")
	lb_cond_data.place(x=250, y=300)

	lb_nome = Label(area2, text="Nome / Condutor", font=("Arial", 12), bg="#000000", fg="#c1c1c1")
	lb_nome.place(x=25, y=350)

	in_nome = Entry(area2, width="40", font=("Arial", 12))
	in_nome.place(x=160, y=350)

	lb_morada = Label(area2, text="Morada / Condutor", font=("Arial", 12), bg="#000000", fg="#c1c1c1")
	lb_morada.place(x=25, y=400)

	in_morada = Entry(area2, width="40", font=("Arial", 12))
	in_morada.place(x=160, y=400)

	lb_num_BI = Label(area2, text="N° BI / Condutor", font=("Arial", 12), bg="#000000", fg="#c1c1c1")
	lb_num_BI.place(x=25, y=450)

	in_num_BI = Entry(area2, width="40", font=("Arial", 12))
	in_num_BI.place(x=160, y=450)

	lb_num_tel = Label(area2, text="N° Tel / Condutor", font=("Arial", 12), bg="#000000", fg="#c1c1c1")
	lb_num_tel.place(x=25, y=500)

	in_num_tel = Entry(area2, width="40", font=("Arial", 12))
	in_num_tel.place(x=160, y=500)

	bt_cad = Button(area2, width="10", text="Cadastrar", font=("Arial", 12), bg="#006d68", activebackground="#035a56", command=bt_cad_click)
	bt_cad.place(x=270, y=550)

	janela.mainloop()

#Tela principal
def main():
    def cad_viat():
        janela.destroy()
        tela_cad_viat()
    
    def ajuda():
        pass
    
    def sair():
        janela.destroy()

    def cad_func():
    	janela.destroy()
    	tela_cad_func()

    def pag_inicial():
    	janela.destroy()
    	tela_inicial()

    def delete_cad():
    	def bt_delete_cad():
    		nome = str(in_nome.get()).strip()
    		num_BI = str(in_num_BI.get())
    		num_tel = str(in_num_tel.get())
    		senha = str(in_senha.get())
    		if nome == "" or senha == "":
    			messagebox.showwarning("Atenção", "Preencha todos os campos.")
    		else:
    			instrucao = f"DELETE FROM Funcionarios WHERE Nome = '{nome}' AND N_BI = '{num_BI}'"
    			cursor.execute(instrucao)
    			database.commit()
    			messagebox.showinfo("Verificação", "Cadastro removido com sucesso.")
    			in_nome.delete(0, "end")
    			in_num_BI.delete(0, "end")
    			in_num_tel.delete(0, "end")
    			in_senha.delete(0, "end")

    	def voltar():
    		janela.destroy()
    		main()

    	def sair():
    		janela.destroy()

    	janela = Tk()
    	janela.title("Oficina Quase Perfeita - Remover Cadastro de funcionários")
    	janela.config(bg="#006d68")
    	janela.resizable(False, False)
    	janela.geometry("600x500+200+0")

    	barra_menu = Menu(janela)
    	menu_ver = Menu(barra_menu, tearoff=0)
    	menu_ver.add_command(label="Página anterior", command=voltar)
    	menu_ver.add_separator()
    	menu_ver.add_command(label="Sair", command=sair)
    	barra_menu.add_cascade(label="Ver", menu=menu_ver)

    	janela.config(menu=barra_menu)

    	area2 = Frame(janela, bg="#000000", width="400", height="500")
    	area2.place(x=200)

    	lb_label = Label(janela, text="Oficina Quase\nPerfeita", font=("Arial", 14), bg="#006d68", fg="#000000")
    	lb_label.place(x=30, y=180)

    	lb_nome = Label(area2, text="Nome", font=("Arial", 12), bg="#000000", fg="#c1c1c1")
    	lb_nome.place(x=25, y=130)

    	in_nome = Entry(area2, width="25", font=("Arial", 12))
    	in_nome.place(x=100, y=130)

    	lb_num_BI = Label(area2, text="N° BI", font=("Arial", 12), bg="#000000", fg="#c1c1c1")
    	lb_num_BI.place(x=25, y=180)

    	in_num_BI = Entry(area2, width="25", font=("Arial", 12))
    	in_num_BI.place(x=100, y=180)

    	lb_num_tel = Label(area2, text="N° Tel", font=("Arial", 12), bg="#000000", fg="#c1c1c1")
    	lb_num_tel.place(x=25, y=230)

    	in_num_tel = Entry(area2, width="25", font=("Arial", 12))
    	in_num_tel.place(x=100, y=230)

    	lb_senha = Label(area2, text="Senha", font=("Arial", 12), bg="#000000", fg="#c1c1c1")
    	lb_senha.place(x=25, y=280)

    	in_senha = Entry(area2, width="25", font=("Arial", 12), show="*")
    	in_senha.place(x=100, y=280)

    	bt_delete_cad = Button(area2, width="10", text="Remover", font=("Arial", 12), bg="#006d68", activebackground="#035a56", command=bt_delete_cad)
    	bt_delete_cad.place(x=170, y=330)

    	janela.mainloop()

    def remove_func():
    	janela.destroy()
    	delete_cad()

    def others():
    	def qtd_marca():
		    marca = str(in_marca.get())
		    if True:		        
		        instrucao = f"SELECT Marca FROM Manutencao WHERE Marca like '{marca}'"
		        
		        cursor.execute(instrucao)
		        dados = cursor.fetchall()
		        n1 = int(len(dados))
		        database.commit()
		    if True:
		        instrucao = f"SELECT Marca FROM Reparacao WHERE Marca like '{marca}'"
		        
		        cursor.execute(instrucao)
		        dados = cursor.fetchall()
		        n2 = int(len(dados))
		        nt = n1 + n2
		        messagebox.showinfo("Verificação", f"A marca {marca} aparece {nt} vezes no sistema")
		        database.commit()

    	def del_viat():
    		num_tel = str(in_num_tel.get())
    		clicked = chosen.get()
    		if num_tel == "":
    			messagebox.showwarning("Atenção", "Preencha todos os campos.")
    		else:
    			if clicked == "Reparação":
    				instrucao = f"DELETE FROM  Reparacao WHERE N_tel = '{num_tel}'"
    			else:
    				instrucao = f"DELETE FROM  Manutencao WHERE N_tel = '{num_tel}'"
    			cursor.execute(instrucao)
    			database.commit()
    			messagebox.showinfo("Verificação", "Viatura removida com êxito.")

    		instrucao = f"UPDATE Reparacao SET Ficha = Ficha - 1 WHERE Ficha >= 2"
    		cursor.execute(instrucao)
    		database.commit()

    		instrucao = f"UPDATE Manutencao SET Ficha = Ficha - 1 WHERE Ficha >= 2"
    		cursor.execute(instrucao)
    		database.commit()

    	def sair():
    		janela.destroy()

    	def voltar():
    		janela.destroy()
    		main()

    	def next_viat():
    		clicked = str(chosen2.get())
    		if clicked == "Reparação":
    			instrucao = f"SELECT Nome_cond, Modelo, Marca, N_tel FROM Reparacao WHERE Ficha = 2"
    		elif clicked == "Manutenção":
    			instrucao = f"SELECT Nome_cond, Modelo, Marca, N_tel FROM Manutencao WHERE Ficha = 2"
    		cursor.execute(instrucao)
    		dados = cursor.fetchall()
    		database.commit()
    		if len(dados) >= 1:
    			messagebox.showinfo("Próxima Viatura", f"Nome do Condutor: {dados[0][0]}\nModelo da viatura: {dados[0][1]}\nMarca da viatura: {dados[0][2]}\nN° Tel do Condutor: {dados[0][3]}")
    		else:
    			messagebox.showinfo("Próxima Viatura", "Nenhuma viatura a espera.")

    	janela = Tk()
    	janela.title("Oficina Quase Perfeita - Outras funcionalidades")
    	janela.config(bg="#006d68")
    	janela.geometry("800x600+200+0")
    	janela.resizable(False, False)

    	barra_menu = Menu(janela)
    	menu_ver = Menu(barra_menu, tearoff=0)
    	menu_ver.add_command(label="Página anterior", command=voltar)
    	menu_ver.add_separator()
    	menu_ver.add_command(label="Sair", command=sair)
    	barra_menu.add_cascade(label="Ver", menu=menu_ver)

    	janela.config(menu=barra_menu)

    	area2 = Frame(janela, bg="#000000", width="800", height="600")
    	area2.place(x=200, y=0)

    	lb_del_viat = Label(area2, text="Eliminar Viatura", font=("Arial", 12), bg="#000000", fg="#c1c1c1")
    	lb_del_viat.place(x=25, y=20)

    	lb_num_BI = Label(area2, text="N° Tel do Condutor", font=("Arial", 12), bg="#000000", fg="#c1c1c1")
    	lb_num_BI.place(x=25, y=70)

    	in_num_tel = Entry(area2, width=40, font=("Arial", 12))
    	in_num_tel.place(x=185, y=70)

    	bt_remove = Button(area2, width="10", text="Remover", font=("Arial", 12), bg="#006d68", activebackground="#035a56", command=del_viat)
    	bt_remove.place(x=25, y=120)

    	chosen = StringVar()

    	rb_reparacao = Radiobutton(area2, text="Reparação", value="Reparação", variable=chosen)
    	rb_reparacao.place(x=360, y=120)

    	rb_manutencao = Radiobutton(area2, text="Manutenção", value="Manutenção", variable=chosen)
    	rb_manutencao.place(x=450, y=120)

    	lb_qtd_marca = Label(area2, text="Quantidades de vezes que uma marca aparece no sistema", font=("Arial", 12), bg="#000000", fg="#c1c1c1")
    	lb_qtd_marca.place(x=25, y=180)

    	lb_marca = Label(area2, text="Marca da Viatura", font=("Arial", 12), bg="#000000", fg="#c1c1c1")
    	lb_marca.place(x=25, y=230)

    	in_marca = Entry(area2, width=40, font=("Arial", 12))
    	in_marca.place(x=185, y=230)

    	bt_enter = Button(area2, width="10", text="Procurar", font=("Arial", 12), bg="#006d68", activebackground="#035a56", command=qtd_marca)
    	bt_enter.place(x=25, y=280)

    	lb_next_viat = Label(area2, text="Próxima Viatura a ser atendida", font=("Arial", 12), bg="#000000", fg="#c1c1c1")
    	lb_next_viat.place(x=25, y=340)

    	bt_next = Button(area2, width="10", text="Ver", font=("Arial", 12), bg="#006d68", activebackground="#035a56", command=next_viat)
    	bt_next.place(x=25, y=390)

    	chosen2 = StringVar()

    	rb_reparacao2 = Radiobutton(area2, text="Reparação", value="Reparação", variable=chosen2)
    	rb_reparacao2.place(x=360, y=390)

    	rb_manutencao2 = Radiobutton(area2, text="Manutenção", value="Manutenção", variable=chosen2)
    	rb_manutencao2.place(x=450, y=390)

    	lb_label = Label(janela, text="Oficina Quase\nPerfeita", font=("Arial", 14), bg="#006d68", fg="#000000")
    	lb_label.place(x=30, y=220)

    	janela.mainloop()

    def other_function():
    	janela.destroy()
    	others()

    def update_list_box():
    	instrucao = f"SELECT Ficha, Servico, Modelo, Marca, Nome_cond, Morada, N_tel FROM Reparacao"
    	cursor.execute(instrucao)
    	dados = cursor.fetchall()
    	database.commit()
    	if len(dados) >= 1:
    		for x in dados:
    			x = f"{x[0]} - {x[1]} - {x[2]} - {x[3]} - {x[4]} - {x[5]} - {x[6]}"
    			lista_viat.insert(END, x)

    	instrucao = f"SELECT Ficha, Servico, Modelo, Marca, Nome_cond, Morada, N_tel FROM Manutencao"
    	cursor.execute(instrucao)
    	dados = cursor.fetchall()
    	database.commit()
    	if len(dados) >= 1:
    		for x in dados:
    			x = f"{x[0]} - {x[1]} - {x[2]} - {x[3]} - {x[4]} - {x[5]} - {x[6]}"
    			lista_viat.insert(END, x)

    janela = Tk()
    janela.title("Oficina Quase Perfeita - Viaturas Cadastradas")
    janela.config(bg="#006d68")
    janela.geometry("800x600+200+0")
    janela.resizable(False, False)

    barra_menu = Menu(janela)
    menu_ver = Menu(barra_menu, tearoff=0)
    menu_ver.add_command(label="Cadastrar funcinário", command=cad_func)
    menu_ver.add_command(label="Eliminar cadastro de funcionário", command=remove_func)
    menu_ver.add_command(label="Cadastrar Viatura", command=cad_viat)
    menu_ver.add_command(label="Quantidades de carros atendidos", command=show_atendidos)
    menu_ver.add_command(label="Outras funcionalidades", command=other_function)
    menu_ver.add_separator()
    menu_ver.add_command(label="Página inicial", command=pag_inicial)
    menu_ver.add_command(label="Sair", command=sair)
    barra_menu.add_cascade(label="Ver", menu=menu_ver)

    janela.config(menu=barra_menu)
    
    area2 = Frame(janela, bg="#000000", width="600", height="600")
    area2.place(x=200, y=0)

    lb_1 = Label(area2, text="Veículos Cadastrados", font=("Arial", 18), bg="#000000", fg="#c1c1c1")
    lb_1.place(x=170, y=16)

    lista_viat = Listbox(area2, width=80, height=30, font=("Arial", 10), bg="#000000", fg="#ffffff")
    lista_viat.place(x=20, y=60)

    update_list_box()

    lb_label = Label(janela, text="Oficina Quase\nPerfeita", font=("Arial", 14), bg="#006d68", fg="#000000")
    lb_label.place(x=30, y=220)

    janela.mainloop()

def tela_cad_func():
	def bt_cad_click():
		nome = str(in_nome.get()).strip()
		num_BI = str(in_num_BI.get())
		num_tel = str(in_num_tel.get())
		senha = str(in_senha.get())
		if nome == "" or senha == "":
		    messagebox.showwarning("Atenção", "Preencha todos os campos.")
		else:
			cursor.execute("""CREATE TABLE IF NOT EXISTS Funcionarios(Nome text, N_BI text, N_Tel text, Senha text)""")
			instrucao = f"INSERT INTO Funcionarios VALUES('{nome}', '{num_BI}', '{num_tel}', '{senha}')"
			cursor.execute(instrucao)
			database.commit()
			messagebox.showinfo("Verificação", "Cadastro realizado com sucesso.")
			in_nome.delete(0, "end")
			in_num_BI.delete(0, "end")
			in_num_tel.delete(0, "end")
			in_senha.delete(0, "end")

	def voltar():
		janela.destroy()
		main()

	def sair():
		janela.destroy()

	janela = Tk()
	janela.title("Oficina Quase Perfeita - Cadastro de funcionários")
	janela.config(bg="#006d68")
	janela.resizable(False, False)
	janela.geometry("600x500+200+0")

	barra_menu = Menu(janela)
	menu_ver = Menu(barra_menu, tearoff=0)
	menu_ver.add_command(label="Página anterior", command=voltar)
	menu_ver.add_separator()
	menu_ver.add_command(label="Sair", command=sair)
	barra_menu.add_cascade(label="Ver", menu=menu_ver)
	
	janela.config(menu=barra_menu)

	area2 = Frame(janela, bg="#000000", width="400", height="500")
	area2.place(x=200)

	lb_label = Label(janela, text="Oficina Quase\nPerfeita", font=("Arial", 14), bg="#006d68", fg="#000000")
	lb_label.place(x=30, y=180)

	lb_nome = Label(area2, text="Nome", font=("Arial", 12), bg="#000000", fg="#c1c1c1")
	lb_nome.place(x=25, y=130)

	in_nome = Entry(area2, width="25", font=("Arial", 12))
	in_nome.place(x=100, y=130)
	
	lb_num_BI = Label(area2, text="N° BI", font=("Arial", 12), bg="#000000", fg="#c1c1c1")
	lb_num_BI.place(x=25, y=180)

	in_num_BI = Entry(area2, width="25", font=("Arial", 12))
	in_num_BI.place(x=100, y=180)

	lb_num_tel = Label(area2, text="N° Tel", font=("Arial", 12), bg="#000000", fg="#c1c1c1")
	lb_num_tel.place(x=25, y=230)

	in_num_tel = Entry(area2, width="25", font=("Arial", 12))
	in_num_tel.place(x=100, y=230)

	lb_senha = Label(area2, text="Senha", font=("Arial", 12), bg="#000000", fg="#c1c1c1")
	lb_senha.place(x=25, y=280)

	in_senha = Entry(area2, width="25", font=("Arial", 12), show="*")
	in_senha.place(x=100, y=280)

	bt_cad = Button(area2, width="10", text="Cadastrar", font=("Arial", 12), bg="#006d68", activebackground="#035a56", command=bt_cad_click)
	bt_cad.place(x=170, y=330)

	janela.mainloop()

def tela_login():
	def bt_login_click():
		nome = str(in_nome.get())
		senha = str(in_senha.get())
		tupla = (nome, senha)
		dados_user = []
		dados_user.append(tupla)
		instrucao = f"SELECT Nome, Senha FROM Funcionarios WHERE Nome = '{nome}' AND Senha = '{senha}'"
		cursor.execute(instrucao)
		dados = cursor.fetchall()
		database.commit()
		if dados == dados_user:
			messagebox.showinfo("Verificação", "Acesso concedido.")
			janela.destroy()
			main()
		elif nome == "" or senha == "":
			messagebox.showinfo("Atenção", "Preencha todos os campos.")
		else:
			messagebox.showwarning("Verificação", "Acesso negado.")
			in_nome.delete(0, "end")
			in_senha.delete(0, "end")

	def voltar():
		janela.destroy()
		tela_inicial()

	def sair():
		janela.destroy()

	janela = Tk()
	janela.title("Oficina Quase Perfeita - Entrar")
	janela.config(bg="#006d68")
	janela.resizable(False, False)
	janela.geometry("600x500+200+0")
	
	barra_menu = Menu(janela)
	menu_ver = Menu(barra_menu, tearoff=0)
	menu_ver.add_command(label="Página anterior", command=voltar)
	menu_ver.add_separator()
	menu_ver.add_command(label="Sair", command=sair)
	barra_menu.add_cascade(label="Ver", menu=menu_ver)
	
	janela.config(menu=barra_menu)
    
	area2 = Frame(janela, bg="#000000", width="400", height="500")
	area2.place(x=200)

	lb_label = Label(janela, text="Oficina Quase\nPerfeita", font=("Arial", 14), bg="#006d68", fg="#000000")
	lb_label.place(x=30, y=180)

	lb_nome = Label(area2, text="Nome", font=("Arial", 12), bg="#000000", fg="#c1c1c1")
	lb_nome.place(x=25, y=150)

	in_nome = Entry(area2, width="25", font=("Arial", 12))
	in_nome.place(x=100, y=150)

	lb_senha = Label(area2, text="Senha", font=("Arial", 12), bg="#000000", fg="#c1c1c1")
	lb_senha.place(x=25, y=210)

	in_senha = Entry(area2, width="25", font=("Arial", 12), show="*")
	in_senha.place(x=100, y=210)

	bt_login = Button(area2, width="10", activebackground="#035a56", text="Login", font=("Arial", 12), bg="#006d68", command=bt_login_click)
	bt_login.place(x=170, y=270)

	janela.mainloop()

def tela_inicial():
    def login():
        janela.destroy()
        tela_login()
    
    def sobre():
        messagebox.showinfo("Sobre este software", "Este software foi concebido pelos estudantes\ndo curso de Engenharia em Informática:\n*  Luís Manuel Muhele\n*  Marcelino Jamba Manuel\n*  Filomena Demilde Ndala")
    
    def sair():
        janela.destroy()

    janela = Tk()
    janela.title("Oficina Quase Perfeita")
    janela.config(bg="#006d68")
    janela.geometry("800x600+200+0")
    janela.resizable(False, False)

    barra_menu = Menu(janela)
    menu_ver = Menu(barra_menu, tearoff=0)
    menu_ver.add_command(label="Login", command=login)
    menu_ver.add_separator()
    menu_ver.add_command(label="Sair", command=sair)
    barra_menu.add_cascade(label="Ver", menu=menu_ver)

    menu_ajuda = Menu(barra_menu, tearoff=0)
    menu_ajuda.add_command(label="Sobre", command=sobre)
    barra_menu.add_cascade(label="Sobre", menu=menu_ajuda)

    janela.config(menu=barra_menu)
    
    area2 = Frame(janela, bg="#000000", width="600", height="600")
    area2.place(x=200, y=0)
    
    lb_1 = Label(area2, text="Bem-Vindos à Oficina Quase Perfeita", font=("Arial", 18), bg="#000000", fg="#c1c1c1")
    lb_1.place(x=95, y=20)

    lb_slogan = Label(area2, text="Cuide da sua saúde, porque da da sua viatura cuidamos nós!", font=("Comic Sans MS", 10), bg="#000000", fg="#c1c1c1")
    lb_slogan.place(x=115, y=55)

    lb_service = Label(area2, text="Prestamos serviços de reparação e manutenção de viaturas", font=("Arial", 12), bg="#000000", fg="#c1c1c1")
    lb_service.place(x=35, y=120)

    lb_2 = Label(area2, text="Aceda às ferramentas do gestor abaixo descritas, fazendo login a sua conta", font=("Arial", 12), bg="#000000", fg="#c1c1c1")
    lb_2.place(x=35, y=170)

    lb_3 = Label(area2, text="* Cadastrar novos funcionários;", font=("Arial", 12), bg="#000000", fg="#006d68")
    lb_3.place(x=35, y=230)

    lb_4 = Label(area2, text="* Cadastrar e remover viaturas;", font=("Arial", 12), bg="#000000", fg="#006d68")
    lb_4.place(x=35, y=270)

    lb_5 = Label(area2, text="* Saber qual é a próxima viatura a ser atenndida;", font=("Arial", 12), bg="#000000", fg="#006d68")
    lb_5.place(x=35, y=310)

    lb_6 = Label(area2, text="* Contabilizar o total de viaturas atendidas por dia;", font=("Arial", 12), bg="#000000", fg="#006d68")
    lb_6.place(x=35, y=350)

    lb_7 = Label(area2, text="* Saber quantas vezes uma marca aparece no sistema.", font=("Arial", 12), bg="#000000", fg="#006d68")
    lb_7.place(x=35, y=390)

    lb_label = Label(janela, text="Oficina Quase\nPerfeita", font=("Arial", 14), bg="#006d68", fg="#000000")
    lb_label.place(x=30, y=220)

    janela.mainloop()

if __name__ == "__main__":
    tela_inicial()
    
database.close()