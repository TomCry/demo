__author__ = 'enzyme'
__date__ = '2019/7/11 11:55 AM'
from rest_framework import serializers


class BookInfoSerializer(serializers.Serializer):
    """图书数据序列化器"""

    id = serializers.IntegerField(label='ID', read_only=True)
    btitle = serializers.CharField(label='名称', max_length=20)
    bpub_date = serializers.DateField(label='发布日期', required=False)
    bread = serializers.IntegerField(label='阅读量', required=False)
    bcomment = serializers.IntegerField(label='评论量', required=False)
    image = serializers.ImageField(label='图片', required=False)
    heroinfo_set = serializers.PrimaryKeyRelatedField(read_only=True, many=True)


class HeroInfoSerializer(serializers.Serializer):
    """英雄数据序列化器"""
    GENDER_CHOICES = (
        (0, 'male'),
        (1, 'female')
    )
    id = serializers.IntegerField(label='ID', read_only=True)
    hname = serializers.CharField(label='名字', max_length=20)
    hgender = serializers.ChoiceField(choices=GENDER_CHOICES, label='性别', required=False)
    hcomment = serializers.CharField(label='描述信息', max_length=200, required=False, allow_null=True)
    hbook = serializers.PrimaryKeyRelatedField(read_only=True)


from .models import BookInfo


class BookReadSerialzer(serializers.ModelSerializer):
    class Meta:
        model = BookInfo
        fields = ('bread',)
        extra_kwargs = {
            'bread': {
                'required': True,
                'min_value': 0,
            }
        }

    def update(self, instance, validated_data):
        instance.bread = validated_data['bread']
        instance.save()
        return instance
