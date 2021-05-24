
import uuid
from customers.models import Customers
from profiles.models import Profile
def generate_code():
    code = str(uuid.uuid4()).replace('-', '').upper()[:12]
    return code

def get_salesman_from_id(val):
    salesman = Profile.objects.get(id=val)
    return salesman.user.username
def get_customer_from_id(val):
    customer = Customers.objects.get(id=val)
    return customer