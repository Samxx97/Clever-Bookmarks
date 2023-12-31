from rest_framework import serializers
from bookmarks.models import Bookmark

class BookmarkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bookmark
        fields = ['id','title', 'url', 'tags', 'domain', 'content', 'isCommitted']