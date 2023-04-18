from django.http import HttpResponse


def add_comment(request, article_slug):
    return HttpResponse("Share your thoughts on this article!")


def show_blog(request):
    return HttpResponse("Now you're looking at the future blog.")


def show_about(request):
    return HttpResponse("Here you can find some function descriptions.")


def show_article(request, article_slug):
    return HttpResponse(f"Look at this article with slug '{article_slug}'.")


def create_article(request):
    return HttpResponse("It's time to create a new great article. Let your imagination go wild!")


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
    return HttpResponse("Welcome aboard! Please, fill in the register form.")


def login(request):
    return HttpResponse("Already registered? Fill in the login form.")


def logout(request):
    return HttpResponse("Already leaving? Hope to see you again soon.")
