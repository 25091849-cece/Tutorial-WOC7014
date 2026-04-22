from django.core.management.base import BaseCommand

from games.models import Game, Review, Tags


class Command(BaseCommand):
    help = 'Seed demo data for the game review site.'

    def handle(self, *args, **options):
        tags_data = ['Action', 'Cooking', 'Adventure', 'Racing', 'Simulation']
        tag_map = {}

        for label in tags_data:
            tag, _ = Tags.objects.get_or_create(label=label)
            tag_map[label] = tag

        games_data = [
            {
                'title': 'Overcook',
                'developer': 'Nintendo',
                'platform': 'Switch',
                'tags': ['Cooking', 'Action'],
            },
            {
                'title': 'Loss Ark',
                'developer': 'Smilegate',
                'platform': 'PC',
                'tags': ['Action', 'Adventure'],
            },
            {
                'title': 'Animal Crossing: Happy Home Paradise',
                'developer': 'Nintendo',
                'platform': 'Switch',
                'tags': ['Simulation', 'Cooking'],
            },
            {
                'title': 'Mario Kart 8 Deluxe',
                'developer': 'Nintendo',
                'platform': 'Switch',
                'tags': ['Racing', 'Action'],
            },
        ]

        game_map = {}
        for item in games_data:
            game, _ = Game.objects.get_or_create(
                title=item['title'],
                defaults={
                    'developer': item['developer'],
                    'platform': item['platform'],
                },
            )
            game.developer = item['developer']
            game.platform = item['platform']
            game.save()
            game.label_tag.set([tag_map[tag_label] for tag_label in item['tags']])  # type: ignore[attr-defined]
            game_map[item['title']] = game

        reviews_data = [
            {
                'game_title': 'Overcook',
                'review': 'Amazing game! One of the best on Nintendo. Highly recommend!'
            },
            {
                'game_title': 'Overcook',
                'review': 'Fun racing mechanics but a bit short. Still worth playing.'
            },
            {
                'game_title': 'Loss Ark',
                'review': 'Huge world with exciting combat and many things to explore.'
            },
            {
                'game_title': 'Animal Crossing: Happy Home Paradise',
                'review': 'Relaxing and creative. Great for decorating and casual play.'
            },
        ]

        for item in reviews_data:
            Review.objects.get_or_create(
                game=game_map[item['game_title']],
                review=item['review'],
            )

        self.stdout.write(self.style.SUCCESS('Demo data seeded successfully.'))

