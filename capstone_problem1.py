class SecurityControl:
    def __init__(self, name, priority):
        self.name = name
        self.priority = priority

my_controls = [SecurityControl('password', 10),
               SecurityControl('firewall', 7),
               SecurityControl('anti-virus', 5),
               SecurityControl('ad blocker', 2)]

def get_controls(list_of_controls):
    control_list = []
    for control in list_of_controls:
        if control.priority > 5:
            control_list.append(control.name)
    control_string = ':'.join(control_list)
    print(control_string)

if __name__ == '__main__':
    get_controls(my_controls)

