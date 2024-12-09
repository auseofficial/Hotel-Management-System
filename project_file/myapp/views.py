from django.shortcuts import render
from .models import Restaurant
from django.core.paginator import Paginator


def restaurant_list(request):
    # Get all restaurants ordered by name
    restaurant_list = Restaurant.objects.all().order_by('name')
    paginator = Paginator(restaurant_list, 5)  # Display 5 restaurants per page

    # Get the current page number from the URL
    page_number = request.GET.get('page')

    # Fetch the correct page data
    try:
        page_obj = paginator.get_page(page_number)
    except:
        page_obj = paginator.page(1)  # Default to the first page if the page is out of range

    # Prepare pagination information
    page_range = paginator.page_range
    show_all = request.GET.get('show_all')

    # Determine whether to show all items or paginate
    if show_all:
        page_obj = paginator.page(paginator.num_pages)
        page_range = [1]  # Only show 'Show all' link

    context = {
        'page_obj': page_obj,
        'page_range': page_range,
        'show_all': show_all,
    }

    return render(request, 'myapp/restaurant_list.html', context)
