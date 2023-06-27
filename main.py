import os
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.button import MDFlatButton, MDIconButton
from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.gridlayout import MDGridLayout
from kivymd.uix.menu import MDDropdownMenu

from kivymd.uix.tab import MDTabsBase
from kivy.core.window import Window
from kivymd.uix.list import OneLineIconListItem, OneLineListItem, MDList, TwoLineIconListItem, \
    OneLineAvatarIconListItem, IconRightWidget, IconLeftWidget, IRightBodyTouch
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.video import Video
from kivymd.app import MDApp
from kivy.lang import Builder

Window.size = (450, 800)

class MyScreenManager(ScreenManager):
    pass

class MainScreen(Screen):
    pass
class MusicListScreen(Screen):
    pass


class ListIcons(IRightBodyTouch ,MDBoxLayout):
    adaptive_width = True


class AllMusic(MDList):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        music_root_path = '/home/bonface/Music'

        # clear any existing widgets from MyList

        music_files = [m for m in os.listdir(music_root_path) if
                       m.endswith('.mp3') or m.endswith('.wav')]

        for i in music_files:
            list = OneLineAvatarIconListItem(IconLeftWidget(icon = 'music-note',
            theme_icon_color = 'Custom',
            icon_color = (0,0,0,1)),
            ListIcons(MDIconButton(icon = 'dots-vertical',
            theme_icon_color = 'Custom',
            icon_color = (0,0,0,1),
            on_press = lambda x: self.dropdown2(x))),
            text=i,
            theme_text_color ='Custom',
            text_color =(0,0,0,1)
            )
            #button.bind(on_press=lambda x: self.play_video(os.path.join(root_path, x.text)))
            self.add_widget(list)

class VideoListScreen(Screen):
    pass
class AllVideos(MDList):
    sm = ScreenManager()
    video_screen = Screen()
    video_page = MDGridLayout(cols = 1 , rows =1)
    video_screen.add_widget(video_page)
    sm.add_widget(video_screen)
    main = MainScreen()
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        root_path = '/home/bonface/Videos'
        video_files = [f for f in os.listdir(root_path) if
                       f.endswith('.mp4') or f.endswith('.avi') or f.endswith('.mkv')]

        for video_file in video_files:
            button = OneLineListItem(text=f'{video_file}')
            button.bind(on_press=lambda x: self.play_video(os.path.join(root_path, x.text)))
            self.add_widget(button)

        #self.video = Video()
        #self.add_widget(self.video)

    def play_video(self, path):
        #self.clear_widget()
        self.sm.switch_to(self.video_screen)
        self.video = Video()
        self.video_page.add_widget(self.video)
        #self.add_widget(self.video)
        self.video.source = path
        self.video.state = 'play'
        #self.video.volume = 1
class SettingScreen(Screen):
    pass
class myApp(MDApp):
    icon = 'appicon.png'
    title = 'My player'

    def build(self):
        pass



myApp().run()

