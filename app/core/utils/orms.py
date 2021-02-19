from app.models.stock import DailyPrice
from app.models import Company

def get_all_corper():
    codes = []
    for c in Company.objects.values('code'):
        codes.append(c['code'])
    return codes

def get_valid_pricies():
    return DailyPrice.objects.filter(volume__gt=0)