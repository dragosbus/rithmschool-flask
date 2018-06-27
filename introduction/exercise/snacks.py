class Snacks():

    snack_id = 1

    def __init__(self, name, kind):
        self.name = name
        self.kind = kind
        self.id = Snacks.snack_id

        Snacks.snack_id += 1
