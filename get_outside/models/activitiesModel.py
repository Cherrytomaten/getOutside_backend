from django.db import models


class Activities(models.Model):
    category = models.ForeignKey("Category", on_delete=models.CASCADE)
    title= models.CharField(max_length=30)
    activity_id = models.CharField(max_length=255, blank=True)
    created = models.DateTimeField(auto_now=True)
    longitude = models.ForeignKey("Mappoint", on_delete= models.CASCADE)
    latitude = models.ForeignKey("Mappoint", on_delete= models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ["-created"]


class Category(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


"""
def save(self, *args, **kwargs):
        if len(self.ticket_id.strip(" "))==0:
            self.ticket_id = generate_ticket_id()

        super(Ticket, self).save(*args, **kwargs) # Call the real   save() method
 """
