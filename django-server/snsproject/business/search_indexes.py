from .models import Discovery
from haystack import indexes

class DiscoveryIndex(indexes.SearchIndex, indexes.Indexable):
	text = indexes.EdgeNgramField(document=True, use_template=True)
	ig_id = indexes.IntegerField(model_attr='ig_id')
	username = indexes.CharField(model_attr='username')
	name = indexes.CharField(model_attr='name')
	profile_picture_url = indexes.CharField(model_attr='profile_picture_url')
	follows_count = indexes.IntegerField(model_attr='follows_count')
	followers_count = indexes.IntegerField(model_attr='followers_count')
	media_count = indexes.IntegerField(model_attr='media_count')
	id = indexes.CharField(model_attr='id')

	def get_model(self):
		return Discovery

	def index_queryset(self, using=None):
		return self.get_model().objects.all()
