from django.http import HttpResponse

from kat_corner.settings import THE_SITE_NAME


THE_APP_NAME = "Kat Corner"


def index(request):
    """
    Simple function-based view to display the kitten list
    """
    return HttpResponse(
        f"<title>{THE_SITE_NAME} - {THE_APP_NAME}</title>"
        f"Hello, Kats! You're at the {THE_SITE_NAME} : {THE_APP_NAME} site."
    )
