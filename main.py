import os
from kivy.config import Config

# Set the window size to fit an average Android device
debugging = True
if debugging:
    Config.set('graphics', 'width', '360')
    Config.set('graphics', 'height', '640')

from kivy.properties import StringProperty, NumericProperty
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen
from kivymd.app import MDApp
from kivy.uix.boxlayout import BoxLayout
from kivy.metrics import dp
from kivy.uix.recycleview import RecycleView
from kivymd.uix.card import MDCard

from scripts.database import check_db, Player, Ship
from scripts.character_methods import CharacterMethods, CharacterCard
from scripts.ship_methods import ShipMethods, ShipCard
from scripts.menu_methods import MenuMethods
from scripts.swipe_manager import SwipeManager

class HomeScreen(Screen):
    pass

class MainScreen(Screen):
    pass

class CharacterScreen(Screen):
    pass

class ShipScreen(Screen):
    pass

class RulesScreen(Screen):
    pass    

class AboutScreen(Screen):
    pass

class CreateCharacterScreen(Screen):
    pass  

class CharacterInfoScreen(Screen):
    pass  

class ShipCreationScreen(Screen):
    pass  

class ShipInfoScreen(Screen):
    pass  

class NavigationBar(BoxLayout):
    pass


class MainApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"

        check_db()

        kv_path = os.path.dirname(__file__)
        Builder.load_file(os.path.join(kv_path, 'kv', 'main.kv'))
        Builder.load_file(os.path.join(kv_path, 'kv', 'about_screen.kv'))
        Builder.load_file(os.path.join(kv_path, 'kv', 'character_info_screen.kv'))
        Builder.load_file(os.path.join(kv_path, 'kv', 'character_sheet.kv'))
        Builder.load_file(os.path.join(kv_path, 'kv', 'create_character_screen.kv'))
        Builder.load_file(os.path.join(kv_path, 'kv', 'home_screen.kv'))
        Builder.load_file(os.path.join(kv_path, 'kv', 'navigation_bar.kv'))
        Builder.load_file(os.path.join(kv_path, 'kv', 'rules_screen.kv'))
        Builder.load_file(os.path.join(kv_path, 'kv', 'ship_creation_screen.kv'))
        Builder.load_file(os.path.join(kv_path, 'kv', 'ship_info_screen.kv'))
        Builder.load_file(os.path.join(kv_path, 'kv', 'ship_screen.kv'))
        
        self.sm = SwipeManager()
        self.sm.add_widget(HomeScreen(name='home'))
        self.sm.add_widget(CharacterScreen(name='character_sheet'))
        self.sm.add_widget(ShipScreen(name='ship_screen'))
        self.sm.add_widget(RulesScreen(name='rules_screen'))
        self.sm.add_widget(AboutScreen(name='about'))
        self.sm.add_widget(CreateCharacterScreen(name='create_character'))
        self.sm.add_widget(CharacterInfoScreen(name='character_info_screen'))
        self.sm.add_widget(ShipCreationScreen(name='ship_creation_screen'))
        self.sm.add_widget(ShipInfoScreen(name='ship_info_screen'))

        root = BoxLayout(orientation='vertical')
        root.add_widget(NavigationBar())
        root.add_widget(self.sm)
        root.ids = {'sm': self.sm, 'create_character': self.sm.get_screen('create_character')}  # Assign the ScreenManager and CreateCharacterScreen to the ids dictionary

        self.character_methods = CharacterMethods(self.sm)  # Initialize CharacterMethods
        self.ship_methods = ShipMethods(self.sm)  # Initialize ShipMethods
        self.menu_methods = MenuMethods(self)  # Initialize MenuMethods

        self.on_start()
        
        return root
    
    def on_start(self):
        # Initialize the dropdown menus
        self.menu_methods.init_menus()
        # Update character/ship list on start
        self.character_methods.update_character_list()
        self.ship_methods.update_ship_list()
    
    def switch_screen(self, screen_name):
        self.sm.current = screen_name
        self.menu_methods.dismiss_menu()

if __name__ == '__main__':
    MainApp().run()

