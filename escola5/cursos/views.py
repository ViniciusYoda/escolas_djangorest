from rest_framework import generics
from .models import Curso, Avaliacao
from .serializers import CursoSerializer, AvaliacaoSerializer
from rest_framework.generics import get_object_or_404
from rest_framework import viewsets, mixins
from rest_framework.decorators import action 
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination

# =========================== API V1 ==========================

class CursosAPIView(generics.ListCreateAPIView):
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer

class CursoAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer

class AvaliacoesAPIView(generics.ListCreateAPIView):
    queryset = Avaliacao.objects.all()
    serializer_class = AvaliacaoSerializer

    def get_querset(self):
        if self.kwargs.get('curso_pk'):
            return self.queryset.filter(curso_id = self.kwargs.get('curso_pk'))
        return self.queryset.all()
    
class AvaliacaoAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Avaliacao.objects.all()
    serializer_class = AvaliacaoSerializer

    def get_object(self):
        if self.kwargs.get('curso_pk'):
            return get_object_or_404(self.get_queryset(), curso_id=self.kwargs.get('curso_pk'), pk=self.kwargs.get('avaliaco_pl'))
        return get_object_or_404(self.get_queryset(), pk=self.kwargs.get('avaliacao_pk'))
    
# =========================== API V2 ==========================
class CursoViewSet(viewsets.ModelViewSet):
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer

    class AvaliacaoPagination(PageNumberPagination):
        page_size = 1

    @action(detail=True, methods=["get"])
    def avaliacoes(self, request, pk=None):
        avaliacoes = Avaliacao.objects.filter(curso_id = pk)
        paginator = self.AvaliacaoPagination()
        page = paginator.paginate_queryset(avaliacoes, request)
        if page is not None:
            serializer = AvaliacaoSerializer(page, many=True)
            return paginator.get_paginated_response(serializer.data)        
        serializer = AvaliacaoSerializer(avaliacoes.all(), many = True)
        return Response(serializer.data)
        return Response(serializer.data)

# View set padrão    
# class AvaliacaoViewSet(viewsets.ModelViewSet):
#     queryset = Avaliacao.objects.all()
#     serializer_class = AvaliacaoSerializer

# VIew set costomizada
class AvaliacaoViewSet(mixins.CreateModelMixin, mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, viewsets.GenericViewSet):
    queryset = Avaliacao.objects.all()
    serializer_class = AvaliacaoSerializer