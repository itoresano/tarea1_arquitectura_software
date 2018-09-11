from .models import Comment
from django.utils import timezone
from django.shortcuts import render

def index(request):
  if request.method == 'POST':
    comment_text = request.POST['comment_text']
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
      ip_client = x_forwarded_for.split(',')[0]
    else:
      ip_client = request.META.get('REMOTE_ADDR')
    new_comment = Comment(comment_text=comment_text, pub_date=timezone.now(), ip_client=ip_client, ip_server="")
    new_comment.save()
  latest_comment_list = Comment.objects.order_by('-pub_date')
  context = {
        'latest_comment_list': latest_comment_list,
    }
  return render(request, 'comments/index.html', context)
