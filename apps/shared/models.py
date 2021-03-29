# Django
from django.db import models


class BaseManager(models.Manager):
    def get_queryset(self):
        return QuerySetBase(self.model).filter(is_deleted=False)


class QuerySetBase(models.QuerySet):
    as_manager = BaseManager

    def delete(self):
        self.update(is_deleted=True)

    def force_delete(self):
        super().delete()


class ModifyModel(models.Model):
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class BaseModel(ModifyModel):
    is_deleted = models.BooleanField(default=False)

    class Meta():
        abstract = True

    objects = QuerySetBase.as_manager()
    raw_objects = models.Manager()

    def delete(self, using=None, keep_parents=False):
        # related_fields = [
        #     i for i in self._meta.get_fields()
        #     if i.is_relation and hasattr(i, 'parent_link')
        # ]
        #
        # for field in related_fields:
        #     name = field.get_accessor_name()
        #     if hasattr(self, name):
        #         getattr(self, name).all().delete()

        self.is_deleted = True
        self.save()
