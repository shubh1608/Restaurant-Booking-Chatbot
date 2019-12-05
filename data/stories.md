## -,L,C,P
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_price
* restaurant_search{"price": "low"}
    - slot{"price": "low"}
    - action_search_restaurants
    - slot{"location": "delhi"}
* affirm
    - utter_goodbye
	
## -,L,C,P
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "Mumbai"}
    - slot{"location": "Mumbai"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Mexican"}
    - slot{"cuisine": "chinese"}
    - utter_ask_price
* restaurant_search{"price": "high"}
    - slot{"price": "high"}
    - action_search_restaurants
    - slot{"location": "Mumbai"}
* affirm
    - utter_goodbye
	
## -,L,C,P
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "Kochi"}
    - slot{"location": "Kochi"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "American"}
    - slot{"cuisine": "American"}
    - utter_ask_price
* restaurant_search{"price": "medium"}
    - slot{"price": "medium"}
    - action_search_restaurants
    - slot{"location": "Kochi"}
* affirm
    - utter_goodbye

## L,C,P
* greet
    - utter_greet
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_price
* restaurant_search{"price": "low"}
    - slot{"price": "low"}
    - action_search_restaurants
    - slot{"location": "delhi"}
* affirm
    - utter_goodbye
	
## L,C,P
* greet
    - utter_greet
* restaurant_search{"location": "Kochi"}
    - slot{"location": "Kochi"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_price
* restaurant_search{"price": "low"}
    - slot{"price": "low"}
    - action_search_restaurants
    - slot{"location": "Kochi"}
* affirm
    - utter_goodbye

## L,C,P
* greet
    - utter_greet
* restaurant_search{"location": "Bangalore"}
    - slot{"location": "Bangalore"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "South Indian"}
    - slot{"cuisine": "South Indian"}
    - utter_ask_price
* restaurant_search{"price": "low"}
    - slot{"price": "low"}
    - action_search_restaurants
    - slot{"location": "Bangalore"}
* affirm
    - utter_goodbye

## C,L,P
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
	- utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - utter_ask_price
* restaurant_search{"price": "low"}
    - slot{"price": "low"}
    - action_search_restaurants
    - slot{"location": "delhi"}
* affirm
    - utter_goodbye
	
## C,L,P
* greet
    - utter_greet
* restaurant_search{"cuisine": "North Indian"}
    - slot{"cuisine": "North Indian"}
	- utter_ask_location
* restaurant_search{"location": "New Delhi"}
    - slot{"location": "New Delhi"}
    - utter_ask_price
* restaurant_search{"price": "low"}
    - slot{"price": "low"}
    - action_search_restaurants
    - slot{"location": "New Delhi"}
* affirm
    - utter_goodbye
	
## C,L,P
* greet
    - utter_greet
* restaurant_search{"cuisine": "mexican"}
    - slot{"cuisine": "mexican"}
	- utter_ask_location
* restaurant_search{"location": "Hyderabad"}
    - slot{"location": "Hyderabad"}
    - utter_ask_price
* restaurant_search{"price": "medium"}
    - slot{"price": "medium"}
    - action_search_restaurants
    - slot{"location": "Hyderabad"}
* affirm
    - utter_goodbye


## interactive_story_1
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "Mumbai"}
    - slot{"location": "Mumbai"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Italian"}
    - slot{"cuisine": "Italian"}
    - utter_ask_price
* restaurant_search{"price": "medium"}
    - slot{"price": "medium"}
    - action_search_restaurants
    - slot{"location": "Mumbai"}
* affirm
    - utter_goodbye
