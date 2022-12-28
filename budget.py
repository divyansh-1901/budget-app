class Category:
    def __init__(self,name):
        self.name = name
        self.ledger=[]
        
    def deposit(self,amount,desc=''):
        x_dep = {'amount':amount,'description':desc}
        self.ledger.append(x_dep)
    
    def withdraw(self,amount,desc=''):
        x_withd = {'amount':-amount,'description':desc}
        if self.check_funds(amount):
            self.ledger.append(x_withd)
            return True
        else:
            return False
    
    def get_balance(self):
        am = 0
        for i in self.ledger:
            i_am = i['amount']
            am = i_am + am
        return am
    
    def transfer(self,amount,destination):
        initial_name = self.name
        if self.check_funds(amount):
            self.withdraw(amount,'Transfer to {}'.format(destination.name))
            destination.deposit(amount,'Transfer from {}'.format(initial_name))
            return True
        else:
            return False
    
    def check_funds(self,amount):
        am = self.get_balance()
        if amount > am:
            return False
        else:
            return True

    def __str__(self):
        x = self.ledger
        title = self.name.center(30,'*') + '\n'
        x = ''
        for i in self.ledger:
            x = x + '{}'.format(i['description'][:23].ljust(23)) + '{:7.2f}'.format(i['amount']).rjust(7) + '\n'
        total = 'Total: '+ str(Category.get_balance(self))
        return (title+x+total)
    
    
# OUTSIDE THE CLASS
def create_spend_chart(lst):
    i = 0
    withdraw = []
    for cat in lst:
        neg_amt = 0
        for x in cat.ledger:
            if x['amount']<0:
                neg_amt = neg_amt - x['amount']
        withdraw.append(neg_amt)
        i = i+1
    total_withdraw = sum(withdraw)
    w = []
    for i in range(len(lst)):
        w.append(int((withdraw[i]/total_withdraw)*10))
    
    #printing starts here
    final ='Percentage spent by category\n'
    for i in range(10,-1,-1):
        x = 0
        final = final + '{}| '.format(str(10*i).rjust(3))
        while x<len(w):
            if w[x] >= i:
                final = final + 'o  '
            else:
                final = final + '   '
            x = x+1
        final = final + '\n'
    
    
    final = final + '----------'.rjust(14,' ')
    
    
    x =[]  
    for cat in lst:
        x.append(cat.name)
    y=[]
    for word in x:
        y.append(len(word))
    length = max(y)
    a=0
    for i in range(length):
        a=0
        final = final + '\n'
        final = final +'     '
        while a < len(x):
            try:
                x[a][i]
                final = final +x[a][i]+'  '
            except:
                final = final +'   '
            a=a+1
    return final
