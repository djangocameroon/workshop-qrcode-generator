from django.db import models

from website.utils import generate_qrcode, generate_uuid


class DataInformation(models.Model):
    uuid = models.CharField(
        max_length=100, 
        primary_key=True, 
        default=generate_uuid,
        editable=False,
    )
    content = models.TextField(unique=True)
    qr_code = models.ImageField(
        upload_to='qr_codes/', 
        blank=True, 
        editable=False,
    )
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.uuid
    
    def save(self, *args, **kwargs):
        qr_code_image = generate_qrcode(self.content)
        filename = f"qrcode-{self.uuid}.png"
        self.qr_code.save(filename, qr_code_image, save=False)
        
        super().save(*args, **kwargs)
