import pytest
from src.models.product import Product
from src.models.exceptions import (
  InvalidIdError,
  InvalidNameError,
  EmptyNameError,
  InvalidURLError,
  EmptyURLError,
  InvalidPriceError
)

#* Happy Paths 😃 =======================================================

def test_create_valid_product():
  """Ensure that a product with 100% correct data is successfully instantiated."""
  product = Product(
    id = 1,
    name = "Camiseta Oversized Legacy Azul Marinho",
    url = "https://usealphaco.com.br/products/camiseta-legacy-oversized-azul-marinho",
    price = 49.99
  )
  
  assert product.id == 1
  assert product.name == "Camiseta Oversized Legacy Azul Marinho"
  assert product.url == "https://usealphaco.com.br/products/camiseta-legacy-oversized-azul-marinho"
  assert product.price == 49.99
  assert product.is_available is True

def test_create_out_of_stock_product():
  """Ensures that out-of-stock products (price None) are created with 'is_available' set to False."""
  product = Product(
    id=42,
    name="Camiseta Poliamida Prime Branco",
    url="https://usealphaco.com.br/products/camiseta-poliamida-prime-branco",
    price=None
  )
  
  assert product.id == 42
  assert product.name == "Camiseta Poliamida Prime Branco"
  assert product.url == "https://usealphaco.com.br/products/camiseta-poliamida-prime-branco"
  assert product.price is None
  assert product.is_available is False
  

#! Sad Paths   🙁 =======================================================

# ID SAD VALIDATIONS

@pytest.mark.parametrize("invalid_id", [
  "1",      # String instead int
  1.5,      # Float instead int
  True,     # Boolean (Validator blocks bool escape)
  False,    # Boolean (Validator blocks bool escape)
  0,        # Value must be higher than 0
  -1        # Value must be positive 
])

def test_product_invalid_id_raises_exception(invalid_id):
  """Ensure that IDs of the wrong type or less than or equal to 0 trigger an InvalidIdError."""
  with pytest.raises(InvalidIdError):
    Product(id=invalid_id, name="Produto", url="https://link.com", price=10.0)

# ==================================================
# NAME SAD VALIDATIONS

@pytest.mark.parametrize("invalid_name", [
  1,        # int instead String
  1.0,      # Float instead String
  True,     # Boolean instead String
  False,    # Boolean instead String
])

def test_product_invalid_name_raises_exception(invalid_name):
  """Ensure that names that aren't str triggers InvalidNameError."""
  with pytest.raises(InvalidNameError):
    Product(id=1, name=invalid_name, url="https://link.com", price=10.0)
    
@pytest.mark.parametrize("empty_name", [
  "",     # Absolut empty
  " ",    # Only white spaces
  "\n\t"  # breakline and tabulation
])

def test_product_empty_name_raises_exception(empty_name):
  """Ensure that empty names or purely composed by spaces triggers EmptyNameError."""
  with pytest.raises(EmptyNameError):
    Product(id=1, name=empty_name, url="https://link.com", price=10.0)
    
# ==================================================
# URL SAD VALIDATIONS

@pytest.mark.parametrize("invalid_url", [
  1,        # int instead String
  1.0,      # Float instead String
  True,     # Boolean instead String
  False,    # Boolean instead String
])

def test_product_invalid_url_raises_exception(invalid_url):
  """Ensure that urls that aren't str triggers InvalidURLError."""
  with pytest.raises(InvalidURLError):
    Product(id=1, name="produto", url=invalid_url, price=10.0)
    
@pytest.mark.parametrize("empty_url", [
  "",     # Absolut empty
  " ",    # Only white spaces
  "\n\t"  # breakline and tabulation
])

def test_product_empty_url_raises_exception(empty_url):
  """Ensure that empty URLs or purely composed by spaces trigger EmptyURLError."""
  with pytest.raises(EmptyURLError):
    Product(id=1, name="produto", url=empty_url, price=10.0)
    
@pytest.mark.parametrize("bad_url", [
  "www.usealphaco.com.br",   # without protocol
  "https://",                # only protocol
  "ftp://usealphaco.com"     # protocol unsuported
])  
  
def test_product_bad_url_raises_exception(bad_url):
  """Ensure that URLs that do not start with http:// or https:// raise an InvalidURLError."""
  with pytest.raises(InvalidURLError):
    Product(id=1, name="produto", url=bad_url, price=10.0)

# ==================================================
# PRICE SAD VALIDATIONS

@pytest.mark.parametrize("invalid_price", [
  "10",
  True,
  False,
  -1,
  0,
  -1.0,
  0.0
])

def test_product_invalid_price_value_raises_exception(invalid_price):
  with pytest.raises(InvalidPriceError):
    Product(id=1, name="product", url="https://link.com", price=invalid_price)