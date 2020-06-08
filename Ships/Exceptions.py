class AddingShipException(Exception):
    """
    Klasa bazowa dla wyjątków związanych z dodawaniem statku
    """
    pass
class CoordinatesOutOfRangeException(AddingShipException):
    pass

class WrongOrientationException(AddingShipException):
    pass

class OccupiedException(AddingShipException):
    pass

class WrongLengthException(AddingShipException):
    pass

class ShootingShipException(Exception):
    """
    Klasa bazowa dla wyjątków związanach z zestrzeleniem statku
    """
    pass

class MissedException(ShootingShipException):
    pass

class HitException(ShootingShipException):
    def __init__(self,name):
        """
        konstruktor
        :param name: string : nazwa stanu Trafiony lub Zatopiony
        """
        self.name=name

