from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import ListView
from .models import Post

# Представления на основе классов
# class MyPaginator(Paginator):
#     def validate_number(self, number):
#         try:
#             return super().validate_number(number)
#         except EmptyPage:
#             if int(number) > 1:
#                 # return the last page
#                 return self.num_pages
#             elif int(number) < 1:
#                 # return the first page
#                 return 1
#             else:
#                 raise
#
#
# class PostListView(ListView):
#     queryset = Post.published.all()
#     context_object_name = "posts"
#     paginate_by = 2
#     template_name = "blog/post/list.html"
#     paginator_class = MyPaginator


# Представления на основе функций
def posts_list(request):
    post_list = Post.published.all()
    paginator = Paginator(post_list, 2)
    page_number = request.GET.get("page", 1)
    try:
        posts = paginator.page(page_number)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    return render(request, "blog/post/list.html", {"posts": posts})

def post_detail(request, year, month, day, post):
    post = get_object_or_404(Post,
                             status=Post.Status.PUBLISHED,
                             slug=post,
                             publish__year=year,
                             publish__month=month,
                             publish__day=day,
                             )
    return render(request, "blog/post/detail.html", {"post": post})


# slug = models.SlugField(max_length=250, unique=True)

# def post_detail(request, id):
#     post = get_object_or_404(Post, id=id, status=Post.Status.PUBLISHED)
#     return render(request, 'blog/post/detail.html', {'post': post})
