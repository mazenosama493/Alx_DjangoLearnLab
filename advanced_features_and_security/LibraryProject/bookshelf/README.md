# User Permissions and Groups in Django

## Custom Permissions
The `Article` model has the following permissions:
- `can_view`: Can view articles
- `can_create`: Can create articles
- `can_edit`: Can edit articles
- `can_delete`: Can delete articles

## Groups and Assigned Permissions
- **Viewers**: Can only view articles.
- **Editors**: Can view, create, and edit articles.
- **Admins**: Can view, create, edit, and delete articles.

## Managing Permissions in Django Admin
1. Navigate to `/admin/`
2. Under **Users**, assign users to `Viewers`, `Editors`, or `Admins`.
3. Under **Groups**, ensure permissions are correctly assigned.

## Testing
- Log in as a Viewer → Try accessing create/edit/delete → **Access Denied**
- Log in as an Editor → Try creating/editing → **Allowed**
- Log in as an Admin → Try deleting → **Allowed**
