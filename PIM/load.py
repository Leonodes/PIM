taskItem = None
date = None

def setTaskItem(taskItem):
    taskItem = taskItem
    return

def setDate(date):
    date = date
    return

def from_string(s):
    regx = r"([^ ]*) ([^ ]*) ([^\n]*)"
    pattern = re.compile(regx)
    matcher = pattern.match(s)
    if matcher:
        setDate(matcher.group(2))
        setTaskItem(matcher.group(3))