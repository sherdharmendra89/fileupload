# tasks.py

import os
from celery import shared_task
from .models import File

@shared_task
def process_file_upload(file_id):
    try:
        file = File.objects.get(pk=file_id)
        file_path = file.file.path
        new_file_path = '/path/to/destination/' + file.file.name
        os.rename(file_path, new_file_path)
        file.file.name = new_file_path
        file.save()
    except File.DoesNotExist:
        pass
