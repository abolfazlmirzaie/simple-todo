from celery import shared_task

# @shared_task
# def add(x, y):
#     print("adding {x} , {y}")
#     return x + y
#



@shared_task
def say_hello():
    print("say hello every 10 seconds ✅")