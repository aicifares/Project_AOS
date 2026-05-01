from django.urls import path
from . import views

urlpatterns = [
    # ─── Page HTML ───
    path('',
            views.page_accueil,         name='accueil'),
    path('admin-tables/',
        views.page_admin_tables,    name='admin_tables'),     
    path('tables/<int:id>/detail/',
        views.page_detail_table,    name='detail_table_page'),       

    # ─── API REST ───
    path('tables/',
            views.liste_tables,         name='liste_tables'),
    path('tables/ajouter/',
            views.ajouter_table,        name='ajouter_table'),        # ← monter avant <int:id>
    path('tables/disponibles/',
            views.tables_disponibles,   name='tables_disponibles'),   # ← monter avant <int:id>
    path('tables/<int:id>/',
            views.detail_table,         name='detail_table'),         # ← après les URLs fixes
    path('tables/<int:id>/modifier/',
            views.modifier_table,       name='modifier_table'),
    path('tables/<int:id>/supprimer/',
            views.supprimer_table,      name='supprimer_table'),
]