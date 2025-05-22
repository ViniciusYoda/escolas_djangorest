from rest_framework import serializers
from .models import Curso, Avaliacao

class AvaliacaoSerializer(serializers.ModelSerializer):
    class Meta:
        extra_kwargs = {
            'email': {'write_only': True}
        }
        model = Avaliacao
        fields = [
            'id',
            'curso',
            'nome',
            'email',
            'comentario',
            'avaliacao',
            'atualizacao',
            'criacao',
            'ativo'
        ]

class CursoSerializer(serializers.ModelSerializer): 

    # 1 Nested Relationship:
    # avaliacoes = AvaliacaoSerializer(many=True, read_only=True)

    # 2 HyperLinked Related Field:
    # avaliacoes = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name="Avaliações")

    #3 Primary Key elated Field:
    avaliacoes = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Curso
        fields = [
            'id',
            'titulo',
            'url',
            'criacao',
            'ativo',
            'avaliacoes'
        ]