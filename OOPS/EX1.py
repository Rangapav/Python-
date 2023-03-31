#CLASS-IS USED TO DEFINE OBJECT
# CLASS IS A BLUE PRINT OF OBJECT
# OBJECT IS A MAPPING OF CLASS


class car:
    def pavan(self):
        self.carname="mahindra"
        self.carprice="10,00,000"
        self.carcolor="blue"
        print("car name=",self.carname,'\n'"car price=",self.carprice,'\n'"carcolor=",self.carcolor)
p=car()
p.pavan()