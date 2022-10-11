from  rest_framework import  serializers
from  article import  models
from  user_info.serializers import  UserSerializers
from  comment.serializers import CommentSerializers


# 文章标题图片序列化器
class   AvatarModelSerializer(serializers.ModelSerializer):

    url = serializers.HyperlinkedIdentityField(view_name='avatar-detail')
    class Meta:
        model = models.Avatar
        fields = '__all__'


# 文章标签序列化器
class TagHyperlinkedModelSerializer(serializers.HyperlinkedModelSerializer):

    def check_tag_obj_exists(self,validated_data):
        text = validated_data.get('title')
        msg = "Tag with title {} exists".format(text)
        if models.Tag.objects.filter(title=text).exists():
            raise  serializers.ValidationError(msg)

    def create(self, validated_data):
        self.check_tag_obj_exists(validated_data)
        return  super().create(validated_data)

    def update(self, instance, validated_data):
        self.check_tag_obj_exists(validated_data)
        return  super().update(instance,validated_data)

    class Meta:
        model = models.Tag
        fields = '__all__'

# 文章分类序列化器
class CategorySerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='category-detail')
    class Meta:
        model = models.Category
        fields = '__all__'
        read_only_fields = ['created']


# 文章父类序列化器
class ArticleBaseHyperlinkedModelSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.IntegerField(read_only=True)
    auther = UserSerializers(read_only=True)
    category = CategorySerializer(read_only=True)
    category_id = serializers.IntegerField(write_only=True, allow_null=True, required=False)
    # 标签
    tag = serializers.SlugRelatedField(queryset=models.Tag.objects.all(),many=True,required=False,slug_field='title')
    # 图片
    avatar = AvatarModelSerializer(read_only=True)
    # 图片ID
    avatar_id = serializers.IntegerField(write_only=True,allow_null=True,required=False)

    default_error_messages = {
        'incorrect_avatar_id': "Avatar with id {value} not exists.",
        'incorrect_category_id': 'Category with id {value} not exists.',
        'default':'No more message here..'
    }
    # 检查过程
    def check_obj_exists_or_fail(self,model,value,message='default'):
        if not self.default_error_messages.get(message,None):
            message = 'default'
        if not model.objects.filter(id=value).exists() and value is not None:
            self.fail(message,value=value)

    # 验证avatar_id 是否存在
    def validate_avatar_id(self, value):
        self.check_obj_exists_or_fail(
            model=models.Avatar,
            value=value,
            message='incorrect_avatar_id'
        )
        return  value

    # 检查传进来的分类ID是否存在
    def validate_category_id(self,value):
        self.check_obj_exists_or_fail(
            model=models.Category,
            value=value,
            message='incorrect_category_id'
        )
        return value
    # 如果标签不存在 就创建
    def to_internal_value(self, data):
        tags_data = data.get('tag')
        if isinstance(tags_data,list):
            for text in tags_data:
                if not models.Tag.objects.filter(title=text).exists():
                    models.Tag.objects.create(title=text)
        return   super().to_internal_value(data)

# 子文章list序列化器
class ArticleSerializers(ArticleBaseHyperlinkedModelSerializer):

    class Meta:
        model = models.Article
        fields = '__all__'
        # 让 content字段不显示，但可写
        extra_kwargs = {
            'content':{'write_only':True}
        }

# 子文章详细的序列化器
class ArticleDetailSerializers(ArticleBaseHyperlinkedModelSerializer):
    # 渲染后的正文
    content_html =  serializers.SerializerMethodField()
    # 渲染后的目录
    toc_html = serializers.SerializerMethodField()
    # 评论
    comments = CommentSerializers(read_only=True,many=True)

    def get_content_html(self,obj):
        return obj.get_md()[0]

    def get_toc_html(self,obj):
        return  obj.get_md()[1]

    class Meta:
        model = models.Article
        fields = '__all__'



# CategoryDetailModelSerializers 的序列化器
class ArticleCategoryDetailModelSerializers(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='article-detail')

    class Meta:
        model = models.Article
        fields = ['url','title']

# 分类详情页展示 分类下面的所有文章
class CategoryDetailModelSerializers(serializers.ModelSerializer):
    articles = ArticleCategoryDetailModelSerializers(many=True,read_only=True)
    class Meta:
        model = models.Category
        fields = ['id','title','created','articles']





class TagDetailModelSerializers(serializers.ModelSerializer):
    articles = ArticleCategoryDetailModelSerializers(many= True,read_only=True)

    class Meta:
        model = models.Tag
        fields = ['id','title','created','articles']