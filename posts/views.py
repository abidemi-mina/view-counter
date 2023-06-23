from django.shortcuts import render


from django.views.generic.list import ListView
from hitcount.views import HitCountDetailView
from .models import Post

class PostListView(ListView):
    model = Post
    context_object_name = 'face'
    template_name = 'post-list.html'


class PostDetailView(HitCountDetailView):
    model = Post
    template_name = 'post-detail.html'
    context_object_name = 'book'
    slug_field = 'slug'
    # set to True to count the hit
    count_hit = True

    def get_object(self):
        obj = super().get_object()
        return obj

    def get_context_data(self, **kwargs):
        context = super(PostDetailView, self).get_context_data(**kwargs)
        context.update({
        'popular_posts': Post.objects.order_by('-hit_count_generic__hits')[:3],
        })
        return context
