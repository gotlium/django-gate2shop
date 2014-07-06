# -*- coding: utf-8 -*-

from django.contrib import admin

from g2s.models import G2STransaction


class G2STransactionAdmin(admin.ModelAdmin):

    def __init__(self, model, admin_site):
        super(G2STransactionAdmin, self).__init__(model, admin_site)

        self.readonly_fields = [field.name for field in model._meta.fields]
        self.readonly_model = model

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

    def has_change_permission(self, request, obj=None):
        return request.method != 'POST'


admin.site.register(G2STransaction, G2STransactionAdmin)
