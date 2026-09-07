class ProductMonitorError(Exception): pass

class InvalidIdError(ProductMonitorError): pass
class InvalidNameError(ProductMonitorError): pass
class EmptyNameError(ProductMonitorError): pass
class InvalidURLError(ProductMonitorError): pass
class EmptyURLError(ProductMonitorError): pass
class InvalidPriceError(ProductMonitorError): pass