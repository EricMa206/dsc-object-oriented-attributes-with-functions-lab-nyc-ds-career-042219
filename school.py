class School:

    def __init__(self, school_name, roster={9: [], 10: [], 11: [], 12: []}):
        self.school_name = school_name
        self.roster = roster

    def add_student(self, full_name, grade):
        self.roster[grade].append(full_name)

    def grade(self, grade):
        return self.roster[grade]

    def sort_roster(self):
        return sorted(self.roster.values())
