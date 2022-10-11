
from  article.models import Article,Category,Tag,Avatar
from  article.serializers import *
from  rest_framework.viewsets import  ModelViewSet
from  article import  permissions
from  rest_framework import filters
# Create your views here.

# 测试
# class TestRelated_name():
#     category = Category.objects.filter(pk=1).first()
#     print('TestRelated_name方法')
#     print(category.articles.all())





# 文章接口集
class ArticleModelViewSet(ModelViewSet):
    # 修改权限
    permission_classes = [permissions.IsAdminUserOrReadOnly]
    # 数据模型引入
    queryset = Article.objects.all()
    # 引入序列号器
    serializer_class = ArticleSerializers
    # 搜索
    filter_backends = [filters.SearchFilter]
    search_fields = ['title']

    # 保存作者
    def perform_create(self, serializer):
        """
        继承 自ListCreateAPIView
        """
        serializer.save(auther=self.request.user)

    def get_serializer_class(self):
        print(self.action)
        if self.action == 'list':
            return ArticleSerializers
        else:
            return  ArticleDetailSerializers



#  文章分类接口集
class CategoryModelViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    # 修改权限
    permission_classes = [permissions.IsAdminUserOrReadOnly]
    # 不用翻页
    pagination_class = None
    def get_serializer_class(self):
        if self.action == 'list':
            return  CategorySerializer
        else:
            return  CategoryDetailModelSerializers

# 标签接口集
class TagModelViewSet(ModelViewSet):
    queryset =  Tag.objects.all()
    serializer_class =  TagHyperlinkedModelSerializer
    # 修改权限
    permission_classes = [permissions.IsAdminUserOrReadOnly]
    # 不用翻页
    pagination_class = None

# 图片接口集
class AvatarModelViewSet(ModelViewSet):
    queryset = Avatar.objects.all()
    serializer_class = AvatarModelSerializer
    permission_classes = [permissions.IsAdminUserOrReadOnly]