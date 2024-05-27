from plyer import notification
from win10toast import ToastNotifier
from PIL import Image
def win_notif(Title, Message, Icon):
    notification.notify(
        title = Title,
        message = Message,
        app_icon = r"..\REMT\FinishedProduct\MainInterface\white.ico",
        timeout = 5,
    )

def win_notif2(Title, Body, Icon):
    toast = ToastNotifier()
    toast.show_toast(
        Title,
        Body,
        duration = 10,
        icon_path = Icon,
        threaded = True,
    )


# ..\REMT\FinishedProduct\MainInterface\white.png

# from PIL import Image

# logo = Image.open("..\\REMT\\FinishedProduct\\MainInterface\\white.png")

# logo.save("..\\REMT\\FinishedProduct\\MainInterface\\white.ico",format='ICO')
