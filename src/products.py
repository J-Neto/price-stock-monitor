from playwright.sync_api import Page
import re
import json
from datetime import datetime, timezone


# class Product:
#   id: int
#   name: str
#   link: str
  
#   def __init__(self):
#     pass


def check_if_value_changed():
  pass

def price_to_numeric(price_str: str) -> float:
  price_without_coin = price_str.replace("R$", "") # R$ 54,99 -> 54,99
  price_with_dot_instead_of_stroke = price_without_coin.replace(",", ".") # 54,99 -> 54.99
  price_float = float(price_with_dot_instead_of_stroke)
  
  return price_float

def get_product_price(page: Page, product: dict) -> None:
  # Go to product page
  page.goto(url=product['link'], wait_until='domcontentloaded')
  
  # Get product price
  price_element = page.locator(".price-item__group.price").first
  raw_text = price_element.inner_text() # Example: Preço promocional R$ 54,99
  
  # Using regex to get only the value part
  match = re.search(r"R\$\s*[\d.,]+", raw_text)
  price = match.group(0) if match else None # Example: R$ 54,99
  
  # TODO: Tratar exceção de elemento não encontrado
  return price
  
def save_report_json(report: list):
  file_path = "data\mock_products_report.json"
    
  with open(file_path, "w", encoding="utf-8") as file:
    json.dump(report, file, indent=4)
  
  print(f"Data successfully written to {file_path}")
  
def save_product_report(page: Page, products: list):
  all_reports = []
  
  for product in products:
    product_price_value = get_product_price(page=page, product=product)
    
    # Convert value para float
    price_float = price_to_numeric(product_price_value)
      
    did_value_change = False
    
    # Actual timestamp 
    utc_time = datetime.now(timezone.utc)
    
    product_report = {
      "id": 1,
      "product_id": product["id"],
      "price": price_float,
      "timestamp": str(utc_time),
      "didValueChange": did_value_change
    }
    
    all_reports.append(product_report)
    
  # Saving report into JSON
  save_report_json(all_reports)