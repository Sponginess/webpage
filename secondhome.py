import urllib
import webapp2
import jinja2
import os
import datetime
import cgi
import re

from google.appengine.ext import ndb

jinja_environment = jinja2.Environment(loader=jinja2.FileSystemLoader(os.path.dirname(__file__) + "/templates"))


class MainPage(webapp2.RequestHandler):
    """ Handler for the front page."""

    def get(self):
		template = jinja_environment.get_template('index.html')
		self.response.out.write(template.render())
		

class Study(webapp2.RequestHandler):
    """ Handler for the study page."""

    def get(self):
        template = jinja_environment.get_template('study.html')
        self.response.out.write(template.render())
class StudyChoose(webapp2.RequestHandler):
		
	def get(self):
		study_choice = self.request.get('study-select')
		
		chairs = self.request.get('wantsChairs')
		sofas = self.request.get('wantsSofas')
		tables = self.request.get('wantsTables')
		sockets = self.request.get('wantsSockets')
		aircon = self.request.get('wantsAircon')
		
		template = jinja_environment.get_template('study-choice.html')
		if study_choice!="everywhere":
			study_query = StudyLocation.query(StudyLocation.faculty==study_choice).order(StudyLocation.area)
		else:
			study_query = StudyLocation.query().order(StudyLocation.area)
		
		
		study_locations = study_query.fetch()
		
		#filtering process
		if chairs=="on":
			study_locations = [locations for locations in study_locations if locations.chairs=="on"]
		if sofas=="on":
			study_locations = [locations for locations in study_locations if locations.sofas=="on"]
		if tables=="on":
			study_locations = [locations for locations in study_locations if locations.tables=="on"]
		if sockets=="on":
			study_locations = [locations for locations in study_locations if locations.sockets=="on"]
		if aircon=="on":
			study_locations = [locations for locations in study_locations if locations.aircon=="on"]
		
		template_values = {
			'locations': study_locations,
			'faculty_name': study_choice.upper(),
			'chairs': chairs,
			'sofas': sofas,
			'tables': tables,
			'sockets': sockets,
			'aircon': aircon
		}
		self.response.write(template.render(template_values))

class StudySort(webapp2.RequestHandler):
	"""Handler for the sorting function"""
	def get(self):
		sort_choice = self.request.get('study-sort')
		order_choice = self.request.get('order-study')
		
		study_choice = self.request.get('study-select')
		chairs = self.request.get('wantsChairs')
		sofas = self.request.get('wantsSofas')
		tables = self.request.get('wantsTables')
		sockets = self.request.get('wantsSockets')
		aircon = self.request.get('wantsAircon')
		template = jinja_environment.get_template('study-choice.html')
		if study_choice!="everywhere":
			study_query = StudyLocation.query(StudyLocation.faculty==study_choice)
		else:
			study_query = StudyLocation.query()
			
		#Sorting process
		if order_choice=="descending order":
			if sort_choice=="rating":
				study_query = study_query.order(-StudyLocation.rating)
			elif sort_choice=="total number of amenities":			
				study_query = study_query.order(-StudyLocation.total)
			else:
				study_query = study_query.order(-StudyLocation.area)
		else:
			if sort_choice=="rating":
				study_query = study_query.order(StudyLocation.rating)
			elif sort_choice=="total number of amenities":			
				study_query = study_query.order(StudyLocation.total)
			else:
				study_query = study_query.order(StudyLocation.area)
		
		study_locations = study_query.fetch()
		
		#filtering process
		if chairs=="on":
			study_locations = [locations for locations in study_locations if locations.chairs=="on"]
		if sofas=="on":
			study_locations = [locations for locations in study_locations if locations.sofas=="on"]
		if tables=="on":
			study_locations = [locations for locations in study_locations if locations.tables=="on"]
		if sockets=="on":
			study_locations = [locations for locations in study_locations if locations.sockets=="on"]
		if aircon=="on":
			study_locations = [locations for locations in study_locations if locations.aircon=="on"]
		
		template_values = {
			'locations': study_locations,
			'faculty_name': study_choice.upper(),
			'chairs': chairs,
			'sofas': sofas,
			'tables': tables,
			'sockets': sockets,
			'aircon': aircon
		}
		self.response.write(template.render(template_values))
				
		
class Shop(webapp2.RequestHandler):
    """ Handler for the shop page."""

    def get(self):
        template = jinja_environment.get_template('shop.html')
        self.response.out.write(template.render())
class ShopChoose(webapp2.RequestHandler):
		
	def get(self):
		shop_choice = self.request.get('shop-select')
		bazaars = self.request.get('wantsBazaars')
		food = self.request.get('wantsFood')
		books = self.request.get('wantsBooks')
		if bazaars=="" and food=="" and books=="":
			bazaars="on"
			food="on"
			books="on"
		template = jinja_environment.get_template('shop-choice.html')
		if shop_choice!="everywhere":
			shop_query = ShopLocation.query(ShopLocation.faculty==shop_choice).order(ShopLocation.shopName)
		else:
			shop_query = ShopLocation.query().order(ShopLocation.buildingfloor)
		shop_locations = shop_query.fetch()
		filtered_locations = []
		temp = []
		
		#filtering process
		if bazaars=="on" or food=="on" or books=="on":
			if bazaars=="on":
				temp = [locations for locations in shop_locations if locations.shopType.lower()=="bazaar"]
				if len(temp) > 0:
					filtered_locations.extend(temp)
			if food=="on":
				temp = [locations for locations in shop_locations if locations.shopType.lower()=="food outlet"]
				if len(temp) > 0:
					filtered_locations.extend(temp)
			if books=="on":
				temp = [locations for locations in shop_locations if locations.shopType.lower()=="bookshop"]
				if len(temp) > 0:
					filtered_locations.extend(temp)
		
		template_values = {
			'locations': filtered_locations,
			'faculty_name': shop_choice.upper(),
			'bazaars': bazaars,
			'food': food,
			'books': books
		}
		self.response.write(template.render(template_values))

class ShopSort(webapp2.RequestHandler):
	"""Handler for the sorting function"""
	def get(self):
		canSort = self.request.get('canSort')
		result = []
		
		sort_choice = self.request.get('shop-sort')
		order_choice = self.request.get('order-shop')
		shop_choice = self.request.get('shop-select')
		bazaars = self.request.get('wantsBazaars')
		food = self.request.get('wantsFood')
		books = self.request.get('wantsBooks')
		template = jinja_environment.get_template('shop-choice.html')
		if canSort=="on":
			if bazaars=="" and food=="" and books=="":
				bazaars="on"
				food="on"
				books="on"
				
			
			if shop_choice!="everywhere":
				shop_query = ShopLocation.query(ShopLocation.faculty==shop_choice)
			else:
				shop_query = ShopLocation.query()
			
			filtered_locations = []
			temp = []
			
			#Sorting process
			if order_choice=="descending order":
				if sort_choice=="date":
					shop_query = shop_query.order(-ShopLocation.dateStart)
					if bazaars=="" and food=="" and books=="":
						bazaars = "on"
						food = ""
						books = ""
					else:
						food = ""
						books = ""
				elif sort_choice=="rating":
					shop_query = shop_query.order(-ShopLocation.rating)
					if bazaars=="" and food=="" and books=="":
						bazaars = ""
						food = "on"
						books = ""
					else:
						bazaars = ""
						books = ""
				else:
					shop_query = shop_query.order(-ShopLocation.area)
			else:
				if sort_choice=="date":
					shop_query = shop_query.order(ShopLocation.dateStart)
					if bazaars=="" and food=="" and books=="":
						bazaars = "on"
						food = ""
						books = ""
					else:
						food = ""
						books = ""
				elif sort_choice=="rating":
					shop_query = shop_query.order(-ShopLocation.rating)
					if bazaars=="" and food=="" and books=="":
						bazaars = ""
						food = "on"
						books = ""
					else:
						bazaars = ""
						books = ""
				else:
					shop_query = shop_query.order(ShopLocation.area)
			shop_locations = shop_query.fetch()
		
			#filtering process
			if bazaars=="on":
				temp = [locations for locations in shop_locations if locations.shopType.lower()=="bazaar"]
				if len(temp) > 0:
					filtered_locations.extend(temp)
			if food=="on":
				temp = [locations for locations in shop_locations if locations.shopType.lower()=="food outlet"]
				if len(temp) > 0:
					filtered_locations.extend(temp)
			if books=="on":
				temp = [locations for locations in shop_locations if locations.shopType.lower()=="bookshop"]
				if len(temp) > 0:
					filtered_locations.extend(temp)
			result.extend(filtered_locations)
		template_values = {
			'locations': result,
			'faculty_name': shop_choice.upper(),
			'bazaars': bazaars,
			'food': food,
			'books': books
		}

		self.response.write(template.render(template_values))		
		
class Poop(webapp2.RequestHandler):
    """ Handler for the poop page."""

    def get(self):
        template = jinja_environment.get_template('poop.html')
        self.response.out.write(template.render())
		
class PoopChoose(webapp2.RequestHandler):
		
	def get(self):
		poop_choice = self.request.get('poop-select')
		handicapped = self.request.get('wantsHandicapped')
		template = jinja_environment.get_template('poop-choice.html')
		if poop_choice!="everywhere":
			poop_query = PoopLocation.query(PoopLocation.faculty==poop_choice).order(PoopLocation.area)
		else:
			poop_query = PoopLocation.query().order(PoopLocation.area)
		poop_locations = poop_query.fetch()
		
		#filtering process
		handicapped = self.request.get('wantsHandicapped')
		if handicapped:
			poop_locations = [locations for locations in poop_locations if locations.hasHandicapped=="on"]
			
		template_values = {
			'locations': poop_locations,
			'handicapped': handicapped,
			'faculty_name': poop_choice.upper()
		}
		self.response.write(template.render(template_values))
		
class PoopSort(webapp2.RequestHandler):
	"""Handler for the sorting function"""
	def get(self):
		sort_choice = self.request.get('poop-sort')
		order_choice = self.request.get('order-poop')
		
		handicapped = self.request.get('wantsHandicapped')
		
		poop_choice = self.request.get('poop-select')
		
		template = jinja_environment.get_template('poop-choice.html')
		if poop_choice!="everywhere":
			poop_query = PoopLocation.query(PoopLocation.faculty==poop_choice)
		else:
			poop_query = PoopLocation.query()
			
		#Sorting process
		if order_choice=="descending order":
			if sort_choice=="cleanliness":
				poop_query = poop_query.order(-PoopLocation.cleanliness)
			else:
				poop_query = poop_query.order(-PoopLocation.area)
		else:
			if sort_choice=="cleanliness":
				poop_query = poop_query.order(PoopLocation.cleanliness)
			else:
				poop_query = poop_query.order(PoopLocation.area)
		
		poop_locations = poop_query.fetch()
		
		#filtering process
		handicapped = self.request.get('wantsHandicapped')
		if handicapped:
			poop_locations = [locations for locations in poop_locations if locations.hasHandicapped=="on"]
		
		template_values = {
			'locations': poop_locations,
			'handicapped': handicapped,
			'faculty_name': poop_choice.upper()
		}
		self.response.write(template.render(template_values))
		
class Contact(webapp2.RequestHandler):
	""" Handler for the contact page."""
	
	def get(self):
		template = jinja_environment.get_template('contact.html')
		self.response.out.write(template.render())
	def post(self):
		contact = ContactForm()
		contact.name = self.request.get('name')
		contact.email = self.request.get('email')
		contact.message = self.request.get('message')
		emailAdd = contact.email
		emailArr = emailAdd.split('@')
		emailChar = list(emailAdd)
		count = 0
		for character in emailChar:
			if character == '@':
				count += 1
		if len(emailArr) != 2 or count != 1:
			self.redirect('/error')
		else:	
			contact.put()
			self.redirect('/thanks')
		
class Area(webapp2.RequestHandler):
    """ Handler for the area page."""

    def get(self):
        template = jinja_environment.get_template('area.html')
        self.response.out.write(template.render())
		
class Add(webapp2.RequestHandler):
	""" Handler for the add page."""
	def get(self):
		template = jinja_environment.get_template('add.html')
		self.response.write(template.render())

class AddStudy(webapp2.RequestHandler):
	""" Handler for the add study page."""
	def post(self):
		content = StudyLocation()
		content.faculty = self.request.get('select1')
		content.area = self.request.get('input2')
		content.buildingfloor = self.request.get('buidingfloor')
		
		content.shop = self.request.get('input3')
		content.poop = self.request.get('input4')
		
		content.numSeats = int(self.request.get('input5'))
		content.numTables = int(self.request.get('input6'))
		content.numSockets = int(self.request.get('input7'))
		
		content.chairs = self.request.get('input8')
		content.sofas = self.request.get('input9')
		content.tables = self.request.get('input10')
		content.sockets = self.request.get('input11')
		content.aircon = self.request.get('input12')
		
		content.rating = int(self.request.get('input13'))
		
		content.image1 = self.request.get('input14')
		content.image2 = self.request.get('input15')
		content.image3 = self.request.get('input16')

		content.total = content.numSeats + content.numTables + content.numSockets
		content.directions = self.request.get('directions')
		content.put();
		self.redirect('/add')

class AddShop(webapp2.RequestHandler):
	""" Handler for the add shop page."""
	def post(self):
		content = ShopLocation()
		
		content.faculty = self.request.get('select1')
		content.buildingfloor = self.request.get('buidingfloor')
		
		content.shopName = self.request.get('input3')
		
		content.study = self.request.get('input4')
		content.poop = self.request.get('input5')
		
		content.shopType = self.request.get('input6')
		content.shopDesc = self.request.get('input7')
		
		content.rating = int(self.request.get('rating'))

		content.image1 = self.request.get('input8')
		content.image2 = self.request.get('input9')
		
		dateStart = self.request.get('dateStart')
		dateEnd = self.request.get('dateEnd')
		if dateStart and dateEnd:
			content.dateStart = datetime.datetime.strptime(self.request.get('dateStart'), "%Y-%m-%d").date()
			content.dateEnd = datetime.datetime.strptime(self.request.get('dateEnd'), "%Y-%m-%d").date()
			
		content.time = self.request.get('time')
		content.directions = self.request.get('directions')
		content.put()
		
		self.redirect('/add')
		
class AddPoop(webapp2.RequestHandler):
	""" Handler for the add shop page."""
	def post(self):
		content = PoopLocation()
		content.faculty = self.request.get('select1')
		content.area = self.request.get('input2')
		content.buildingfloor = self.request.get('buidingfloor')
		
		content.study = self.request.get('input3')
		content.shop = self.request.get('input4')
		
		content.cleanlinessGents = int(self.request.get('input5'))
		
		content.cleanlinessLadies = int(self.request.get('input6'))
		
		content.ladies = self.request.get('input7')
		content.gents = self.request.get('input8')
		
		content.hasHandicapped = self.request.get('hasHandicapped')
		content.cleanlinessHandicapped = int(self.request.get('cleanlinessHandicapped'))
		
		if content.hasHandicapped=="on":
			content.cleanliness = (content.cleanlinessGents + content.cleanlinessLadies + content.cleanlinessHandicapped)/3
		else:
			content.cleanliness = (content.cleanlinessGents + content.cleanlinessLadies)/2
		
		content.directions = self.request.get('directions')
		content.put();
		self.redirect('/add')
class Information(webapp2.RequestHandler):
	""" Handler for the about page."""

	def get(self):
		template = jinja_environment.get_template('info.html')
		self.response.write(template.render())

class ShopArea(webapp2.RequestHandler):
	def get(self):
		area_input = self.request.get('shop-name')
		area_info = ShopLocation.query(ShopLocation.shopName==area_input)
		area = area_info.fetch().pop()
		template = jinja_environment.get_template('area-shop.html')
		template_values = {
			'Area': area,
			'activity':'Shop'
		}
		self.response.write(template.render(template_values))
		
class StudyArea(webapp2.RequestHandler):
	def get(self):
		area_input = self.request.get('study-area')
		area_info = StudyLocation.query(StudyLocation.area==area_input)
		area = area_info.fetch().pop()
		template = jinja_environment.get_template('area-study.html')
		template_values = {
			'Area': area,
			'activity':'Study'
		}
		self.response.write(template.render(template_values))
		
class PoopArea(webapp2.RequestHandler):
	def get(self):
		area_input = self.request.get('poop-area')
		area_info = PoopLocation.query(PoopLocation.area==area_input)
		area = area_info.fetch().pop()
		template = jinja_environment.get_template('area-poop.html')
		template_values = {
			'Area': area,
			'activity':'Poop'
			
		}
		self.response.write(template.render(template_values))



class Thanks(webapp2.RequestHandler):
    """ Handler for the thanks page."""

    def get(self):
        template = jinja_environment.get_template('thanks.html')
        self.response.out.write(template.render())
		
class Error(webapp2.RequestHandler):
    """ Handler for the error page."""

    def get(self):
        template = jinja_environment.get_template('error.html')
        self.response.out.write(template.render())

##################Datastore Definitions##################
class StudyLocation(ndb.Model):
	date = ndb.DateTimeProperty(auto_now_add=True)
	
	#Location, string
	faculty = ndb.StringProperty()
	area = ndb.StringProperty()
	buildingfloor = ndb.StringProperty()
	
	#Nearby facilities, boolean
	shop = ndb.StringProperty()
	poop = ndb.StringProperty()
	
	#Number of Amenities, integer
	numSeats = ndb.IntegerProperty()
	numTables = ndb.IntegerProperty()
	numSockets = ndb.IntegerProperty()
	total = ndb.IntegerProperty()
	
	#Has Amenities, boolean
	chairs = ndb.StringProperty()
	sofas = ndb.StringProperty()
	tables = ndb.StringProperty()
	sockets = ndb.StringProperty()
	aircon = ndb.StringProperty()
	
	#Sort by rating
	rating = ndb.IntegerProperty()

	#Images, string
	image1 = ndb.StringProperty()
	image2 = ndb.StringProperty()
	image3 = ndb.StringProperty()
	
	directions = ndb.StringProperty()
class ShopLocation(ndb.Model):
	date = ndb.DateTimeProperty(auto_now_add=True)
	
	#Location, string
	faculty = ndb.StringProperty()
	buildingfloor = ndb.StringProperty()
	
	shopName = ndb.StringProperty()
	
	#Nearby Amenities, boolean
	study = ndb.StringProperty()
	poop = ndb.StringProperty()
	
	#Type of shop, what does it sell(bazaar, co-op ...etc), string
	shopType = ndb.StringProperty()
	
	#Short description of the shop
	shopDesc = ndb.StringProperty()

	#Rating, only applicable to food outlets
	rating = ndb.IntegerProperty()
	
	#Images, string
	image1 = ndb.StringProperty()
	image2 = ndb.StringProperty()
	
	#Bazaar Info
	dateStart = ndb.DateProperty()
	dateEnd = ndb.DateProperty()
	time = ndb.StringProperty()
	
	directions = ndb.StringProperty()

class PoopLocation(ndb.Model):
	date = ndb.DateTimeProperty(auto_now_add=True)
		
	#Location, string	
	faculty = ndb.StringProperty()
	area = ndb.StringProperty()
	buildingfloor = ndb.StringProperty()
	
	#Nearby Amenities, boolean
	study = ndb.StringProperty()
	shop = ndb.StringProperty()
	
	#Cleanliness, integer
	cleanlinessGents = ndb.IntegerProperty()
	cleanlinessLadies = ndb.IntegerProperty()
	
	total = ndb.IntegerProperty()
	cleanliness = ndb.IntegerProperty()
	
	hasHandicapped = ndb.StringProperty()
	cleanlinessHandicapped = ndb.IntegerProperty()
	
	#Images, string
	ladies = ndb.StringProperty()
	gents = ndb.StringProperty()
	
	directions = ndb.StringProperty()
"""
class BazaarInfo(ndb.Model):
	bazaarName = ndb.StringProperty()
	dateStart = ndb.DateProperty()
	dateEnd = ndb.DateProperty()
	time = ndb.StringProperty()
"""
class ContactForm(ndb.Model):
	name = ndb.StringProperty()
	email = ndb.StringProperty()
	message = ndb.StringProperty()

class AddFileStudy(webapp2.RequestHandler):
	def post(self):
		
		f = open("study2.txt", "r")
		line = f.readline()
		while True:
			if line == "":
				break

			data = [element.strip() for element in line.split('|')]
			content = StudyLocation()
			content.faculty = data[0]
			content.buildingfloor = data[1]
			content.area = data[2]
			
			content.shop = data[3]
			content.poop = data[4]
				
			content.chairs = data[5]
			content.sofas = data[6]
			content.tables = data[7]
			content.sockets = data[8]
			content.aircon = data[9]
			
			content.numSeats = int(data[10])
			content.numTables = int(data[11])
			content.numSockets = int(data[12])
			
			content.rating = int(data[13])
			
			content.directions = data[14]
			content.image1 = data[15]
			content.image2 = data[16]
			content.image3 = data[17]

			content.total = content.numSeats + content.numTables + content.numSockets
			
			content.put();
			line = f.readline()
		
		f.close()
		self.redirect('/add')
				
class AddFileShop(webapp2.RequestHandler):
	def post(self):
		
		f = open("shop.txt", "r")
		line = f.readline()
		while True:
			if line == "":
				break

			data = [element.strip() for element in line.split('|')]
			content = ShopLocation()
			content.faculty = data[0]
			content.buildingfloor = data[1]
			content.shopName = data[2]
			
			content.study = data[3]
			content.poop = data[4]
			
			content.shopType = data[5]
			
			content.rating = int(data[6])
			
			content.directions = data[7]
			
			content.shopDesc = data[8]
			
			content.image1 = data[9]
			content.image2 = data[10]
			
			content.put();
			line = f.readline()
		
		f.close()
		self.redirect('/add')		

class AddFilePoop(webapp2.RequestHandler):
	def post(self):
		
		f = open("poop.txt", "r")
		line = f.readline()
		while True:
			if line == "":
				break

			data = [element.strip() for element in line.split('|')]
			content = PoopLocation()
			content.faculty = data[0]
			content.buildingfloor = data[1]
			content.area = data[2]
			content.study = data[3]
			content.poop = data[4]
			content.cleanlinessGents = int(data[5])
			content.cleanlinessLadies = int(data[6])
			
			content.hasHandicapped = data[7]
			
			content.cleanlinessHandicapped = int(data[8])
			content.directions = data[9]
			if content.hasHandicapped=="on":
				content.cleanliness = (content.cleanlinessGents + content.cleanlinessLadies + content.cleanlinessHandicapped)/3
			else:
				content.cleanliness = (content.cleanlinessGents + content.cleanlinessLadies)/2
			"""
			content.ladies = data[10]
			content.gents = data[11]
			"""
			content.put();
			line = f.readline()
		
		f.close()
		self.redirect('/add')				
		
app = webapp2.WSGIApplication([('/', MainPage),
								('/contact', Contact),
								('/shop', Shop),
								('/study', Study),
								('/poop', Poop),
								('/add', Add),
								('/edit-study', AddStudy),
								('/edit-shop', AddShop),
								('/edit-poop', AddPoop),
								('/shop-choose', ShopChoose),
								('/shop-sort', ShopSort),
								('/submit-shop-name', ShopArea),
								('/study-choose', StudyChoose),
								('/study-sort', StudySort),
								('/submit-study-area', StudyArea),
								('/poop-choose', PoopChoose),
								('/poop-sort', PoopSort),
								('/submit-poop-area', PoopArea),
								('/contact-submit', Contact),
								('/thanks', Thanks),
								('/error', Error),
								('/more-info', Information),
								('/add-file-study', AddFileStudy),
								('/add-file-shop', AddFileShop),
								('/add-file-poop', AddFilePoop)],
								debug=True)
