import scrapy

#https://www.kayak.com/hotels/Karachi,Pakistan/2018-11-09/2018-11-11/4adults/2children/3rooms
#https://www.kayak.com/hotels/Lahore,Pakistan/2018-11-09/2018-11-11/4adults/2children/3rooms
# main_domain+category+"/"+city+","+country+"/"+check_in+"/"+check_out+"/"+adults+children+rooms
class BookSpider(scrapy.Spider):
	name='bookspider'
	main_domain="https://www.kayak.com/"
	category="hotels"
	city="karachi"
	country="Pakistan"
	check_in="2018-11-10"
	check_out="2018-11-17"
	adults="4adults/"
	children="2children/"
	rooms="3rooms/"
	start_url=main_domain+category+"/"+city+","+country+"/"+check_in+"/"+check_out+"/"+adults+children+rooms