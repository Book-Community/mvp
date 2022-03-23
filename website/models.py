import uuid
from django.db import models

# Create your models here.

class Author(models.Model):
	first_name = models.CharField(max_length=30)
	last_name = models.CharField(max_length=30)
	born = models.DateField()
	dead = models.DateField()
	bio = models.TextField(max_length=3000)
class Publisher(models.Model):
	name = models.CharField(max_length=30)
	country = models.CharField(max_length=50)
class Genres(models.Model):
	id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
	name = models.CharField(max_length=50, unique=True)
class Book(models.Model):
	title = models.CharField(max_length=300)
	original_title = models.CharField(max_length=300, blank=True)
	authors = models.ManyToManyField(Author)
	publisher = models.ForeignKey(Publisher, on_delete=models.SET_NULL, null=True)
	language = models.CharField(max_length=100)
	publication_date = models.DateField()
	isbn13 = models.BigIntegerField(primary_key=True)
	description = models.TextField(max_length=3000)
	rating = models.FloatField()
	genres = models.ManyToManyField(Genres)
class User(models.Model):
	first_name = models.CharField(max_length=30)
	last_name = models.CharField(max_length=30)
	email = models.EmailField(max_length=254, unique=True, primary_key=True)
	books = models.ManyToManyField(Book)

class List(models.Model):
	name = models.CharField(max_length=300)
	user = models.ForeignKey(User, on_delete=models.CASCADE, db_index=True)
	date_created = models.DateTimeField()
	date_last_update = models.DateTimeField()
	id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
	books = models.ManyToManyField(Book)
class userList(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	to_read = models.OneToOneField(List, on_delete=models.PROTECT, related_name='to_read')
	currently_reading = models.OneToOneField(List, on_delete=models.PROTECT, related_name='currently_reading')
	read = models.OneToOneField(List, on_delete=models.PROTECT, related_name='read')
class Review(models.Model):
	id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	book = models.OneToOneField(Book, on_delete=models.CASCADE, db_index=True)
	rating = models.IntegerField()
	text_review = models.TextField(max_length=500)






