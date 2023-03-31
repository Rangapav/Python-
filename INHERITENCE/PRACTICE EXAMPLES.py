
# class person:
#     def myfunc(self):
#        print("pavan")
# class child (person):
#      def display(self):
#           print("kalyan")
# x=child()
# x.myfunc()
# x.display()
#
# class parent:
#     def display(self):
#         print("pavan")
# class child(parent):
#     def show(self):
#         print("kalyan")

# c=child()
# c.display()
# c.show()

class grandparent:
    def gdisplay(self):
        print("grand parent")
class parent(grandparent):
    def pdisplay(self):
        print("parent")
class child(parent):
    def cdisplay(self):
        print("child")

# x=parent()
# x.pdisplay()
# x.gdisplay()
# c=child()
# c.gdisplay()
# c.cdisplay()
x=child()
x.gdisplay()
x.pdisplay()
x.cdisplay()
