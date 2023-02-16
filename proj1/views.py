from django.shortcuts import render,redirect
from django.contrib import messages
import pathlib
from django.http import FileResponse
from django.utils.datastructures import MultiValueDictKeyError
from markdown2 import markdown
from jinja2 import Environment,FileSystemLoader
from json import load
import os.path

from io import StringIO
from django.http import HttpResponse
import shutil
from zipfile import ZipFile, Path







# this function modifies the Mark Down Files
def modifyArticleMarkDownFile(y):
    with open("proj1/markDownFiles/article.md", "w") as f:
      #f.write("new line\n")
      f.write(y)
def modifyAboutMarkDown(y):
    with open("proj1/markDownFiles/about.md", "w") as f:
      #f.write("new line\n")
      f.write(y)
def modifyArticleDescription(y):
    with open("proj1/markDownFiles/articleDescription.md", "w") as f:
      #f.write("new line\n")
      f.write(y)

# Create your views here.

def index(request):
    webname=''
    description=''
    email=''
    phone=''
    address=''
    website=''
    articleDescription=''
    articlename=''
    companyVision=''

    if request.method == 'POST':
        webname=request.POST['webname']
        email=request.POST['email']
        phone=request.POST['phone']
        address=request.POST['address']
        website=request.POST['website']
        description=request.POST['desc1']
        try:
         articlename=request.POST['articlename']
         articleDescription=request.POST['articleDescription']
         companyVision=request.POST['companyVision']
         
        except MultiValueDictKeyError:
         articlename = False
         articleDescription = False
         companyVision=False


        
    modifyArticleMarkDownFile(description)
    modifyArticleDescription(articleDescription)
    modifyAboutMarkDown(companyVision)
    
    template_env=Environment(loader=FileSystemLoader(searchpath='proj1/LayoutTemplate'))
    template=template_env.get_template('index_layout.html')

    with open('proj1/markDownFiles/article.md') as markdown_file:
        article=markdown(
        markdown_file.read(),
        extras=['fenced-code-blocks','code-friendly'])

    with open('proj1/markDownFiles/articleDescription.md') as markdown_file:
        articleDescription1=markdown(
        markdown_file.read(),
        extras=['fenced-code-blocks','code-friendly'])

    with open('proj1/markDownFiles/about.md') as markdown_file:
        aboutVision=markdown(
        markdown_file.read(),
        extras=['fenced-code-blocks','code-friendly'])

    with open('proj1/configFiles/config.json') as config_file:
        config=load(config_file)
        config['title']=webname
        config['email']=email
        config['phoneNumber']=phone
        config['location']=address
        config['webLink']=website
        config['articleHeadline']=articlename

    with open('proj1/outPutFiles/index.html','w') as output_file:
        output_file.write(
        template.render(
            title=config['title'],
            article=article,
            phone=config['phoneNumber'],
            location=config['location'],
        )
    )
    template=template_env.get_template('article_layout.html')
    with open('proj1/outPutFiles/article.html','w') as output_file:
        output_file.write(
        template.render(
            title=config['title'],
            articleHeadline=config['articleHeadline'],
            article=article,
            articleDescription1=articleDescription1
        )
    )
    template=template_env.get_template('contact_layout.html')
    with open('proj1/outPutFiles/contact.html','w') as output_file:
        output_file.write(
        template.render(
            title=config['title'],
            email=config['email'],
            phone=config['phoneNumber'],
            location=config['location'],
            weblink=config['webLink'],
            article=article
        )
    )
    template=template_env.get_template('about_layout.html')
    with open('proj1/outPutFiles/about.html','w') as output_file:
        output_file.write(
        template.render(
            title=config['title'],
            # email=config['email'],
            phone=config['phoneNumber'],
            location=config['location'],
            # weblink=config['webLink'],
            # article=article
            aboutVision=aboutVision

            
        ))
        
    if webname!="":
     zip_name = 'proj1/Zipy'
     directory_name = 'proj1/outPutFiles'
     path_to_file=shutil.make_archive(zip_name, 'zip', directory_name)
     print(path_to_file)
     zip_file = open(path_to_file, 'rb')
     response = HttpResponse(zip_file, content_type='application/force-download')
     response['Content-Disposition'] = 'attachment; filename="%s"' % 'GeneratedWebsite.zip'
     return response
        #return redirect('/downloads')
    
        
    else:
       
      return render(request,'index.html')



def downloadspage(request):
    return render(request,'downloads.html')





def download(request):
     

    # Create 'path\to\zip_file.zip'
     
    # path_to_file='proj1/Zipy.zip'
    # check_file = os.path.isfile(path_to_file)

    # print(check_file)
     
    #  if  os.path.isfile(path_to_file)==True:
    #       messages.error(request, 'file not found.')
          
    #  else:
     zip_name = 'proj1/Zipy'
     directory_name = 'proj1/outPutFiles'
     path_to_file=shutil.make_archive(zip_name, 'zip', directory_name)
     print(path_to_file)
     zip_file = open(path_to_file, 'rb')
     response = HttpResponse(zip_file, content_type='application/force-download')
     response['Content-Disposition'] = 'attachment; filename="%s"' % 'GeneratedWebsite.zip'
     return response

    

    

def home(request):
    return render(request,'home.html')




