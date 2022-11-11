from django.db import models


class Comment(models.Model):
    comment_id = models.CharField(max_length=255, blank=True)
    mappoint_id = models.ForeignKey("Mappoint", on_delete= models.CASCADE)
    author_id = models.ForeignKey("User", on_delete=models.SET_NULL) # oder SET() ???
    created_at = models.DateTimeField(auto_now=True)
    text = models.CharField(max_length=255, blank=True)
    rating = models.IntegerField()
    image = models.CharField(max_length=255, blank=True)
    video = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.text

    class Meta:
        ordering = ["-created"]



"""
def save(self, *args, **kwargs):
        if len(self.ticket_id.strip(" "))==0:
            self.ticket_id = generate_ticket_id()

        super(Ticket, self).save(*args, **kwargs) # Call the real   save() method
 """
