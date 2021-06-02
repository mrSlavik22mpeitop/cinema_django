from django.db import models

class BranchShots(models.Model):
    title = models.CharField(max_length=70, null=True)
    description = models.TextField(null=True)
    image = models.ImageField(upload_to='academia/', null=True, blank=True)
    branch = models.ForeignKey('branch.Branch', on_delete=models.CASCADE)

    def __str__(self):
        return self.id

