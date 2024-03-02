import pytest

from blog.models import Post

@pytest.fixture
def one_draft():
    return Post.objects.create(
        title="fake title",
        body="fake content",
        status="draft",
    )