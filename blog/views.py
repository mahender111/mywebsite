from django.shortcuts import render
from rest_framework.renderers import JSONRenderer

from .forms import ContactForm

# from rest_framework.views import APIView
#
# # Create your views here.
# from .models import Post
#
# from django.http import Http404
# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework import status
#
# class PostList(APIView):
#     def get(self, request):
#         post= Post.objects.all()
#         serializer =PostSerializer(post, many=True)
#         return Response(serializer.data)
#
#     # def post(self, request):
#     #     serializer = PostSerializer(data=request.data)
#     #     if serializer.is_valid():
#     #         serializer.save()
#     #         return Response(serializer.data, status=status.HTTP_201_CREATED)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


from django.http import HttpResponse
from django.views import View

from .models import Post


def ListView(request):
    return HttpResponse('<h1>fuction based view</h1>')

# class based view

class MyView(View):
    name ='mahender singh'

    def get(self,request):
        # return HttpResponse('<h1>class based view</h1>')
        return HttpResponse(self.name)

class MyViewChild(MyView):
    def get(self,request):
        return HttpResponse(self.name)


def HomeFun(request):
    return render(request,'home.html')

class HomeClass(View):
    def get(self,request):
        return render(request,'blog/home.html')


def about_func(request):
    context ={'msg':'A great invention of a computer in 2021 by mahender singh'}

    return render(request,'blog/about.html',context )

class AboutClassView(View):
    def get(self,request):
        context = {'msg': 'A great invention of a computer in 2021 by mahender singh'}
        return render(request, 'blog/about.html', context)

def contactfun(request):
    if request.method == 'POST':
        form =ContactForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data['name'])
            return HttpResponse('Thank form submitted !!')
    else:
        form =ContactForm()
    return render(request,'blog/about.html',{'form':form})



#######################################################################


# Model objects

# def Post_detail(request):
#     post= Post.objects.get(id=1)
#     serializer =serializer(post)
#     json_data = JSONRenderer().render(serializer.data)
#     return HttpResponse(json_data,content_type="application/json")
#




