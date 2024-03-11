from plyer import notification


def win_notif(Title, Message, Icon):
    notification.notify(
        title = Title,
        message = Message,
        app_icon = Icon,
        timeout = 5,
    )

