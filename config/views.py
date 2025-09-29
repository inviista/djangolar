from django.shortcuts import render
import pytz
from django.utils import timezone

# 1. Welcome page
def welcome(request):
    return render(request, "welcome.html")

# 2. Users list
def users_list(request):
    users = [
        {"full_name": "Aldiyar Sadykov", "age": 21},
        {"full_name": "Alexey Mihaylov", "age": 30},
        {"full_name": "Yuji Nishida", "age": 22},
    ]
    return render(request, "users.html", {"users": users})

# 3. City time
def city_time(request):
    cities = {
        'Almaty': 'Asia/Almaty',
        'Calgary': 'America/Edmonton',
        'Moscow': 'Europe/Moscow',
        'UTC': 'UTC'
    }

    selected_city = request.GET.get('city', 'Almaty')
    timezone_str = cities.get(selected_city, 'Asia/Almaty')

    try:
        tz = pytz.timezone(timezone_str)
        current_time = timezone.now().astimezone(tz)
        formatted_time = current_time.strftime('%H:%M')
    except Exception as e:
        formatted_time = f"Error: {str(e)}"

    return render(request, 'city_time.html', {
        'cities': cities.keys(),
        'selected_city': selected_city,
        'current_time': formatted_time
    })


# 4. Counter
counter_value = 0
def counter(request):
    global counter_value
    if "inc" in request.GET:
        counter_value += 1
    elif "reset" in request.GET:
        counter_value = 0
    return render(request, "counter.html", {"counter": counter_value})
