class Toy():
    def __init__(self, colour, age):
        self.colour = colour
        self.age = age
        self.my_dict = {
            'name': ' yoyo',
            'has_pets': False
        }

    def __str__(self):
        return f'{self.colour}'

    def __len__(self):
        return 5

    def __del__(self):
        print('deleted!')

    def __call__(self):
        return ('yes???')

    def __getitem__(self, i):
        return self.my_dict[i]


action_figure = Toy('red', 0)
print(action_figure.__str__())   # both are same
print(str(action_figure))
print(len(action_figure))
# del action_figure
print(action_figure())
print(action_figure['name'])
