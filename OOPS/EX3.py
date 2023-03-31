#__INIT__ METHOD IS A IN BUILT FUNCTION TO ASSIGN VALUES TO OBJECT PROPERTIES(OR)
# OTHER OPERATIONS THAT ARE NECESSARY TO DO WHEN THE OBJECT IS BEING CREATED

class Laptop:
    def __init__(self,companyname,generation,ram,rom,laptoptype,price,operatingsystem):
        self.cname=companyname
        self.gener=generation
        self.ram=ram
        self.rom=rom
        self.ltype=laptoptype
        self.price=price
        self.os=operatingsystem
        print("Company Name=",self.cname,'\n'"GENERATION=",self.gener,'\n'"RAM=",self.ram,'\n'"ROM=",self.rom,'\n'"Laptop type=",self.ltype,'\n'"Laptop Price=",self.price,'\n'"Operating System=",self.os)
Laptop("lenovo","5th generation","8gb","256gb","foldable","40,000","windows"'\n')
Laptop("HP","5th generation","8gb","256gb","foldable","50,000","LINUX"'\n')
Laptop("DELL","5th generation","8gb","256gb","foldable","45,000","windows"'\n')
Laptop("APPLE","5th generation","8gb","256gb","foldable","80,000","MACKBOOK"'\n')
Laptop("INFINIX","5th generation","8gb","256gb","foldable","30,000","windows"'\n')

# init is used to reduce code lines in program
# by using this constructor we reuse the code multiple times