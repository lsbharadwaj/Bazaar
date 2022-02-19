from django.db.models.signals import post_delete,pre_save
from django.dispatch import receiver
from .models import Product, Store


@receiver(post_delete, sender=Store)
def deleteStorePhotoOnDelete(sender, instance, using, **kwargs):
    try:
        instance.store_img.delete(save=False)
    except:
        pass




@receiver(post_delete, sender=Product)
def deleteProductPhotoOnDelete(sender, instance,  using,**kwargs):
    try:
        instance.product_img.delete(save=False)
    except:
        pass

@receiver(pre_save, sender=Product)
def pre_save_image(sender, instance, *args, **kwargs):
    """ instance old image file will delete from os """
    try:
        old_img = instance.__class__.objects.get(id=instance.id).product_img.path
        try:
            new_img = instance.product_img.path
        except:
            new_img = None
        if new_img != old_img:
            import os
            if os.path.exists(old_img):
                os.remove(old_img)
    except:
        pass



@receiver(pre_save, sender=Store)
def pre_save_image(sender, instance, *args, **kwargs):
    """ instance old image file will delete from os """
    try:
        old_img = instance.__class__.objects.get(id=instance.id).store_img.path
        try:
            new_img = instance.store_img.path
        except:
            new_img = None
        if new_img != old_img:
            import os
            if os.path.exists(old_img):
                os.remove(old_img)
    except:
        pass