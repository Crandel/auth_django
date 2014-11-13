from django.template import Context,loader
from django.utils.html import strip_tags
from django.core.mail import EmailMultiAlternatives
from django.conf import settings

def get_or_none(classmodel, **kwargs):
    try:
        return classmodel.objects.get(**kwargs)
    except classmodel.DoesNotExist:
        return None


def send_generic_mail(template=None, context_dict={}, subject=None, to=[]):
    t = loader.get_template(template)
    c = Context(context_dict)
    rendered = t.render(c)
    text_content = strip_tags(rendered)
    html_content = rendered
    from_email = settings.DEFAULT_FROM_EMAIL
    msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
    msg.attach_alternative(html_content, "text/html")
    msg.send()
