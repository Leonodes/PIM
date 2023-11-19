from datetime import datetime
def checkDate(date):
        if date is None:
            return False
        date_format = "%m/%d/%y %H:%M"
        if len(date.strip()) != len(date_format):
            return False
        try:
            datetime.strptime(date.strip(), date_format)
        except ValueError:
            return False
        return True
    