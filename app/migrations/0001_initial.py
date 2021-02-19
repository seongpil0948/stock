# Generated by Django 3.1.6 on 2021-02-19 17:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True, help_text='데이터가 생성된 날짜입니다.', verbose_name='생성 일시')),
                ('updated_at', models.DateTimeField(auto_now=True, help_text='데이터가 수정된 날짜입니다.', verbose_name='수정 일시')),
                ('is_active', models.BooleanField(db_index=True, default=True, help_text='활성화할지 여부를 결정합니다.', verbose_name='활성화 여부')),
                ('name_en', models.CharField(blank=True, help_text='고유 영어 명칭을 나타냅니다.', max_length=40, null=True, verbose_name='영어 명칭')),
                ('name_ko', models.CharField(blank=True, help_text='고유 한국어 명칭을 나타냅니다.', max_length=40, null=True, verbose_name='한국어 명칭')),
                ('code', models.CharField(help_text='회사 종목 코드', max_length=50, primary_key=True, serialize=False, unique=True)),
                ('industry_code', models.CharField(help_text='업종코드', max_length=50)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='DailyPrice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('open_price', models.IntegerField()),
                ('high_price', models.IntegerField()),
                ('low_price', models.IntegerField()),
                ('close_price', models.IntegerField()),
                ('date', models.CharField(help_text='날짜별 주식시세', max_length=50)),
                ('volume', models.IntegerField(help_text='거래량')),
                ('code', models.ForeignKey(help_text='회사 종목 코드', on_delete=django.db.models.deletion.DO_NOTHING, to='app.company')),
            ],
            options={
                'unique_together': {('code', 'date')},
            },
        ),
    ]
