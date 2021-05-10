from widgets.login import LoginWindow
from widgets.register import RegisterWindow
from widgets.object_list import ObjectsWindow


class Controller:
    def __init__(self):
        self.login = None
        self.objects_list = None
        self.register = None

    def show_login(self, username=None):
        self.login = LoginWindow()
        self.login.registration_signal.connect(self.show_register)
        self.login.login_signal.connect(self.show_objects_list)
        if username:
            self.login.success_register(username)
        self.login.show()

        if self.register:
            self.register.close()

        if self.objects_list:
            self.objects_list.close()

    def show_register(self):
        self.register = RegisterWindow()
        self.register.registration_signal.connect(self.show_login)
        self.register.cancel_signal.connect(self.show_login)
        self.login.close()
        self.register.show()

    def show_objects_list(self, username, access_token, refresh_token):
        self.objects_list = ObjectsWindow()
        self.objects_list.logout_signal.connect(self.show_login)
        self.objects_list.set_login_data(username, access_token, refresh_token)
        self.login.close()
        self.objects_list.show()
