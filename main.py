from selenium import webdriver
from selenium.webdriver.common.by import By


browser = webdriver.Chrome()
browser.get('https://www.amazon.com/s?k=dyson+hair+dryer&i=stripbooks-intl-ship&crid=29H1MBADOCP5V&sprefix=dyson%2Cstripbooks-intl-ship%2C465&ref=nb_sb_ss_ts-doa-p_3_5')
elem_list = browser.find_element(By.CSS_SELECTOR,"div.s-main-slot.s-result-list.s-search-results.sg-row")

items =elem_list.find_elements(By.XPATH,'//div[@data-component-type="s-search-result"]')
print(len(items))
elem = browser.find_element