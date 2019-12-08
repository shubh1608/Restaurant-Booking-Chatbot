## Complete Happy path: _, L, VT, C, P, EY
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "Goa"}
    - slot{"location": "Goa"}
    - action_validate_city
    - slot{"location": "goa"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Mexican"}
    - slot{"cuisine": "Mexican"}
    - utter_ask_price
* restaurant_search{"price": "medium"}
    - slot{"price": "medium"}
    - action_search_restaurants
    - slot{"results": "1. Toy Beach Club in Candolim Beach Road, Candolim, Goa has been rated 4.9.\n2. Purple Martini in Anjuna Beach, Anjuna, Goa has been rated 4.9.\n3. The Fisherman's Wharf in Behind The Leela, Mobor, Cavelossim, Goa has been rated 4.6.\n4. Thalassa in Plot 301, 1, Near Teso Waterfront, Vaddy, Siolim, Goa has been rated 4.4.\n5. Britto's Bar & Restaurant in Baga Calangute, Bardez, Baga, Goa has been rated 4.3.\n"}
    - utter_suggest_email
* affirm
    - utter_ask_email
* restaurant_search{"email": "swayam@yahoo.com"}
    - slot{"email": "swayam@yahoo.com"}
    - action_send_mail
    - slot{"email": "swayam@yahoo.com"}
* affirm
    - utter_goodbye
	
## _, L, VT, C, P, EN
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "Goa"}
    - slot{"location": "Goa"}
    - action_validate_city
    - slot{"location": "goa"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Mexican"}
    - slot{"cuisine": "Mexican"}
    - utter_ask_price
* restaurant_search{"price": "medium"}
    - slot{"price": "medium"}
    - action_search_restaurants
    - slot{"results": "1. Toy Beach Club in Candolim Beach Road, Candolim, Goa has been rated 4.9.\n2. Purple Martini in Anjuna Beach, Anjuna, Goa has been rated 4.9.\n3. The Fisherman's Wharf in Behind The Leela, Mobor, Cavelossim, Goa has been rated 4.6.\n4. Thalassa in Plot 301, 1, Near Teso Waterfront, Vaddy, Siolim, Goa has been rated 4.4.\n5. Britto's Bar & Restaurant in Baga Calangute, Bardez, Baga, Goa has been rated 4.3.\n"}
    - utter_suggest_email
* restaurant_search
    - utter_goodbye

## _, L, VF, C, P, EY 
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "Bhilai"}
    - slot{"location": "Bhilai"}
    - action_validate_city
    - slot{"location": null}
* restaurant_search{"location": "Kolkata"}
    - slot{"location": "Kolkata"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Italian"}
    - slot{"cuisine": "Italian"}
    - utter_ask_price
* restaurant_search{"price": "medium"}
    - slot{"price": "medium"}
    - action_search_restaurants
    - slot{"results": "1. Urban Masala in 882, Lake Town Road, Near Jaya Cinema, Lake Town, Kolkata has been rated 4.8.\n2. Roastery Coffee House in 70 B, Calcutta South India Club, Gariahat, Kolkata has been rated 4.6.\n3. Eagle Boys Pizza in 24, Sarada Pally, Block D, Near Tagore Park, Ruby Hospital Area, Kolkata has been rated 4.5.\n4. ITC Royal Bengal- Grand Market Pavilion in ITC Sonar, JBS Haldane Avenue, EM Bypass, Science City Area, Kolkata has been rated 4.5.\n5. Nawwarah Fine Dine & Lounge in 48A, Syed Amir Ali Avenue, Ballygunge, Kolkata has been rated 4.5.\n"}
    - utter_suggest_email
* affirm
    - utter_ask_email
* restaurant_search{"email": "shubh@gmail.com"}
    - slot{"email": "shubh@gmail.com"}
    - action_send_mail
    - slot{"email": "shubh@gmail.com"}
* affirm
    - utter_goodbye
	
## _, L, VF, C, P, EN
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "Raigarh"}
    - slot{"location": "Raigarh"}
    - action_validate_city
    - slot{"location": null}
* restaurant_search{"location": "Bhilai"}
    - slot{"location": "Bhilai"}
    - action_validate_city
    - slot{"location": "bhilai"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "North Indian"}
    - slot{"cuisine": "North Indian"}
    - utter_ask_price
* restaurant_search{"price": "medium"}
    - slot{"price": "medium"}
    - action_search_restaurants
    - slot{"results": "1. KFC in Ground Floor, Surya Treasure Island Mall, Junwani Road, Smriti Nagar, Nehru Nagar, Bhilai has been rated 4.9.\n2. Hari Raj Fine Dine in 1, Main Road Civic Centre, Near Mini Market, Bhilai Nagar Township, Durg Bhilai has been rated 4.6.\n3. The 90s Cafe in Behind Wakodkar Nursing Home, KPS Road, Nehru Nagar, Durg Bhilai has been rated 4.4.\n4. Al Lazeez Biryani in 34/1 Dakshin Gangotri, G E Road, Near Indus Land Bank, Supela, Bhilai has been rated 4.1.\n5. Grill Inn in Shop no. 38, Civic Center, Bhilai Nagar Township, Durg Bhilai has been rated 4.1.\n"}
    - utter_suggest_email
* restaurant_search
    - utter_goodbye
	
##_, C, L, VT, P, EY
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
	- utter_ask_location
* restaurant_search{"location": "goa"}
    - slot{"location": "delhi"}
    - action_validate_city
    - slot{"location": "goa"}
    - utter_ask_price
* restaurant_search{"price": "medium"}
    - slot{"price": "medium"}
    - action_search_restaurants
    - slot{"results": "1. Toy Beach Club in Candolim Beach Road, Candolim, Goa has been rated 4.9.\n2. Purple Martini in Anjuna Beach, Anjuna, Goa has been rated 4.9.\n3. The Fisherman's Wharf in Behind The Leela, Mobor, Cavelossim, Goa has been rated 4.6.\n4. Thalassa in Plot 301, 1, Near Teso Waterfront, Vaddy, Siolim, Goa has been rated 4.4.\n5. Britto's Bar & Restaurant in Baga Calangute, Bardez, Baga, Goa has been rated 4.3.\n"}
    - utter_suggest_email
* affirm
    - utter_ask_email
* restaurant_search{"email": "swayam@yahoo.com"}
    - slot{"email": "swayam@yahoo.com"}
    - action_send_mail
    - slot{"email": "swayam@yahoo.com"}
* affirm
    - utter_goodbye
	
##_, C, L, VT, P, EN
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
	- utter_ask_location
* restaurant_search{"location": "goa"}
    - slot{"location": "delhi"}
    - action_validate_city
    - slot{"location": "goa"}
    - utter_ask_price
* restaurant_search{"price": "medium"}
    - slot{"price": "medium"}
    - action_search_restaurants
    - slot{"results": "1. Toy Beach Club in Candolim Beach Road, Candolim, Goa has been rated 4.9.\n2. Purple Martini in Anjuna Beach, Anjuna, Goa has been rated 4.9.\n3. The Fisherman's Wharf in Behind The Leela, Mobor, Cavelossim, Goa has been rated 4.6.\n4. Thalassa in Plot 301, 1, Near Teso Waterfront, Vaddy, Siolim, Goa has been rated 4.4.\n5. Britto's Bar & Restaurant in Baga Calangute, Bardez, Baga, Goa has been rated 4.3.\n"}
    - utter_suggest_email
* restaurant_search
    - utter_goodbye

##_, C, L, VF, P, EY
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
	- utter_ask_location
* restaurant_search{"location": "Raigarh"}
    - slot{"location": "Raigarh"}
    - action_validate_city
    - slot{"location": null}
* restaurant_search{"location": "goa"}
    - slot{"location": "delhi"}
    - action_validate_city
    - slot{"location": "goa"}
    - utter_ask_price
* restaurant_search{"price": "medium"}
    - slot{"price": "medium"}
    - action_search_restaurants
    - slot{"results": "1. Toy Beach Club in Candolim Beach Road, Candolim, Goa has been rated 4.9.\n2. Purple Martini in Anjuna Beach, Anjuna, Goa has been rated 4.9.\n3. The Fisherman's Wharf in Behind The Leela, Mobor, Cavelossim, Goa has been rated 4.6.\n4. Thalassa in Plot 301, 1, Near Teso Waterfront, Vaddy, Siolim, Goa has been rated 4.4.\n5. Britto's Bar & Restaurant in Baga Calangute, Bardez, Baga, Goa has been rated 4.3.\n"}
    - utter_suggest_email
* affirm
    - utter_ask_email
* restaurant_search{"email": "swayam@yahoo.com"}
    - slot{"email": "swayam@yahoo.com"}
    - action_send_mail
    - slot{"email": "swayam@yahoo.com"}
* affirm
    - utter_goodbye
	
##_, C, L, VF, P, EN
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
	- utter_ask_location
* restaurant_search{"location": "Durg"}
    - slot{"location": "Durg"}
    - action_validate_city
    - slot{"location": null}
* restaurant_search{"location": "goa"}
    - slot{"location": "delhi"}
    - action_validate_city
    - slot{"location": "goa"}
    - utter_ask_price
* restaurant_search{"price": "medium"}
    - slot{"price": "medium"}
    - action_search_restaurants
    - slot{"results": "1. Toy Beach Club in Candolim Beach Road, Candolim, Goa has been rated 4.9.\n2. Purple Martini in Anjuna Beach, Anjuna, Goa has been rated 4.9.\n3. The Fisherman's Wharf in Behind The Leela, Mobor, Cavelossim, Goa has been rated 4.6.\n4. Thalassa in Plot 301, 1, Near Teso Waterfront, Vaddy, Siolim, Goa has been rated 4.4.\n5. Britto's Bar & Restaurant in Baga Calangute, Bardez, Baga, Goa has been rated 4.3.\n"}
    - utter_suggest_email
* restaurant_search
    - utter_goodbye

## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"cuisine": "italian"}
    - slot{"cuisine": "italian"}
    - utter_ask_location
* restaurant_search{"location": "Bhilai"}
    - slot{"location": "Bhilai"}
    - action_validate_city
    - slot{"location": "bhilai"}
    - utter_ask_price
* restaurant_search{"price": "medium"}
    - slot{"price": "medium"}
    - action_search_restaurants
    - slot{"results": "1. The 90s Cafe in Behind Wakodkar Nursing Home, KPS Road, Nehru Nagar, Durg Bhilai has been rated 4.4.\n2. Tripti Restaurant in Gourav Path Road, Behind LIC Building, Near Patel Complex, Durg, Durg Bhilai has been rated 4.4.\n3. Grill Inn in Shop no. 38, Civic Center, Bhilai Nagar Township, Durg Bhilai has been rated 4.1.\n4. Max Bakers in Opposite Wakodakar Nursing Home, KPS Road, Nehru Nagar, Durg Bhilai has been rated 3.8.\n5. The Super Bowl in C-159, Market Area, Junwani Road, Smriti Nagar, Durg, Nehru Nagar, Durg Bhilai has been rated 3.7.\n"}
    - utter_suggest_email
* affirm
    - utter_ask_email
* restaurant_search{"email": "spatel@xyz.com"}
    - slot{"email": "spatel@xyz.com"}
    - action_send_mail
    - slot{"email": "spatel@xyz.com"}
* affirm
    - utter_goodbye

## LC, VT, P, EY
* greet
    - utter_greet
* restaurant_search{"cuisine": "mexican", "location": "Pune"}
    - slot{"cuisine": "mexican"}
    - slot{"location": "Pune"}
    - action_validate_city
    - slot{"location": "pune"}
    - utter_ask_price
*restaurant_search{"price": "medium"}
    - slot{"price": "medium"}
    - action_search_restaurants
    - slot{"results": "1. Toy Beach Club in Candolim Beach Road, Candolim, Goa has been rated 4.9.\n2. Purple Martini in Anjuna Beach, Anjuna, Goa has been rated 4.9.\n3. The Fisherman's Wharf in Behind The Leela, Mobor, Cavelossim, Goa has been rated 4.6.\n4. Thalassa in Plot 301, 1, Near Teso Waterfront, Vaddy, Siolim, Goa has been rated 4.4.\n5. Britto's Bar & Restaurant in Baga Calangute, Bardez, Baga, Goa has been rated 4.3.\n"}
    - utter_suggest_email
* affirm
    - utter_ask_email
* restaurant_search{"email": "swayam@yahoo.com"}
    - slot{"email": "swayam@yahoo.com"}
    - action_send_mail
    - slot{"email": "swayam@yahoo.com"}
* affirm
    - utter_goodbye
	
## LC, VT, P, EN
* greet
    - utter_greet
* restaurant_search{"cuisine": "mexican", "location": "Pune"}
    - slot{"cuisine": "mexican"}
    - slot{"location": "Pune"}
    - action_validate_city
    - slot{"location": "pune"}
    - utter_ask_price
*restaurant_search{"price": "medium"}
    - slot{"price": "medium"}
    - action_search_restaurants
    - slot{"results": "1. Toy Beach Club in Candolim Beach Road, Candolim, Goa has been rated 4.9.\n2. Purple Martini in Anjuna Beach, Anjuna, Goa has been rated 4.9.\n3. The Fisherman's Wharf in Behind The Leela, Mobor, Cavelossim, Goa has been rated 4.6.\n4. Thalassa in Plot 301, 1, Near Teso Waterfront, Vaddy, Siolim, Goa has been rated 4.4.\n5. Britto's Bar & Restaurant in Baga Calangute, Bardez, Baga, Goa has been rated 4.3.\n"}
    - utter_suggest_email
* restaurant_search
    - utter_goodbye
	
## LC, VF, P, EY
* greet
    - utter_greet
* restaurant_search{"cuisine": "mexican", "location": "Raigarh"}
    - slot{"cuisine": "mexican"}
    - slot{"location": "Raigarh"}
    - action_validate_city
    - slot{"location": "null"}
*restaurant_search{"location": "Bhilai"}
	- slot{"location": "Bhilai"}
	- utter_ask_price
*restaurant_search{"price": "medium"}
    - slot{"price": "medium"}
    - action_search_restaurants
    - slot{"results": "1. Toy Beach Club in Candolim Beach Road, Candolim, Goa has been rated 4.9.\n2. Purple Martini in Anjuna Beach, Anjuna, Goa has been rated 4.9.\n3. The Fisherman's Wharf in Behind The Leela, Mobor, Cavelossim, Goa has been rated 4.6.\n4. Thalassa in Plot 301, 1, Near Teso Waterfront, Vaddy, Siolim, Goa has been rated 4.4.\n5. Britto's Bar & Restaurant in Baga Calangute, Bardez, Baga, Goa has been rated 4.3.\n"}
    - utter_suggest_email
* affirm
    - utter_ask_email
* restaurant_search{"email": "swayam@yahoo.com"}
    - slot{"email": "swayam@yahoo.com"}
    - action_send_mail
    - slot{"email": "swayam@yahoo.com"}
* affirm
    - utter_goodbye
	
## LC, VF, P, EN
* greet
    - utter_greet
* restaurant_search{"cuisine": "mexican", "location": "Raigarh"}
    - slot{"cuisine": "mexican"}
    - slot{"location": "Raigarh"}
    - action_validate_city
    - slot{"location": "null"}
*restaurant_search{"location": "Bhilai"}
	- slot{"location": "Bhilai"}
	- utter_ask_price
*restaurant_search{"price": "medium"}
    - slot{"price": "medium"}
    - action_search_restaurants
    - slot{"results": "1. Toy Beach Club in Candolim Beach Road, Candolim, Goa has been rated 4.9.\n2. Purple Martini in Anjuna Beach, Anjuna, Goa has been rated 4.9.\n3. The Fisherman's Wharf in Behind The Leela, Mobor, Cavelossim, Goa has been rated 4.6.\n4. Thalassa in Plot 301, 1, Near Teso Waterfront, Vaddy, Siolim, Goa has been rated 4.4.\n5. Britto's Bar & Restaurant in Baga Calangute, Bardez, Baga, Goa has been rated 4.3.\n"}
    - utter_suggest_email
* restaurant_search
    - utter_goodbye

## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "location": "Pune"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "Pune"}
    - action_validate_city
    - slot{"location": "pune"}
    - utter_ask_price
* restaurant_search{"price": "high"}
    - slot{"price": "high"}
    - action_search_restaurants
    - slot{"results": "1. Asia Kitchen By Mainland China in City Point, Ground Floor, Dhole Patil Road, Pune has been rated 4.6.\n2. Shizusan in Upper Ground Floor, Phoenix Market City, Viman Nagar, Pune has been rated 4.5.\n3. Mainland China in 403/2, Ground Floor, BIG ICC Road, Senapati Bapat Road, Pune has been rated 4.4.\n4. Kimchi in Sambhaji Nagar, Opposite Hyundai Showroom, Beside HP Petrol Pump, Kharadi, Pune has been rated 4.3.\n5. Chang's in King Sport Home 7, Datta Mandir Chowk, Viman Nagar, Pune has been rated 4.1.\n"}
    - utter_suggest_email
* affirm
    - utter_ask_email
* restaurant_search{"email": "shubh@gmail.com"}
    - slot{"email": "shubh@gmail.com"}
    - action_send_mail
    - slot{"email": "shubh@gmail.com"}
* affirm
    - utter_goodbye
