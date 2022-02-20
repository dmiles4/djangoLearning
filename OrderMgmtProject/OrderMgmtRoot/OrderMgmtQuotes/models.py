from django.db import models
from django.contrib.auth.models import User

# Create your models here.
# Creating a tuple, that we'll use as drop down options below in our table
STATUS_CHOICES = (
    # The first value, NEW, is what's saved to the database. The second, New Site, is what's displayed for the user
    ('NEW','New Site'),
    ('EX', 'Existing Site'),
)

PRIORITY_CHOICES = (
    ('U', 'Urgent - 1 week or less'),
    ('N', 'Normal - 2 to 4 weeks'),
    ('L', 'Low - Still researching'),
)

# Remember in models, a class = a table. So we are creating the quotes table.
class Quote(models.Model):
    # Attributes are columns.
    name = models.CharField(max_length=100)   # A simple character column, with a max length set
    position = models.CharField(max_length=60, blank=True)  # blank = true means the field isn't mandatory
    company = models.CharField(max_length=60, blank=True)
    address = models.CharField(max_length=200, blank=True)
    phone = models.CharField(max_length=30, blank=True)
    email = models.EmailField()     # Django can automatically pick up if a valid email has been entered
    web = models.URLField(blank=True)   # Same for a URL
    description = models.TextField()    # TextField is the larger text entry box
    sitestatus = models.CharField(max_length=20, choices=STATUS_CHOICES)    # This uses the tuple we placed up top
    priority = models.CharField(max_length=40, choices=PRIORITY_CHOICES)
    # This will allow django to upload files, and we set it to upload them to the uploads folder
    jobfile = models.FileField(upload_to='uploads/', blank=True)
    # auto_now_add will automatically use the current date and time to timestamp submissions
    submitted = models.DateField(auto_now_add=True)
    # If the quotedate is left blank, null=True will automatically fill the field with a null
    quotedate = models.DateField(blank=True, null=True)
    quoteprice = models.DecimalField(decimal_places=2, max_digits=7, blank=True, default=0)
    # This is our first foreign key to the user table. User management will be covered later.
    # A couple of things to note, foreign key fields can't be empty, so if there's a blank it needs to be set to null
    # Also the on_delete models.CASCADE sets django to delete related entries on other tables if this entity is deleted
    username = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id)