class Snacks():

    snack_id = 1

    def __init__(self, name, kind):
        self.snack_id = Snacks.id
        self.name = name
        self.kind = kind

        Snacks.snack_id += 1
