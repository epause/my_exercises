#o kairos gia tis poleis

import urllib2
import sys
from argparse
import minidom
import ArgumentParser

def getWeather(city):

    url = "http://www.google.com/ig/api?weather=" + urllib2.quote(city)#create google weather api url
    try:      
        f = urllib2.urlopen(url)# open google weather api url
    except:        
        return "Error opening url"# if there was an error opening the url, return

def main():
	while True:
        city = raw_input("Give me a city: ")
        weather = getWeather(city)
        print(weather)
	

if __name__ == "__main__":
	main()
	
	arguments = ArgumentParser(prog="weather")
	arguments.add_argument("--unit", choices="CF", dest="unit", default="C", help="Which unit to display the temperatures in")
	arguments.add_argument("location", nargs="+")
	args = arguments.parse_args(sys.argv[1:])

	
	for location in args.location:
		url = API_URL + urlencode({"weather": location})
		xml = urlopen(url).read()
		doc = minidom.parseString(xml)

		forecast_information = doc.documentElement.getElementsByTagName("forecast_information")[0]
		city = forecast_information.getElementsByTagName("city")[0].getAttribute("data")
		current_conditions = doc.documentElement.getElementsByTagName("current_conditions")[0]
	
		city = forecast_information.getElementsByTagName("city")[0].getAttribute("data")
		country = current_conditions.getElementsByTagName("country")[0].getAttribute("data")
		count = current_conditions.getElementsByTagName("count")[0].getAttribute("data")
		location = current_conditions.getElementsByTagName("location")[0].getAttribute("data")
		wind_condition = current_conditions.getElementsByTagName("wind_condition")[0].getAttribute("data")
		
		indent = "  "
		print("Weather for {0}:".format(city))
		print(indent + country)
		print(indent + count)
		print(indent + location)
		print(indent + wind_condition)
