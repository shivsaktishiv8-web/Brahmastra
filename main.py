from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

class BrahmastraCore:
    def process(self, text):
        # Panini-style logic base
        text = text.lower()
        if "trade" in text: return "Analyzing Market Offline..."
        if "msg" in text: return "Mesh Network: Scanning for Offline Peers..."
        return f"AI Response: {text} (Panini Logic Active)"

class MainApp(App):
    def build(self):
        self.ai = BrahmastraCore()
        layout = BoxLayout(orientation='vertical', padding=20, spacing=10)
        self.lbl = Label(text="BRAHMASTRA V1\nStatus: Offline & Ready", halign='center')
        self.inpt = TextInput(hint_text="Enter command...", multiline=False)
        btn = Button(text="EXECUTE", size_hint_y=0.3, background_color=(1,0,0,1))
        btn.bind(on_press=self.run)
        layout.add(self.lbl); layout.add(self.inpt); layout.add(btn)
        return layout

    def run(self, instance):
        self.lbl.text = self.ai.process(self.inpt.text)

if __name__ == "__main__":
    MainApp().run()
