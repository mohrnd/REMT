from plyer import notification
from win10toast import ToastNotifier

def win_notif(Title, Message, Icon):
    notification.notify(
        title = Title,
        message = Message,
        app_icon = Icon,
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