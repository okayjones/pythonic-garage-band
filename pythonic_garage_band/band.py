class Band:
    
    instances = []

    def __init__(self, name, members=None):
        self.name = name
        self.members = members
        Band.instances.append(self.name)

    def __str__(self):
        return f"The band {self.name}"

    def __repr__(self):
        return f"Band instance. name={self.name}, members={self.members}"

    def play_solos(self):
        solos = map(lambda member: member.play_solo(), self.members)
        return list(solos)

    @classmethod
    def to_list(cls):
        return cls.instances

class Musician:
    def __init__(self, name, instrument=None):
        self.name = name
        self.instrument = instrument
    
    def __str__(self):
        return f"My name is {self.name} and I play {self.instrument}"

    def get_instrument(self):
        return self.instrument

class Guitarist(Musician):
    def __init__(self, name):
        super().__init__(name)
        self.instrument= 'guitar'
    
    def __repr__(self):
        return f"Guitarist instance. Name = {self.name}"

    @staticmethod
    def play_solo():
        return "face melting guitar solo"

class Bassist(Musician):
    def __init__(self, name):
        super().__init__(name)
        self.instrument= 'bass'

    def __repr__(self):
        return f"Bassist instance. Name = {self.name}"

    @staticmethod
    def play_solo():
        return "bom bom buh bom"

class Drummer(Musician):
    def __init__(self, name):
        super().__init__(name)
        self.instrument= 'drums'

    def __repr__(self):
        return f"Drummer instance. Name = {self.name}"

    @staticmethod
    def play_solo():
        return "rattle boom crash"