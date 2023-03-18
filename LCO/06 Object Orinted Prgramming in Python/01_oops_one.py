class Phone:
    "A simple class for test"
    phone_version = "S10"     # class variables
    brand_name = "Samsung"
    user_name = ""

    model = "S10+"
    def get_model(self):    # class methods
        return self.model
        # return "S10+"

    def set_model(self, val):
        self.model = "S10+, " + val



    #constructor
    def __init__(self, user_name):
        self.user_name = user_name


    def BootLogo(self):
        print("SUMSUNG", self.phone_version)




hitesh = Phone("Hitesh phone")
# hitesh.phone_version = "iPhone 10 X Max"

hitesh.set_model("iPhone")
print(hitesh.get_model())


hitesh.BootLogo()

