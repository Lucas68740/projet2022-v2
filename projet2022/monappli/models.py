from django.db import models

class Tel(models.Model):
    marque = models.CharField(max_length=100)
    memoire = models.CharField(max_length=100)
    date = models.DateField(blank=True, null=True)
    prix = models.IntegerField(blank=False)
    resume = models.TextField(null=True, blank=True)

    def __str__(self):
        chaine = f"{self.marque} en version {self.memoire} go sortie en {self.date} avec un prix de {self.prix} €"
        return chaine
    def dico(self):
        return {"marque":self.marque, "memoire":self.memoire, "date":self.date, "prix":self.prix,"resume":self.resume}

