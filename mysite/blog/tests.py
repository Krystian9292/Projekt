import pytest

from blog.models import Post

@pytest.mark.django_db
def test_published_manager():
    Post.objects.create(title="Test Post1", body="This is a test", status="draft")
    Post.objects.create(title="Test Post1", body="This is a test", status="published")

    published_posts = Post.published.all()
    assert published_posts.count() == 2

    for post in published_posts:
        assert post.status == "published"
