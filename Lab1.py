
class ElectricLamp:

    purpose_of_electric_lamp = "room lighting"

    def __init__ (self, firm="Unknown", power="Unknown", guarantee="Unknown", country_manufacturer="Unknown"):

        self.firm = firm
        self.power = power
        self.guarantee = guarantee
        self.country_manufacturer = country_manufacturer

    def __del__ (self):
        pass

    def __str__(self) -> str:
        return f"\nFirm: {self.firm}\nPower: {self.power}\nGuarantee: {self.guarantee}\nCountry manufacturer: {self.country_manufacturer}" 

    @staticmethod
    def show_purpose() -> str:
        return ElectricLamp.purpose_of_electric_lamp


def main():

    lamps : [ElectricLamp] = [
        ElectricLamp(firm="Philips", power=11, guarantee=730, country_manufacturer="China"),
        ElectricLamp(power=35, guarantee=90),
        ElectricLamp(firm="MAXUS", power=10, country_manufacturer="China")]        

    print(f"\nLamps for {ElectricLamp.show_purpose()}:")

    for lamp in lamps:
        print(lamp)
    

if __name__ == "__main__":
    main()