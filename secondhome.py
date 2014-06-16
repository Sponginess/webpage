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

class Study(webapp2.RequestHandler):
    """ Handler for the study page."""

    def get(self):
        template = jinja_environment.get_template('study.html')
        self.response.out.write(template.render())
		
class Poop(webapp2.RequestHandler):
    """ Handler for the poop page."""

    def get(self):
        template = jinja_environment.get_template('poop.html')
        self.response.out.write(template.render())
		
class Contact(webapp2.RequestHandler):
    """ Handler for the contact page."""

    def get(self):
        template = jinja_environment.get_template('contact.html')
        self.response.out.write(template.render())
		
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

app = webapp2.WSGIApplication([('/', MainPage),
								('/contact', Contact),
								('/sleep', Sleep),
								('/shop', Shop),
								('/study', Study),
								('/poop', Poop),
								('/add', Add),
								('/edit', Add),
								('/area', Area),
								('/sleep-choose', SleepChoose)],
								debug=True)
