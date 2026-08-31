from playwright.sync_api import sync_playwright
from src.products import save_product_report
import json



# 1. Read JSON before opening the browser
# Path to JSON file
file_path = "data\mock_product_list.json"

# Open and parse file
with open(file_path, "r", encoding="utf-8") as file:
  products = json.load(file)

# 2. Open the browser
with sync_playwright() as p:
  browser = p.chromium.launch(
    headless=False,
    downloads_path=r'D:\Code\Projetos\automacoes\price-stock-monitor'
  )
  
  # Session configs
  context = browser.new_context(
    viewport={
      'width':  1920,
      'height': 1080
    },
    locale='pt-BR',
    timezone_id='America/Sao_Paulo',
    record_video_dir='r/.videos',
    record_video_size={
      'width':  1920,
      'height': 1080
    },
    color_scheme='light'
  )
  
  page = context.new_page()
  
  page.set_default_navigation_timeout(30000) #30s
  page.set_default_navigation_timeout(60000) #60s
  
  # Website url
  website_url = 'https://usealphaco.com.br/'
  
  page.goto(url=website_url, wait_until='domcontentloaded')
  
  # 3. Get product prices
  save_product_report(page=page, products=products)
  input('..........\nPress any key to continue')
  
  browser.close()