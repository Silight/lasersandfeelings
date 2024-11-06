from kivymd.uix.menu import MDDropdownMenu

class MenuMethods:
    def __init__(self, app):
        self.app = app

    def init_menus(self):
        # Define the menu items
        self.menu_items = [
            {"text": "Home", "viewclass": "OneLineListItem", "on_release": lambda x="home": self.switch_and_dismiss(x)},
            {"text": "Rules", "viewclass": "OneLineListItem", "on_release": lambda x="rules_screen": self.switch_and_dismiss(x)},
            {"text": "Character Sheet", "viewclass": "OneLineListItem", "on_release": lambda x="character_sheet": self.switch_and_dismiss(x)},
            {"text": "Ship Sheet", "viewclass": "OneLineListItem", "on_release": lambda x="ship_screen": self.switch_and_dismiss(x)},
            {"text": "About", "viewclass": "OneLineListItem", "on_release": lambda x="about": self.switch_and_dismiss(x)},
        ]
        # Initialize the dropdown menu
        self.menu = MDDropdownMenu(
            caller=None,
            items=self.menu_items,
            width_mult=4,
        )

    def open_menu(self, caller):
        self.menu.caller = caller
        self.menu.open()
    
    def dismiss_menu(self):
        if self.menu:
            self.menu.dismiss()

    def switch_and_dismiss(self, screen_name):
        self.app.switch_screen(screen_name)
        self.dismiss_menu()

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
        # Set the selected style
        screen = self.app.sm.get_screen('create_character')
        screen.ids.style_input.text = style
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
        # Set the selected role
        screen = self.app.sm.get_screen('create_character')
        screen.ids.role_input.text = role
        self.role_menu.dismiss()

    def open_num_menu(self, caller):
        num_items = [
            {"text": "2", "viewclass": "OneLineListItem", "on_release": lambda x="2": self.set_num(x)},
            {"text": "3", "viewclass": "OneLineListItem", "on_release": lambda x="3": self.set_num(x)},
            {"text": "4", "viewclass": "OneLineListItem", "on_release": lambda x="4": self.set_num(x)},
            {"text": "5", "viewclass": "OneLineListItem", "on_release": lambda x="5": self.set_num(x)},
        ]
        self.num_menu = MDDropdownMenu(
            caller=caller,
            items=num_items,
            width_mult=4,
        )
        self.num_menu.open()

    def set_num(self, num):
        # Set the selected number
        screen = self.app.sm.get_screen('create_character')
        screen.ids.number_input.text = num
        self.num_menu.dismiss()

    # Ship Creation Menus
    def open_strength_menu(self, caller, set_strength_method):
        strength_items = [
            {"text": "Fast", "viewclass": "OneLineListItem", "on_release": lambda x="Fast": set_strength_method(x)},
            {"text": "Nimble", "viewclass": "OneLineListItem", "on_release": lambda x="Nimble": set_strength_method(x)},
            {"text": "Well-armed", "viewclass": "OneLineListItem", "on_release": lambda x="Well-armed": set_strength_method(x)},
            {"text": "Powerful Shields", "viewclass": "OneLineListItem", "on_release": lambda x="Powerful Shields": set_strength_method(x)},
            {"text": "Superior Sensors", "viewclass": "OneLineListItem", "on_release": lambda x="Superior Sensors": set_strength_method(x)},
            {"text": "Cloaking Device", "viewclass": "OneLineListItem", "on_release": lambda x="Cloaking Device": set_strength_method(x)},
            {"text": "Transporters", "viewclass": "OneLineListItem", "on_release": lambda x="Transporters": set_strength_method(x)},
            {"text": "Fightercraft", "viewclass": "OneLineListItem", "on_release": lambda x="Fightercraft": set_strength_method(x)},
        ]
        self.strength_menu = MDDropdownMenu(
            caller=caller,
            items=strength_items,
            width_mult=4,
        )
        self.strength_menu.open()

    def set_strength_one(self, strength_one):
        # Set the selected strength one
        screen = self.app.sm.get_screen('ship_creation_screen')
        screen.ids.strength_one_input.text = strength_one
        self.strength_menu.dismiss()

    def set_strength_two(self, strength_two):
        # Set the selected strength two
        screen = self.app.sm.get_screen('ship_creation_screen')
        screen.ids.strength_two_input.text = strength_two
        self.strength_menu.dismiss()

    def open_problem_menu(self, caller):
        problem_items = [
            {"text": "Fuel Hog", "viewclass": "OneLineListItem", "on_release": lambda x="Fuel Hog": self.set_problem(x)},
            {"text": "Only One Medical Pod", "viewclass": "OneLineListItem", "on_release": lambda x="Only One Medical Pod": self.set_problem(x)},
            {"text": "Horrible Circuit Breakers", "viewclass": "OneLineListItem", "on_release": lambda x="Horrible Circuit Breakers": self.set_problem(x)},
            {"text": "Grim Reputation", "viewclass": "OneLineListItem", "on_release": lambda x="Grim Reputation": self.set_problem(x)},
            {"text": "Twitchy Hyperdrive", "viewclass": "OneLineListItem", "on_release": lambda x="Twitchy Hyperdrive": self.set_problem(x)},
            {"text": "Sketchy Life Support", "viewclass": "OneLineListItem", "on_release": lambda x="Sketchy Life Support": self.set_problem(x)},
            {"text": "Unreliable Com System", "viewclass": "OneLineListItem", "on_release": lambda x="Unreliable Com System": self.set_problem(x)}
        ]
        self.problem_menu = MDDropdownMenu(
            caller=caller,
            items=problem_items,
            width_mult=4,
        )
        self.problem_menu.open()

    def set_problem(self, problem):
        # Set the selected problem
        screen = self.app.sm.get_screen('ship_creation_screen')
        screen.ids.problem_input.text = problem
        self.problem_menu.dismiss()