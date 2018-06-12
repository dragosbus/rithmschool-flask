class Users():

    user_id = 1

    def __init__(self, f_name, l_name):
        self.f_name = f_name
        self.l_name = l_name
        self.id = Users.user_id
        Users.user_id += 1

    def full_name(self):
        return '{} {}'.format(self.f_name, self.l_name)