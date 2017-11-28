from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^cadastra_funcionario/$', views.cadastra_funcionario, name='cadastra_funcionario'),
    url(r'^consulta_funcionario/$', views.consulta_funcionario, name='consulta_funcionario'),
    url(r'^edita_funcionario/(?P<id>[0-9]+)$', views.edita_funcionario, name='edita_funcionario'),
    url(r'^deleta_funcionario/(?P<id>[0-9]+)$', views.deleta_funcionario, name='deleta_funcionario'),
    url(r'^cadastra_venda/$', views.cadastra_venda, name='cadastra_venda'),
    url(r'^consulta_venda/$', views.consulta_venda, name='consulta_venda'),
    url(r'^edita_venda/(?P<id>[0-9]+)$', views.edita_venda, name='edita_venda'),
    url(r'^deleta_venda/(?P<id>[0-9]+)$', views.deleta_venda, name='deleta_venda'),
]
