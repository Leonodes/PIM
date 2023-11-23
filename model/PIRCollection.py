import os
import datetime
class PIRCollection:
    def __init__(self):
        self.searchType = "All"
        self.record_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),'records.pim')
        self.include_or_not = False
        self.operator = "&&"
        self.type_content = None
        self.not_ornot = ""
    
    # private 實例對象無需訪問
    def matches_text(self,text_criteria):
        found_lines = []
        for line in self.type_content:
            if text_criteria in line:
                found_lines.append(line.strip())
        return found_lines
    
    def matches_time(self,time_criteria,condition):
        found_lines = []
        for line in self.type_content:
            parts = line.split(",")
            for part in parts:
                time = datetime.strptime(time_criteria.strip(),"%Y/%m/%d %H:%M")
                value = datetime.strptime(part.strip(),"%Y/%m/%d %H:%M")
                condition = condition
                if condition == "<" and value < time:
                    found_lines.append(line.strip())
                elif condition == ">" and value > time:
                    found_lines.append(line.strip())
                elif condition == "=" and value == time:
                    found_lines.append(line.strip())
                else:
                    pass
            return found_lines
        
    def updateSearchType(self,searchType):
        self.searchType = searchType
    
    def findIndex(self,searchType):
        with open(self.record_path, "r") as file:
            lines = file.readlines()
        if searchType == 1:
            word_to_find = "Note"
        elif searchType == 2:
            word_to_find = "Task"
        elif searchType == 3:
            word_to_find = "Contact"
        elif searchType == 4:
            word_to_find = "Event"
        else:
            word_to_find = "End"
        for i, line in enumerate(lines):
            if word_to_find in line:
                index = i
                return index

    def matches_type(self):
        with open(self.record_path, "r") as file:
            lines = file.readlines()
            if self.searchType == 1 or self.searchType == 2 or self.searchType == 3 or self.searchType == 4:
                self.type_content = lines[self.findIndex(self.searchType)+1:self.findIndex(self.searchType+1)]
            else:
                self.type_content = lines
        return self.type_content
    
    def not_included_file(self,strings_to_remove):
        found_lines = []
        for line in self.type_content:
            if not any(string in line for string in strings_to_remove):
                found_lines.append(line.rstrip())
        return found_lines
    
    def not_ornot_filter(self,not_ornot,text_criteria):
        if not_ornot == "-":
            return self.not_included_file(self.matches_text(text_criteria))
        if not_ornot == "+":
            return self.matches_text(text_criteria)






