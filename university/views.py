from django.db.models import Avg
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.views.generic import DetailView, ListView

from .models import Student, University


@method_decorator(cache_page(10), name='dispatch')
class StudentList(ListView):
    model = Student
    paginate_by = 100
    template_name = 'student_list.html'
    context_object_name = 'students'
    queryset = Student.objects.select_related('university')


class StudentDetail(DetailView):
    model = Student
    template_name = 'student_detail.html'
    context_object_name = 'student'


@method_decorator(cache_page(10), name='dispatch')
class UniversityList(ListView):
    model = University
    paginate_by = 100
    template_name = 'university_list.html'
    context_object_name = 'universities'
    queryset = University.objects.all().prefetch_related('student_set')


class UniversityDetail(DetailView):
    model = University
    template_name = 'university_detail.html'
    context_object_name = 'university'

    def get_context_data(self, **kwargs):
        context = super(UniversityDetail, self).get_context_data(**kwargs)
        context['avg_student_in_uni'] = University.objects.filter(pk=self.kwargs.get('pk')).aggregate(
            student_avg=Avg('student'),
        )
        return context
