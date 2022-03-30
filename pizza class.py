# class Pizza:

#     def add_topping(self,veggie, cheese, protein):
#         self.veggie = veggie
#         self.cheese = cheese
#         self.protein = protein
#         print(f"Your pizza has a topping of {veggie}, {cheese} and {protein}")
#         return

# pizza = Pizza()

# a = input("Enter a Veggie of ur choice:")
# b = input("Enter a cheese of your choice:")
# c = input("Enter a protein of your choice:")

# my_custom_pizza = pizza.add_topping(a, b, c)

class Pizza:

    def add_topping(self, topping1, topping2):
        self.topping1 = topping1
        self.topping2 = topping2

        print(f"Your pizza has a topping of {topping1}, {topping2}") 
        return

pizza = Pizza()

my_custom_pizza = pizza.add_topping("corn", "paneer")


        
    