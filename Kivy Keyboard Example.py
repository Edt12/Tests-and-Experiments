
import kivy
kivy.require('1.0.8')
from kivy.app import App
from kivy.core.window import Window
from kivy.uix.widget import Widget
from kivy.uix.gridlayout import GridLayout

class KeyboardListener(Widget):
        def __init__(self, **kwargs):
            super(KeyboardListener, self).__init__(**kwargs)
            self._keyboard = Window.request_keyboard(
                self.k,self, 'tet')#requested a keyboard first function is what will be triggered when release is pressed 2nd is give keyboard attribute sef third is name of keyboard
            if self._keyboard.widget:
                # If it exists, this widget is a VKeyboard object which you can use
                # to change the keyboard layout.
                pass
            self._keyboard.bind(on_key_down=self._on_keyboard_down)#Gives keydown variable
  
        def k(self):
            print('My keyboard have been closed!')
            self._keyboard.unbind(on_key_down=self._on_keyboard_down)
            self._keyboard = None

        def _on_keyboard_down(self, keyboard, keycode, text, modifiers):
            if keycode[1]=='escape':
                keyboard.release() #calls first function in request command

            # Return True to accept the key. Otherwise, it will be used by
            # the system.
            return True 
            
class Layout(Widget):
    TestLayout=GridLayout()

    
class TestApp(App):
    def build(self):
        return KeyboardListener()
      
TestApp().run()
    