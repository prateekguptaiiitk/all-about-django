from django.core.files.storage import FileSystemStorage
from django.db import connection
from django_tenants.files.storage import TenantFileSystemStorage
from django.conf import settings


class CustomSchemaStorage:
    def _get_storage_backend(self):
        schema_name = connection.schema_name
        if settings.ENVIRONMENT == 'development':
            if schema_name == 'public':
                return FileSystemStorage()
            else:
                return TenantFileSystemStorage()

    def save(self, name, content, max_length=None):
        storage_backend = self._get_storage_backend()
        return storage_backend.save(name, content, max_length)

    def url(self, name):
        storage_backend = self._get_storage_backend()
        return storage_backend.url(name)

    def generate_filename(self, name):
        storage_backend = self._get_storage_backend()
        return storage_backend.generate_filename(name)

    def delete(self, name):
        storage_backend = self._get_storage_backend()
        storage_backend.delete(name)