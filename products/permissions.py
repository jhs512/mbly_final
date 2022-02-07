from rest_framework.permissions import BasePermission

from markets.models import Market


class IsMarketMasterOrAdminUser(BasePermission):
    """
    Allows access only to admin users.
    """

    def has_permission(self, request, view):
        if request.user and request.user.is_staff:
            return bool(True)

        market_id = view.kwargs.get('market_id', None)
        market = Market.objects.get(pk=market_id)

        return bool(request.user and market.master == request.user)
