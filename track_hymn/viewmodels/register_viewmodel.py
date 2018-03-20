from track_hymn.viewmodels.viewmodelbase import ViewModelBase


class RegisterViewModel(ViewModelBase):
    def __init__(self) -> object:
        self.username = None
        self.stake = None
        self.ward = None
        self.zip = None
        self.password = None
        self.confirm_password = None
        self.error = None

    def from_dict(self, data_dict):
        self.username = data_dict.get('username')
        self.stake = data_dict.get('stake')
        self.ward = data_dict.get('ward')
        self.zip = data_dict.get('zip')
        self.password = data_dict.get('password')
        self.confirm_password = data_dict.get('confirm_password')

    def validate(self):
        self.error = None

        if self.password != self.confirm_password:
            self.error = "Password does not match..."
            return

        if not self.password:
            self.error = "You must enter a password."
            return

        if not self.username:
            self.error = "You must specify a valid username."
            return
