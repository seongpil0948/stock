from .common import *
from django.db import models


class Company(DateModel, BaseActiveModel, BaseNameModel):
    code = models.CharField(
        help_text='회사 종목 코드',
        primary_key=True,
        unique=True,
        max_length=50
    )
    industry_code = models.CharField(
        help_text='업종코드',
        max_length=50,
        blank=True,
        null=True,        
    )

    def __str__(self):
        return f"{self.name_ko}-{self.code}"


class DailyPrice(OHLC):
    # 다음에 외래키 만들때는 related_name 설정 반드시 해주자 지금 접근하려면
    # code_id 로 접근해야만 한다. ....shit
    code = models.ForeignKey(
        Company,
        on_delete=models.DO_NOTHING,
        help_text='회사 종목 코드',
    )    
    
    date = models.CharField(
        help_text='날짜별 주식시세',
        max_length=50
    )

    volume = models.IntegerField(
        help_text='거래량', 
        blank=False)
    
    class Meta:
        # FYI(참고로) it throws a django.db.utils.IntegrityError if you try to add a duplicate
        unique_together = ('code', 'date',)

    def __str__(self):
        return f"{self.date}-{self.code_id}"
