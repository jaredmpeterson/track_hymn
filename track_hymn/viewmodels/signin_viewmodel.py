from track_hymn.viewmodels.viewmodelbase import ViewModelBase


class SigninViewModel(ViewModelBase):
    def __init__(self):
        self.username = None
        self.password = None
        self.error = None

    def from_dict(self, data_dict):
        self.username = data_dict.get('username')
        self.password = data_dict.get('password')
