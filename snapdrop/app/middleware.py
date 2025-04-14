from django.conf import settings
import os

class CleanupUploadedFilesMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        return response

    def process_request(self, request):
        if not request.session.session_key:
            return
        uploaded_files = request.session.get('uploaded_files', [])
        for file_path in uploaded_files:
            if os.path.exists(file_path):
                os.remove(file_path)
        request.session['uploaded_files'] = []