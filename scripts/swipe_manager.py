from kivy.uix.screenmanager import ScreenManager, SlideTransition
from kivy.properties import NumericProperty

class SwipeManager(ScreenManager):
    touch_start_x = NumericProperty(0)
    touch_start_y = NumericProperty(0)
    swipe_screens = ['home', 'rules_screen', 'character_sheet', 'ship_screen', 'about']

    def on_touch_down(self, touch):
        self.touch_start_x = touch.x
        self.touch_start_y = touch.y
        return super(SwipeManager, self).on_touch_down(touch)

    def on_touch_up(self, touch):
        dx = touch.x - self.touch_start_x
        dy = touch.y - self.touch_start_y

        if abs(dx) > abs(dy):
            if dx > 50:
                self.transition = SlideTransition(direction='right')
                self.current = self.previous()
            elif dx < -50:
                self.transition = SlideTransition(direction='left')
                self.current = self.next()
        return super(SwipeManager, self).on_touch_up(touch)

    def previous(self):
        if self.current not in self.swipe_screens:
            return self.current
        current_index = self.swipe_screens.index(self.current)
        previous_index = (current_index - 1) % len(self.swipe_screens)
        if self.swipe_screens[previous_index] == 'about' and self.current == 'home':
            return self.current
        return self.swipe_screens[previous_index]

    def next(self):
        if self.current not in self.swipe_screens:
            return self.current
        current_index = self.swipe_screens.index(self.current)
        next_index = (current_index + 1) % len(self.swipe_screens)
        if self.swipe_screens[next_index] == 'home' and self.current == 'about':
            return self.current
        return self.swipe_screens[next_index]