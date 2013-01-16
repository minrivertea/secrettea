from django.db import models
from datetime import date

from ckeditor.fields import RichTextField


class Tour(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200)
    promo_image = models.ImageField(upload_to='tours', blank=True, null=True)
    intro_content = models.TextField(blank=True, null=True)
    main_content = RichTextField(blank=True, null=True)
    remaining_places = models.IntegerField(default=0)
    price = models.IntegerField(blank=True, null=True)
    starting_point = models.CharField(max_length=200, blank=True, null=True)
    start_date = models.DateField()
    end_date = models.DateField()
    
    def __unicode__(self):
        month = self.end_date.strftime("%B")
        name = "%s (%s-%s %s %s)" % (self.name, self.start_date.day, self.end_date.day, month, self.end_date.year)
        return name
    
    def get_photos(self):
        photos = GalleryImage.objects.filter(tour=self)
        return photos


class GalleryImage(models.Model):
    image = models.ImageField(upload_to='gallery-images')
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    tour = models.ForeignKey(Tour, blank=True, null=True)
    
    def __unicode__(self):
        return self.title
        
    def get_next(self):
        photos = []
        i = 5
        this_id = self.id
        while i > 0:
            try:
                next_id = this_id + 1
                photos.append(GalleryImage.objects.get(pk=next_id, tour=self.tour))
            except:
                pass
            i -= 1
            this_id += 1
        return photos

    def get_prev(self):
        photos = []
        i = 5
        this_id = self.id
        while i > 0:
            try:
                next_id = this_id - 1
                photos.append(GalleryImage.objects.get(pk=next_id, tour=self.tour))
            except:
                break
            i -= 1
            this_id -= 1
        photos = sorted(photos, key=lambda x: x.id, reverse=False)
        return photos
        

class Page(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField()
    content = RichTextField()
    is_draft = models.BooleanField(default=True)
    
    def __unicode__(self):
        return self.title