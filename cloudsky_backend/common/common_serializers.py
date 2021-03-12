from rest_framework import serializers
from rest_framework.serializers import raise_errors_on_nested_writes
from rest_framework.utils import model_meta
import logging

logger = logging.getLogger(__file__)


class BaseSerializer(serializers.ModelSerializer):

    def update(self, instance, validated_data):
        raise_errors_on_nested_writes('update', self, validated_data)
        info = model_meta.get_field_info(instance)
        # Simply set each attribute on the instance, and then save it.
        # Note that unlike `.create()` we don't need to treat many-to-many
        # relationships as being a special case. During updates we already
        # have an instance pk for the relationships to be associated with.
        for attr, value in validated_data.items():
            if attr in info.relations and info.relations[attr].to_many:
                field = getattr(instance, attr)
                field.set(value)
            else:
                setattr(instance, attr, value)
        instance.update_by = self.context["request"].user.username
        instance.save()
        return instance

    def create(self, validated_data):
        instance = super(BaseSerializer, self).create(validated_data)
        try:
            username = self.context["request"].user.username
            if hasattr(instance, 'create_by'):
                instance.createBy = username
            if hasattr(instance, 'create_by'):
                instance.createBy = username
        except Exception as e:
            logger.error("create add default msg error: %s" % str(e))
        instance.save()
        return instance
