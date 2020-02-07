from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="ngs_home"),

    path('pipeline/',views.pipeline,name="ngs pipeline home"),
    path('pipeline/fastqc-<int:id_request>/', views.fastqc, name="ngs fastqc"),
    path('pipeline/hisat/',views.hisat, name="hisat2"),
    path('pipeline/R_analysis/',views.ranalysis, name='R analysis'),

    path('proteo/fasta',views.proteo, name='Proteo fasta'),

    path('phylo/', views.phylo_align, name="phylogenic pipeline hub"),
    path('phylo/tree', views.phylo_tree, name="phylogenic compute tree"),
    path('phylo/visu', views.phylo_visu, name="phylogenic visualization")
]
