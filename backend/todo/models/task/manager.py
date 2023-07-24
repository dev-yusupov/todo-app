from django.db import models

from django.core.exceptions import ValidationError

class TaskManager(models.Manager):
    """Manager for Task model in todo app."""
    def create_task(self, title, **extra_fields):
        if not title:
            raise ValueError("User must provide title of task.")
        
        try:
            task = self.model(
                title=title,
                **extra_fields,
            )
            task.save(using=self._db)

            return task

        except ValidationError as _:
            print(_)
            return {
                'error': 'There was an error creating user.'
            }
