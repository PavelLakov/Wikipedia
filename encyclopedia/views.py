#####################################################
####Required  Packages and Libraries#################
#####################################################
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
import markdown2
from . import util
import random
from markdown2 import Markdown
from django.http import HttpResponse
#######################################################

# Existing index view
def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })
################################################################################
# Existing entry view, updated to convert Markdown to HTML######################
################################################################################


def convert(title):
    content = util.get_entry(title)
    mardowner=Markdown()
    if content is None:
        return None
    else:
        return mardowner.convert(content)
    
##################################################################################

def entry(request, title):
    content = convert(title)
    
    if content is None:
        return render(request, "encyclopedia/error.html", {"message": "The requested page was not found."})
    else:
        # content = markdown2.markdown(content)
        return render(request, "encyclopedia/entry.html", {
            "title": title,
            "content": content
        })


##################################################################################
############################Search################################################
##################################################################################

def search(request):
    if request.method == "GET":
        query = request.GET.get('q', '').strip()
        entries = util.list_entries()
       
        query_lower = query.lower()
        entries_lower = [entry.lower() for entry in entries]
       
        if query_lower in entries_lower:
            
            original_case_entry = entries[entries_lower.index(query_lower)]
            return redirect('entry', title=original_case_entry)
        
        matching_entries = [entry for entry in entries if query_lower in entry.lower()]
        
        if matching_entries:
            
            return render(request, "encyclopedia/search.html", {
                "entries": matching_entries,
                "query": query
            })
        else:
            
            return render(request, "encyclopedia/no_results.html", {"query": query})
    else:
        
        return HttpResponse("Method not allowed", status=405)



###############################################################################
##################### New page ################################################
###############################################################################

def new_page(request):
    if request.method == "POST":
        title = request.POST.get('title').strip()
        content = request.POST.get('content').strip()
        existing_entries = [entry.lower() for entry in util.list_entries()]
        if title.lower() in existing_entries:
            return render(request, "encyclopedia/new_page.html", {
                "error": "An entry with this title already exists. Please use a different title.",
                "title": title,
                "content": content
            })
        else:
            util.save_entry(title, content)
            return HttpResponseRedirect(reverse("entry", kwargs={'title': title}))
   
    return render(request, "encyclopedia/new_page.html")

################################################################################
##################### Edit page ################################################
################################################################################

def edit_page(request, title):
    if request.method == "POST":
        content = request.POST.get('content')
        util.save_entry(title, content)
        return HttpResponseRedirect(reverse("entry", kwargs={'title': title}))
    else:
        content = util.get_entry(title)
        return render(request, "encyclopedia/edit_page.html", {
            "title": title,
            "content": content
        })


####################################################################
###################### Random page#################################
####################################################################

def random_page(request):
    entries = util.list_entries()
    random_title = random.choice(entries)
    return HttpResponseRedirect(reverse("entry", kwargs={'title': random_title}))
