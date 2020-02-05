from django.db import models

# keep in mind that django automatically adds the id to the database without us needing to specify it in our code
# search for django database datatypes to see the full list of datatypes we can use
# also see the django docs (https://docs.djangoproject.com/en/3.0/topics/db/models/) for more info about validators for instance

class List(models.Model):
    item = models.CharField(max_length=200)
    completed = models.BooleanField(default=False)


    #this is important for the admin page, shows the name of the action when we add it (the item)
    def __str__(self):
        return self.item + ' ' + str(self.completed)

