from rest_framework import permissions

class IsOwnerOrReadOnly(permissions.BasePermission):


    def has_object_permission(self, request, view, obj):
        print("IsOwnerOrReadOnly has_obj_perms")
        print("Object:", obj)
        print("Request user:", request.user)

        
        # Allow full access to admin users.
        if request.user.is_staff:
            return True
        
        # Check if the object is the request user for cases where users are requesting their account info.
        if obj == request.user:
            return True

        # Check if the object has an 'user' attribute for cases where users are requesting LifeDomains. 
        if hasattr(obj, "user"):
            print("Has user attr")
            print(f"OBJ user: {obj.user}")

            return obj.user == request.user
    