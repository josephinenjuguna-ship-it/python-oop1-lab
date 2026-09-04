#!/usr/bin/env python3

class Coffee:
    def __init__(self,size, price):
        self.size = size
        self.price = price

        @property
        def size(self):
            return self.size

        @size.setter
        def size(self, value):
            if value is not ["Small", "Medium", "Large"]:
                print("Size must be Small, Medium or Large")
            else:
                self.size = value
        def tip(self):
            print("This coffee is great, here is a tip")
            self.price +=1

    pass