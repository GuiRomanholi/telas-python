from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.config import Config

class GestaoCarros(App):

    lista = []

    carro_atual = None

    txt_marca = TextInput()
    txt_modelo = TextInput()
    txt_ano = TextInput()
    txt_placa = TextInput()

    def __init__(self):
        App.__init__(self)
        Config.set('input', 'mouse', 'mouse,multitouch_on_demand')
    

    def salvar(self, e):
        print("Botão pressionado")
        obj_salvo = {
            "marca": self.txt_marca.text,
            "modelo": self.txt_modelo.text,
            "ano": self.txt_ano.text,
            "placa": self.txt_placa.text
        }
        if self.carro_atual is not None:
            self.lista.remove(self.carro_atual)
            self.carro_atual = None
        self.lista.append(obj_salvo)
        self.txt_marca.text = ""
        self.txt_modelo.text = ""
        self.txt_ano.text = ""
        self.txt_placa.text = ""
        print(self.lista)

    def pesquisar(self, e): 
        for i in self.lista:
            if self.txt_marca.text.lower() in i["marca"].lower():
                self.carro_atual = i
                self.txt_marca.text = i["marca"]
                self.txt_modelo.text = i["modelo"]
                self.txt_ano.text = i["ano"]
                self.txt_placa.text = i["placa"]
                print(i)
                break  # Para após encontrar o primeiro resultado

    def informacoes(self):
        print("App Agenda de Contato")

    def build(self):

        box = BoxLayout(orientation='vertical')
        txt_box_marca = BoxLayout(orientation='horizontal')
        txt_box_modelo = BoxLayout(orientation='horizontal')
        txt_box_ano = BoxLayout(orientation='horizontal')
        txt_box_placa = BoxLayout(orientation='horizontal')
        txt_box_button = BoxLayout(orientation='horizontal')

        lbl_marca = Label(text="Marca:")

        lbl_modelo = Label(text="Modelo:")

        lbl_ano = Label(text="Ano:")

        lbl_placa = Label(text="Placa:")
        

        btn_gravar = Button(text='Gravar', on_release = self.salvar)
        btn_pesquisar = Button(text='Pesquisar', on_release = self.pesquisar)

        box.add_widget(txt_box_marca)
        box.add_widget(txt_box_modelo)
        box.add_widget(txt_box_ano)
        box.add_widget(txt_box_placa)
        box.add_widget(txt_box_button)

        txt_box_marca.add_widget(lbl_marca)
        txt_box_marca.add_widget(self.txt_marca)

        txt_box_modelo.add_widget(lbl_modelo)
        txt_box_modelo.add_widget(self.txt_modelo)

        txt_box_ano.add_widget(lbl_ano)
        txt_box_ano.add_widget(self.txt_ano)

        txt_box_placa.add_widget(lbl_placa)
        txt_box_placa.add_widget(self.txt_placa)

        txt_box_button.add_widget(btn_gravar)
        txt_box_button.add_widget(btn_pesquisar)

        return box

if __name__ == "__main__":
    obj_carro = GestaoCarros()
    obj_carro.informacoes()
    obj_carro.run()