from  DateModel import DataModel

class DatasFestivas(DataModel):

    def __str__(self):
        return f'{self.dia}/{self.mes}/{self.ano},{self.comemoracao}'

