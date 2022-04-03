from collections import UserDict
import uuid
from django.db import models

# Create your models here.

class Country(models.Model):
	id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
	name_el = models.CharField(max_length=100)
	name_en = models.CharField(max_length=100)

class Author(models.Model):
	first_name = models.CharField(max_length=30)
	last_name = models.CharField(max_length=30)
	first_name_el = models.CharField(max_length=30, blank=True)
	last_name_el = models.CharField(max_length=30, blank=True)
	country = models.ForeignKey(Country, null = True, on_delete=models.SET_NULL)
	born = models.DateField(blank=True)
	dead = models.DateField(blank=True)
	bio = models.TextField(max_length=3000, blank=True)
class Publisher(models.Model):
	name = models.CharField(max_length=30)
	country = models.CharField(max_length=50, blank=True)
class Genres(models.Model):
	id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
	name = models.CharField(max_length=50, unique=True)
class Book(models.Model):
	title = models.CharField(max_length=300)
	original_title = models.CharField(max_length=300, blank=True)
	original_isbn13 = models.BigIntegerField(blank=True)
	authors = models.ManyToManyField(Author)
	publisher = models.ForeignKey(Publisher, on_delete=models.SET_NULL, null=True)
	language = models.CharField(max_length=100)
	publication_date = models.DateField(blank=True)
	isbn13 = models.BigIntegerField(primary_key=True)
	description = models.TextField(max_length=3000, blank=True)
	rating = models.FloatField(blank=True)
	genres = models.ManyToManyField(Genres)
class User(models.Model):
	first_name = models.CharField(max_length=30)
	last_name = models.CharField(max_length=30)
	email = models.EmailField(max_length=254, unique=True, primary_key=True)

class Friends(models.model):
	user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key= True)
	friends = models.ManyToManyField(User, blank=True)

class FriendRequest(models.Model):
	id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
	from_user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True)
	to_user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, db_index= True)

class List(models.Model):
	name = models.CharField(max_length=300)
	user = models.ForeignKey(User, on_delete=models.CASCADE, db_index=True)
	date_created = models.DateTimeField(auto_now_add=True, editable=False)
	date_last_update = models.DateTimeField(auto_now=True, editable=False)
	id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
	books = models.ManyToManyField(Book)
class ReadList(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
	date_created = models.DateTimeField(auto_now_add=True, editable=False)
	date_last_update = models.DateTimeField(auto_now=True, editable=False)
	books = models.ManyToManyField(Book)

class ToReadList(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
	date_created = models.DateTimeField(auto_now_add=True, editable=False)
	date_last_update = models.DateTimeField(auto_now=True, editable=False)
	books = models.ManyToManyField(Book)

class CurrentlyReadingList(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
	date_created = models.DateTimeField(auto_now_add=True, editable=False)
	date_last_update = models.DateTimeField(auto_now=True, editable=False)
	books = models.ManyToManyField(Book)	
class Review(models.Model):
	id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	book = models.OneToOneField(Book, on_delete=models.CASCADE, db_index=True)
	rating = models.IntegerField()
	text_review = models.TextField(max_length=500)
	date_created = models.DateTimeField(auto_now_add=True, editable=False)
	date_last_update = models.DateTimeField(auto_now=True, editable=False)







