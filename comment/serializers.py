from  rest_framework import  serializers
from  article import  models
from  user_info.serializers import UserSerializers
from comment import  models

class CommentChildenSerializers(serializers.ModelSerializer):

    url = serializers.HyperlinkedIdentityField(view_name='comment-detail')
    auther = UserSerializers(read_only=True)
    class Meta:
        model = models.Comment
        #不需要的字段
        exclude = [
            'parent',
            'article'
        ]

class CommentSerializers(serializers.ModelSerializer):

    url = serializers.HyperlinkedIdentityField(view_name='comment-detail')
    auther = UserSerializers(read_only=True)
    article = serializers.HyperlinkedRelatedField(view_name='article-detail',read_only=True)
    article_id = serializers.IntegerField(write_only=True,allow_null=True,required=False)

    parent = CommentChildenSerializers(read_only=True)
    parent_id = serializers.IntegerField(write_only=True,allow_null=True,required=False)

    def update(self, instance, validated_data):
        validated_data.pop('parent_id',None)
        return  super().update(instance,validated_data)

    class Meta:
        model = models.Comment
        fields = '__all__'
        extra_kwargs = {'created': {'read_only': True}}


