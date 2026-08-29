from playwright.sync_api import Page
import re

mock_product_list = [
  {
    'id': 1,
    'name': 'Camiseta Oversized Legacy Azul Marinho',
    'link': 'https://usealphaco.com.br/products/camiseta-legacy-oversized-azul-marinho'
  },
  {
    'id': 2,
    'name': 'Camiseta Poliamida Prime Branco',
    'link': 'https://usealphaco.com.br/products/camiseta-poliamida-prime-branco'
  },
  {
    'id': 3,
    'name': 'Camiseta Oversized Plate Marrom Telha',
    'link': 'https://usealphaco.com.br/products/camiseta-oversized-plate-marrom-telha'
  },
  {
    'id': 4,
    'name': 'Camiseta Oversized Plate Off White',
    'link': 'https://usealphaco.com.br/products/camiseta-oversized-plate-off-white'
  },
  {
    'id': 5,
    'name': 'Camiseta Oversized Legacy Marrom Telha',
    'link': 'https://usealphaco.com.br/products/camiseta-oversized-legacy-marrom-telha'
  },
  {
    'id': 6,
    'name': 'Regata Machão Oversized Lupus Preto',
    'link': 'https://usealphaco.com.br/products/regata-machao-oversized-lupus-preto'
  },
  {
    'id': 7,
    'name': 'Camiseta Oversized Empire Bege Duna',
    'link': 'https://usealphaco.com.br/products/camiseta-oversized-empire-bege-duna'
  },
  {
    'id': 8,
    'name': 'Camiseta Oversized Cutting Season Branco',
    'link': 'https://usealphaco.com.br/products/camiseta-oversized-cutting-season-branco'
  },
  {
    'id': 9,
    'name': 'Camiseta Oversized In Motion Off White',
    'link': 'https://usealphaco.com.br/products/camiseta-oversized-in-motion-off-white'
  },
  {
    'id': 10,
    'name': 'Camiseta Oversized Hunter Preto',
    'link': 'https://usealphaco.com.br/products/camiseta-oversized-hunter-preto'
  },
]

products_report = []

class Product:
  id: int
  name: str
  link: str
  
  def __init__(self):
    pass


def check_if_value_changed():
  pass

def get_product_price(page: Page, product: Product) -> None:
  # Go to product page
  page.goto(url=product['link'], wait_until='domcontentloaded')
  
  # Get product price
  price_element = page.locator(".price-item__group.price").first
  raw_text = price_element.inner_text() # Example: Preço promocional R$ 54,99
  
  # Using regex to get only the value part
  match = re.search(r"R\$\s*[\d.,]+", raw_text)
  price = match.group(0) if match else None # Example: R$ 54,99
  
  return price
  
def save_product_report(page: Page, products: list[Product]):
  for product in products:
    product_price_value = get_product_price(page=page, product=product)
    
    #? Converter valor para inteiro
    
    
    #? Verificar se o valor mudou com
    # did_value_change = check_if_value_changed()
    #* E salvar o valor
    
    products_report.append(product_price_value)
  
  print(products_report)