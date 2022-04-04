from django.shortcuts import render, get_object_or_404
from recipe.models import Recipe ,Topic
from django.db.models import Q
from django.contrib.auth.models import  User
from django.utils import timezone


from django.views import generic
from django.core.paginator import Paginator

def recipe_list(request):
    recipe=Recipe.objects.all()
    paginator = Paginator(recipe, 5)
    page_number=request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'list.html', {'recipe': recipe,'page_obj': page_obj,})


#def recipe_detail(request,pk):
    #recipe=Recipe.objects.filter(title=pk)
    #context={
    #   'recipe':recipe,
   # }
    
   # return render(request, 'detail.html', context)

#def recipe_detail(request, id=None):
   #recipe = get_object_or_404(Recipe, title=id)
   #types = Topic.objects.all()
  # t = types.get(id=recipe.topic.id)
   #context= {
  #     'recipe': recipe,
  #     'topic': t.title,
   #     }
#   return render(request, 'detail.html', context)


#def recipe_detail(request, slug=None):
 #  recipe = get_object_or_404(Recipe, slug=slug)
#
 # 
  # context= {
   #    'recipe': recipe,
    #   
       # }
   #return render(request, 'detail.html', context)

class RecipeDetailView(generic.DetailView):
    model=Recipe
    template_name='detail.html' 
    def recipe_detail_view(request, primary_key):
        recipe= get_object_or_404(Recipe, pk=primary_key)
        return render (request, 'detail.html', context={'recipe': recipe})




def search(request):
    results = []
 
    if request.method == "GET":

        query = request.GET.get('search')

        if query == '':
           query = 'None'

        results = Recipe.objects.filter(Q(title__icontains=query) | Q(topic__title__icontains=query) | Q(ingredients__icontains=query) )

    return render(request, 'search.html', {'query': query, 'results': results})
