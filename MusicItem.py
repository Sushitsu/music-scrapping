class MusicItem:

    def __init__(self, img, brand, model, price, description):
        self.img = img
        self.brand = brand
        self.model = model
        self.price = price
        self.description = description

    def get_img(self):
        return self.img

    def get_brand(self):
        return self.brand

    def get_model(self):
        return self.model

    def get_price(self):
        return self.price

    def get_description(self):
        return self.description

    def set_img(self, img):
        self.img = img

    def set_brand(self, brand):
        self.brand = brand

    def set_model(self, model):
        self.model = model

    def set_price(self, price):
        self.price = price

    def set_description(self, description):
        self.description = description


