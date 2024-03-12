from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import json
driver = webdriver.Firefox()

with open(f"data.json","w") as f:
    json.dump([],f)


def write_data(new_data,filename='data.json'):
    with open(filename,"r+") as file:
        file_data = json.load(file)
        file_data.append(new_data)
        file.seek(0)

        json.dump(file_data,file,indent=4)

page_no = 0
while page_no<11:
    driver.get(f'http://ebravo.pk/classic/softwares?page={page_no}')

    elem_list = driver.find_element(By.CSS_SELECTOR,".panel")
    item_list = elem_list.find_elements(By.XPATH,"/html/body/div[4]/div/div[1]/div/div[3]/div")
    
    for item in item_list:
        dt = item.find_elements(By.CSS_SELECTOR,"div.thumb")
    
        for j in dt:
                name = j.find_element(By.CSS_SELECTOR,"div.thumb> a> div > div> h6")
                added = j.find_element(By.CSS_SELECTOR,"div.thumb > a > div > div> div> div > div")
                view = j.find_element(By.CSS_SELECTOR,"div.thumb > a > div > div > div > div > div:nth-child(2)")
                downloaded = j.find_element(By.CSS_SELECTOR,"div.thumb > a > div > div > div > div > div:nth-child(3)")
               
                write_data({
                     "Name":name.text,
                     "Added":added.text.split(":")[1],
                     "View":view.text.split(":")[1],
                     "Downloaded":downloaded.text.split(":")[1],
                })
                #print(name.text,"\n",added.text,"\n",view.text,"\n",downloaded.text)

    
    page_no += 1



