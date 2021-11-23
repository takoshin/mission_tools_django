from django.test import TestCase
from api.models import User, LostArticle

class LostArticleModelTests(TestCase):

    def test_is_empty(self):
        save_items = LostArticle.objects.all()
        self.assertEqual(save_items.count(), 0)

    def test_user_save_and_retrieve(self):

        User.objects.create(
            id = 1,
            email = 'hogehoge@gmail.com',
            username = 'hogehoge'
        )
        actual_user = User.objects.get(id = 1)
        self.assertEqual(actual_user.email, 'hogehoge@gmail.com')