from track_hymn.viewmodels.viewmodelbase import ViewModelBase


class HymnViewModel(ViewModelBase):
    def __init__(self):
        self.opening = None
        self.sacrament = None
        self.rest = None
        self.closing = None
        self.error = None

    def from_dict(self, data_dict):
        self.opening = data_dict.get('opening')
        self.sacrament = data_dict.get('sacrament')
        self.rest = data_dict.get('rest')
        self.closing = data_dict.get('closing')

    def validate(self):
        self.error = None
