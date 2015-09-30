from django.http import Http404
from django.shortcuts import render, redirect
from django.views.generic import View
from cms.models import Page
from django.conf import settings

if 'blog' in settings.INSTALLED_APPS:
    from blog.models import Post
    BLOG = True
else:
    BLOG = False


class CMSView(View):
    def get(self, request):
        try:
            if request.user.is_authenticated():
                page = Page.objects.get(path=request.path)
            else:
                page = Page.objects.get(path=request.path, published=True)
        except Page.DoesNotExist:
            if request.path == '/404/':
                raise Http404
            else:
                return redirect('/404/')

        context = {placeholder.name: placeholder.content for placeholder in page.placeholder_set.all()}
        context['path'] = request.path

        if BLOG and request.path in ('/', '/home/'):
            if request.user.is_authenticated():
                recent_posts = Post.objects.all().order_by('-date_created')[:4]
            else:
                recent_posts = Post.objects.filter(published=True).order_by('-date_created')[:4]
            context['recent_posts'] = recent_posts
        return render(request, page.template, context)



