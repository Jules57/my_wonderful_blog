from django.http import HttpResponse
from django.shortcuts import render


def add_comment(request, article_slug):
    return HttpResponse("Share your thoughts on this article!")


def show_blog(request):
    return render(request, 'base.html')


def show_about(request):
    return HttpResponse("Here you can find some function descriptions.")


def show_article(request, article_slug):
    return render(request, 'single_article.html', {
        'article_slug': article_slug,
    })


def create_article(request):
    return render(request, 'create_article.html')


def update_article(request, article_slug):
    return HttpResponse(f"Now you can thrive for perfection "
                        f"and make your best out of article with slug '{article_slug}'.")


def delete_article(request, article_slug):
    return HttpResponse(f"Don't need the article with slug '{article_slug}' anymore? Sad to hear it(")


def show_profile(request, username: str):
    return HttpResponse(f"Hello, {username.title()}! Here are your profile details.")


def change_password(request):
    return HttpResponse("Here you can change password.")


def register(request):
    return render(request, 'register.html')


def login(request):
    return render(request, 'login.html')


def logout(request):
    return render(request, 'logout.html')
