import time
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.clock import Clock
from pylsl import StreamInfo, StreamOutlet


class LSLStreamerApp(App):
    def build(self):
        # 1. Setup LSL Stream Info: Name='AndroidValueStream', Type='Markers/Data', 1 channel, nominal rate 100Hz
        self.info = StreamInfo(
            name='AndroidValueStream',
            type='Data',
            channel_count=1,
            nominal_srate=100,  # 10 samples per second
            channel_format='int32',
            source_id='android_phone_05'
        )
        self.outlet = StreamOutlet(self.info)

        # App state variable
        self.current_value = 0

        # UI Layout
        layout = BoxLayout(orientation='vertical', padding=20, spacing=20)

        self.status_label = Label(
            text="Current LSL Output: 0", 
            font_size='24sp'
        )
        layout.add_widget(self.status_label)

        # Button 0
        btn_0 = Button(
            text="Set Value to 0", 
            font_size='20sp', 
            background_color=(0.8, 0.2, 0.2, 1)
        )
        btn_0.bind(on_press=self.set_value_0)
        layout.add_widget(btn_0)

        # Button 5
        btn_5 = Button(
            text="Set Value to 5", 
            font_size='20sp', 
            background_color=(0.2, 0.8, 0.2, 1)
        )
        btn_5.bind(on_press=self.set_value_5)
        layout.add_widget(btn_5)

        # 2. Schedule continuous LSL push (10 times per second)
        Clock.schedule_interval(self.send_lsl_data, 1.0 / 100.0)

        return layout

    def set_value_0(self, instance):
        self.current_value = 0
        self.status_label.text = f"Current LSL Output: {self.current_value}"

    def set_value_5(self, instance):
        self.current_value = 5
        self.status_label.text = f"Current LSL Output: {self.current_value}"

    def send_lsl_data(self, dt):
        # Push sample to LSL stream continuously
        self.outlet.push_sample([int(self.current_value)])


if __name__ == '__main__':
    LSLStreamerApp().run()