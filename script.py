import time
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from progress.bar import Bar
from progress.spinner import Spinner,LineSpinner

spinner = Spinner('Loading.. ')
lineSpinner = LineSpinner('Scanning ')

print("\nExecuting Script")
url  = "https://www.portal.cfm.org.br/busca-medicos/"

#Opções
option = Options()

option.headless = True
#options=option -> Ocultar bot
#driver = webdriver.Firefox(options=option)
driver = webdriver.Firefox()

#Acessa o site
driver.get(url)
print(f"Accessing website: {url}")

#Accepting Cookies
driver.find_element(By.CLASS_NAME, 'button').click()

#Searching button by class name and submite to loading doctores into the page
driver.find_element(By.CLASS_NAME, 'btnPesquisar').submit()

#Wait until server full the page with contents
for i in range(10):
    spinner.next()
    time.sleep(1)
spinner.finish()

def inputPag():
    try:
        nPag = eval(input('Type the number of pages to be scanned: '))
    except NameError:
        print(f'\nErro:\nInvalid!\n')
        return inputPag()
    else:
        def selectPag():
            try:
                initPag = eval(input('Scanning from page: '))
            except NameError:
                print(f'\nErro:\nInvalid!\n')
                return selectPag()
            else:
                #Def starting page
                firstPage = initPag
                nextPage = 1

                #Counting Doctors and Pages
                totalPage = 0
                medicos = 0

                #Progress Bar
                bar = Bar('Processando',max=firstPage)
                
                #Unnecessary If, but i was lazy to fix this
                if firstPage:
                    #The right way starts here
                    if firstPage > 1:
                        for reach in range(1,firstPage-1):
                            #Clicking through pagination util reach the typed page
                            nextPage += 1
                            driver.find_element(By.XPATH,f"//div[@class='paginationjs-pages']//ul//li[@data-num='{nextPage}']//a").click()
                            bar.next()
                        bar.next()
                        bar.next()
                        bar.finish()
                        
                        #Waiting content be loaded
                        print("Wait...")
                        time.sleep(10)

                        driver.find_element(By.XPATH,f"//div[@class='paginationjs-pages']//ul//li[@data-num='{nextPage+1}']//a").click()
                        nextPage += 1

                        for i in range(10):
                            spinner.next()
                            time.sleep(1)
                        spinner.finish()

                    initPage = nextPage
                    print(f"\nStarting Scan on {initPage} \n")

                    #Opening File quotes.csv to writing content
                    f = open("quotes.csv","w")

                    #Scraping
                    for pages in range(nPag):
                        
                        #Selecionar os elementos
                        print("Scanning")
                        nomes = driver.find_elements(By.XPATH,"//div[@class='card-body']//h4")
                        telefones = driver.find_elements(By.XPATH,"//div[@class='row telefone']//div")
                        elementos = len(nomes)
                        medicos += elementos

                        
                        print("Saving...\n")
                        for i in range(elementos):
                            n = nomes[i].text
                            t = telefones[i].text

                        #Saving contents into quotes.csv
                            f.write(f"{n}, {t}\n")
                        driver.find_element(By.XPATH,f"//div[@class='paginationjs-pages']//ul//li[@data-num='{nextPage}']//a").click()
                        print(f"\n Page {nextPage} scanned.")
                        nextPage += 1
                        totalPage += 1    

                        time.sleep(10)

                    print(f"\nScanned pages: {totalPage}")  
                    print(f"{medicos} doctor saved in: quotes.csv")  
                    print(f"\n Finished at pag {nextPage-1}")
                    
                    f.close()
        selectPag()        
inputPag()



driver.quit()
