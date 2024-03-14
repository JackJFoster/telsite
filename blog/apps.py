from django.apps import AppConfig
from django.contrib.admin.apps import AdminConfig

class BlogAdminConfig(AdminConfig):
    default_site = 'blog.admin.BlogAdminArea'


    #ask Rob what this error is RuntimeError: 'blog.apps' declares more than one default AppConfig: 'AdminConfig', 'BlogAdminConfig'.
    #on the Setup Custom/Multiple Django Admin Sites - Django Admin Series on Youtube 