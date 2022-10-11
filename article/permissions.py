from  rest_framework import  permissions

class IsAdminUserOrReadOnly(permissions.BasePermission):
    """
    只能管理员修改，其他用户可查看
    """
    def  has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        # print(request.user.is_superuser)
        return  request.user.is_superuser