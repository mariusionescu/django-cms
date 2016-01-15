# django-cms
A very simple CMS.

INSTALL
=======

    # Using pip
    pip install git+git://github.com/mariusionescu/django-cms.git#egg=django-cms

    # requirements.txt
    git+git://github.com/mariusionescu/django-cms.git#egg=django-cms


CONFIGURATION
=============

    # urls.py:
    
    from django.conf.urls import include, url, patterns
    from django.contrib import admin
    admin.site.site_header = 'CMS Admin'

    urlpatterns = [
        url(r'^admin/', include(admin.site.urls)),
        url(r'blog/', include('blog.urls')),
        url(r'', include('cms.urls')),
    ]
    
    # settings.py:    
    INSTALLED_APPS = (
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.staticfiles',
        'cms',
        'blog'
    )

