from django.test import TestCase
from api.models import User, LostArticle

class LostArticleModelTests(TestCase):

    def test_is_empty(self):
        save_items = LostArticle.object.all()
        self.assertEqual(save_items.count(), 1)

    def test_user_save_and_retrieve(self):

        User.objects.create(
            id = '1',
            email = 'hogehoge@gmail.com',
            username = 'hogehoge'
        )
        actual_user = User.pbjects.get(id = '1')
        self.assertEqual(actual_user, '1')