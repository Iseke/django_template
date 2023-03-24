from django.conf import settings
from storages.backends.s3boto3 import S3Boto3Storage

# Create yous storages here.


class StaticStorage(S3Boto3Storage):
    querystring_auth = False
    default_acl = 'public-read'
    location = settings.AWS_STATIC_LOCATION


class MediaStorage(S3Boto3Storage):
    location = settings.AWS_MEDIA_LOCATION
