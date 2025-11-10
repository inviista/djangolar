import django
import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
django.setup()

from django.db.models import Q, Count, Avg, Max, Min, Sum, Case, When, Value, BooleanField, CharField, F, ExpressionWrapper, DurationField
from django.db.models.functions import ExtractYear, Now, Concat
from users.models import CustomUser
from datetime import timedelta
from django.utils import timezone

seven_days_ago = timezone.now() - timedelta(days=7)
now = timezone.now()
start_of_year = now.replace(month=1, day=1, hour=0, minute=0, second=0, microsecond=0)
overall_avg = CustomUser.objects.aggregate(avg=Avg('salary'))['avg'] or 0

qs_2_1 = CustomUser.objects.filter(is_active=True)
qs_2_2 = CustomUser.objects.filter(email__iendswith='@gmail.com')
qs_2_3 = CustomUser.objects.filter(city__iexact='Almaty')
qs_2_4 = CustomUser.objects.exclude(city__iexact='Almaty')
qs_2_5 = CustomUser.objects.filter(salary__gt=500000)
qs_2_6 = CustomUser.objects.filter(department='IT', country__iexact='Kazakhstan')
qs_2_7 = CustomUser.objects.filter(birth_date__isnull=True)
qs_2_8 = CustomUser.objects.filter(first_name__istartswith='A')
qs_2_9 = CustomUser.objects.count()
qs_2_10 = CustomUser.objects.order_by('-date_joined')[:20]
qs_2_11 = CustomUser.objects.order_by().values_list('city', flat=True).distinct()
qs_2_12 = CustomUser.objects.filter(department='Sales').count()
qs_2_13 = CustomUser.objects.filter(last_login__gte=seven_days_ago)
qs_2_14 = CustomUser.objects.filter(Q(first_name__icontains='bek') | Q(last_name__icontains='bek'))
qs_2_15 = CustomUser.objects.filter(salary__gte=300000, salary__lte=700000)
qs_2_16 = CustomUser.objects.filter(department__in=['IT','HR','Finance'])
qs_2_17 = CustomUser.objects.values('department').annotate(count=Count('id'))
qs_2_18 = CustomUser.objects.values('department').annotate(count=Count('id')).order_by('-count')
qs_2_19 = CustomUser.objects.values('city').annotate(count=Count('id')).order_by('-count')[:5]
qs_2_20 = CustomUser.objects.filter(last_login__isnull=True)
qs_2_21 = CustomUser.objects.aggregate(avg=Avg('salary'))['avg']
qs_2_22 = CustomUser.objects.aggregate(max_salary=Max('salary'), min_salary=Min('salary'))
qs_2_23 = CustomUser.objects.filter(phone__contains='+7')
qs_2_24 = CustomUser.objects.annotate(full_name=Concat(F('first_name'), Value(' '), F('last_name'), output_field=CharField()))
qs_2_25 = CustomUser.objects.annotate(birth_year=ExtractYear('birth_date')).order_by('birth_year')
qs_2_26 = CustomUser.objects.filter(birth_date__month=5)
qs_2_27 = CustomUser.objects.filter(role='manager', salary__gt=400000)
qs_2_28 = CustomUser.objects.filter(Q(role='employee') | Q(department='HR'))
qs_2_29 = CustomUser.objects.filter(is_active=True).values('city').annotate(active_count=Count('id'))
qs_2_30 = CustomUser.objects.order_by('date_joined')[:10]
qs_2_31 = CustomUser.objects.filter(city__istartswith='A', salary__gt=300000)
qs_2_32 = CustomUser.objects.filter(Q(department__isnull=True) | Q(department=''))
qs_2_33 = CustomUser.objects.values('country').annotate(count=Count('id'), avg_salary=Avg('salary'))
qs_2_34 = CustomUser.objects.filter(is_staff=True).order_by('-last_login')
qs_2_35 = CustomUser.objects.exclude(email__icontains='example.com')
qs_2_36 = CustomUser.objects.filter(salary__gt=overall_avg)
qs_2_37 = CustomUser.objects.values('email').annotate(cnt=Count('id')).filter(cnt__gt=1)
qs_2_38 = CustomUser.objects.annotate(
    salary_level=Case(
        When(salary__lt=300000, then=Value('low')),
        When(salary__gte=300000, salary__lte=700000, then=Value('medium')),
        When(salary__gt=700000, then=Value('high')),
        default=Value('unknown'),
        output_field=CharField()
    )
).order_by('salary_level')
qs_2_39 = CustomUser.objects.filter(date_joined__gte=start_of_year)
qs_2_40 = CustomUser.objects.values('department').annotate(total_payroll=Sum('salary'))
qs_2_41 = CustomUser.objects.filter(department='IT', last_login__isnull=True)
qs_2_42 = CustomUser.objects.filter(country__iexact='Kazakhstan').filter(Q(city__isnull=True) | Q(city=''))
qs_2_43 = CustomUser.objects.filter(birth_date__lt='1990-01-01', salary__isnull=False)
qs_2_44 = CustomUser.objects.annotate(days_since_joined=ExpressionWrapper(Now() - F('date_joined'), output_field=DurationField()))
qs_2_45 = CustomUser.objects.filter(department='Sales', email__iendswith='@gmail.com', salary__gt=350000)
qs_2_46 = CustomUser.objects.order_by('country', '-salary')
qs_2_47 = CustomUser.objects.values('role').annotate(cnt=Count('id')).filter(cnt__gt=100)
qs_2_48 = CustomUser.objects.filter(last_login__lt=F('date_joined'))
qs_2_49 = CustomUser.objects.annotate(
    is_senior=Case(
        When(birth_date__lt='1985-01-01', then=Value(True)),
        default=Value(False),
        output_field=BooleanField()
    )
)
qs_2_50 = CustomUser.objects.values('department').annotate(
    avg_salary=Avg('salary'),
    cnt=Count('id')
).filter(cnt__gte=20).order_by('-avg_salary')