from kivy.uix.screenmanager import ScreenManager
from scripts.database import Player
from datetime import date
from kivymd.uix.card import MDCard
from kivy.properties import StringProperty, NumericProperty
from kivy.metrics import dp
from kivymd.app import MDApp
from kivy.uix.recycleview import RecycleView

class CharacterMethods:
    def __init__(self, sm: ScreenManager):
        self.sm = sm

    def save_character(self):
        screen = self.sm.get_screen('create_character')
        name = screen.ids.name_input.text
        style = screen.ids.style_input.text
        role = screen.ids.role_input.text
        goal = screen.ids.goal_input.text
        number = screen.ids.number_input.text
        journal = screen.ids.journal_input.text
        # Save character to the database
        player_id = Player.insert_player(name, style, role, goal, number)
        Player.insert_player_notes(player_id, journal)
        self.update_character_list()
        self.sm.current = 'character_sheet'
    
    def update_character_list(self):
        screen = self.sm.get_screen('character_sheet')
        character_list = screen.ids.character_list
        characters = Player.get_characters()
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
        screen.ids.journal_input.text = note
        self.sm.current = 'character_info_screen'

    def create_character(self):
        self.switch_screen('create_character')

    def existing_character(self): 
        self.update_character_list()
        self.switch_screen('character_sheet')

    def fetch_characters(self):
        # Fetch characters from the database
        characters = Player.get_players()
        return characters

    def save_notes(self):
        screen = self.sm.get_screen('character_info_screen')
        player_id = self.current_player_id
        notes = screen.ids.notes_input.text
        # Save notes to the database
        Player.insert_player_notes(player_id, notes)
        self.update_character_list()

    def switch_screen(self, screen_name):
        self.sm.current = screen_name

class CharacterCard(MDCard):
    player_id = NumericProperty()
    name = StringProperty()
    style = StringProperty()
    role = StringProperty()
    goal = StringProperty()
    number = StringProperty()
    journal_notes = StringProperty()  # Update to journal_notes

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

class CharacterList(RecycleView):    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.data = []

    def update_characters(self, characters):
        self.data = [{'player_id': char[0], 'name': str(char[1]), 'style': str(char[2]), 'role': str(char[3]), 'goal': str(char[4]), 'number': str(char[5]), 'journal_notes': str(char[6])} for char in characters if len(char) >= 7]