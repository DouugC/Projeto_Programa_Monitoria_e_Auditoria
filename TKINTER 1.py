from tkinter import *
from datetime import date
import numpy as np
from tkinter import ttk
from tkinter import messagebox

Cinza = '#BDBDBD'
Preto = '#000000'
Cinza_Claro = '#D8D8D8'
Today = date.today()
All_rights_reserved = '  ©  Todos os direitos reservados, Douglas Costa'

# valores dos itens do checklist

item_value10 = [0.10, '10%']
item_value15 = [0.15, '15%']
item_value20 = [0.20, '20%']
item_value25 = [0.25, '25%']
item_value30 = [0.30, '30%']
item_value100 = [1.00, '100%']


# Função para gerar os números Random -----------------------------------------------------------
def id_random():
    numero_aleatorio = np.random.randint(1, 999, (3,))
    ID_text['text'] = numero_aleatorio


# Função para validar se os campos obrigatórios foram preenchidos
def preencher_obrigatorio():
    if Monitorado_Por_Text.get() == "" or Nome_Analisado_Text.get() == "" \
            or Matricula_Text.get() == "" or ID_text == ""\
            or Fila_Text == "" or Motivo_do_contato_Text == "" or Motivo_do_contato_Text == ""\
            or Celula_Text == "" or Data_e_hora_atendimento_Text == "":
        messagebox.showinfo(title="ERRO", message='Digite todos os dados antes de Salvar')
        return
    Tabela.insert("", "end", values=(ID_text['text'], Data_Monitoria_Text.get(), Monitorado_Por_Text.get(), Nome_Analisado_Text.get(), Matricula_Text.get(), Celula_Text.get(),
                                     Fila_Text.get(), Protocolo_Text.get(), Motivo_do_contato_Text.get(), Data_e_hora_atendimento_Text.get(), NotaFinal_Label['text']))


# Função para salvar os dados salvos nas caixas de texto  ----------------------------------------
def dados():
    defmonitoradopor = Monitorado_Por_Text.get()
    defnomeanalisado = Nome_Analisado_Text.get()
    defmatricula = Matricula_Text.get()
    defcelula = Celula_Text.get()
    defila = Fila_Text.get()
    defprotocolo = Protocolo_Text.get()
    defdataehoradoatendimento = Data_e_hora_atendimento_Text.get()
    defmotivodocontato = Motivo_do_contato_Text.get()
    defid = ID_text['text']
    defdatadaanalise = Data_Monitoria_Text.get()

    print(defid, defdatadaanalise, defmonitoradopor, defnomeanalisado, defmatricula, defcelula, defila, defprotocolo, defdataehoradoatendimento, defmotivodocontato)


def item1_def():
    valoritem1 = item_value10[1]
    item1_label['text'] = valoritem1


def item2_def():
    valoritem2 = item_value15[1]
    item2_label['text'] = valoritem2


def item3_def_100():
    valoritem3100 = item_value100[1]
    item9_label['text'] = valoritem3100


# Informações sobre tamanho da Janela, cor de fundo, icone da Janela e Título da Janela --
Janela = Tk()
Janela.title('       Relatório de Monitoria')
Janela.geometry('1300x2000')
Janela.configure(bg='white')


# Canvas
canvas = Canvas(Janela, scrollregion=(0, 0, 2000, 5000))
canvas.create_line(0, 0, 0, 2000, fill='green', width=10)
canvas.pack(expand=True, fill='both')


# Frame --------------------------------------------------------------------------------
frame = Frame(canvas, bg=Cinza)
canvas.create_window(0, 0, window=frame, anchor=NW, width=1200, height=1500)
frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))


# MouseScroll ----------------------------------------------------------------------------
canvas.bind('<MouseWheel>', lambda event: canvas.yview_scroll(-int(event.delta / 100), "units"))


# Scrollbar -------------------------------------------------------------------------------
scrollbar = Scrollbar(Janela, orient='vertical', command=canvas.yview())
canvas.configure(yscrollcommand=scrollbar.set)
scrollbar.pack(side=RIGHT, fill=BOTH, expand=True)


# Bottons - Label - Entry -----------------------------------------------------------------
ID_text = Label(frame, width=12, border="2")
ID_text.place(x=20, y=20)
ID = Button(frame, command=id_random, width=14, height=1, justify="center", text="Gerar Número")
ID.place(x=123, y=19)

espaco_coluna_2 = Label(frame, width=15, bg=Cinza, height=1)
espaco_coluna_2.grid(column=3, row=0)
Buscar_Text = Entry(frame, width=20, border="2")
Buscar_Text.place(x=500, y=19)
Buscar = Button(frame, width=15, height=1, justify="center", text="Buscar Nome")
Buscar.place(x=638, y=19)

Excluir_monitoria = Button(frame, width=15, height=1, justify="center", text="Excluir Monitoria")
Excluir_monitoria.place(x=920, y=430)


Monitorado_Por = Label(frame, width=25, height=1, justify="left", text="Monitorado Por:", bg=Cinza_Claro, anchor=W)
Monitorado_Por.place(x=20, y=64)
Monitorado_Por_Text = Entry(frame, width=40, border="2")
Monitorado_Por_Text.place(x=210, y=64)

Data_Monitoria_Text = Entry(frame, width=20, border="2")
Data_Monitoria_Text.insert(0, Today)
Data_Monitoria_Text.place(x=500, y=64)
Data_Monitoria = Label(frame, width=25, height=1, justify="center", text="Data da Monitoria", bg=Cinza_Claro, anchor=W)
Data_Monitoria.place(x=638, y=64)

Nome_Analisado = Label(frame, width=25, height=1, justify="center", text="Nome Analisado:", bg=Cinza_Claro, anchor=W)
Nome_Analisado.place(x=20, y=105)
Nome_Analisado_Text = Entry(frame, width=40, border="2")
Nome_Analisado_Text.place(x=210, y=105)

Matricula = Label(frame, width=25, height=1, justify="center", text="Matrícula:", bg=Cinza_Claro, anchor=W)
Matricula.place(x=20, y=147)
Matricula_Text = Entry(frame, width=40, border="2")
Matricula_Text.place(x=210, y=147)

Celula = Label(frame, width=25, height=1, justify="center", text="Célula:", bg=Cinza_Claro, anchor=W)
Celula.place(x=20, y=190)
Celula_Text = Entry(frame, width=40, border="2")
Celula_Text.place(x=210, y=190)

Fila = Label(frame, width=25, height=1, justify="center", text="Fila:", bg=Cinza_Claro, anchor=W)
Fila.place(x=20, y=232)
Fila_Text = Entry(frame, width=40, border="2")
Fila_Text.place(x=210, y=232)

Protocolo = Label(frame, width=25, height=1, justify="center", text="Protocolo:", bg=Cinza_Claro, anchor=W)
Protocolo.place(x=20, y=274)
Protocolo_Text = Entry(frame, width=40, border="2")
Protocolo_Text.place(x=210, y=274)

Data_e_hora_atendimento = Label(frame, width=25, height=1, anchor=W, text="Data e Hora do Atendimento:", bg=Cinza_Claro)
Data_e_hora_atendimento.place(x=20, y=316)
Data_e_hora_atendimento_Text = Entry(frame, width=40, border="2")
Data_e_hora_atendimento_Text.place(x=210, y=316)

Motivo_do_contato = Label(frame, width=25, height=1, anchor=W, text="Motivo do Contato:", bg=Cinza_Claro)
Motivo_do_contato.place(x=20, y=357)
Motivo_do_contato_Text = Entry(frame, width=40, border="2")
Motivo_do_contato_Text.place(x=210, y=357)

Salvar = Button(frame, command=preencher_obrigatorio, width=10, height=1, justify="center", text="Salvar")
Salvar.place(x=1050, y=430)

Check_list = Label(frame, width=25, height=1, text="CheckList do Atendimento", bg=Cinza, font='Arial 10')
Check_list.place(x=50, y=450)

Desconto = Label(frame, width=8, height=2, text="Desconto", bg=Cinza, font='Arial 10')
Desconto.place(x=621, y=450)

NotaFinal = Label(frame, width=10, height=2, text="Nota Final", bg=Cinza, font='Arial 10')
NotaFinal.place(x=775, y=450)

NotaFinal_Label = Label(frame, width=10, height=1, )
NotaFinal_Label.place(x=785, y=480)

# Itens para o checklist ---------------------------------------------------------------
item1 = Checkbutton(frame, width=80, height=1, text='Tratativa ocorreu no prazo de 24h', offvalue=0, command=item1_def,
                    anchor=W)
item1.place(x=10, y=480,)
item2 = Checkbutton(frame, width=80, height=1, text='2.1 Avaliou Ponto de Controle primeira entrega',
                    command=item2_def, anchor=W)
item2.place(x=10, y=500)
item3 = Checkbutton(frame, width=80, height=1, text='2.2 Avaliou Ponto de Controle da intância de Reversa/troca/cancelamento',
                    anchor=W, command=item2_def)
item3.place(x=10, y=520)
item4 = Checkbutton(frame, width=80, height=1, text='2.3 Avaliou histórico de Atendimento e interação CRL',
                    anchor=W, command=item2_def)
item4.place(x=10, y=540)
item5 = Checkbutton(frame, width=80, height=1, text='2.4 Avaliou descrição do Solicitante',
                    anchor=W, command=item1_def)
item5.place(x=10, y=560)
item6 = Checkbutton(frame, width=80, height=1, text='2.5 Avaliou aba de anexos com os comprovantes/Autorização',
                    anchor=W, command=item2_def)
item6.place(x=10, y=580)
item7 = Checkbutton(frame, width=80, height=1, text='3.1 Aplicou solução correta (IF aprovada/IF reprovada/Encerrar tratativa)',
                    anchor=W, command=item1_def)
item7.place(x=10, y=600)
item8 = Checkbutton(frame, width=80, height=1, text='3.2 Inseriu justificativa',
                    anchor=W, command=item1_def)
item8.place(x=10, y=620)
item9 = Checkbutton(frame, width=80, height=1, text='Não liberação da instancia com pontos de controle elegíveis ',
                    anchor=W, command=item3_def_100)
item9.place(x=10, y=640)
item10 = Checkbutton(frame, width=80, height=1, text='Liberação da Instancia de forma indevida - sem ponto finalizador de acordo com política',
                    anchor=W, command=item3_def_100)
item10.place(x=10, y=660)
item11 = Checkbutton(frame, width=80, height=1, text='Direcionamento indevido paras as áreas',
                    anchor=W, command=item3_def_100)
item11.place(x=10, y=680)


# Valor do item do Checklist
item1_label = Label(frame, width=10, height=1)
item1_label.place(x=620, y=480)
item2_label = Label(frame, width=10, height=1)
item2_label.place(x=620, y=500)
item3_label = Label(frame, width=10, height=1)
item3_label.place(x=620, y=520)
item4_label = Label(frame, width=10, height=1)
item4_label.place(x=620, y=540)
item5_label = Label(frame, width=10, height=1)
item5_label.place(x=620, y=560)
item6_label = Label(frame, width=10, height=1)
item6_label.place(x=620, y=580)
item7_label = Label(frame, width=10, height=1)
item7_label.place(x=620, y=600)
item8_label = Label(frame, width=10, height=1)
item8_label.place(x=620, y=620)
item9_label = Label(frame, width=10, height=1)
item9_label.place(x=620, y=640)
item10_label = Label(frame, width=10, height=1)
item10_label.place(x=620, y=660)
item11_label = Label(frame, width=10, height=1)
item11_label.place(x=620, y=680)


Tabela_titulo = Label(frame, width=10, height=1, text="Tabela", bg=Cinza, font='Arial 11')
Tabela_titulo.place(x=50, y=773)

# Tabela de dados na frame Tkinter -----------------------------------------------------
Tabela = ttk.Treeview(frame, selectmode=EXTENDED, columns=("column1", "column2", "column3", "column4", "column5", "column6",
                                                             "column7", "column8", "column9", "column10", "column11"),
                      show='headings')
Tabela.column('column1', width=50, minwidth=50, stretch=NO)
Tabela.heading('#1', text='ID')
Tabela.place(x=10, y=800)
Tabela.column('column2', width=100, minwidth=50, stretch=NO)
Tabela.heading('#2', text='Data da Monitoria')
Tabela.place(x=10, y=800)
Tabela.column('column3', width=100, minwidth=50, stretch=NO)
Tabela.heading('#3', text='Monitorado Por')
Tabela.place(x=10, y=800)
Tabela.column('column4', width=120, minwidth=50, stretch=NO)
Tabela.heading('#4', text='Nome Analisado')
Tabela.place(x=10, y=800)
Tabela.column('column5', width=100, minwidth=50, stretch=NO)
Tabela.heading('#5', text='Matricula')
Tabela.place(x=10, y=800)
Tabela.column('column6', width=80, minwidth=50, stretch=NO)
Tabela.heading('#6', text='Célula')
Tabela.place(x=10, y=800)
Tabela.column('column7', width=80, minwidth=50, stretch=NO)
Tabela.heading('#7', text='Fila')
Tabela.place(x=10, y=800)
Tabela.column('column8', width=100, minwidth=50, stretch=NO)
Tabela.heading('#8', text='Protocolo')
Tabela.place(x=10, y=800)
Tabela.column('column9', width=100, minwidth=50, stretch=NO)
Tabela.heading('#9', text='Motivo do Contato')
Tabela.place(x=10, y=800)
Tabela.column('column10', width=100, minwidth=50, stretch=NO)
Tabela.heading('#10', text='Data e hora do atendimento')
Tabela.place(x=10, y=800)
Tabela.column('column11', width=50, minwidth=50, stretch=NO)
Tabela.heading('#11', text='Nota Final')
Tabela.place(x=10, y=800)

Todos_os_direitos_reservados = Label(frame, width=50, bg=Cinza, text=All_rights_reserved)
Todos_os_direitos_reservados.place(x=810, y=1900)


Janela.mainloop()