class Medicine:
    def __init__(self,id,name,price,description,amount):
        self.id = id 
        self.name = name
        self.price = price
        self.description = description
        self.amount = amount
        


    def dump(self):
        return {
            'id': self.id,
            'name': self.name,
            'price':  self.price,
            'description': self.description,
            'amount': self.amount,
        }