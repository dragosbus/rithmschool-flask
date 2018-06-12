class Users():

    user_id = 1

    def __init_(self, f_name, l_name):
        self.f_name = f_name
        self.l_name = l_name
        self.id = Users.user_id

    def full_name():
        return '{} {}'.format(self.f_name, self.l_name)