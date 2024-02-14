from bs4 import BeautifulSoup
import requests

# VARIABLES FOR HOW MANY SITES ARE WORKING
count_of_working_sites = 0
count_of_potentially_broken_sites = 0 

# SITE 1 - "SHELTERDATABASE" APP CHECK

try: 
    shelterdatabase_page_to_scrape = requests.get("https://secure-nextjs-homeless-shelter-database.vercel.app/")
    soup = BeautifulSoup(shelterdatabase_page_to_scrape.content, 'html.parser')
    shelterdatabase_first_touch_points = soup.findAll("h1", attrs={"class": "white-font"})
    shelterdatabase_second_touch_points = soup.findAll("strong")

    # Check if both lists are non-empty before proceeding
    if shelterdatabase_first_touch_points and shelterdatabase_second_touch_points:
        for shelterdatabase_first_touch_point, shelterdatabase_second_touch_point in zip(shelterdatabase_first_touch_points, shelterdatabase_second_touch_points):
            print(shelterdatabase_first_touch_point.text)
            print(shelterdatabase_second_touch_point.text)
        shelterdatabase_status = 'True'
    else:
        print("No shelterdatabase_first_touch_points or shelterdatabase_second_touch_points found.")
        shelterdatabase_status = 'False'

    if shelterdatabase_status == 'True':
        print('shelterdatabase is up and running and specified touch points were found')
        count_of_working_sites += 1
    else: 
        print('The request went through suggesting the URL was valid, but the touch points you set may have changed')
        count_of_potentially_broken_sites += 1

except requests.exceptions.RequestException as e:
    print("Error making request to shelterdatabase. Maybe there was a typo?") 
    # print(e)
    count_of_potentially_broken_sites += 1






# PRINTING VARIABLES FOR HOW MANY SITES ARE WORKING
print('count_of_working_sites:', count_of_working_sites)
print('count_of_potentially_broken_sites:', count_of_potentially_broken_sites)