import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
  # versão do kivy


class CarreiroApp(App):

    def build(self):
        self.title = 'Marcação de Carreiro'
        self.layout = BoxLayout(orientation='vertical', padding=10)

        self.name_input = TextInput(hint_text='Nome da Pessoa')
        self.line_length_input = TextInput(hint_text='Comprimento da Linha (metros)')
        self.spacing_input = TextInput(hint_text='Espaçamento entre Mudas (centímetros)')
        self.start_button = Button(text='Iniciar Carreiro')
        self.end_button = Button(text='Finalizar Carreiro')
        self.add_button = Button(text='+ Carreiro')
        self.remove_button = Button(text='- Carreiro')
        self.view_button = Button(text='Ver Carreiros')
        self.log_label = Label(text='Registros de Carreiros:')

        self.start_button.bind(on_press=self.start_carreiro)
        self.end_button.bind(on_press=self.end_carreiro)
        self.add_button.bind(on_press=self.add_carreiro)
        self.remove_button.bind(on_press=self.remove_carreiro)
        self.view_button.bind(on_press=self.view_carreiros)

        self.layout.add_widget(self.name_input)
        self.layout.add_widget(self.line_length_input)
        self.layout.add_widget(self.spacing_input)
        self.layout.add_widget(self.start_button)
        self.layout.add_widget(self.end_button)
        self.layout.add_widget(self.add_button)
        self.layout.add_widget(self.remove_button)
        self.layout.add_widget(self.view_button)
        self.layout.add_widget(self.log_label)

        # Dicionário para armazenar o número de carreiros por pessoa
        self.carreiros_por_pessoa = {}

        return self.layout

    def start_carreiro(self, instance):
        nome = self.name_input.text
        line_length = float(self.line_length_input.text)
        spacing = float(self.spacing_input.text)

        num_mudas = int(line_length * 100 / spacing)  # Converter metros em centímetros
        num_carreiros = num_mudas // 2000  # Uma muda a cada 2000 pés

        if nome in self.carreiros_por_pessoa:
            self.carreiros_por_pessoa[nome] += num_carreiros
        else:
            self.carreiros_por_pessoa[nome] = num_carreiros

        self.log_label.text += f'\nCarreiro iniciado por {nome}. {num_carreiros} carreiros a serem feitos.'

    def end_carreiro(self, instance):
        nome = self.name_input.text
        line_length = float(self.line_length_input.text)
        spacing = float(self.spacing_input.text)

        num_mudas = int(line_length * 100 / spacing)  # Converter metros em centímetros
        num_carreiros = num_mudas // 2000  # Uma muda a cada 2000 pés

        if nome in self.carreiros_por_pessoa:
            self.carreiros_por_pessoa[nome] += num_carreiros
        else:
            self.carreiros_por_pessoa[nome] = num_carreiros

        self.log_label.text += f'\nCarreiro finalizado por {nome}. {num_carreiros} carreiros concluídos.'

    def add_carreiro(self, instance):
        nome = self.name_input.text

        if nome in self.carreiros_por_pessoa:
            self.carreiros_por_pessoa[nome] += 1
        else:
            self.carreiros_por_pessoa[nome] = 1

        self.log_label.text += f'\n+1 Carreiro adicionado para {nome}.'

    def remove_carreiro(self, instance):
        nome = self.name_input.text

        if nome in self.carreiros_por_pessoa:
            if self.carreiros_por_pessoa[nome] > 0:
                self.carreiros_por_pessoa[nome] -= 1
                self.log_label.text += f'\n-1 Carreiro removido de {nome}.'
            else:
                self.log_label.text += f'\n{nome} não tem mais carreiros para remover.'
        else:
            self.log_label.text += f'\n{nome} não tem carreiros registrados.'

    def view_carreiros(self, instance):
        nome = self.name_input.text

        if nome in self.carreiros_por_pessoa:
            num_carreiros = self.carreiros_por_pessoa[nome]
            self.log_label.text += f'\n{nome} fez um total de {num_carreiros} carreiros.'
        else:
            self.log_label.text += f'\n{nome} não tem carreiros registrados.'


if __name__ == '__main__':
    CarreiroApp().run()
