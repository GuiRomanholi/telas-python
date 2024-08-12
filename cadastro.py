from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout

class Cadastro( App ):

    def build(self):
        box = BoxLayout(orientation ='vertical')
        txt_box1 = BoxLayout(orientation ='horizontal')
        txt_box2 = BoxLayout(orientation ='horizontal')
        txt_box3 = BoxLayout(orientation ='horizontal')
        btn_box = BoxLayout(orientation='horizontal')

        lbl_nome = Label(text="Digite seu nome: ")
        txt_nome = TextInput()
        lbl_telefone = Label(text="Digite seu Telefone: ")
        txt_tel = TextInput()
        lbl_email = Label(text="Digite seu email: ")
        txt_email = TextInput()
        btn_salvo = Button(text='Salvar')
        btn_pesq = Button(text='Pesquisar')

        box.add_widget(txt_box1)
        box.add_widget(txt_box2)
        box.add_widget(txt_box3)
        box.add_widget(btn_box)

        txt_box1.add_widget(lbl_nome)
        txt_box1.add_widget(txt_nome)

        txt_box2.add_widget(lbl_telefone)
        txt_box2.add_widget(txt_tel)

        txt_box3.add_widget(lbl_email)
        txt_box3.add_widget(txt_email)

        btn_box.add_widget(btn_salvo)
        btn_box.add_widget(btn_pesq)

        return box


obj_cadastro = Cadastro()
obj_cadastro.run()


