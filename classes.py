
import pytz

from datetime import datetime, timedelta


class Branch:
    name = ''
    city = ''
    state = ''
    tz = ''
    employees = 0
    revenue = 0
    opentime = 9
    closetime = 17
    def isOpen(self):
        def getTime():
            tz1 = pytz.timezone(self.tz)
            tz1 = datetime.now(tz1)
            tz1 = tz1.strftime("%H")
            return int(tz1)
        time = getTime()
        print('Time Zone: {}'.format(self.tz))
        if time >= self.opentime and time < self.closetime:
            print('Status: OPEN')
        else:
            print('Status: CLOSED')
    def branchinfo(self):
        msg = 'The {} branch is located in {}, {}. \nIt has {} employees and a revenue of {}. \nBranch hours: {}:00 to {}:00'.format(self.name,self.city,\
            self.state,self.employees,self.revenue,self.opentime,self.closetime)
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
    sales = 0
    def __init__(self,name,city,state,tz,employees,revenue,opentime,closetime,sales):
        Branch.__init__(self,name,city,state,tz,employees,revenue)
        self.opentime = opentime
        self.closetime = closetime
        self.sales = sales
    def sale(self):
        print('The {} branch makes {} in sales.'.format(self.city,self.sales))
    def getAllSales(Branch,self):
        Branch.getAll()
        self.sale()

    

if __name__ == '__main__':
    p = Branch('Portlandia','Portland','OR','America/Los_Angeles',25,1000000)
    print(p.getAll())
    
    p1 = purchasingBranch('Other Branch','London','EN','Europe/London',12,1400000,12000)
    print(p1.getAllPur(p1))
    
    p2 = SalesBranch('Third Branch','New York','NY','America/New_York',182,1400000000,8,18,120000000)
    print(p2.getAllSales(p2))
