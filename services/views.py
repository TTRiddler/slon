from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from services.models import WeekDay, WeekDayArtclassElem, WeekDayServiceElem, Specialist, Artclass, Service, Category


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


class StaffView(View):
    def get(self, request):
        specialists = Specialist.objects.all()

        context = {
            'specialists': specialists,
        }

        return render(request, 'services/staff.html', context)


class CategoryView(View):
    def get(self, request, service_type, category_slug):
        category = get_object_or_404(Category, slug=category_slug)

        if service_type == 'artclass':
            services = Artclass.objects.filter(categories__in=[category], is_active=True)
            service_type_name = 'Кружки'
        elif service_type == 'service':
            services = Service.objects.filter(categories__in=[category], is_active=True)
            service_type_name = 'Услуги'
        else:
            return redirect('/')

        context = {
            'category': category,
            'services': services,
            'service_type': service_type,
            'service_type_name': service_type_name,
        }

        return render(request, 'services/category.html', context)


class CategoriesView(View):
    def get(self, request, service_type):
        categories = Category.objects.all()
        if service_type == 'service':
            service_type_name = 'Услуги'
        elif service_type == 'artclass':
            service_type_name = 'Кружки'
        else:
            return redirect('/')

        context = {
            'categories': categories,
            'service_type': service_type,
            'service_type_name': service_type_name,
        }

        return render(request, 'services/categories.html', context)


class ServiceView(View):
    def get(self, request, service_type, service_slug):

        if service_type == 'artclass':
            service = get_object_or_404(Artclass, slug=service_slug)
            service_type_name = 'Кружки'
        elif service_type == 'service':
            service = get_object_or_404(Service, slug=service_slug)
            service_type_name = 'Услуги'
        else:
            return redirect('/')

        context = {
            'service': service,
            'service_type': service_type,
            'service_type_name': service_type_name,
        }

        return render(request, 'services/service.html', context)


