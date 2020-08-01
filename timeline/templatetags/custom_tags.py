from django import template

register = template.Library()


@register.simple_tag(name='get_gallery')
def get_moment_gallery(moment):
    result = []
    gallery = moment.gallery.get_queryset()
    for media in gallery:
        result.append(media.file)
    return result
