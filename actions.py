from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

from rasa_sdk import Action
from rasa_sdk.events import SlotSet
import zomatopy
import json

class ActionSearchRestaurants(Action):
	def name(self):
		return 'action_search_restaurants'
		
	
	def run(self, dispatcher, tracker, domain):
		
		def create_response(restaurants):
			response=""
			if d['results_found'] == 0:
				response= "no results"
			else:
				srnum=0
				for restaurant in restaurants:
					srnum=srnum+1
					response=response+str(srnum)+". "+restaurant[0]+ " in "+ restaurant[1]+" has been rated "+str(restaurant[3])+"."+"\n"
			return response

		def filter_restaurants_by_price(d, price_limit):
			result = []
			for restaurant in d['restaurants']:
				if price_limit != -1 and restaurant['restaurant']['average_cost_for_two'] <= price_limit:
					result.append(restaurant_tuple(restaurant))
				else:
					result.append(restaurant_tuple(restaurant))
			result = sorted(result,reverse=True, key=lambda x:x[3])
			result = result[:5]
			return result

		def restaurant_tuple(restaurant):
			tup = (
						restaurant['restaurant']['name'],
						restaurant['restaurant']['location']['address'],
						restaurant['restaurant']['average_cost_for_two'],
						restaurant['restaurant']['user_rating']['aggregate_rating']
					)
			return tup
		
		config={ "user_key":"e09b845afff853b9646348fb80920eaf"}
		zomato = zomatopy.initialize_app(config)
		
		loc = tracker.get_slot('location')
		location_detail=zomato.get_location(loc, 1)
		d1 = json.loads(location_detail)
		lat=d1["location_suggestions"][0]["latitude"]
		lon=d1["location_suggestions"][0]["longitude"]
		
		cuisine = tracker.get_slot('cuisine')
		cuisines_dict={'bakery':5,'chinese':25,'cafe':30,'italian':55,'biryani':7,'north indian':50,'south indian':85,'american':1,'mexican':3}
		
		results=zomato.restaurant_search("", lat, lon, str(cuisines_dict.get(cuisine)), 5)
		d = json.loads(results)
		
		response=""
		if d['results_found'] == 0:
			response= "no results"
		else:
			price_dict = {'low': 300, 'medium': 700, 'high': -1} #-1 is for no limit in price
			price_limit = price_dict.get(tracker.get_slot('price'))
			restaurants = filter_restaurants_by_price(d, price_limit)
			response = create_response(restaurants)
		
		dispatcher.utter_message("-----"+response)
		
		return [SlotSet('location',loc)]
		
		

class ActionSendEmail(Action):
	def name(self):
		return 'action_send_mail'
	
	def run(self, dispatcher, tracker, domain):
		
		port = 465  # For SSL
		smtp_server = "smtp.gmail.com"
		sender_email = "testMail@gmail.com"  # Enter your address
		receiver_email = tracker.get_slot('email')
		password = 'testPassword'
		message = MIMEMultipart("alternative")
		message["Subject"] = "Restaurant Search Details For You!!!"
		message["From"] = sender_email
		message["To"] = receiver_email
		text = tracker.get_slot('results')
		
		message.attach(MIMEText(text, "plain"))
		
		context = ssl.create_default_context()
		with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
			server.login(sender_email, password)
			server.sendmail(sender_email, receiver_email, message.as_string())

		dispatcher.utter_message("Email Sent.\n Please check.")
		return [SlotSet('email',receiver_email)]		


class ActionValidateCity(Action):
	def name(self):
		return 'action_validate_city'
	
	def run(self, dispatcher, tracker, domain):
		list_of_cities = ['bangalore', 'chennai', 'delhi', 'hyderabad', 'kolkata', 'mumbai', 'ahmedabad', 'pune', 'kochi','agra', 'ajmer', 'aligarh', 'amravati', 'amritsar', 'asansol', 
						  'aurangabad', 'bareilly', 'belgaum', 'bhavnagar', 'bhiwandi', 'bhopal', 'bhubaneswar', 'bikaner', 'bilaspur', 'bokaro steel city', 'chandigarh', 'coimbatore nagpur', 
						  'cuttack', 'dehradun', 'dhanbad', 'bhilai', 'durgapur', 'erode', 'faridabad', 'firozabad', 'ghaziabad', 'gorakhpur', 
						  'gulbarga', 'guntur', 'gwalior', 'gurgaon', 'guwahati', 'hamirpur', 'hubli–dharwad', 
						  'indore', 'jabalpur', 'jaipur', 'jalandhar', 'jammu', 'jamnagar', 'jamshedpur', 'jhansi', 'jodhpur', 'kakinada', 
						  'kannur', 'kanpur', 'kottayam', 'kolhapur', 'kollam', 'kozhikode', 'kurnool', 'ludhiana', 'lucknow', 'madurai', 'malappuram', 
						  'mathura', 'goa', 'mangalore', 'meerut', 'moradabad', 'mysore', 'nanded', 'nashik', 'nellore', 'noida', 'palakkad', 'patna', 
						  'perinthalmanna', 'pondicherry', 'purulia prayagraj', 'raipur', 'rajkot', 'rajahmundry', 'ranchi', 'rourkela', 'salem', 
						  'sangli', 'shimla', 'siliguri', 'solapur', 'srinagar', 'thiruvananthapuram', 'thrissur', 'tiruchirappalli', 'tirur', 
						  'tirupati', 'tirunelveli', 'tiruppur', 'tiruvannamalai', 'ujjain', 'bijapur', 'vadodara', 'varanasi', 'vasai-virar city', 
						  'vijayawada', 'vellore', 'warangal', 'surat' ,'visakhapatnam'] 
		if tracker.get_slot('location') not in list_of_cities:
		 dispatcher.utter_message("We don't operate in that city yet. Sorry.")
		
		return [SlotSet('location',None)]

	
