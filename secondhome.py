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

class Sleep(webapp2.RequestHandler):
    """ Handler for the sleep page."""

    def get(self):
        template = jinja_environment.get_template('sleep.html')
        self.response.out.write(template.render())

class SleepChoose(webapp2.RequestHandler):
		
	def get(self):
		sleep_choice = self.request.get('sleep-select')
		template = jinja_environment.get_template('sleep-choice.html')
		if sleep_choice=="arts and social sciences":
			sleep_query = Location.query(ndb.AND(Location.faculty=='arts and social sciences', Location.sleep=='t')).order(-Location.date)
		elif sleep_choice=="business":
			sleep_query = Location.query(ndb.AND(Location.faculty=='business', Location.sleep=='t')).order(-Location.date)
		elif sleep_choice=="computing":
			sleep_query = Location.query(ndb.AND(Location.faculty=='computing', Location.sleep=='t')).order(-Location.date)
		elif sleep_choice=="design and environment":
			sleep_query = Location.query(ndb.AND(Location.faculty=='design and environment', Location.sleep=='t')).order(-Location.date)
		elif sleep_choice=="engineering":
			sleep_query = Location.query(ndb.AND(Location.faculty=='engineering', Location.sleep=='t')).order(-Location.date)
		elif sleep_choice=="music":
			sleep_query = Location.query(ndb.AND(Location.faculty=='music', Location.sleep=='t')).order(-Location.date)
		elif sleep_choice=="science":
			sleep_query = Location.query(ndb.AND(Location.faculty=='science', Location.sleep=='t')).order(-Location.date)
		elif sleep_choice=="utown":
			sleep_query = Location.query(ndb.AND(Location.faculty=='utown', Location.sleep=='t')).order(-Location.date)
		else:
			sleep_query = Location.query(Location.sleep=='t').order(-Location.date)
		sleep_locations = sleep_query.fetch()
		template_values = {
			'locations': sleep_locations,
			'faculty_name': sleep_choice.upper()
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
		template = jinja_environment.get_template('shop-choice.html')
		if shop_choice=="arts and social sciences":
			shop_query = Location.query(ndb.AND(Location.faculty=='arts and social sciences', Location.shop=='t')).order(-Location.date)
		elif shop_choice=="business":
			shop_query = Location.query(ndb.AND(Location.faculty=='business', Location.shop=='t')).order(-Location.date)
		elif shop_choice=="computing":
			shop_query = Location.query(ndb.AND(Location.faculty=='computing', Location.shop=='t')).order(-Location.date)
		elif shop_choice=="design and environment":
			shop_query = Location.query(ndb.AND(Location.faculty=='design and environment', Location.shop=='t')).order(-Location.date)
		elif shop_choice=="engineering":
			shop_query = Location.query(ndb.AND(Location.faculty=='engineering', Location.shop=='t')).order(-Location.date)
		elif shop_choice=="music":
			shop_query = Location.query(ndb.AND(Location.faculty=='music', Location.shop=='t')).order(-Location.date)
		elif shop_choice=="science":
			shop_query = Location.query(ndb.AND(Location.faculty=='science', Location.shop=='t')).order(-Location.date)
		elif shop_choice=="utown":
			shop_query = Location.query(ndb.AND(Location.faculty=='utown', Location.shop=='t')).order(-Location.date)
		else:
			shop_query = Location.query(Location.shop=='t').order(-Location.date)
		shop_locations = shop_query.fetch()
		template_values = {
			'locations': shop_locations,
			'faculty_name': shop_choice.upper()
		}
		self.response.write(template.render(template_values))
class Study(webapp2.RequestHandler):
    """ Handler for the study page."""

    def get(self):
        template = jinja_environment.get_template('study.html')
        self.response.out.write(template.render())
class StudyChoose(webapp2.RequestHandler):
		
	def get(self):
		study_choice = self.request.get('study-select')
		template = jinja_environment.get_template('study-choice.html')
		if study_choice=="arts and social sciences":
			study_query = Location.query(ndb.AND(Location.faculty=='arts and social sciences', Location.study=='t')).order(-Location.date)
		elif study_choice=="business":
			study_query = Location.query(ndb.AND(Location.faculty=='business', Location.study=='t')).order(-Location.date)
		elif study_choice=="computing":
			study_query = Location.query(ndb.AND(Location.faculty=='computing', Location.study=='t')).order(-Location.date)
		elif study_choice=="design and environment":
			study_query = Location.query(ndb.AND(Location.faculty=='design and environment', Location.study=='t')).order(-Location.date)
		elif study_choice=="engineering":
			study_query = Location.query(ndb.AND(Location.faculty=='engineering', Location.study=='t')).order(-Location.date)
		elif study_choice=="music":
			study_query = Location.query(ndb.AND(Location.faculty=='music', Location.study=='t')).order(-Location.date)
		elif study_choice=="science":
			study_query = Location.query(ndb.AND(Location.faculty=='science', Location.study=='t')).order(-Location.date)
		elif study_choice=="utown":
			study_query = Location.query(ndb.AND(Location.faculty=='utown', Location.study=='t')).order(-Location.date)
		else:
			study_query = Location.query(Location.study=='t').order(-Location.date)
		study_locations = study_query.fetch()
		template_values = {
			'locations': study_locations,
			'faculty_name': study_choice.upper()
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
		template = jinja_environment.get_template('poop-choice.html')
		if poop_choice=="arts and social sciences":
			poop_query = Location.query(ndb.AND(Location.faculty=='arts and social sciences', Location.poop=='t')).order(-Location.date)
		elif poop_choice=="business":
			poop_query = Location.query(ndb.AND(Location.faculty=='business', Location.poop=='t')).order(-Location.date)
		elif poop_choice=="computing":
			poop_query = Location.query(ndb.AND(Location.faculty=='computing', Location.poop=='t')).order(-Location.date)
		elif poop_choice=="design and environment":
			poop_query = Location.query(ndb.AND(Location.faculty=='design and environment', Location.poop=='t')).order(-Location.date)
		elif poop_choice=="engineering":
			poop_query = Location.query(ndb.AND(Location.faculty=='engineering', Location.poop=='t')).order(-Location.date)
		elif poop_choice=="music":
			poop_query = Location.query(ndb.AND(Location.faculty=='music', Location.poop=='t')).order(-Location.date)
		elif poop_choice=="science":
			poop_query = Location.query(ndb.AND(Location.faculty=='science', Location.poop=='t')).order(-Location.date)
		elif poop_choice=="utown":
			poop_query = Location.query(ndb.AND(Location.faculty=='utown', Location.poop=='t')).order(-Location.date)
		else:
			poop_query = Location.query(Location.poop=='t').order(-Location.date)
		poop_locations = poop_query.fetch()
		template_values = {
			'locations': poop_locations,
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
		contact.put();
		self.redirect('/thanks')
		
class Area(webapp2.RequestHandler):
    """ Handler for the area page."""

    def get(self):
        template = jinja_environment.get_template('area.html')
        self.response.out.write(template.render())

class Add(webapp2.RequestHandler):
	""" Handler for the add page."""
	def get(self):
		location_query = Location.query().order(-Location.date)
		locations = location_query.fetch()
		template = jinja_environment.get_template('add.html')
		self.response.write(template.render(locations=locations))
		
	def post(self):
		content = Location()
		content.faculty = self.request.get('select1')
		content.area = self.request.get('input2')
		
		content.sleep = self.request.get('input3')
		content.shop = self.request.get('input4')
		content.study = self.request.get('input5')
		content.poop = self.request.get('input6')
		
		content.sofas = self.request.get('input7')
		content.tables = self.request.get('input8')
		content.sockets = self.request.get('input9')
		content.beds = self.request.get('input10')
		content.shops = self.request.get('input11')
		content.toilets = self.request.get('input12')
		
		content.put();
		self.redirect('/add')
		
class SleepArea(webapp2.RequestHandler):
	def get(self):
		area_input = self.request.get('sleep-area')
		area_info = Location.query(Location.area==area_input)
		area = area_info.fetch().pop()
		template = jinja_environment.get_template('area-sleep.html')
		template_values = {
			'AreaName': area_input,
			'FacultyName': area.faculty.upper(),
			'sofas': area.sofas,
			'tables': area.tables,
			'beds': area.beds,
			'activity':'Sleep'
		}
		self.response.write(template.render(template_values))

class ShopArea(webapp2.RequestHandler):
	def get(self):
		area_input = self.request.get('shop-area')
		area_info = Location.query(Location.area==area_input)
		area = area_info.fetch().pop()
		template = jinja_environment.get_template('area-shop.html')
		template_values = {
			'AreaName': area_input,
			'FacultyName': area.faculty.upper(),
			'shops': area.shops,
			'activity':'Shop'
			
		}
		self.response.write(template.render(template_values))
		
class StudyArea(webapp2.RequestHandler):
	def get(self):
		area_input = self.request.get('study-area')
		area_info = Location.query(Location.area==area_input)
		area = area_info.fetch().pop()
		template = jinja_environment.get_template('area-study.html')
		template_values = {
			'AreaName': area_input,
			'FacultyName': area.faculty.upper(),
			'sofas': area.sofas,
			'tables': area.tables,
			'activity':'Study'
			
		}
		self.response.write(template.render(template_values))
		
class PoopArea(webapp2.RequestHandler):
	def get(self):
		area_input = self.request.get('poop-area')
		area_info = Location.query(Location.area==area_input)
		area = area_info.fetch().pop()
		template = jinja_environment.get_template('area-poop.html')
		template_values = {
			'AreaName': area_input,
			'FacultyName': area.faculty.upper(),
			'toilets': area.toilets,
			'activity':'Poop'
			
		}
		self.response.write(template.render(template_values))



class Thanks(webapp2.RequestHandler):
    """ Handler for the thanks page."""

    def get(self):
        template = jinja_environment.get_template('thanks.html')
        self.response.out.write(template.render())

##################Datastore Definitions##################
class Location(ndb.Model):
	date = ndb.DateTimeProperty(auto_now_add=True)
		
	faculty = ndb.StringProperty()
	area = ndb.StringProperty()
	
	sleep = ndb.StringProperty()
	shop = ndb.StringProperty()
	study = ndb.StringProperty()
	poop = ndb.StringProperty()
	
	sofas = ndb.StringProperty()
	tables = ndb.StringProperty()
	sockets = ndb.StringProperty()
	beds = ndb.StringProperty()
	shops = ndb.StringProperty()
	toilets = ndb.StringProperty()

class ContactForm(ndb.Model):
	name = ndb.StringProperty()
	email = ndb.StringProperty()
	message = ndb.StringProperty()

app = webapp2.WSGIApplication([('/', MainPage),
								('/contact', Contact),
								('/sleep', Sleep),
								('/shop', Shop),
								('/study', Study),
								('/poop', Poop),
								('/add', Add),
								('/edit', Add),
								('/sleep-choose', SleepChoose),
								('/submit-sleep-area', SleepArea),
								('/shop-choose', ShopChoose),
								('/submit-shop-area', ShopArea),
								('/study-choose', StudyChoose),
								('/submit-study-area', StudyArea),
								('/poop-choose', PoopChoose),
								('/submit-poop-area', PoopArea),
								('/contact-submit', Contact),
								('/thanks', Thanks)],
								debug=True)
