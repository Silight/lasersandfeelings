from kivy.uix.screenmanager import ScreenManager
from scripts.database import Ship
from datetime import date

class ShipMethods:
    def __init__(self, sm: ScreenManager):
        self.sm = sm

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
    
    def open_ship_info(self, ship_id, ship_name, strength_one, strength_two, problem, ship_notes):
        self.current_ship_id = ship_id
        screen = self.sm.get_screen('ship_info_screen')
        screen.ids.name_label.text = f"Name: {ship_name}"
        screen.ids.strength_one_label.text = f"Strength One: {strength_one}"
        screen.ids.strength_two_label.text = f"Strength Two: {strength_two}"
        screen.ids.problem_label.text = f"Problem: {problem}"
        screen.ids.ship_notes_input.text = ship_notes
        self.update_ship_notes_list(ship_id)
        self.switch_screen('ship_info_screen')
    
    def save_ship_notes(self):
        screen = self.sm.get_screen('ship_info_screen')
        ship_id = self.current_ship_id
        notes = screen.ids.ship_notes_input.text
        # Save notes to the database
        Ship.insert_ship_notes(ship_id, notes)
        self.update_ship_notes_list(ship_id)
    
    def update_ship_notes_list(self, ship_id):
        screen = self.sm.get_screen('ship_info_screen')
        notes_list = screen.ids.notes_list
        notes = Ship.get_all_ship_notes(ship_id)
        notes_list.data = [{'text': f"{datetime}: {note}"} for note, datetime in notes]
    
    def update_ship_list(self):
        screen = self.sm.get_screen('ship_screen')
        ship_list = screen.ids.ship_list
        ships = Ship.get_ships()
        ship_list.update_ships(ships)
    
    def switch_screen(self, screen_name):
        self.sm.current = screen_name