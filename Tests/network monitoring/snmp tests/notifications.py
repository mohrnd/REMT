from plyer import notification


def win_notif(Title, Message, Icon):
    notification.notify(
        title = Title,
        message = Message,
        app_icon = Icon,
        timeout = 5,
    )

from win10toast import ToastNotifier
toast = ToastNotifier()
toast.show_toast(
    "Notification",
    "Notification body",
    duration = 20,
    icon_path = r'C:\Users\BALLS2 (rip BALLS)\Desktop\REMT\Tests\network monitoring\snmp tests\white (1).ico',
    threaded = True,
)