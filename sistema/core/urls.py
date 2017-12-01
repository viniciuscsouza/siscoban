from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^cadastra-funcionario/$', views.cadastra_funcionario, name='cadastra_funcionario'),
    url(r'^consulta-funcionario/$', views.consulta_funcionario, name='consulta_funcionario'),
    url(r'^edita-funcionario/(?P<id>[0-9]+)$', views.edita_funcionario, name='edita_funcionario'),
    url(r'^deleta-funcionario/(?P<id>[0-9]+)$', views.deleta_funcionario, name='deleta_funcionario'),
    url(r'^cadastra-venda/$', views.cadastra_venda, name='cadastra_venda'),
    url(r'^consulta-venda/$', views.consulta_venda, name='consulta_venda'),
    url(r'^edita-venda/(?P<id>[0-9]+)$', views.edita_venda, name='edita_venda'),
    url(r'^deleta-venda/(?P<id>[0-9]+)$', views.deleta_venda, name='deleta_venda'),
    url(r'^novo-usuario/$', views.add_user, name='add_user'),
    url(r'^login-usuario/$', views.user_login, name='user_login'),
    url(r'^logout-usuario/$', views.user_logout, name='user_logout'),
    url(r'^altera-senha/$', views.change_password, name='change_password'),
    url(r'^venda-funcionario/$', views.venda_funcionario, name='venda_funcionario'),
    url(r'^grafico-funcionario/$', views.grafico_funcionario, name='grafico_funcionario'),
]
