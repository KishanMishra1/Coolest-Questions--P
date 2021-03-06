ABC DTH (Direct to Home) firm wants to calculate monthly rent for its consumers. 
'''A consumer can register for one Base Package. Write a python program to implement the below given class diagram.

                              

Class Description:
DirectToHomeService class:

Initialize static variable counter to 101
Inside constructor, auto-generate consumer_number starting from 101
BasePackage class:

validate_base_pack_name():
Validate base pack name. Valid values are "Silver", "Gold" and "Platinum".
If invalid, set attribute, base_pack_name as "Silver" and display "Base package name is incorrect, set to Silver"
calculate_monthly_rent():
Check if subscription period is between 1 and 24 (both inclusive). If so,
Validate base pack name
Identify monthly rent based on base pack. Refer table given.
Consumers are eligible for discount of one month's rent, if subscription period is more than 12 months
Calculate final monthly rent as per the formula given below:
final monthly rent = ((monthly rent * subscription period) – discount amount)/subscription period
Return the calculated final monthly rent
If not, return -1'''



from abc import ABCMeta, abstractmethod
class DirectToHomeService(metaclass=ABCMeta):
    __counter=101
    def __init__(self,consumer_name):
        self.__consumer_name=consumer_name
        self.__consumer_number=DirectToHomeService.__counter
        DirectToHomeService.__counter+=1
        
    def get_consumer_number(self):
        return self.__consumer_number
    def get_consumer_name(self):
        return self.__consumer_name
    
    @abstractmethod
    def calculate_monthly_rent(self):
        pass

    
class BasePackage(DirectToHomeService):
    def __init__(self,consumer_name,base_pack_name,subscription_period):
        self.__base_pack_name=base_pack_name
        self.__subscription_period=subscription_period
        super().__init__(consumer_name)
        
    def get_base_pack_name(self):
        return self.__base_pack_name
    def get_subscription_period(self):
        return self.__subscription_period
    
    def validate_base_pack_name(self):
        if self.__base_pack_name=="Silver" or self.__base_pack_name=="Gold" or self.__base_pack_name=="Platinum":
            return True
            
        else:
            self.__base_pack_name="Silver"
            print("Base package name is incorrect, set to Silver")
            return True
        
    def calculate_monthly_rent(self):
        if self.__subscription_period>=1 and self.__subscription_period<=24:
            if self.validate_base_pack_name() is True:
                if self.__subscription_period>12:
                    if self.__base_pack_name=="Silver":
                        discount=350
                        monthly_rent=350
                    elif self.__base_pack_name=="Gold":
                        discount=440
                        monthly_rent=440
                    elif self.__base_pack_name=="Platinum":
                        discount=560
                        monthly_rent=560
                else:
                    if self.__base_pack_name=="Silver":
                        discount=0 
                        monthly_rent=350
                    elif self.__base_pack_name=="Gold":
                        discount=0 
                        monthly_rent=440
                    elif self.__base_pack_name=="Platinum":
                        discount=0 
                        monthly_rent=560 
                final_monthly_rent=((monthly_rent*self.__subscription_period)-discount)/self.__subscription_period
                return final_monthly_rent
            else:
                return -1
        else:
            return -1
            
obj1=BasePackage("Vetri","Platinum",4,)
res=obj1.calculate_monthly_rent()
print(res)
