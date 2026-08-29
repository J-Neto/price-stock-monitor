from playwright.sync_api import sync_playwright
from src.products import mock_product_list
from src.products import save_product_report

url = 'https://usealphaco.com.br/'


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
  
  page.goto(url=url, wait_until='domcontentloaded')
  
  save_product_report(page=page, products=mock_product_list)
  input('..........\nPress any key to continue')
  
  browser.close()