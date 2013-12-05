import re
import urllib2
from django.db import models
from datetime import datetime
from datetime import timedelta

class Book(models.Model):
    name = models.CharField(max_length = 200)
    ISBN = models.CharField(max_length = 200)

    def get_current_price(self):
        recent_prices = self.prices.filter(datetime__gte = datetime.now() - timedelta(days=1))
        if recent_prices:
            return recent_prices[0]

        request = urllib2.urlopen("http://literaryduck.uoduckstore.com/BuybackBooks.aspx?i=%s" % self.ISBN[:-1])
        html = request.read()
        m = re.search('Estimated Buyback Price: \$(.*)\<', html)
        if m:
            price = float(m.group(1))
            p = self.prices.create(datetime = datetime.now(), price = price)
            return p

        else:
            return False

class BookPrice(models.Model):
    book = models.ForeignKey(Book, related_name='prices')
    datetime = models.DateTimeField()
    price = models.FloatField()

    def __unicode__(self):
        return u'%s: %s at %s' % (self.book.ISBN, self.price, self.datetime)
