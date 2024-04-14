from pynamodb.models import Model
from pynamodb.attributes import UnicodeAttribute, NumberAttribute

class UrlModel(Model):
    class Meta:
        table_name = "Url"
    short_url = UnicodeAttribute(hash_key= True)
    og_url = UnicodeAttribute()


class UserModel(Model):
    class Meta:
        table_name = "User"
    email = UnicodeAttribute(hash_key=True)
    username = UnicodeAttribute()
    password = UnicodeAttribute()
    level = NumberAttribute(default=0)


