from kivymd.app import MDApp
from kivymd.uix.card import MDCard
from kivy.properties import StringProperty, NumericProperty
from kivy.uix.screenmanager import ScreenManager
from kivy.metrics import dp
from scripts.database import Ship
from datetime import date
from kivy.uix.recycleview import RecycleView

class ShipMethods:
    def __init__(self, sm: ScreenManager):
        self.sm = sm
        self.current_ship_id = None

    def create_ship(self):
        self.switch_screen('ship_creation_screen')

    def save_ship(self):
        # Collect values from the input fields
        screen = self.sm.get_screen('ship_creation_screen')
        name = screen.ids.name_input.text
        strength_one = screen.ids.strength_one_input.text
        strength_two = screen.ids.strength_two_input.text
        problem = screen.ids.problem_input.text
        ship_notes = screen.ids.ship_notes_input.text
        # Insert the new ship into the database and get the last inserted ship_id
        ship_id = Ship.insert_ship(name, strength_one, strength_two, problem)
        # Insert the initial notes into the ship_notes table
        Ship.insert_ship_notes(ship_id, ship_notes)
        self.update_ship_list()
        self.switch_screen('ship_screen')  # Transition back to the ship_screen
    
    def existing_ship(self):
        self.update_ship_list()
        self.switch_screen('ship_screen')
    
    def open_ship_info(self, ship_id, name, strength_one, strength_two, problem):
        self.current_ship_id = ship_id
        screen = self.sm.get_screen('ship_info_screen')
        screen.ids.name_label.text = name
        screen.ids.strength_one_label.text = strength_one
        screen.ids.strength_two_label.text = strength_two
        screen.ids.problem_label.text = problem
        notes = Ship.get_all_ship_notes(ship_id)
        notes_list = screen.ids.notes_list
        notes_list.data = [{'text': f"{datetime}: {note}"} for note, datetime in notes]
        self.sm.current = 'ship_info_screen'
    
    def save_ship_notes(self):
        screen = self.sm.get_screen('ship_info_screen')
        ship_id = self.current_ship_id
        notes = screen.ids.ship_notes_input.text
        # Save notes to the database
        Ship.insert_ship_notes(ship_id, notes)
        # Update the notes list
        self.open_ship_info(ship_id, screen.ids.name_label.text, screen.ids.strength_one_label.text, screen.ids.strength_two_label.text, screen.ids.problem_label.text)
    
    def update_ship_list(self):
        screen = self.sm.get_screen('ship_screen')
        ship_list = screen.ids.ship_list
        ships = Ship.get_ships()
        ship_list.update_ships(ships)
    
    def switch_screen(self, screen_name):
        self.sm.current = screen_name


class ShipCard(MDCard):
    ship_id = NumericProperty()
    ship_name = StringProperty()
    ship_type = StringProperty()
    ship_class = StringProperty()
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
        app.ship_methods.open_ship_info(self.ship_id, self.ship_name, self.ship_type, self.ship_class)


class ShipList(RecycleView):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.data = []

    def update_ships(self, ships):
        self.data = [{'ship_id': ship[0], 'ship_name': ship[1], 'strength_one': ship[2], 'strength_two': ship[3], 'problem': ship[4]} for ship in ships]
