from .exceptions import InvalidIdError, EmptyNameError, InvalidURLError, InvalidPriceError, InvalidNameError, EmptyURLError

class Product:
  _id: int
  _name: str
  _url: str
  _price: float
  
  def __init__(self, id: int, name: str, url: str, price: float | None):
    self.id = id
    self.name = name
    self.url = url
    self.price = price
    
  @property
  def id(self):
    return self._id
  
  @id.setter
  def id(self, value: int):
    if not isinstance(value, int) or isinstance(value, bool):
      raise InvalidIdError("ID Error! \nMessage: type must be int!")
    elif value <= 0:
      raise InvalidIdError("ID Error! \nMessage: Value must be higher than 0!")
    else:
      self._id = value
    
  @property
  def name(self):
    return self._name
  
  @name.setter
  def name(self, value: str):
    if not isinstance(value, str):
      raise InvalidNameError("Name Error! \nMessage: type must be string!")
    elif len(value.strip()) == 0:
      raise EmptyNameError("Name Error! \nMessage: string cannot be empty!")
    else:
      self._name = value
  
  @property
  def url(self):
    return self._url
  
  @url.setter
  def url(self, value: str):
    validPrefixes = ("http://", "https://")
    
    if not isinstance(value, str):
      raise InvalidURLError("URL Error! \nMessage: type must be string!")
    elif len(value.strip()) == 0:
      raise EmptyURLError("URL Error! \nMessage: URL cannot be empty!")
    elif not value.startswith(validPrefixes):
      raise InvalidURLError("URL Error! \nMessage: Invalid URL")
    else:
      self._url = value
    
  @property
  def price(self):
    return self._price
  
  @price.setter
  def price(self, value: float):
    if value is None:
      self._price = value
    elif not isinstance(value, (float, int)):
      raise InvalidPriceError("Value Error! \nMessage: type must be numeric!")
    elif value <= 0:
      raise InvalidPriceError("Value Error! \nMessage: value must be higher than 0!")
    else:
      self._price = value
    
  @property
  def is_available(self) -> bool:
    return self._price is not None