#INSTANCE VARIABLE IS USED TO CREATE OBJECT TO ACCESS THE PROGRAM VERY QUICKLY
class car:
    # SELF IS A INSTANCE METHOD
    def pavan(self):
        # OBJECT.ATTRIBUTE=VALUE
        self.carname="mahindra"
        self.carprice="10,00,000"
        self.carcolor="blue"
        print("car name=",self.carname,'\n'"car price=",self.carprice,'\n'"carcolor=",self.carcolor)
p=car()
p.pavan()