from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Table
from .serializers import TableSerializer

# ─── GET toutes les tables ───
@api_view(['GET'])
def liste_tables(request):
    tables = Table.objects.all()
    serializer = TableSerializer(tables, many=True)
    return Response({
        'status': 'success',
        'data': serializer.data
    })

# ─── GET détail d'une table ───
@api_view(['GET'])
def detail_table(request, id):
    try:
        table = Table.objects.get(id=id)
    except Table.DoesNotExist:
        return Response({
            'status': 'error',
            'message': 'Table non trouvée'
        }, status=404)

    serializer = TableSerializer(table)
    return Response({
        'status': 'success',
        'data': serializer.data
    })

# ─── POST ajouter une table ───
@api_view(['POST'])
def ajouter_table(request):
    serializer = TableSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({
            'status': 'success',
            'data': serializer.data
        }, status=201)
    return Response({
        'status': 'error',
        'errors': serializer.errors
    }, status=400)

# ─── PUT modifier une table ───
@api_view(['PUT'])
def modifier_table(request, id):
    try:
        table = Table.objects.get(id=id)
    except Table.DoesNotExist:
        return Response({
            'status': 'error',
            'message': 'Table non trouvée'
        }, status=404)

    serializer = TableSerializer(table, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({
            'status': 'success',
            'data': serializer.data
        })
    return Response({
        'status': 'error',
        'errors': serializer.errors
    }, status=400)

# ─── DELETE supprimer une table ───
@api_view(['DELETE'])
def supprimer_table(request, id):
    try:
        table = Table.objects.get(id=id)
        table.delete()
        return Response({
            'status': 'success',
            'message': 'Table supprimée avec succès'
        })
    except Table.DoesNotExist:
        return Response({
            'status': 'error',
            'message': 'Table non trouvée'
        }, status=404)
    
    # ─── GET tables disponibles ───
@api_view(['GET'])
def tables_disponibles(request):
    date         = request.query_params.get('date')
    heure        = request.query_params.get('heure')
    nb_personnes = request.query_params.get('nb_personnes', 1)

    # Vérifier que les paramètres sont présents
    if not date or not heure:
        return Response({
            'status': 'error',
            'message': 'Paramètres date et heure obligatoires'
        }, status=400)

    # Filtrer les tables selon la capacité
    tables = Table.objects.filter(
        statut='disponible',
        capacite__gte=int(nb_personnes)
    )

    serializer = TableSerializer(tables, many=True)
    return Response({
        'status': 'success',
        'data': serializer.data
    })

# ─── Page Accueil HTML ───
def page_accueil(request):
    return render(request, 'tables/accueil.html')

# ─── Page Admin HTML ───
def page_admin_tables(request):
    return render(request, 'tables/admin_table.html')

# ─── Page Détail Table HTML ───
def page_detail_table(request, id):
    return render(request, 'tables/detail_table.html', {'table_id': id})