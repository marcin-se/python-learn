# CARworth v1.0                                                                 #
# project calculating the cost of the selected car model                       #
# -*- coding: UTF-8 -*-                                                        #


brandOnSale = 'Opel'
lineOfText = ['Ford:Fiesta:True:True:True:False',
              'Opel:Corsa:True:True:True:True',
              'Renault:Megane:True:True:False:False'
]


class Car:

    def __init__(self, brand, model, isAirBagOK, isPaintingOK,
                 isMechanicOK, isOnSale):
        self.brand = brand
        self.model = model
        self.isAirBagOK = isAirBagOK
        self.isPaintingOK = isPaintingOK
        self.isMechanicOK = isMechanicOK
        self.__isOnSale = isOnSale

    def isDamaged(self):
        return not (self.isAirBagOK and self.isPaintingOK and self.isMechanicOK)

    def getCarInfo(self):
        print('\n{} {}'.format(self.brand, self.model).upper())
        print('Air Bag  - ok -      {}'.format(self.isAirBagOK))
        print('Painting - ok -      {}'.format(self.isPaintingOK))
        print('Mechanic - ok -      {}'.format(self.isMechanicOK))
        print('IS ON SALE           {}'.format(self.__isOnSale))
        print('-' * 30)

    def __getIsOnSale(self):
        return self.__isOnSale

    def __setIsOnSale(self, newIsOnSaleStatus):
        if self.brand == brandOnSale:
            self.__isOnSale = newIsOnSaleStatus
            print('Changing status "isOnSale" to {} for {}'.
                  format(newIsOnSaleStatus, self.brand))
        else:
            print('Cannot change status "isOnSale". Sale valid only for {}'.
                  format(brandOnSale))

    is_On_Sale = property(__getIsOnSale, __setIsOnSale, None,
                  'If set to "True", the car is available in sale/promo.')

    @classmethod
    def readFromText(cls, carText):
        newCar = cls(*carText.split(':'))
        return newCar

    @staticmethod
    def convert_KM_kw(KM):
        return KM * 0.735

    @staticmethod
    def convert_kw_KM(kw):
        return kw * 1.36

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -  #


car_01 = Car.readFromText(lineOfText[0])
car_02 = Car.readFromText(lineOfText[1])
car_03 = Car.readFromText(lineOfText[2])

car_01.getCarInfo()
car_02.getCarInfo()
car_03.getCarInfo()