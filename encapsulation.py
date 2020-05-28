
import pytz

from datetime import datetime, timedelta


class Branch:
    name = ''
    city = ''
    state = ''
    tz = ''
    employees = 0
    revenue = 0
    __opentime = 9
    __closetime = 17
    def isOpen(self):
        def getTime():
            tz1 = pytz.timezone(self.tz)
            tz1 = datetime.now(tz1)
            tz1 = tz1.strftime("%H")
            return int(tz1)
        time = getTime()
        print('Time Zone: {}'.format(self.tz))
        if time >= self.__opentime and time < self.__closetime:
            print('Status: OPEN')
        else:
            print('Status: CLOSED')
    def branchinfo(self):
        msg = 'The {} branch is located in {}, {}. \nIt has {} employees and a revenue of {}. \nBranch hours: {}:00 to {}:00'.format(self.name,self.city,\
            self.state,self.employees,self.revenue,self.__opentime,self.__closetime)
        print(msg)
    def printRevenue(self):
        msg = 'The revenue is {}.'.format(self.revenue)
        print(msg)
    def __init__(self,name,city,state,tz,employees,revenue):
        self.name = name
        self.city = city
        self.state = state
        self.tz = tz
        self.employees = employees
        self.revenue = revenue
    def getAll(self):
        self.branchinfo()
        self.isOpen()
    def setOpenCloseTime(self,opentime,closetime):
        self.__opentime = opentime
        self.__closetime = closetime
        
        
class purchasingBranch(Branch):
    purchasing = 0
    def __init__(self,name,city,state,tz,employees,revenue,purchasing):
        Branch.__init__(self,name,city,state,tz,employees,revenue)
        self.purchasing = purchasing
    def purchase(self):
        print('The {} branch can purchase {} worth of goods.'.format(self.city, self.purchasing))
    def getAllPur(Branch,self):
        Branch.getAll()
        self.purchase()

class SalesBranch(Branch):
    _sales = 0
    def __init__(self,name,city,state,tz,employees,revenue,opentime,closetime,sales):
        Branch.__init__(self,name,city,state,tz,employees,revenue)
        self.__opentime = opentime
        self.__closetime = closetime
        self._sales = sales
    def setSales(self,newSales):
        self._sales = newSales
    def sale(self):
        print('The {} branch makes {} in sales.'.format(self.city,self._sales))
    def getAllSales(Branch,self):
        Branch.getAll()
        self.sale()

    

if __name__ == '__main__':
    p = Branch('Portlandia','Portland','OR','America/Los_Angeles',25,1000000)
    print(p.getAll())
    
    p1 = purchasingBranch('Other Branch','London','EN','Europe/London',12,1400000,12000)
    print(p1.getAllPur(p1))

    #THE BELOW WILL NOT CHANGE THE OPEN/CLOSE TIME DUE TO ENCAPSULATION (EVEN THOUGH THEY ARE GIVEN IN THE ARGUEMENTS)
    
    p2 = SalesBranch('Third Branch','New York','NY','America/New_York',182,1400000000,8,18,120000000)
    print(p2.getAllSales(p2))

    #THE BELOW WILL CHANGE THE OPEN/CLOSE TIME USING THE PARENT CLASS METHOD

    p2.setOpenCloseTime(8,18)

    #THE BELOW WILL PRINT THE NEW OPEN/CLOSE VALUES

    print(p2.getAllSales(p2))

    p2.setSales(1234567)

    print(p2.sale())
