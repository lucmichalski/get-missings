from selenium import webdriver

url = input("URL: ")

if url:
    driver = webdriver.Chrome(executable_path='./driver/chromedriver')
    driver.get(url)

    a_tags = driver.find_elements_by_xpath('//a')

    for a in a_tags:
        if a.get_attribute('title') == '':
            print(a.get_attribute('href'))
