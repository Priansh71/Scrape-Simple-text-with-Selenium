from selenium import webdriver
import time
# for winddows to run in any IDE
# from selenium.webdriver.chrome.service import Service
# service = Service("C:absolute path to the downloaded chrome driver file")
def get_driver():
  #set options to make browsing easier
  options= webdriver.ChromeOptions()
  options.add_argument("disable-infobars")
  options.add_argument("start-maximized")
  options.add_argument("disable-dev-shm-usage ")
  options.add_argument("no-sandbox")
  options.add_experimental_option("excludeSwitches",  ["enable-automation"])
  options.add_argument("disable-blink-features=AutomationControlled")
    
  driver=webdriver.Chrome(options=options)
  #For windows to run in any IDE
  #  driver=webdriver.Chrome(service=service,options=options)

  driver.get("http://automated.pythonanywhere.com")
  return driver


def clean_text(text):
  """ Extract only temprature form text"""
  output = float(text.split(": ")[1])
  return output

def main():
  driver = get_driver()
  time.sleep(2)
  #element = driver.find_element(by="xpath",value="/html/body/div[1]/div/h1[1]")
  element = driver.find_element(by="xpath",value="/html/body/div[1]/div/h1[2]")
  #return element.text
  return clean_text(element.text)
  
print(main())

'''So on Rep, it worked well.But if I get this codeand I put it on PyCharm, for example, on my Windows computer,and then I run it.I'm going to get this error.It says that chrome driver needs to be in path.So chromedriver is a file which you need to download.So lets download chromedriver and place it in a folder and then connect to that folder with our code.So go to your browser and then do a search for Chrome driver and then go to this web page.So you want to download one of these files, but first you want to know what version of Chrome you have.So I assume you are on your Chrome browser.An easy way to find the version of your Chrome browser is by searching what's my browser version on Google.And then visit this page.And this says that I'm using Chrome 100.That's the version on Windows.So I go back to the ChromeDriver web page and I download the Chrome Driver 100.Version and I get the Win32.zip version.So in my downloads folder, now I have this chromedriver.exe file.
'''