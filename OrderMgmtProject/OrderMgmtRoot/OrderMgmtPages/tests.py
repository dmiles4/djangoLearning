from django.test import TestCase
from .models import Customer

# Create your tests here.
class CustomerTestCase(TestCase):
    def setUp(self):
        Customer.objects.create(firstname='Neel', lastname='Patel')
        Customer.objects.create(firstname='David', lastname='Patel')
        Customer.objects.create(firstname='Henry', lastname='Patel')

        Customer.objects.create(firstname=form_fname, lastname=form_lname)
    def testCustomer(selfself):
        neel = Customer.objects.get(firstname = 'Neel')
        print(neel.firstname)
        print(neel.lastname)