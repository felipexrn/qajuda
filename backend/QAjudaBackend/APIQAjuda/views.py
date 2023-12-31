from rest_framework import viewsets, status, generics
from .models import Colaborador_acao, Acao, Colaborador, Status
from .serializers import ColaboradorAcaoSerializer
from rest_framework.decorators import action
from rest_framework.response import Response
from django.db.models import F, ExpressionWrapper, BooleanField

class SolicitacoesEmAbertoView(generics.ListAPIView):
    serializer_class = ColaboradorAcaoSerializer

    def get_queryset(self):
        acao_id = self.kwargs['acao_id']
        print(Colaborador_acao.objects.filter(acao_id=acao_id, solicitacao='E').select_related('colaborador'))
        return Colaborador_acao.objects.filter(acao_id=acao_id, solicitacao='E').select_related('colaborador')


    def perfom_update(self, serializer):
        instance = serializer.instance
        aceitar_solicitacao = serializer.validated_data.get('aceitar_solicitacao')
        recusar_solicitacao = serializer.validated_data.get('recusar_solicitacao')

        if aceitar_solicitacao:
            instance.solicitacao = 'A'
            instance.save()
            return Response({'status': 'Solicitação aceita'})

        if recusar_solicitacao:
            instance.solicitacao = 'R'
            instance.save()
            return Response({'status': 'Solicitação recusada'})