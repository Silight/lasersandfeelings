from kivymd.uix.menu import MDDropdownMenu

class MenuMethods:
    def __init__(self, app):
        self.app = app
        self.menu_items = [
            {"text": "Home", "viewclass": "OneLineListItem", "on_release": lambda x="home": self.switch_screen(x)},
            {"text": "Rules", "viewclass": "OneLineListItem", "on_release": lambda x="rules_screen": self.switch_screen(x)},
            {"text": "Ship Screen", "viewclass": "OneLineListItem", "on_release": lambda x="ship_screen": self.switch_screen(x)},
            {"text": "Character Sheet", "viewclass": "OneLineListItem", "on_release": lambda x="character_sheet": self.switch_screen(x)},
            {"text": "About", "viewclass": "OneLineListItem", "on_release": lambda x="about": self.switch_screen(x)},
        ]
        self.menu = MDDropdownMenu(
            caller=None,
            items=self.menu_items,
            width_mult=4,
        )

    def init_menus(self):
        # Initialize the dropdown menu
        self.menu = MDDropdownMenu(
            caller=None,
            items=self.menu_items,
            width_mult=4,
        )

    def open_menu(self, caller):
        self.menu.caller = caller
        self.menu.open()

    def switch_screen(self, screen_name):
        self.app.switch_screen(screen_name)
        self.menu.dismiss()
    
    def dismiss_menu(self):
        self.menu.dismiss()

    # Character Creation Menus
    def open_style_menu(self, caller):
        style_items = [
            {"text": "Alien", "viewclass": "OneLineListItem", "on_release": lambda x="Alien": self.set_style(x)},
            {"text": "Android", "viewclass": "OneLineListItem", "on_release": lambda x="Android": self.set_style(x)},
            {"text": "Dangerous", "viewclass": "OneLineListItem", "on_release": lambda x="Dangerous": self.set_style(x)},
            {"text": "Heroic", "viewclass": "OneLineListItem", "on_release": lambda x="Heroic": self.set_style(x)},
            {"text": "Hot-Shot", "viewclass": "OneLineListItem", "on_release": lambda x="Hot-Shot": self.set_style(x)},
            {"text": "Intrepid", "viewclass": "OneLineListItem", "on_release": lambda x="Intrepid": self.set_style(x)},
            {"text": "Savvy", "viewclass": "OneLineListItem", "on_release": lambda x="Savvy": self.set_style(x)},
        ]
        self.style_menu = MDDropdownMenu(
            caller=caller,
            items=style_items,
            width_mult=4,
        )
        self.style_menu.open()

    def set_style(self, style):
        self.app.root.ids.create_character.ids.style_input.text = style
        self.style_menu.dismiss()

    def open_role_menu(self, caller):
        role_items = [
            {"text": "Captain", "viewclass": "OneLineListItem", "on_release": lambda x="Captain": self.set_role(x)},
            {"text": "Doctor", "viewclass": "OneLineListItem", "on_release": lambda x="Doctor": self.set_role(x)},
            {"text": "Engineer", "viewclass": "OneLineListItem", "on_release": lambda x="Engineer": self.set_role(x)},
            {"text": "Explorer", "viewclass": "OneLineListItem", "on_release": lambda x="Explorer": self.set_role(x)},
            {"text": "Pilot", "viewclass": "OneLineListItem", "on_release": lambda x="Pilot": self.set_role(x)},
            {"text": "Scientist", "viewclass": "OneLineListItem", "on_release": lambda x="Scientist": self.set_role(x)},
        ]
        self.role_menu = MDDropdownMenu(
            caller=caller,
            items=role_items,
            width_mult=4,
        )
        self.role_menu.open()

    def set_role(self, role):
        self.app.root.ids.create_character.ids.role_input.text = role
        self.role_menu.dismiss()

    def open_goal_menu(self, caller):
        goal_items = [
            {"text": "Explore", "viewclass": "OneLineListItem", "on_release": lambda x="Explore": self.set_goal(x)},
            {"text": "Defend", "viewclass": "OneLineListItem", "on_release": lambda x="Defend": self.set_goal(x)},
            {"text": "Research", "viewclass": "OneLineListItem", "on_release": lambda x="Research": self.set_goal(x)},
            {"text": "Trade", "viewclass": "OneLineListItem", "on_release": lambda x="Trade": self.set_goal(x)},
            {"text": "Rescue", "viewclass": "OneLineListItem", "on_release": lambda x="Rescue": self.set_goal(x)},
        ]
        self.goal_menu = MDDropdownMenu(
            caller=caller,
            items=goal_items,
            width_mult=4,
        )
        self.goal_menu.open()

    def set_goal(self, goal):
        self.app.root.ids.create_character.ids.goal_input.text = goal
        self.goal_menu.dismiss()

    def open_number_menu(self, caller):
        number_items = [
            {"text": "2", "viewclass": "OneLineListItem", "on_release": lambda x="2": self.set_number(x)},
            {"text": "3", "viewclass": "OneLineListItem", "on_release": lambda x="3": self.set_number(x)},
            {"text": "4", "viewclass": "OneLineListItem", "on_release": lambda x="4": self.set_number(x)},
            {"text": "5", "viewclass": "OneLineListItem", "on_release": lambda x="5": self.set_number(x)},
        ]
        self.number_menu = MDDropdownMenu(
            caller=caller,
            items=number_items,
            width_mult=4,
        )
        self.number_menu.open()

    def set_number(self, number):
        self.app.root.ids.create_character.ids.number_input.text = number
        self.number_menu.dismiss()