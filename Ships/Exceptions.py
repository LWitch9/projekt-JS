class AddingShipException(Exception):
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
    pass

class MissedException(ShootingShipException):
    pass

class HitException(ShootingShipException):
    pass

class SunkException(ShootingShipException):
    pass