from django.shortcuts import render
from .models import Skill
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.http import HttpResponseRedirect


def home(request):
    return render(request, 'home.html')


def user_detail(request, user_id):
    user = User.objects.get(id=user_id)
    return render(request, 'users/detail.html', {'user': user})

# def users(request):
#     return render(request, 'users/index.html', {'users': users})


class SkillCreate(CreateView):
    model = Skill
    fields = '__all__'
    success_url = '/home'


class SkillUpdate(UpdateView):
    model = Skill
    fields = ['description', 'skill_level']

    def form_valid(self, form)
    self.object = form.save(commit=False)
    self.object.save()
    return HttpResponseRedirect('/home/' + str(self.object.pk))


class CatDelete(DeleteView):
    model = Skill
    success_url = '/home'
