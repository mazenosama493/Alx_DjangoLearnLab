from django.db.models.signals import post_migrate
from django.contrib.auth.models import Group, Permission
from django.dispatch import receiver
from django.contrib.contenttypes.models import ContentType
from .models import Article

@receiver(post_migrate)
def create_groups_and_permissions(sender, **kwargs):
    if sender.name == 'your_app_name':  # Replace with your app's name
        content_type = ContentType.objects.get_for_model(Article)

        # Define permissions
        permissions = {
            "can_view": "Can view article",
            "can_create": "Can create article",
            "can_edit": "Can edit article",
            "can_delete": "Can delete article",
        }

        # Create or get permissions
        for codename, name in permissions.items():
            perm, created = Permission.objects.get_or_create(codename=codename, name=name, content_type=content_type)

        # Create groups and assign permissions
        groups_permissions = {
            "Viewers": ["can_view"],
            "Editors": ["can_view", "can_create", "can_edit"],
            "Admins": ["can_view", "can_create", "can_edit", "can_delete"],
        }

        for group_name, perms in groups_permissions.items():
            group, created = Group.objects.get_or_create(name=group_name)
            for perm_codename in perms:
                perm = Permission.objects.get(codename=perm_codename)
                group.permissions.add(perm)

        print("Groups and permissions created successfully.")
