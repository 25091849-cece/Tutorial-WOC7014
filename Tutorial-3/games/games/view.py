from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, ListView

from games.forms import GameForm, ReviewForm, TagForm
from games.models import Game, Review, Tags

class GameReviewListView(ListView):
    model = Review
    template_name = 'review.html'
    context_object_name = 'reviews'

    def get_queryset(self):
        return Review.objects.select_related('game').prefetch_related('game__label_tag')


class TagListView(ListView):
    model = Tags
    template_name = 'taglist.html'
    context_object_name = 'tags'


class TagCreateView(CreateView):
    form_class = TagForm
    template_name = 'tag_form.html'
    success_url = reverse_lazy('tag_list')


class GameListView(ListView):
    model = Game
    template_name = 'game_list.html'
    context_object_name = 'games'

    def get_queryset(self):
        return Game.objects.prefetch_related('label_tag')


class GameCreateView(CreateView):
    form_class = GameForm
    template_name = 'game_form.html'
    success_url = reverse_lazy('game_list')


class ReviewCreateView(CreateView):
    form_class = ReviewForm
    template_name = 'review_form.html'
    success_url = reverse_lazy('review_list')


class ReviewDeleteView(DeleteView):
    model = Review
    template_name = 'review_delete_confirm.html'
    success_url = reverse_lazy('review_list')


