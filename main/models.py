from django.db import models
from django.contrib.auth.models import *
import random
from django.utils import timezone
from django.db.models import Sum
from django_countries.fields import CountryField
from datetime import timedelta

class User_OTP(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    otp = models.CharField(max_length=6)
    created = models.DateTimeField(auto_now_add=True)
    
    
    def generate_otp(self):
        self.otp = str(random.randint(100000,999999))
        self.save()
    
    def is_expired(self):
        return timezone.now() > self.created + timezone.timedelta(minutes=60)



class Package(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    tier = models.CharField(max_length=50)
    days_to_complete = models.PositiveIntegerField(help_text="Estimated number of days to complete this package")
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title
    


class Backlink_cart(models.Model):
    package_name = models.ForeignKey(Package,on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    website_url = models.URLField(verbose_name="Website URL", max_length=500)
    keyword_1 = models.CharField(verbose_name="Keyword 1", max_length=255)
    keyword_2 = models.CharField(verbose_name="Keyword 2", max_length=255, blank=True, null=True)
    keyword_3 = models.CharField(verbose_name="Keyword 3", max_length=255, blank=True, null=True)
    keyword_4 = models.CharField(verbose_name="Keyword 4", max_length=255, blank=True, null=True)
    keyword_5 = models.CharField(verbose_name="Keyword 5", max_length=255, blank=True, null=True)
    keyword_6 = models.CharField(verbose_name="Keyword 6", max_length=255, blank=True, null=True)
    keyword_7 = models.CharField(verbose_name="Keyword 7", max_length=255, blank=True, null=True)
    keyword_8 = models.CharField(verbose_name="Keyword 8", max_length=255, blank=True, null=True)
    keyword_9 = models.CharField(verbose_name="Keyword 9", max_length=255, blank=True, null=True)
    keyword_10 = models.CharField(verbose_name="Keyword 10", max_length=255, blank=True, null=True)
    image_url = models.URLField(verbose_name="Image URL", max_length=500, blank=True, null=True)
    youtube_url = models.URLField(verbose_name="YouTube Video URL", max_length=500, blank=True, null=True)
    article_document = models.FileField(
        verbose_name="Upload Article Document",
        upload_to="articles/",
        blank=True,
        null=True,
        help_text="Only .doc or .docx files allowed"
    )
    is_paid = models.BooleanField(default=False)
    created_at = models.DateField(auto_now_add=True)
    
    @property
    def completed_date(self):
        return self.created_at + timedelta(days=self.package_name.days_to_complete)



class TempBacklinkCart(models.Model):
    session_key = models.CharField(max_length=255)
    package_name = models.ForeignKey(Package, on_delete=models.CASCADE)
    website_url = models.URLField(verbose_name="Website URL", max_length=500)
    keyword_1 = models.CharField(verbose_name="Keyword 1", max_length=255)
    keyword_2 = models.CharField(verbose_name="Keyword 2", max_length=255, blank=True, null=True)
    keyword_3 = models.CharField(verbose_name="Keyword 3", max_length=255, blank=True, null=True)
    keyword_4 = models.CharField(verbose_name="Keyword 4", max_length=255, blank=True, null=True)
    keyword_5 = models.CharField(verbose_name="Keyword 5", max_length=255, blank=True, null=True)
    keyword_6 = models.CharField(verbose_name="Keyword 6", max_length=255, blank=True, null=True)
    keyword_7 = models.CharField(verbose_name="Keyword 7", max_length=255, blank=True, null=True)
    keyword_8 = models.CharField(verbose_name="Keyword 8", max_length=255, blank=True, null=True)
    keyword_9 = models.CharField(verbose_name="Keyword 9", max_length=255, blank=True, null=True)
    keyword_10 = models.CharField(verbose_name="Keyword 10", max_length=255, blank=True, null=True)
    image_url = models.URLField(verbose_name="Image URL", max_length=500, blank=True, null=True)
    youtube_url = models.URLField(verbose_name="YouTube Video URL", max_length=500, blank=True, null=True)
    article_document = models.FileField(
        verbose_name="Upload Article Document",
        upload_to="temp_articles/",
        blank=True,
        null=True,
        help_text="Only .doc or .docx files allowed"
    )
    created_at = models.DateField(auto_now_add=True)

    @property
    def completed_date(self):
        return self.created_at + timedelta(days=self.package_name.days_to_complete)

    def __str__(self):
        return f"TempCart - {self.package_name} (Session: {self.session_key})"



class BillingDetail(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='billing_details')
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100, blank=True, null=True)
    company_name = models.CharField(max_length=150, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    city = models.CharField(max_length=100)
    pin_code = models.CharField(max_length=10)
    state = models.CharField(max_length=100)
    country = CountryField()
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.first_name} - {self.city}"



order_status = (('Pending','Pending'),('Completed','Completed'),('Cancelled','Cancelled'))
work_status = (('Payment_pending','Payment_pending'),('onprogress','onprogress'),('Delivered','Delivered'))



class Orders(models.Model):
    order_id = models.CharField(max_length=50, null=True, blank=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    payment_status = models.CharField(max_length=20, choices=order_status, null=True, blank=False, default='Pending')
    total_amount = models.CharField(max_length=50, null=True, blank=False)
    backlink_cart = models.ManyToManyField(Backlink_cart)
    work_status = models.CharField(max_length=30, choices=work_status, null=True, blank=False, default='Payment_pending')
    report_file = models.FileField(upload_to='order_reports/', null=True, blank=True)
    order_date = models.DateField(null=True, blank=True)
    stripe_payment_intent = models.CharField(max_length=255, null=True, blank=True)
    created_at = models.DateField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.order_id:
            last_order = Orders.objects.order_by('-id').first()
            if last_order and last_order.order_id and last_order.order_id.startswith('ORD-'):
                try:
                    last_number = int(last_order.order_id.split('-')[1])
                    next_id = last_number + 1
                except (IndexError, ValueError):
                    next_id = 1
            else:
                next_id = 1
            self.order_id = f"ORD-{str(next_id).zfill(4)}"
        if self.payment_status == 'Completed' and not self.order_date:
            self.order_date = timezone.now().date()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Order #{self.order_id}"


class Invoice(models.Model):
    order = models.ForeignKey(Orders,on_delete=models.CASCADE)
    invoice = models.FileField(upload_to='order_invoice/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)


class CustomerQuery(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='customer_queries')
    subject = models.CharField(max_length=100)
    message = models.TextField(max_length=5000)
    attachment = models.FileField(upload_to='query_attachments/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Query #{self.id} - {self.subject}"
    
    
class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=255, blank=True, null=True)
    message = models.TextField()
    submitted_at = models.DateTimeField(auto_now_add=True)
    is_seen = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.name} ({self.email})"
