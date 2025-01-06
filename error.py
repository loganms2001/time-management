class Error(Exception):
    '''
    Base error class for time_management
    Exception + dump
    '''
    dump: str
    def __init__(self, *args, dump: str = "-- no dump --"):
        super().__init__(*args)
        self.dump = dump

    def __str__(self):
        return f"{super().__str__()} (dump = {self.dump})"
    
class SaveError(Error):
    '''
    Temp
    '''
    def __str__(self):
        return f"SaveError: {super().__str__()}"