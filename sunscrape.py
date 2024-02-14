from bs4 import BeautifulSoup
import requests

try: 
    page_to_scrape = requests.get("https://secure-nextjs-homeless-shelter-database.vesrcel.app/")
    soup = BeautifulSoup(page_to_scrape.content, 'html.parser')
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
        print('shelterdatabase is up and running')
    else: 
        print('shelterdatabase may be down or the touch points you set may have changed')

except requests.exceptions.RequestException as e:
    print("Error making request:", e)