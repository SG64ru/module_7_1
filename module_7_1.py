class Product:
    def __init__(self, name, weight, category):
        self.name = name
        self.weight = weight
        self.catrgory = category

    def __str__(self):
        # self.weight = str(self.weight)
        return f"{self.name}, {self.weight}, {self.catrgory}"

class Shop:
       def __init__(self):
           self.__file_name = "products.txt"

       def get_products(self):
           self.f_product = open(self.__file_name, "r")
           products = self.f_product.read()
           self.f_product.close()
           return products

       def add(self, *products):
           name_prod = self.__file_name
           f_product = open(name_prod, "a")
           for product in products:
               if product.name in self.get_products():
                   print(f"Продукт {product.name} уже есть в магазине")
               else:
                   file_prod.write(self.file_name)
           f_product.close()



s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p1)   #__str__

s1.add(p1, p2, p3)

print(s1.get_products())