import pathlib
from django.shortcuts import render
from django.http import HttpResponse

from visits.models import PageVisit

this_dir = pathlib.Path(__file__).resolve().parent

def home_page_view(request, *args, **kwargs):
    qs = PageVisit.objects.all()
    page_qs = PageVisit.objects.filter(path=request.path)
    my_title = "My Page"
    my_context = {
        "page_title": my_title,
        "page_visit_count": page_qs.count(),
        "percent": page_qs.count() * 100.0 / qs.count(),
        "total_visit_count": qs.count()
        } 
    html_template = "home.html"
    PageVisit.objects.create(path=request.path)
    return render(request, html_template, my_context)    

from django.http import HttpResponse

this_dir = pathlib.Path(__file__).resolve().parent

def my_old_home_page_view(request, *args, **kwargs):
    queryset = PageVisit.objects.all()
    my_title = "My Page"
    my_context = {
        "page_title": my_title,
        "queryset": queryset
    }
    html_ = """
<!DOCTYPE html>
<html>
  <head>
    <title>Home</title>
  </head>
  <body>
    <h1>{page_title} rendering?</h1>
  </body>
</html>
""".format(**my_context)
    # html_file_path = this_dir / "home.html"
     # html_ = html_file_path.read_text()
    return HttpResponse(html_)
    