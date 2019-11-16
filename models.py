
from google.appengine.ext import ndb

class StickUser(ndb.Model):
    first_name = ndb.StringProperty()
    last_name = ndb.StringProperty()
    email = ndb.StringProperty()
    friends = ndb.KeyProperty(kind="SchedifyUser", repeated=True)
    requests = ndb.KeyProperty(kind="SchedifyUser", repeated=True)

    def update_profile(self,new_username,new_firstname,new_lastname,new_bio):
        self.username = new_username
        self.first_name = new_firstname
        self.last_name = new_lastname
        self.bio = new_bio
        self.put()

    def add_request(self, key):
        self.requests.append(key)
        self.put()

    def remove_request(self, key):
        self.requests.remove(key)
        self.put()

    def add_friend(self, key):
        self.friends.append(key)
        self.put()

    def remove_friend(self, key):
        self.friends.remove(key)
        self.put()
        # searches through the friend list and removes friend

class Event(ndb.Model):
    owner = ndb.KeyProperty(SchedifyUser)
    title = ndb.StringProperty()
    # Summary should have a character cap
    summary = ndb.StringProperty()
    notes = ndb.StringProperty()
    time = ndb.IntegerProperty()
    # when outputed, the label should be in caps
    label = ndb.StringProperty()

    def update_event(self,new_title,new_summary, new_notes, new_time):
        self.title = new_title
        self.summary = new_summary
        self.notes = new_notes
        self.time = new_time
        self.put()
