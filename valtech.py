from selenium import webdriver
import re




# Google Chrome driver
driver = webdriver.Chrome()


driver.get('http://www.valtech.co.uk')

# find element with text recent blogs
element = driver.find_elements_by_xpath("//*[contains(text(), 'recent blogs')]")[0]
print "-------------------------------"
print "Finding Recent blogs: "
if element.is_displayed():
  print "Element found"
  #extra layer
  assert "recent blogs" in driver.page_source
else:
  print "Element not found"



driver.get('http://www.valtech.co.uk/services')

e1 = driver.find_element_by_tag_name("h1")
print "-------------------------------"
print "URL : http://www.valtech.co.uk/services"
print "Testing services page: "
if e1.text == "Services":
	print "H1 tag is equal to Services"

print "-------------------------------"


driver.get('http://www.valtech.co.uk/about')

e2 = driver.find_element_by_tag_name("h1")
print "-------------------------------"
print "URL : http://www.valtech.co.uk/about"
print "Testing about page: "
if e2.text == "About":
	print "H1 tag is equal to About"

print "-------------------------------"

driver.get('http://www.valtech.co.uk/work')

e3 = driver.find_element_by_tag_name("h1")
print "-------------------------------"
print "URL : http://www.valtech.co.uk/work"
print "Testing work page: "
if e3.text == "Work":
	print "H1 tag is equal to Work"

print "-------------------------------"


driver.get("http://www.valtech.co.uk/about/contact-us")

e4 = driver.find_elements_by_class_name("office__heading")
print "-------------------------------"
print "URL : http://www.valtech.co.uk/about/contact-us"
print "Number of offices: "
print len(e4)
for e in e4:
	print "[Office] : " + e.text

print "-------------------------------"

# Close the browser!
driver.quit()