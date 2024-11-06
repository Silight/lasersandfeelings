import os
from kivy.config import Config

# Set the window size to fit an average Android device
debugging = True
if debugging:
    Config.set('graphics', 'width', '360')
    Config.set('graphics', 'height', '640')

from kivy.properties import StringProperty, NumericProperty
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen, SlideTransition
from kivymd.app import MDApp
from kivy.uix.boxlayout import BoxLayout
from kivymd.uix.label import MDLabel
from kivymd.uix.menu import MDDropdownMenu
from kivymd.uix.button import MDRaisedButton
from kivy.metrics import dp
from kivymd.theming import ThemeManager
from scripts.database import check_db, Player, Ship
from kivy.uix.recycleview import RecycleView
from kivy.uix.recycleview.views import RecycleDataViewBehavior
from kivymd.uix.card import MDCard
from scripts.character_methods import CharacterMethods  # Import the CharacterMethods class
from scripts.ship_methods import ShipMethods  # Import the ShipMethods class
from scripts.menu_methods import MenuMethods  # Import the MenuMethods class

class HomeScreen(Screen):
    pass

class MainScreen(Screen):
    pass

class CharacterScreen(Screen):
    pass

class AboutScreen(Screen):
    pass

class CreateCharacterScreen(Screen):
    pass

class CharacterInfoScreen(Screen):
    pass

class RulesScreen(Screen):
    pass

class ShipInfoScreen(Screen):
    pass

class ShipCreationScreen(Screen):
    pass

class ShipScreen(Screen):
    pass

class RulesScreen(Screen):
    pass

class NavigationBar(BoxLayout):
    pass

class CharacterList(RecycleView):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.data = []

    def update_characters(self, characters):
        self.data = [{'player_id': char[0], 'name': str(char[1]), 'style': str(char[2]), 'role': str(char[3]), 'goal': str(char[4]), 'number': str(char[5])} for char in characters]

class CharacterCard(MDCard):
    player_id = NumericProperty()
    name = StringProperty()
    style = StringProperty()
    role = StringProperty()
    goal = StringProperty()
    number = StringProperty()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'
        self.size_hint = (1, None)
        self.height = dp(150)
        self.padding = dp(10)
        self.spacing = dp(10)
        self.on_release = self.open_character_info

    def open_character_info(self):
        app = MDApp.get_running_app()
        app.character_methods.open_character_info(self.player_id, self.name, self.style, self.role, self.goal, self.number)

class ShipList(RecycleView):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.data = []

    def update_ships(self, ships):
        self.data = [{'ship_id': ship[0], 'ship_name': str(ship[1]), 'strength_one': str(ship[2]), 'strength_two': str(ship[3]), 'problem': str(ship[4]), 'ship_notes': str(ship[5])} for ship in ships]

class ShipCard(MDCard):
    ship_id = NumericProperty()
    ship_name = StringProperty()
    strength_one = StringProperty()
    strength_two = StringProperty()
    problem = StringProperty()
    ship_notes = StringProperty()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'
        self.size_hint = (1, None)
        self.height = dp(150)
        self.padding = dp(10)
        self.spacing = dp(10)
        self.on_release = self.open_ship_info
    
    def open_ship_info(self):
        app = MDApp.get_running_app()
        app.ship_methods.open_ship_info(self.ship_id, self.ship_name, self.strength_one, self.strength_two, self.problem, self.ship_notes)

class MainApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"

        check_db()

        kv_path = os.path.dirname(__file__)
        Builder.load_file(os.path.join(kv_path, 'kv', 'home_screen.kv'))
        Builder.load_file(os.path.join(kv_path, 'kv', 'character_sheet.kv'))
        Builder.load_file(os.path.join(kv_path, 'kv', 'navigation_bar.kv'))
        Builder.load_file(os.path.join(kv_path, 'kv', 'about_screen.kv'))
        Builder.load_file(os.path.join(kv_path, 'kv', 'create_character_screen.kv'))
        Builder.load_file(os.path.join(kv_path, 'kv', 'character_info_screen.kv'))
        Builder.load_file(os.path.join(kv_path, 'kv', 'ship_creation_screen.kv'))
        Builder.load_file(os.path.join(kv_path, 'kv', 'ship_screen.kv'))
        Builder.load_file(os.path.join(kv_path, 'kv', 'rules_screen.kv'))
        Builder.load_file(os.path.join(kv_path, 'kv', 'ship_info_screen.kv'))
        
        self.sm = ScreenManager(transition=SlideTransition())
        self.sm.add_widget(HomeScreen(name='home'))
        self.sm.add_widget(CharacterScreen(name='character_sheet'))
        self.sm.add_widget(AboutScreen(name='about'))
        self.sm.add_widget(CreateCharacterScreen(name='create_character'))
        self.sm.add_widget(CharacterInfoScreen(name='character_info_screen'))
        self.sm.add_widget(ShipCreationScreen(name='ship_creation_screen'))
        self.sm.add_widget(ShipScreen(name='ship_screen'))
        self.sm.add_widget(RulesScreen(name='rules_screen'))
        self.sm.add_widget(ShipInfoScreen(name='ship_info_screen'))

        root = BoxLayout(orientation='vertical')
        root.add_widget(NavigationBar())
        root.add_widget(self.sm)
        root.ids = {'sm': self.sm}  # Assign the ScreenManager to the ids dictionary

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

if __name__ == '__main__':
    MainApp().run()

