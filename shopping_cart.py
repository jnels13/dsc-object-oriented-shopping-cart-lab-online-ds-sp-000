class ShoppingCart:
    # write your code here
   def __init__(self, total = 0, employee_discount=None, items = []):
      self.total = total
      self.employee_discount = employee_discount
      self.items = items

   def add_item(self, name, price, quantity=1):
      self.name = name
      self.price = price
      self.quantity = quantity

      self.total += self.price * self.quantity
      i=0
      while i < quantity:
         self.items.append([name,price])
         i += 1

      return (self.total)

   def mean_item_price(self):
      return (self.total / len(self.items))

   def median_item_price(self):
      srtd_list = sorted (self.items, key=lambda x: x[1])
      if (len(self.items) % 2) == 0:
         indx = len(self.items)/2
         return round(((self.items[indx][1] + self.items[indx+1][1])/2),2)
      else:
         indx = (len(self.items) // 2) + 1
         return round(self.items[indx][1],2)



   def apply_discount(self):
      if self.employee_discount == None:
         return("Sorry, there is no discount to apply to your cart :(")
      else:
         return(self.total * (1-(self.employee_discount/100)))

   def void_last_item(self):
      if len(self.items) == 0:
         return("There are no items in your cart!")
      else:
         self.total -= self.items[-1][1]
         self.items.pop()
         return self.total