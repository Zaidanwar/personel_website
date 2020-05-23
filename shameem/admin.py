from django.contrib import admin

# Register your models here.
from shameem.models import Personal_detail, Description, Profile_photo,Project,Language_skill,Education,Hobbie

admin.site.register(Personal_detail)
admin.site.register(Description)
admin.site.register(Profile_photo)
admin.site.register(Project)
admin.site.register(Language_skill)
admin.site.register(Education)
admin.site.register(Hobbie)

