from django.shortcuts import HttpResponse, render, \
    get_object_or_404, HttpResponseRedirect

from .models import Post
from django.contrib.auth.decorators import login_required
from .forms import PythonistForm, CommentForm

from django.views import View
from django.views.generic import ListView, TemplateView


def send_basic_info(request):
    cd = False
    if request.method == 'GET':
        form = PythonistForm()
    else:
        form = PythonistForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
    return render(request, 'news/basic_info.html', {'form': form,
                                                    'data': cd})


class PostListView(ListView):
    queryset = Post.objects.filter(status='published')
    context_object_name = 'posts'
    paginate_by = 4
    template_name = 'news/post/list.html'


class HomePageView(TemplateView):
    template_name = 'news/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['post_number'] = Post.objects.filter(
            status='published').count()
        if self.request.user.is_authenticated:
            context['info'] = (self.request.user,
                               Post.objects.filter(
                                   author=self.request.user))
        return context


# @permission_required itp
class AuthorPage(TemplateView):
    template_name = 'news/author.html'


class CatView(View):
    http_method_names = ['delete', 'get']

    def get(self, request, *args, **kwargs):
        arguments = '<p>arguments</p>' + str(*args) + '<br><br>'
        key_args = '<p> key word arguments: </p>' + str(kwargs.items()) \
                   + '<br><br>'
        methods = '<p> request insides </p>' + str(dir(request)) + '<br><br>'
        info = '<p> info </p>' + str(request.body) + '<p> header </p>' + \
               str(request.headers)
        final = arguments + key_args + methods + info
        return HttpResponse(final)

    def http_method_not_allowed(self, request, *args, **kwargs):
        return HttpResponse('METHOD NOT ALLOWED')


#
# def home_page(request):
#     return render(request, 'news/base.html')
#
#
# def post_list(request):
#     posts = Post.objects.filter(status__exact='published')
#     paginator = Paginator(posts, 3)
#     page = request.GET.get('page')
#     try:
#         posts = paginator.page(page)
#     except PageNotAnInteger:
#         posts = paginator.page(1)
#     except EmptyPage:
#         posts = paginator.page(paginator.num_pages)
#     return render(request, 'news/post/list.html', {'page': page,
#                                                    'posts': posts})

@login_required
def post_detail(request, year, month, day, slug):
    post = get_object_or_404(Post, slug=slug, status='published',
                             published__year=year,
                             published__month=month,
                             published__day=day)
    comments = post.comments.filter(active=True)
    form = CommentForm()
    comment = None
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return HttpResponseRedirect(request.path)
    return render(request, 'news/post/detail.html', {'post': post,
                                                     'form': form,
                                                     'comment': comment})


def author(request):
    return render(request, 'news/author.html')
