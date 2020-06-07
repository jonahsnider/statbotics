class TeamEvent:
    number = -1
    key = ""

    TeamYear_p = None  # points to TeamYear parent
    Event_p = None  # points to Event parent
    TeamMatch_c = {}  # maps from match key to TeamMatch children

    def __init__(self, TeamYear, Event):
        self.TeamYear_p = TeamYear
        self.Event_p = Event

        self.number = self.TeamYear_p.getNumber()
        self.key = self.Event_p.getKey()

    def __lt__(self, other):
        if self.getNumber() == other.getNumber():
            return self.getKey() < other.getKey()
        else:
            return self.getNumber() < other.getNumber()

    def __repr__(self):
        return "TeamEvent " + str(self.getNumber()) + "\t" + str(self.getKey())

    def __str__(self):
        return self.__repr__()

    def getNumber(self):
        return self.number

    def getKey(self):
        return self.key
