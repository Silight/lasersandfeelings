from kivy.uix.screenmanager import ScreenManager
from scripts.database import Player

class CharacterMethods:
    def __init__(self, sm: ScreenManager):
        self.sm = sm
        self.current_player_id = None

    def create_character(self):
        self.switch_screen('create_character')

    def save_character(self):
        # Collect values from the input fields
        screen = self.sm.get_screen('create_character')
        name = screen.ids.name_input.text
        style = screen.ids.style_input.text
        role = screen.ids.role_input.text
        goal = screen.ids.goal_input.text
        number = screen.ids.number_input.text
        # Insert the new character into the database
        Player.insert_player(name, style, role, goal, number)
        self.update_character_list()

    def existing_character(self): 
        self.update_character_list()
        self.switch_screen('character_sheet')

    def fetch_characters(self):
        # Fetch characters from the database
        characters = Player.get_players()
        return characters

    def update_character_list(self):
        screen = self.sm.get_screen('character_sheet')
        character_list = screen.ids.character_list
        characters = self.fetch_characters()
        character_list.update_characters(characters)

    def open_character_info(self, player_id, name, style, role, goal, number, notes=""):
        self.current_player_id = player_id
        screen = self.sm.get_screen('character_info_screen')
        screen.ids.name_label.text = f"Name: {name}"
        screen.ids.style_label.text = f"Style: {style}"
        screen.ids.role_label.text = f"Role: {role}"
        screen.ids.goal_label.text = f"Goal: {goal}"
        screen.ids.number_label.text = f"Number: {number}"
        note = Player.get_latest_player_note(player_id)
        screen.ids.notes_input.text = note
        self.switch_screen('character_info_screen')

    def save_notes(self):
        screen = self.sm.get_screen('character_info_screen')
        player_id = self.current_player_id
        notes = screen.ids.notes_input.text
        # Save notes to the database
        Player.insert_player_notes(player_id, notes)

    def switch_screen(self, screen_name):
        self.sm.current = screen_name