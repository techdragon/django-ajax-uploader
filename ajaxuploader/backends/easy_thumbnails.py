from __future__ import absolute_import
import os

from django.conf import settings
from easy_thumbnails.files import get_thumbnailer

from ajaxuploader.backends.local import LocalUploadBackend
from ajaxuploader.backends.default_storage import DefaultStorageUploadBackend


class EasyThumbnailLocalUploadBackend(LocalUploadBackend):
    DIMENSIONS = (100, 000)
    CROP = True
    KEEP_ORIGINAL = False
    QUALITY = 100
    DETAIL = True
    SHARPEN = True
    UPSCALE = True

    # def upload_complete(self, request, filename, *args, **kwargs):
    #     path = settings.MEDIA_URL + self.UPLOAD_DIR + "/" + filename
    #     self._dest.close()
    #     return {"path": path}

    def upload_complete(self, request, filename):

        options = (
            {
                'size': self.DIMENSIONS,
                'crop': self.CROP,
                'quality': self.QUALITY,
                'detail': self.DETAIL,
                'sharpen': self.SHARPEN,
                'upscale': self.UPSCALE,
            }
        )
        thumb = get_thumbnailer(self._path).get_thumbnail(options)

        if not self.KEEP_ORIGINAL:
            os.unlink(self._path)

        return {"path": self.UPLOAD_DIR + '/' + os.path.split(thumb.path)[1]}


class EasyThumbnailDefaultStorageUploadBackend(DefaultStorageUploadBackend):
    DIMENSIONS = (100, 000)
    CROP = True
    KEEP_ORIGINAL = False
    QUALITY = 100
    DETAIL = True
    SHARPEN = True
    UPSCALE = True

    # def upload_complete(self, request, filename, *args, **kwargs):
    #     self._dest.close()
    #     return {"path": self.path}

    def upload_complete(self, request, filename):

        options = (
            {
                'size': self.DIMENSIONS,
                'crop': self.CROP,
                'quality': self.QUALITY,
                'detail': self.DETAIL,
                'sharpen': self.SHARPEN,
                'upscale': self.UPSCALE,
            }
        )
        thumb = get_thumbnailer(self.path).get_thumbnail(options)

        if not self.KEEP_ORIGINAL:
            os.unlink(self.path)

        return {"path": self.UPLOAD_DIR + '/' + os.path.split(thumb.path)[1]}
