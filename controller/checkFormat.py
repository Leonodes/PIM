from datetime import datetime
def checkDateFormat(date):
    if date is None:
        return False
    date_format = "%Y/%m/%d %H:%M"
    try:
        datetime.strptime(date.strip(), date_format)
    except ValueError:
        return False
    return True

def checkConditionFormat(condition):
    if condition == "<" or condition == ">" or condition == "=":
        return True
    return False

def checkOperatorFormat(operator):
    if operator == "!" or operator == "||" or operator == "&&":
        return True
    return False