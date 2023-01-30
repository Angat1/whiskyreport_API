from django.db import models

class Whisky(models.Model):
    title=models.CharField(max_length=255,null=True)
    whiskybase_url = models.CharField(max_length=255,null=True)
    auction_house_names = models.CharField(max_length=255)
    short_description = models.CharField(max_length=255)
    long_description = models.CharField(max_length=255)
    sale_price = models.CharField(max_length=255)
    sale_date = models.CharField(max_length=255)
    url = models.CharField(max_length=255)
    distillery = models.CharField(max_length=255)
    age = models.CharField(max_length=255)
    cask = models.CharField(max_length=255)
    vintage = models.CharField(max_length=255)
    bottled_year = models.CharField(max_length=255)
    abv = models.CharField(max_length=255)
    size = models.CharField(max_length=255)
    bottler = models.CharField(max_length=255)
    source = models.CharField(max_length=255)
    updated_at = models.CharField(max_length=255)
    scraped_at = models.CharField(max_length=255)
    image = models.CharField(max_length=255)


    class Meta:
        indexes=[models.Index(fields=["short_description"],name='short_description_idx'),]
        #indexes=[models.Index(fields=["title","auction_house_names","short_description","long_description","sale_price","sale_date","url","distillery","age","cask","vintage","bottled_year","abv","size","bottler","source","updated_at","scraped_at","image","whiskybase_url"]),]


