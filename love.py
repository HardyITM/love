from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
import random

reasons_love = ['Самая красивая', 'Самая милая', 'Открытая', 'Любящая',
                'Переживаешь за меня и думаешь обо мне', 'Моя любовь на всю жизнь',
                'Веселая', 'Мило-обидчивая', 'Умная', 'Красиво поешь',
                'Заботливая', 'Иногда грубая(', 'Интересная', 'Глупенькая в хорошем смысле :)',
                'Добрая', 'Самая лучшая', 'Нежная', 'Худенькая)', 'Искренняя',
                'Честная', 'Отзывчивая', 'Хороший вкус в музыке',
                'Самый лучший человек в моей жизни', 'Божествеенная',
                'Шутки, которые говоришь раз в год \n они просто разрывают',
                'Самая дорогая для меня',
                ]

class Main(App):

    def build(self):
        box = BoxLayout(orientation='vertical')
        btn1 = Button(text='Нажми на меня <3',
                      font_size=36,
                      background_color= [.6, 0, 0, 1],
                      background_normal = '',
                      on_press = self.btn_press)
        label = Label(text=f'Я еще буду доделывать приложение,\n пока это исходник'
                           f' очень сильно тебя люблю <3', font_size=16)
        box.add_widget(btn1)
        box.add_widget(label)
        
        return box
        

    def btn_press(self, instance):
        instance.text = random.choice(reasons_love)

if __name__ == "__main__":
    Main().run()
