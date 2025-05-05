# from celery import shared_task
# from dateutil.utils import today
# from django.utils import timezone
# from datetime import timedelta
# from .models import Book  # Replace YourModel with your actual model
#
#
# @shared_task
# def update_field(object_id):
#     try:
#         last_10 = today - timedelta(days=3650)
#         old_book = Book.objects.filter(publication_date__gte=last_10)
#
#         obj.your_field = True  # Replace your_field with the actual field
#         obj.save()
#     except Book.DoesNotExist:
#         # Handle the case where the object does not exist
#         pass
#
#
# @shared_task
# def schedule_update(object_id):
#     update_field.apply_async(args=[object_id], countdown=1800)  # 1800 seconds = 30 minutes
#
#
#
#     #
#     # from celery import shared_task
#     # from django.utils import timezone
#     # from datetime import timedelta
#     # from .models import YourModel  # Replace YourModel with your actual model
#     #
#     # @shared_task
#     # def update_field(object_id):
#     #     try:
#     #         obj = YourModel.objects.get(pk=object_id)
#     #         obj.your_field = True  # Replace your_field with the actual field
#     #         obj.save()
#     #     except YourModel.DoesNotExist:
#     #         # Handle the case where the object does not exist
#     #         pass
#     #
#     # @shared_task
#     # def schedule_update(object_id):
#     #   update_field.apply_async(args=[object_id], countdown=1800) # 1800 seconds = 30 minutes
