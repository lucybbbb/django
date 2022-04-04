from django.apps import AppConfig


class PlannerConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'planner'
class UserConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'users'

    # add this
    def ready(self):
        import users.signals 