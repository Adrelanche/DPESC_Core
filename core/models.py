from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class BasePublishModel(models.Model):
    STATUS_CHOICES = [
        ("published", "Publicado"),
        ("not_published", "Não publicado"),
    ]

    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="not_published")
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    published_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        if self.status == "published" and self.published_at is None:
            self.published_at = timezone.now()
        elif self.status != "published":
            self.published_at = None
        super().save(*args, **kwargs)

class FAQ(BasePublishModel):
    question = models.TextField(blank=True, null=True)
    answer = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.question
    
class Core(BasePublishModel):
    core_name = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.core_name
    
class TypeOfService(BasePublishModel):
    service_name = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.service_name

class AreaOfDuty(BasePublishModel):
    dutie_name = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.dutie_name   
    
class Unit(BasePublishModel):
    STATE_CHOICES =[
        ("acre", "Acre"),
        ("alagoas", "Alagoas"),
        ("amapa", "Amapá"),
        ("amazonas", "Amazonas"),
        ("bahia", "Bahia"),
        ("ceara", "Ceará"),
        ("distrito_federal", "Distrito Federal"),
        ("espirito_santo", "Espírito Santo"),
        ("goias", "Goiás"),
        ("maranhao", "Maranhão"),
        ("mato_grosso", "Mato Grosso"),
        ("mato_grosso_do_sul", "Mato Grosso do Sul"),
        ("minas_gerais", "Minas Gerais"),
        ("para", "Pará"),
        ("paraiba", "Paraíba"),
        ("parana", "Paraná"),
        ("pernambuco", "Pernambuco"),
        ("piaui", "Piauí"),
        ("rio_de_janeiro", "Rio de Janeiro"),
        ("rio_grande_do_norte", "Rio Grande do Norte"),
        ("rio_grande_do_sul", "Rio Grande do Sul"),
        ("rondonia", "Rondônia"),
        ("roraima", "Roraima"),
        ("santa_catarina", "Santa Catarina"),
        ("sao_paulo", "São Paulo"),
        ("sergipe", "Sergipe"),
        ("tocantins", "Tocantins"),
    ]

    unit_name = models.CharField(max_length=255, blank=True, null=True)
    core = models.ForeignKey(Core, on_delete=models.CASCADE, related_name="units")
    url = models.URLField(blank=True, null=True)
    observation = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    name_dp = models.CharField(max_length=255, blank=True, null=True)
    email_dp = models.EmailField(blank=True, null=True)
    
    cep = models.CharField(max_length=10, blank=True, null=True)
    street = models.CharField(max_length=255, blank=True, null=True)
    district = models.CharField(max_length=255, blank=True, null=True)
    city = models.CharField(max_length=255, blank=True, null=True)
    state = models.CharField(max_length=255, choices=STATE_CHOICES, default="santa_catarina", blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    is_whatsapp = models.BooleanField(default=False)

    department = models.CharField(max_length=255, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)

    types_of_service = models.ForeignKey(TypeOfService, on_delete=models.SET_NULL, null=True)
    schedules = models.TextField(blank=True, null=True)

    area_of_duty = models.ForeignKey(AreaOfDuty, on_delete=models.SET_NULL, null=True)
    link_schedule_service = models.URLField(blank=True, null=True)

    is_principal = models.BooleanField(default=False)

    def __str__(self):
        return self.unit_name 
    
class Popup(BasePublishModel):
    title = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    start_date =  models.DateTimeField(blank=True, null=True)
    end_date = models.DateTimeField(blank=True, null=True)
    url = models.URLField(blank=True, null=True)
    image = models.ImageField(upload_to='popups/', blank=True, null=True)
    click = models.PositiveIntegerField(default=0)
    visualization = models.PositiveIntegerField(default=0)

    def increment_click(self):
        self.click += 1
        self.save(update_fields=['click'])

    def increment_visualization(self):
        self.visualization += 1
        self.save(update_fields=['visualization'])


    def __str__(self):
        return self.title
    
class Tag(BasePublishModel):
    name_tag = models.CharField(max_length=255, blank=True, null=True)
    times_used = models.PositiveIntegerField(default=0)

    def increment_times_used(self):
        self.times_used += 1
        self.save(update_fields=['times_used'])

    def __str__(self):
        return self.name_tag
    
class AreaOfActivity(BasePublishModel):
    title = models.CharField(max_length=255, blank=True, null=False)
    description = models.TextField(blank=True, null=True)
    url = models.URLField(blank=True, null=True)
    image = models.ImageField(upload_to='area_of_activity/', blank=True, null=True)

    def __str__(self):
        return self.title
    
class WebsiteInformations(BasePublishModel):
    title = models.CharField(max_length=255, blank=True, null=True, default="Defensoria Pública do Estado de Santa Catarina")
    slogan = models.CharField(max_length=400, blank=True, null=True)
    key_words = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.title
    
class SocialMedia(BasePublishModel):
    SOCIAL_MEDIA_ICONS = [
        ("facebook", "Facebook"),
        ("github", "Github"),
        ("gitlab", "Gitlab"),
        ("instagram", "Instagram"),
        ("linkedin", "Linkedin"),
        ("podcast", "Podcast"),
        ("radio_tower", "Rádio"),
        ("slack", "Slack"),
        ("trello", "Trello"),
        ("twitch", "Twitch"),
        ("twitter", "Twitter"),
        ("youtube", "Youtube"),
    ]

    name = models.CharField(max_length=255, blank=True, null=True)
    url = models.URLField(blank=True, null=True)
    icon = models.CharField(max_length=100, choices=SOCIAL_MEDIA_ICONS, blank=True, null=True)

    def __str__(self):
        return self.name
    
class EmailWebsite(BasePublishModel):
    LOCATION_CHOICES = [
        ("email_website", "Email do Website"),
        ("comentarios", "Comentários"),
        ("faq", "FAQ"),
        ("relato_de_erros", "Relato de Erros"),

    ]
    location = models.CharField(max_length=255, choices=LOCATION_CHOICES, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)

    def __str__(self):
        return self.location