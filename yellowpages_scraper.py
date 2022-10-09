from bs4 import BeautifulSoup
import requests
import pandas as pd
import datetime


def get_yellowpages_search_results(base_url, location):

#   fout = open('Yellowpages.txt', 'wt',encoding='utf-8')
#   fclean = open('yellowpages.txt', 'wt')
    search_results = []
    
    page = 1
#   titles = []
    while page < 6:
        url = base_url + location + '&page=' + str(page)
#       url = f"https://www.yellowpages.com/search?search_terms=Furniture&geo_location_terms=Pittsburgh%2C+PA&page={page}"
        response = requests.get(url)
        soup = BeautifulSoup(response.content,'html.parser')
#       fout.write(str(soup))
        mydivs = soup.find_all("div", {"class": "result"})
        for item in mydivs: 
            try: 
                print('-------------------------')
                post_url = "https://www.yellowpages.com/" + (item.find("a", {'class':'business-name'}).attrs['href'])
                name = (item.find("a", {'class':'business-name'}).find('span').text)
                phone = (item.find("div", {'class':'phones phone primary'}).get_text().strip())
                street_Address = (item.find("div", {'class':'street-address'}).get_text().strip())
                locality = (item.find("div", {'class':'locality'}).get_text().strip())
                business_years = (item.find("div", {'class':'years-in-business'}).get_text().strip())
                print("https://www.yellowpages.com/" + (item.find("a", {'class':'business-name'}).attrs['href']))
                print(item.find("a", {'class':'business-name'}).find('span').text)
                print(item.find("div", {'class':'phones phone primary'}).get_text().strip())
                print(item.find("div", {'class':'street-address'}).get_text().strip())
                print(item.find("div", {'class':'locality'}).get_text().strip())
                print(item.find("div", {'class':'years-in-business'}).get_text().strip())
#               fclean.write(post_url)
#               fclean.write(name)
#               fclean.write(phone)
#               fclean.write(street_Address)
#               fclean.write(locality)
#               fclean.write(business_years)
                search_results.append([post_url, name, phone, street_Address, locality, business_years])
            except: 
                    #raise e 
                    #b=0
                    print("Failed to Add New Data")
        page = page+1
        
    columns = ('Store URL', 'Name', 'Phone', 'Street_Address','Locality','Business_years')
    df = pd.DataFrame(search_results, columns=columns)
    
    timestamp = datetime.datetime.now().strftime('%m_%d_%y %H%M%S')
    df.to_csv(f'Yellowpages Results ({timestamp}).csv', index=False)
    
    return df

if __name__ == '__main__':
    yellowpages_base_url = "https://www.yellowpages.com/search?search_terms=Furniture&geo_location_terms="
    location = 'pittsburgh'
    data = get_yellowpages_search_results(yellowpages_base_url, location)
    print(data)





