from enum import Enum

class TempConvert:

    WATER_BOIL_CEL = 100

    class TEMP_SELECT(Enum):
        CELCIUS = 0,
        FAHRENHEIT = 1,
        KELVIN = 2

    @classmethod
    def CelToFahr(cls, celcius):
        fahr = (9/5)*celcius + 32
        return fahr

    @classmethod
    def FahrToCel(cls, fahr):
        cel = (5/9)*(fahr - 32)
        return cel

    @classmethod
    def FahrToKelvin(cls, fahr):
        kelvin = (fahr-32)*(5/9)+273.15
        return kelvin
    
    @classmethod
    def CelToKelvin(cls, cel):
        kelvin = cel + 273.15
        return kelvin

    @classmethod
    def BoilingWater(cls, sel:TEMP_SELECT):
        boilTemp = cls.WATER_BOIL_CEL

        match sel:
            case cls.TEMP_SELECT.CELCIUS:
                boilTemp = cls.WATER_BOIL_CEL
            case cls.TEMP_SELECT.FAHRENHEIT:
                boilTemp = cls.CelToFahr(cls.WATER_BOIL_CEL)
            case cls.TEMP_SELECT.KELVIN:
                boilTemp = cls.CelToKelvin(cls.WATER_BOIL_CEL)

        return boilTemp        

if __name__ == '__main__':

    # for i in range(0, 100):
    #     print(f'{i} Cel = {TempConvert.convertToFahr(i):.2f} Fahr')
    
    # print('------------------')
    # for i in range(60, 0, -1):
    #     print(f'{i} Fahr = {TempConvert.convertToCel(i):.2f} Cel')

    fahrToCel = [round(TempConvert.FahrToCel(i),2) for i in range(0,100)]
    print(f'TempConvert_FahrToCel: {fahrToCel}')

    celToFahr = [round(TempConvert.CelToFahr(i),2) for i in range(0, 60)]
    print(f'TempConvert_CelToFahr: {celToFahr}')

    fahrToKel = [round(TempConvert.FahrToKelvin(i),2) for i in range(0,60)]
    print(f'TempConvert_FahrToKel: {fahrToKel}')

    celToKel = [round(TempConvert.CelToKelvin(i),2) for i in range(0,60)]
    print(f'TempConvert_CelToKel: {celToKel}')

    print(f'Boiling Water Celcius: {TempConvert.BoilingWater(TempConvert.TEMP_SELECT.CELCIUS)}')
    print(f'Boiling Water Fahrenheit: {TempConvert.BoilingWater(TempConvert.TEMP_SELECT.FAHRENHEIT)}')
    print(f'Boiling Water Kelvin: {TempConvert.BoilingWater(TempConvert.TEMP_SELECT.KELVIN)}')