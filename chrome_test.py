import selenium.webdriver as webdriver
import lxml.html as lh
import lxml.html.clean as clean

browser = webdriver.Chrome()
input("Press Enter to continue...")

browser.refresh()

# rdr_content = browser.find_element_by_class_name('rdr-content')
# rdr_cols = rdr_content.find_elements_by_class_name('rdr-col')

# for rdr_col in rdr_cols:
#     rdr_col_content = rdr_col.find_element_by_class_name('rdr-col-content')
#     hsec = rdr_col_content.find_element_by_class_name('hsection1')
#     # bs = hsec.find_elements_by_class_name('b')
#     bs = browser.find_elements()
#     for b in bs:
#         if b.text != "" :
#             print(b.text)

# rdr_content = browser.find_elements_by_xpath("//*[not(*)]")


# for b in rdr_content:
#     print(b.get_attribute("class"))
#     if b.text != "" :
#         print(b.text)

# def find_recursive(els):
#     for el in els:
#         new_els = el.find_elements_by_xpath("//*[not(*)]")
#         if (new_els) == 0:
#             print("0------------")
#             print(el.get_attribute("class"))
#             print(el.text)
#             return
#         if len(new_els) == 1:
#             print("1------------")
#             print(new_els[0].get_attribute("class"))
#             print(new_els[0].text)
#             return
#         find_recursive(new_els)


# rdr_content = browser.find_elements_by_xpath("//*[not(*)]")
# find_recursive(rdr_content)

# https://mybook.ru/author/lyubov-levina/mobilnye-prilozheniya-i-poleznye-sajty-dlya-rzhavy/reader/



# file_object = open("test.html", "w")
# file_object.write(html)
# file_object.close() 

# browser.close()

# browser.save_screenshot("landing_page.png")




# browser = webdriver.Chrome() # Get local session of Chrome
# ch = webdriver.Chrome.current_url
# print (ch.get())
# browser.get("https://mybook.ru/author/lyubov-levina/mobilnye-prilozheniya-i-poleznye-sajty-dlya-rzhavy/reader/") # Load page

# content=browser.page_source
# cleaner=clean.Cleaner()
# content=cleaner.clean_html(content) 
# doc=lh.fromstring(content)

rdr_content = browser.find_elements_by_class_name('b')


for b in rdr_content:
    print(b.get_attribute("class"))
    if b.text != "" :
        print(b.text)