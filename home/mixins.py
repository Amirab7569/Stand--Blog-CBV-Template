from django.shortcuts import redirect

class CustomLoginRequiredMixins:
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect("account:login")
        return super().dispatch(request, *args, **kwargs)