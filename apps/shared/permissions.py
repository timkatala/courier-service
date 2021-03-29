from django.contrib.auth.mixins import LoginRequiredMixin


class IsSuperUser(LoginRequiredMixin):
    def dispatch(self, request, *args, **kwargs):
        instance = super().dispatch(request, *args, **kwargs)
        if not request.user.is_superuser:
            return self.handle_no_permission()
        return instance
