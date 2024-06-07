from django.shortcuts import render, redirect
#from django.contrib.auth.decorators import login_required
from github import Github
from .models import Repository
from django.contrib import messages

#@login_required
def github_connect(request):
    try:# Replace these with your actual GitHub App credentials
        #1. either authemticate with the access token of the user.
        token = 'your_access_token'
        #2. or authenticate the user via the client and secret id.
        client_id = 'your_client_id'
        client_secret = 'client_secret_id'

        # Authenticate the user using the GitHub App
        github = Github(access_token,  retry=9)
        user = github.get_user()

        # Fetch all repositories (public and private)
        repos = user.get_repos()

        # Store repository details in the Django model
        for repo in repos:
            repository, created = Repository.objects.get_or_create(
                repo_id=repo.id,
                defaults={
                    'name': repo.name,
                    'description': repo.description,
                    'is_private': repo.private,
                    'owner': repo.owner.login,
                }
            )
    except Exception as e:
        messages.error(request, f"An error occurred: {str(e)}")
        return redirect('home')

    return redirect('repository_list')

from django.shortcuts import render
from .models import Repository

def repository_list(request):
    repositories = Repository.objects.all()
    return render(request, 'github_app/repository_list.html', {'repositories': repositories})
'''def repository_list(request):
    return HttpResponse("Test response")'''

from django.shortcuts import render

def home(request):
    return render(request, 'home.html')
