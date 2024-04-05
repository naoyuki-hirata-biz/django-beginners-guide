from django.contrib.auth.models import User
from boards.models import Board, Topic, Post

if not Board.objects.exists():
    board = Board(name='Django', description='This is a board about Django.')
    board.save()
    Board.objects.create(name='Python', description='General discussion about Python.')

if not Post.objects.exists() and User.objects.exists():
    board = Board.objects.get(name='Django')
    user = User.objects.last()
    for i in range(100):
        subject = 'Topic test #{}'.format(i)
        topic = Topic.objects.create(subject=subject, board=board, starter=user)
        Post.objects.create(message='Lorem ipsum...', topic=topic, created_by=user)
