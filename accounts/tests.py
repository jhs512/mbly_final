from django.test import TestCase

from accounts.models import User


class AccountsTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        users: list[User] = User.objects.all()[0:2]
        cls.user1 = users[0]
        cls.user2 = users[1]

    def test_2명의_유저가_존재한다(self):
        self.assertTrue(self.user1 != None)
        self.assertTrue(self.user2 != None)

    def test_유저1이_유저2를_팔로우_시도하는게_가능하다(self):
        self.user1.follow(self.user2)

    def test_유저1이_유저2를_팔로우하면_유저1의_팔로잉에는_유저2가_포함되어있어야_한다(self):
        self.user1.follow(self.user2)
        self.assertTrue(self.user1.followings.contains(self.user2))
        # 역은 성립되지 않아야 한다.
        self.assertFalse(self.user2.followings.contains(self.user1))

    def test_유저1이_유저2를_팔로우하면_유저2의_팔로워에는_유저1이_포함되어있어야_한다(self):
        self.user1.follow(self.user2)
        self.assertTrue(self.user2.followers.contains(self.user1))
        # 역은 성립되지 않아야 한다.
        self.assertFalse(self.user1.followers.contains(self.user2))

