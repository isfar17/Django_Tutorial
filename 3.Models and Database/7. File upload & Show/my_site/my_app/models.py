from django.db import models

# Create your models here.
class Demo(models.Model):
    name=models.CharField(max_length=100)
    address=models.CharField(max_length=300)
    image=models.ImageField(upload_to='demo_images') #this will save the image in demo_images folder inside media folder.
    
'''
media/ path is the root path that will hold the images. But the models will have their own folder names. imagine there are
6 apps and each has a model that will store images. so all of them will store image in the MEDIA_ROOT folder, but under the folder
they have defined, thus all the images won't get mixed up and the models will have their own folder with their images.

format:

media
    app_1_model
        image1
        image2
    app_2_model
        imnge1
        image2

'''