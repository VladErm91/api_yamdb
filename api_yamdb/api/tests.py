from django.test import TestCase
from rest_framework.test import APIClient
from reviews.models import Title, Review, User


class ReviewCreateTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()

        # Создание пользователя
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.user.save()

        # Создание объекта Title
        self.title = Title.objects.create(name='Test Title')
        self.title.save()

        # Авторизация пользователя
        self.client.force_authenticate(user=self.user)

    def test_create_review(self):
        url = f'/api/v1/titles/{self.title.id}/reviews/'

        # Данные для нового обзора
        review_data = {
            'review_text': 'Очень хорошее произведение!',
            'score': 9
        }

        response = self.client.post(url, review_data, format='json')
        self.assertEqual(response.status_code, 201)  # проверка на статус ответа

        data = response.json()
        self.assertIn('id', data)  # проверка на наличие id в ответе
        self.assertEqual(data['review_text'], review_data['review_text'])  # проверка текста отзыва
        self.assertEqual(data['score'], review_data['score'])  # проверка оценки отзыва
