import os
from winotify import Notification, audio
from os import getcwd

def Alert(Text):
    icon_path = r"C:\Users\arshb\Desktop\J.A.R.V.I.S 2.O\UI\cbe227_fb70e39e9dd94e30bbe30c48b2367dd8~mv2.gif"

    toast = Notification(
        app_id="🟢 J.A.R.V.I.S.",
        title=Text,
        duration="long",
        icon=icon_path
    )

    toast.set_audio(audio.Default, loop=False)


    toast.add_actions(label="Click me", launch="https://www.google.com")
    toast.add_actions(label="Dismiss", launch="https://www.google.com")


    toast.show()

