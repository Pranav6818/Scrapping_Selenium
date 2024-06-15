from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import pandas as pd

url = r'https://www.youtube.com/'

chrome_options = Options()
chrome_options.add_experimental_option("detach",True)

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

driver.get(url)

driver.maximize_window()

time.sleep(2)
search_type = driver.find_element(By.XPATH,"/html/body/ytd-app/div[1]/div/ytd-masthead/div[4]/div[2]/ytd-searchbox/form/div[1]/div[1]/input").send_keys("Krish Naik")
clk_enter = driver.find_element(By.XPATH,"/html/body/ytd-app/div[1]/div/ytd-masthead/div[4]/div[2]/ytd-searchbox/form/div[1]/div[1]/input").send_keys(Keys.ENTER)

time.sleep(2)
driver.get(r'https://www.youtube.com/@krishnaik06/videos')

all_data = driver.find_elements(By.CLASS_NAME, 'style-scope ytd-rich-grid-media')

youtube = []
for data in all_data:
    try:
        title = data.find_element(By.XPATH, './/*[@id="video-title"]').text
        print(title)
        views = data.find_element(By.XPATH, './/*[@id="metadata-line"]/span[1]').text
        print(views)
        time_of_live = data.find_element(By.XPATH, './/*[@id="metadata-line"]/span[2]').text
        print(time_of_live)
        dict = {
            'Title': title,
            'Views of Video': views,
            'Releasing Date': time_of_live
        }
        youtube.append(dict)
    except Exception as e:
        print(f"Error occurred: {e}")
        continue
df = pd.DataFrame(youtube)
df.to_csv('youtube_data.csv', index=False)

