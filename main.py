import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
import requests  # You'll need to install this library if not already done


class DiscordWebhookApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical', spacing=10, padding=10)

        self.text_input = TextInput(hint_text="Enter your message")
        send_button = Button(text="Send to Discord")
        send_button.bind(on_press=self.send_to_discord)

        layout.add_widget(self.text_input)
        layout.add_widget(send_button)

        self.output_label = TextInput(hint_text="Response from Discord", readonly=True, multiline=True)

        layout.add_widget(self.output_label)
        return layout

    def send_to_discord(self, instance):
        message = self.text_input.text
        webhook_url = "https://discord.com/api/webhooks/1165290854416646225/NFI2Puw2SYeWNetzEm9sr_KtCSjEA-6CS54hTQZDCy7LD-EYLuv0rM2oioO7ObazFZvU"
        data = {
            "content": message
        }

        response = requests.post(webhook_url, json=data)

        if response.status_code == 204:
            self.output_label.text = "Message sent to Discord successfully"
        else:
            self.output_label.text = f"Failed to send message to Discord: {response.status_code}"

if __name__ == '__main__':
    DiscordWebhookApp().run()

