from django.shortcuts import render
from django.views import View
from services.models import WeekDay, WeekDayArtclassElem, WeekDayServiceElem


class ScheduleView(View):
    def get(self, request):
        weekdays = WeekDay.objects.all()
        artclass_elems = WeekDayArtclassElem.objects.all()
        service_elems = WeekDayServiceElem.objects.all()

        weekday_elems = []
        for item in artclass_elems:
            weekday_elems.append(item)
        for item in service_elems:
            weekday_elems.append(item)

        weekday_elems = sorted(weekday_elems, key=lambda weekday: int(''.join(ele for ele in weekday.time if ele.isdigit())))

        context = {
            'weekdays': weekdays,
            'weekday_elems': weekday_elems,
        }

        return render(request, 'services/schedule.html', context)
