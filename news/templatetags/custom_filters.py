# from django import template

# from django.templatetags.static import static

# from datetime import datetime
# import nepali_datetime

# register = template.Library()

# @register.filter
# def multiply(value, arg):
#     return value * arg

# @register.filter
# def nepali_date(value):
#     if not value:
#         return ""
#     dt = value if isinstance(value, datetime) else value
#     nep_dt = nepali_datetime.date.from_datetime_date(dt.date())
#     nep_digits = str.maketrans("0123456789", "०१२३४५६७८९")
#     month_map = {
#         "Baisakh": "बैशाख", "Jestha": "जेठ", "Asar": "असार", "Shrawan": "साउन",
#         "Bhadra": "भदौ", "Ashwin": "असोज", "Kartik": "कार्तिक", "Mangsir": "मंसिर",
#         "Poush": "पुस", "Magh": "माघ", "Falgun": "फागुन", "Chaitra": "चैत"
#     }
#     day_map = {
#         "Sunday": "आइतबार", "Monday": "सोमबार", "Tuesday": "मंगलबार", 
#         "Wednesday": "बुधबार", "Thursday": "बिहीबार", "Friday": "शुक्रबार", 
#         "Saturday": "शनिबार"
#     }
#     nep_month = month_map.get(nep_dt.strftime("%B"), nep_dt.strftime("%B"))
#     nep_day = day_map.get(nep_dt.strftime("%A"), nep_dt.strftime("%A"))
#     day = str(nep_dt.day).translate(nep_digits)
#     year = str(nep_dt.year).translate(nep_digits)
#     time = dt.strftime("%I:%M").translate(nep_digits)
#     return f"{nep_month} {day}, {year}, {nep_day} {time}"


# @register.filter
# def news_image(news, default_image='images/default.jpg'):
#     return news.news_image.file.url if news.news_image else static(default_image)


from django import template
from django.templatetags.static import static
from datetime import datetime
import nepali_datetime

from news.models import Advertisement

register = template.Library()

@register.filter
def multiply(value, arg):
    return value * arg

@register.filter
def nepali_date(value):
    if not value:
        return ""
    dt = value if isinstance(value, datetime) else value
    nep_dt = nepali_datetime.date.from_datetime_date(dt.date())
    nep_digits = str.maketrans("0123456789", "०१२३४५६७८९")
    month_map = {
        "Baisakh": "बैशाख", "Jestha": "जेठ", "Asar": "असार", "Shrawan": "साउन",
        "Bhadra": "भदौ", "Ashwin": "असोज", "Kartik": "कार्तिक", "Mangsir": "मंसिर",
        "Poush": "पुस", "Magh": "माघ", "Falgun": "फागुन", "Chaitra": "चैत"
    }
    day_map = {
        "Sunday": "आइतबार", "Monday": "सोमबार", "Tuesday": "मंगलबार", 
        "Wednesday": "बुधबार", "Thursday": "बिहीबार", "Friday": "शुक्रबार", 
        "Saturday": "शनिबार"
    }
    nep_month = month_map.get(nep_dt.strftime("%B"), nep_dt.strftime("%B"))
    nep_day = day_map.get(nep_dt.strftime("%A"), nep_dt.strftime("%A"))
    day = str(nep_dt.day).translate(nep_digits)
    year = str(nep_dt.year).translate(nep_digits)
    time = dt.strftime("%I:%M").translate(nep_digits)
    return f"{nep_month} {day}, {year}, {nep_day} {time}"


@register.filter
def current_nepali_date(value=None):
    dt = datetime.now()
    nep_dt = nepali_datetime.date.from_datetime_date(dt.date())
    nep_digits = str.maketrans("0123456789", "०१२३४५६७८९")
    month_map = {
        "Baisakh": "बैशाख", "Jestha": "जेठ", "Asar": "असार", "Shrawan": "साउन",
        "Bhadra": "भदौ", "Ashwin": "असोज", "Kartik": "कार्तिक", "Mangsir": "मंसिर",
        "Poush": "पुस", "Magh": "माघ", "Falgun": "फागुन", "Chaitra": "चैत"
    }
    day_map = {
        "Sunday": "आइतबार", "Monday": "सोमबार", "Tuesday": "मंगलबार", 
        "Wednesday": "बुधबार", "Thursday": "बिहीबार", "Friday": "शुक्रबार", 
        "Saturday": "शनिबार"
    }
    nep_month = month_map.get(nep_dt.strftime("%B"), nep_dt.strftime("%B"))
    nep_day = day_map.get(nep_dt.strftime("%A"), nep_dt.strftime("%A"))
    day = str(nep_dt.day).translate(nep_digits)
    year = str(nep_dt.year).translate(nep_digits)
    return f"{day} {nep_month} {year}, {nep_day}"


@register.filter
def news_image(news, default_image='images/default.jpg'):
    return news.news_image.file.url if news.news_image else static(default_image)

@register.filter
def ad_image(obj):
    image_field = getattr(obj, 'image', None)
    return image_field.file.url if image_field else None

@register.simple_tag
def get_ads_by_position(position):
    return Advertisement.objects.filter(position=position).all()

