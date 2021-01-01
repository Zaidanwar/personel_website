from django.shortcuts import render
from shameem.models import Project,Personal_detail,Description,Profile_photo,Language_skill,Education,Hobbie

# Create your views here.



def index(request):
    name=       Personal_detail.objects.get(heading="Name").description
    nick_name= Personal_detail.objects.get(heading="Nick name").description
    profile=    Personal_detail.objects.get(heading="Profile").description
    roles  =      Personal_detail.objects.get(heading="Roles").description
    country =   Personal_detail.objects.get(heading="Country").description
    dob=        Personal_detail.objects.get(heading="DOB").description
    place =     Personal_detail.objects.get(heading="Place").description
    phone =   Personal_detail.objects.get(heading="Phone").description
    email =   Personal_detail.objects.get(heading="Email").description
    insta =   Personal_detail.objects.get(heading="Instagram").description
    gitlab =   Personal_detail.objects.get(heading="Gitlab").description
    linkedin =   Personal_detail.objects.get(heading="Linkedin").description
    about=Description.objects.get(title="About").description
    contact=Description.objects.get(title="Contact").description
    cover_photo=Profile_photo.objects.get(description="Cover photo").image
    passport_photo = Profile_photo.objects.get(description="profile photo").image
    language=Language_skill.objects.all().order_by('no')
    education = Education.objects.all().order_by('no')
    hobby=Hobbie.objects.all().order_by('no')
    #print(language)
    project1=Project.objects.get(no=1)
    p1_title=project1.title
    p1_description=project1.description
    p1_document=project1.document
    project2 = Project.objects.get(no=2)
    p2_title = project2.title
    p2_description = project2.description
    p2_document = project2.document
    project3 = Project.objects.get(no=3)
    p3_title = project3.title
    p3_description = project3.description
    p3_document = project3.document

    context={
        'name':name,'profile':profile,'roles':roles,'country':country,'dob':dob,'place':place,
        'phone':phone,'email':email,'instagram':insta,'gitlab':gitlab,'linkedin':linkedin,'about':about,
        'p1':p1_title,'p1_description':p1_description,'p1_document':p1_document.url,
        'p2': p2_title, 'p2_description': p2_description, 'p2_document': p2_document.url,
        'p3': p3_title, 'p3_description': p3_description, 'p3_document': p3_document.url,
        'cover':cover_photo,'passport':passport_photo,'language':language,'contact':contact,'nick_name':nick_name,
        'edu':education,'hobby':hobby
    }


    return render(request,"index.html",context)
