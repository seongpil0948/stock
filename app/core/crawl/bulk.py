from app.models.stock import Company, DailyPrice
import requests
from datetime import datetime


def create_companies(page_size: int=100000):
    res = requests.get(f"https://m.stock.naver.com/api/json/sise/siseListJson.nhn?menu=market_sum&sosok=0&pageSize={page_size}")
    datas = res.json()['result']['itemList']
    obj_list = [Company(code=i['cd'], name_ko=i['nm']) for i in datas[3:]]
    Company.objects.bulk_create(obj_list)

def create_daily_price(page_size: int=100000):
    dps = []
    for code in Company.objects.values_list('code', flat=True):
        company = Company.objects.get(code=code)
        res = requests.get(f"https://m.stock.naver.com/api/item/getPriceDayList.nhn?code={code}&pageSize={page_size}")
        for data in res.json()['result']['list']:
            dt = data['dt'] 
            dps.append(DailyPrice(
                code=company,
                volume=data['aq'],
                date=datetime(*map(int, [dt[:4], dt[4:6], dt[6:]])),
                open_price=data['ov'],
                high_price=data['hv'],
                low_price=data['lv'],
                close_price=data['ncv'],
            ))
    DailyPrice.objects.bulk_create(dps)