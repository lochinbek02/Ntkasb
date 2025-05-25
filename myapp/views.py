from rest_framework.generics import ListAPIView,CreateAPIView,RetrieveAPIView
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from .models import *
from .serializers import *
from django.views.generic import TemplateView,ListView,CreateView,DetailView
from .forms import StudentForm


class HomeView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['news_list'] = News.objects.order_by('-created_at')[:6]  # So‘nggi 6 ta yangilik
        return context

class YunalishlarViewSet(ListAPIView):
    queryset = Yunalishlar.objects.all()
    serializer_class = YunalishlarSerializer

class ReceptionTemplateView(TemplateView):
    template_name = 'reception.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Reception modelidan oxirgi obyektni olamiz
        context['reception'] = Reception.objects.last()
        return context
class TeacherListView(ListView):
    model = Teacher
    template_name = 'teachers.html'
    context_object_name = 'teachers'

class StudentRegisterView(CreateView):
    model = Student
    form_class = StudentForm
    template_name = 'student_register.html'
    success_url = '/api/' 
class YunalishlarListView(ListView):
    model = Yunalishlar
    template_name = 'courses.html'
    context_object_name = 'yunalishlar'

class TeacherDetailView(DetailView):
    model = Teacher
    template_name = 'teacher_detail.html'
    context_object_name = 'teacher'

class YunalishDetailView(DetailView):
    model = Yunalishlar
    template_name = 'courses_detail.html'
    context_object_name = 'yunalish'

class NewsDetailView(DetailView):
    model = News
    template_name = 'news_detail.html'
    context_object_name = 'news'