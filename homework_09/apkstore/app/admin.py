from django.contrib import admin

from app.models import App, AppKind, AppAgeLimit

admin.site.register(App)
admin.site.register(AppKind)
admin.site.register(AppAgeLimit)
