class Category(self):

    def __init__(self, description):
        self.description = description
        self.ledger = []
        self.balance = 0.0
        
    def check_funds(self, amount):
        if balance < amount:
            return False
        else:
            return True
            
    def deposit(self, amount, description=""):
        ledger.append(f'"amount": {amount}, "description": {description}')
        balance = balance + deposit_amount
    
    def withdraw(self, amount, description=""):
        ledger.append(f'"amount": {-amount}, "description": {description}')
        balance = balance - deposit_amount
    

    def get_balance():
        return balance
    
    def transfer(transfer_amount, from_category, to_category):
        withdraw(transfer_amount, from_category)
        deposit(transfer_amount, to_category)
        
def create_spend_chart(categories):
    chart = """Percentage spent by category
               100|          
                90|          
                80|          
                70|          
                60| o        
                50| o        
                40| o        
                30| o        
                20| o  o     
                10| o  o  o  
                 0| o  o  o  
                    ----------
                    F  C  A  
                    o  l  u  
                    o  o  t  
                    d  t  o  
                       h     
                       i     
                       n     
                       g   
            """
    return chart
    

print(self.food.deposit(900, "deposit"))
print(self.food.deposit(45.56))