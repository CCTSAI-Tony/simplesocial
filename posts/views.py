from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.http import Http404
from django.views import generic

# pip install django-braces
from braces.views import SelectRelatedMixin

from . import forms
from . import models

from django.contrib.auth import get_user_model
from groups.models import Group
User = get_user_model() #access the specific user item and get the specific usermodel,


class PostList(SelectRelatedMixin, generic.ListView):
    model = models.Post
    select_related = ("user", "group")#basicly, the ForeignKey of the post,同時連結兩個數據庫,
    # 在post_list.html 的 _post.html 就需要連結這兩個數據庫"user", "group"
    # queryset=models.Post.objects.all() 這有跟沒有一樣 預設就是全部
    def get_context_data(self, **kwargs):

        context = super(PostList, self).get_context_data(**kwargs)
        context['user_groups'] = Group.objects.filter(members__in=[self.request.user]) #members__in 在成員名單中
        context['other_groups'] = Group.objects.exclude(members__in=[self.request.user])

        return context #產生template tag 用在html



class UserPosts(generic.ListView):#check the person posts not select but point to 與PostList不一樣
    model = models.Post
    template_name = "posts/user_post_list.html"

    def get_queryset(self):#cause we use post pk, so we need to use get_queryset to find the right post via username
        try:
            self.post_user = User.objects.prefetch_related("posts").get(   #User: orm(object ralational model)
                username__iexact=self.kwargs.get("username") #get specific user
            )
        except User.DoesNotExist:
            raise Http404
        else:
            return self.post_user.posts.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs) #assign to a function
        context["post_user"] = self.post_user #self.post_user from above get_queryset
        return context #很少見的技巧 學起來,


class PostDetail(SelectRelatedMixin, generic.DetailView):
    model = models.Post
    select_related = ("user", "group")
    # https://docs.djangoproject.com/en/3.0/ref/models/querysets/
    def get_queryset(self): #get the queryset of the actual post
        queryset = super().get_queryset()
        return queryset.filter(
            user__username__iexact=self.kwargs.get("username")#just like the dic.get()
        )
      # user__username__iexact: customize the get_query call

class CreatePost(LoginRequiredMixin, SelectRelatedMixin, generic.CreateView):
    # form_class = forms.PostForm
    fields = ('message','group')
    model = models.Post

    # def get_form_kwargs(self):
    #     kwargs = super().get_form_kwargs()
    #     kwargs.update({"user": self.request.user})
    #     return kwargs

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return super().form_valid(form)


class DeletePost(LoginRequiredMixin, SelectRelatedMixin, generic.DeleteView):
    model = models.Post
    select_related = ("user", "group")
    success_url = reverse_lazy("posts:all")

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(user_id=self.request.user.id)

    def delete(self, *args, **kwargs): #這有點難懂,多看documentation
        messages.success(self.request, "Post Deleted") #to say something the post is deleted
        return super().delete(*args, **kwargs)
