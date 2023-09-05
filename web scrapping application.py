#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from bs4 import BeautifulSoup
import requests
import re

url = "https://www.daft.ie/property-for-rent/cork-city" # Properties to rent in Cork City
page = requests.get(url).text
doc = BeautifulSoup(page, "html.parser")

print(doc)


# In[1]:


from bs4 import BeautifulSoup
import requests
import re

url = "https://www.daft.ie/property-for-rent/cork-city" # Properties to rent in Cork City
page = requests.get(url).text
doc = BeautifulSoup(page, "html.parser")

listings = doc.find(class_="SearchPage__SearchResults-gg133s-3 jGQNan") #All code within ul container
print(listings)


# In[2]:


from bs4 import BeautifulSoup
import requests
import re

url = "https://www.daft.ie/property-for-rent/cork-city" # Properties to rent in Cork City
page = requests.get(url).text
doc = BeautifulSoup(page, "html.parser")

listings = doc.find(class_="SearchPage__SearchResults-gg133s-3 jGQNan") #All code within ul container
rentals = listings.find_all("h2")# Gets all instances of h2 (name) tag
print(rentals)
# As "rentals" is a list, I am unable to get the string.


# In[3]:


from bs4 import BeautifulSoup
import requests
import re

# Properties to rent in Cork City
url = "https://www.daft.ie/property-for-rent/cork-city" 
page = requests.get(url).text
doc = BeautifulSoup(page, "html.parser")

#All code within ul container
listings = doc.find(class_="SearchPage__SearchResults-gg133s-3 jGQNan") 
# Gets all instances of h2 (name) tag
rentals = listings.find_all("h2") 
# As "rentals" is a list, I am unable to get the string of each h2 tag.

str_rentals = []

# For loop iterates over "rentals", gets the string values of each h2 entry, 
# and appends it to the "str_rentals" list.
for names in rentals: 
    str_rentals.append(names.string)
    
print(str_rentals) 


# In[4]:


from bs4 import BeautifulSoup
import requests
import re

# Properties to rent in Cork City
url = "https://www.daft.ie/property-for-rent/cork-city" 
page = requests.get(url).text
doc = BeautifulSoup(page, "html.parser")

#All code within ul container
listings = doc.find(class_="SearchPage__SearchResults-gg133s-3 jGQNan") 
# Gets all instances of h2 (name) tag
rentals = listings.find_all("h2")

links = listings.find_all("a")

print(links)


# In[5]:


from bs4 import BeautifulSoup
import requests
import re

# Properties to rent in Cork City
url = "https://www.daft.ie/property-for-rent/cork-city" 
page = requests.get(url).text
doc = BeautifulSoup(page, "html.parser")

#All code within ul container
listings = doc.find(class_="SearchPage__SearchResults-gg133s-3 jGQNan") 
# Gets all instances of h2 (name) tag
rentals = listings.find_all("h2")

links = listings.find("a").get("href") # got one link!

print(links)


# In[6]:


from bs4 import BeautifulSoup
import requests
import re

# Properties to rent in Cork City
url = "https://www.daft.ie/property-for-rent/cork-city" 
page = requests.get(url).text
doc = BeautifulSoup(page, "html.parser")

#All code within ul container
listings = doc.find(class_="SearchPage__SearchResults-gg133s-3 jGQNan") 
# Gets all instances of h2 (name) tag
rentals = listings.find_all("h2")

a_tags = listings.find_all("a") 

href = []

# Loop accesses each href of the 'a' tags, adds on the rest of the full link URL
# and then appeands each link to the 'href' list
for tag in a_tags:
    href.append("https://www.daft.ie" + tag.get("href"))

print(href) # Got hrefs, but out-of-order


# In[ ]:


len(href)


# In[7]:


# Full code for names and links 06-03-2023
from bs4 import BeautifulSoup
import requests
import re

# Properties to rent in Cork City
url = "https://www.daft.ie/property-for-rent/cork-city" 
page = requests.get(url).text
doc = BeautifulSoup(page, "html.parser")

#All code within ul container
listings = doc.find(class_="SearchPage__SearchResults-gg133s-3 jGQNan") 
# Gets all instances of h2 (name) tag
rentals = listings.find_all("h2")

str_rentals = []

# For loop iterates over "rentals", gets the string values of each h2 entry, 
# and appends it to the "str_rentals" list.
for names in rentals: 
    str_rentals.append(names.string)
    
print(str_rentals) 

a_tags = listings.find_all("a") 

href = []

# Loop accesses each href of the 'a' tags, adds on the rest of the full link URL
# and then appeands each link to the 'href' list
for tag in a_tags:
    href.append("https://www.daft.ie" + tag.get("href"))

print(href) # Got hrefs, but out-of-order


# In[ ]:





# In[ ]:





# In[8]:


# Now I need to write code the fetch the prices
from bs4 import BeautifulSoup
import requests
import re

# Properties to rent in Cork City
url = "https://www.daft.ie/property-for-rent/cork-city" 
page = requests.get(url).text
doc = BeautifulSoup(page, "html.parser")

#All code within ul container
listings = doc.find(class_="SearchPage__SearchResults-gg133s-3 jGQNan") 
prices = listings.find_all("h3")

str_prices = []

# For loop iterates over "prices", gets the string values of each h3 entry, 
# and appends it to the "str_prices" list.
for value in prices: 
    str_prices.append(value.text)
print(str_prices)


# In[10]:


# Now I need to write code the fetch the prices
from bs4 import BeautifulSoup
import requests
import re

# Properties to rent in Cork City
url = "https://www.daft.ie/property-for-rent/cork-city" 
page = requests.get(url).text
doc = BeautifulSoup(page, "html.parser")

#All code within ul container
listings = doc.find(class_="SearchPage__SearchResults-gg133s-3 jGQNan") 
prices = listings.find_all("h3")

str_prices = []

# For loop iterates over "prices", gets the string values of each h3 entry, 
# and appends it to the "str_prices" list.
for value in prices: 
    str_prices.append(value.text)

for payment in str_prices:
# This took a while! Strings in a list can't be changed, but can be replaced, so I need
# to make a new variable with a "-" and then replace the string in the list
    if payment[0] != "€":
        newString = "-"
        payment = newString
        print(payment)
    


# In[11]:


# Now I need to write code the fetch the prices
from bs4 import BeautifulSoup
import requests
import re

# Properties to rent in Cork City
url = "https://www.daft.ie/property-for-rent/cork-city" 
page = requests.get(url).text
doc = BeautifulSoup(page, "html.parser")

#All code within ul container
listings = doc.find(class_="SearchPage__SearchResults-gg133s-3 jGQNan") 
prices = listings.find_all("h3")

str_prices = []

# For loop iterates over "prices", gets the string values of each h3 entry, 
# and appends it to the "str_prices" list.
for idx, value in enumerate(prices): 
    str_prices.append(value.text)
# Added to code to replace string to the initial for loop
    if str_prices[idx][0] != "€":
        newString = "-"
        str_prices[idx] = newString

print(str_prices)


# In[12]:


# Now I need to write code the fetch the prices
from bs4 import BeautifulSoup
import requests
import re

# Properties to rent in Cork City
url = "https://www.daft.ie/property-for-rent/cork-city" 
page = requests.get(url).text
doc = BeautifulSoup(page, "html.parser")

#All code within ul container
listings = doc.find(class_="SearchPage__SearchResults-gg133s-3 jGQNan") 
prices = listings.find_all("h3")

str_prices = []

# For loop iterates over "prices", gets the string values of each h3 entry, 
# and appends it to the "str_prices" list.
for idx, value in enumerate(prices): 
    value = value.text
    str_prices.append(value[:7])
# Added to code to replace string to the initial for loop
    if str_prices[idx][0] != "€":
        newString = "-"
        str_prices[idx] = newString

print(str_prices)


# In[ ]:


# Full code for names, prices and links 
from bs4 import BeautifulSoup
import requests
import re

# Properties to rent in Cork City
url = "https://www.daft.ie/property-for-rent/cork-city" 
page = requests.get(url).text
doc = BeautifulSoup(page, "html.parser")

#All code within ul container
listings = doc.find(class_="SearchPage__SearchResults-gg133s-3 jGQNan") 
# Gets all instances of h2 (name) tag
rentals = listings.find_all("h2")

str_rentals = []

# For loop iterates over "rentals", gets the string values of each h2 entry, 
# and appends it to the "str_rentals" list.
for names in rentals: 
    str_rentals.append(names.string)

a_tags = listings.find_all("a") 

hrefs = []

# Loop accesses each href of the 'a' tags, adds on the rest of the full link URL
# and then appeands each link to the 'href' list
for tag in a_tags:
    hrefs.append("https://www.daft.ie" + tag.get("href"))

prices = listings.find_all("h3")

str_prices = []

# For loop iterates over "prices", gets the string values of each h3 entry, 
# and appends it to the "str_prices" list.
for idx, value in enumerate(prices): 
    value = value.text
    str_prices.append(value[:7])
# Added to code to replace string to the initial for loop
    if str_prices[idx][0] != "€":
        newString = "-"
        str_prices[idx] = newString

print(str_rentals, "\n", str_prices, "\n", hrefs)


# In[13]:


# Next, find number of bedrooms
from bs4 import BeautifulSoup
import requests
import re

# Properties to rent in Cork City
url = "https://www.daft.ie/property-for-rent/cork-city" 
page = requests.get(url).text
doc = BeautifulSoup(page, "html.parser")

#All code within ul container
listings = doc.find(class_="SearchPage__SearchResults-gg133s-3 jGQNan") 
# Gets all instances of h2 (name) tag
num_beds_baths= listings.find_all(class_ = "TitleBlock__CardInfoItem-sc-1avkvav-9 iLMdur")
print(num_beds_baths) # As beds and bath info uses same class, both are listed


# In[14]:


# Next, find number of bedrooms
from bs4 import BeautifulSoup
import requests
import re

# Properties to rent in Cork City
url = "https://www.daft.ie/property-for-rent/cork-city" 
page = requests.get(url).text
doc = BeautifulSoup(page, "html.parser")

#All code within ul container
listings = doc.find(class_="SearchPage__SearchResults-gg133s-3 jGQNan") 
# Gets all instances of h2 (name) tag
num_beds_baths= listings.find_all(class_ = "TitleBlock__CardInfoItem-sc-1avkvav-9 iLMdur")

str_bed_bath = []

num_beds = []
num_baths = []

for room in num_beds_baths:
        str_bed_bath.append(room.string)
        
print(str_bed_bath)


# In[15]:


# Next, find number of bedrooms
from bs4 import BeautifulSoup
import requests
import re

# Properties to rent in Cork City
url = "https://www.daft.ie/property-for-rent/cork-city" 
page = requests.get(url).text
doc = BeautifulSoup(page, "html.parser")

#All code within ul container
listings = doc.find(class_="SearchPage__SearchResults-gg133s-3 jGQNan") 
# Gets all instances of h2 (name) tag
num_beds_baths= listings.find_all(class_ = "TitleBlock__CardInfoItem-sc-1avkvav-9 iLMdur")

str_bed_bath = []

num_beds = []
num_baths = []

# Appends string values to "str_bed_bath"
for room in num_beds_baths:
    str_bed_bath.append(room.string)

# Appeads any item containing the word "Bed" to "num_beds", else append to "num_baths"
for bed_or_bath in str_bed_bath:
        if "Bed" in bed_or_bath:
            num_beds.append(bed_or_bath)
        else:
            num_baths.append(bed_or_bath)
        
print(num_baths)


# In[ ]:


# Full code for names, prices, number of beds and baths, and links
from bs4 import BeautifulSoup
import requests
import re

# Properties to rent in Cork City
url = "https://www.daft.ie/property-for-rent/cork-city" 
page = requests.get(url).text
doc = BeautifulSoup(page, "html.parser")

#All code within ul container
listings = doc.find(class_="SearchPage__SearchResults-gg133s-3 jGQNan") 
# Gets all instances of h2 (name) tag
rentals = listings.find_all("h2")

str_rentals = []

# For loop iterates over "rentals", gets the string values of each h2 entry, 
# and appends it to the "str_rentals" list.
for names in rentals: 
    str_rentals.append(names.string)

a_tags = listings.find_all("a") 

hrefs = []

# Loop accesses each href of the 'a' tags, adds on the rest of the full link URL
# and then appeands each link to the 'href' list
for tag in a_tags:
    hrefs.append("https://www.daft.ie" + tag.get("href"))

prices = listings.find_all("h3")

str_prices = []

# For loop iterates over "prices", gets the string values of each h3 entry, 
# and appends it to the "str_prices" list.
for idx, value in enumerate(prices): 
    value = value.text
    str_prices.append(value[:7])
# Added to code to replace string to the initial for loop
    if str_prices[idx][0] != "€":
        newString = "-"
        str_prices[idx] = newString

num_beds_baths= listings.find_all(class_ = "TitleBlock__CardInfoItem-sc-1avkvav-9 iLMdur")

str_bed_bath = []

num_beds = []
num_baths = []

# Appends string values to "str_bed_bath"
for room in num_beds_baths:
    str_bed_bath.append(room.string)

# Appeads any item containing the word "Bed" to "num_beds", else append to "num_baths"
for bed_or_bath in str_bed_bath:
        if "Bed" in bed_or_bath:
            num_beds.append(bed_or_bath)
        else:
            num_baths.append(bed_or_bath)

print(str_rentals, "\n", str_prices, "\n", hrefs, "\n", num_beds, "\n", num_baths)


# In[16]:


# Full code for names, prices, number of beds and baths, links and Dataframe 
import pandas as pd
from bs4 import BeautifulSoup
import requests
import time

# Properties to rent in Cork City
url = "https://www.daft.ie/property-for-rent/cork-city" 
page = requests.get(url).text
doc = BeautifulSoup(page, "html.parser")

#All code within ul container
listings = doc.find(class_="SearchPage__SearchResults-gg133s-3 jGQNan") 
# Gets all instances of h2 (name) tag
rentals = listings.find_all("h2")

str_rentals = []

# For loop iterates over "rentals", gets the string values of each h2 entry, 
# and appends it to the "str_rentals" list.
for names in rentals: 
    str_rentals.append(names.string)

a_tags = listings.find_all("a") 

hrefs = []

# Loop accesses each href of the 'a' tags, adds on the rest of the full link URL
# and then appends each link to the 'href' list
for tag in a_tags:
    hrefs.append("https://www.daft.ie" + tag.get("href"))

prices = listings.find_all("h3")

str_prices = []

# For loop iterates over "prices", gets the string values of each h3 entry, 
# and appends it to the "str_prices" list.
for idx, value in enumerate(prices): 
    value = value.text
    str_prices.append(value[:7])
# Added to code to replace string to the initial for loop
    if str_prices[idx][0] != "€":
        newString = "-"
        str_prices[idx] = newString

num_beds_baths= listings.find_all(class_ = "TitleBlock__CardInfoItem-sc-1avkvav-9 iLMdur")

str_bed_bath = []

num_beds = []
num_baths = []

# Appends string values to "str_bed_bath"
for room in num_beds_baths:
    str_bed_bath.append(room.string)

# Appeads any item containing the word "Bed" to "num_beds", else append to "num_baths"
for bed_or_bath in str_bed_bath:
        if "Bed" in bed_or_bath:
            num_beds.append(bed_or_bath)
        else:
            num_baths.append(bed_or_bath)
            
# The five lists cannot be processed, zip is used to combine them into one list of tuples,
# with the values of each tuple being in coordance to the index of each list
zip_list  = list(zip(str_rentals, str_prices, num_beds, num_baths, hrefs))

# Pandas DataFrame made from zip_list, and labeled columns
df = pd.DataFrame(zip_list, columns=['Address', "Monthly Rent", "Number of Bedrooms", "Number of Bathrooms", "Link"])
df
# Create file name with current date.
filename = "daft_scape " + time.strftime("%d-%m-%Y %-H.%M") + ".csv"
# Save file as comma seperated value (csv) to specified path
df.to_csv(f'/home/corey/Documents/{filename}')


# In[ ]:




