import pytest

from blog.models import Post, Comment

@pytest.mark.django_db
def test_published_manager():
    Post.objects.create(title="Test Post1", body="This is a test", status="draft")
    Post.objects.create(title="Test Post1", body="This is a test", status="published")

    published_posts = Post.published.all()
    assert published_posts.count() == 2

    for post in published_posts:
        assert post.status == "published"

@pytest.mark.django_db
def test_comment_creation():
    post_id = 1
    name = "John Test"
    email = "john@test.com"
    body = "This is a test comment."
    comment = Comment.objects.create(post_id=post_id, name=name, email=email, body=body)
    assert isinstance(comment, Comment)

@pytest.mark.django_db
def test_comment_fields():
    post_id = 1
    name = "John Test"
    email = "john@test.com"
    body = "This is a test comment."
    comment = Comment.objects.create(post_id=post_id, name=name, email=email, body=body)
    assert comment.post_id == post_id
    assert comment.name == name
    assert comment.email == email
    assert comment.body == body