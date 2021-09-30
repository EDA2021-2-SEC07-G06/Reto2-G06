"""
 * Copyright 2020, Departamento de sistemas y Computación,
 * Universidad de Los Andes
 *
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along withthis program.  If not, see <http://www.gnu.org/licenses/>.
 """

import config as cf
import model
from DISClib.Algorithms.Sorting import quicksort as qck
from DISClib.Algorithms.Sorting import insertionsort as insrt
from DISClib.Algorithms.Sorting import shellsort as shllsrt
from DISClib.Algorithms.Sorting import mergesort as mrg
from DISClib.ADT import list as lt
from datetime import datetime
import csv


"""
El controlador se encarga de mediar entre la vista y el modelo.
"""
def initCatalog():
    catalog = model.newCatalogArrayList()
    return catalog
# Funciones para la carga de datos

def loadData(catalog):
    loadArtists(catalog)
    loadArtworks(catalog)

def loadArtists(catalog):
    Artistsfile = cf.data_dir + 'Artists-utf8-small.csv'
    input_file = csv.DictReader(open(Artistsfile, encoding='utf-8'))
    for Artist in input_file:
        model.addArtist(catalog, Artist)

def loadArtworks(catalog):
    Artworksfile = cf.data_dir + 'Artworks-utf8-small.csv'
    input_file = csv.DictReader(open(Artworksfile, encoding='utf-8'))
    for Artwork in input_file:
        model.addArtwork(catalog, Artwork)
        model.addMedium(catalog, Artwork)
def loadsublist(lst,pos,numelem):
    return model.sublist(lst,pos,numelem)
#req1
def callartistrangelist(catalog,cmp,start,end):
    size=lt.size(catalog)
    condition1=start < (datetime.strptime(catalog['elements'][0]['BeginDate'],'%Y' ))
    condition2=end > datetime.strptime(catalog['elements'][size-1]['BeginDate'],'%Y' )
    if condition1 and condition2:
        result=print('Invalid Range')
    else:
        result=model.daterangelist(catalog,cmp,start,end)
    return result
def callartistrangecmp(artist,start,end):
    if artist['BeginDate'] != ('0'):
        var= model.cmpartistrange(artist,start,end)
    else:
        var=False
    return var
def calladjustartistvalues(catalog,headers):
    return model.adjustartistvalues(catalog,headers)
def callartistcmp(artist1,artist2):
    return model.cmpArtistByDateAcquired(artist1,artist2)
def callartistcleanordlist(catalog):
    return model.cleanartistordlist(catalog)
#req2
def callcmp(artwork1,artwork2):
    return model.cmpArtworkByDateAcquired(artwork1,artwork2)
def callartworkrangecmp(artwork,start,end):
    if start != ('') and end != ('') and artwork['DateAcquired'] != (''):
        var= model.cmpartworkrange(artwork,start,end)
    else:
        var=False
    return var
def callartworkrangelist(catalog,cmp,start,end):
    size=lt.size(catalog)
    condition1=start < (datetime.strptime(catalog['elements'][0]['DateAcquired'],'%Y-%m-%d' ))
    condition2=end > datetime.strptime(catalog['elements'][size-1]['DateAcquired'],'%Y-%m-%d' )
    if condition1 and condition2:
        result=print('Invalid Range')
    else:
        result=model.daterangelist(catalog,cmp,start,end)
    return result
def callartworkscleanordlist(catalog):
    return model.cleanartworksordlist(catalog)
def calladjustvalues(catalog,headers,secondarycatalog):
    return model.adjustvalues(catalog,headers,secondarycatalog)
def callshowlist(lst):
    return 
#req4
def calldictionarymaker(artists,artworks):
    return model.dictionarymaker( artists,artworks)
def callArtByNation(dictionary,Nationalities):
    return model.ArtByNation(dictionary,Nationalities)
def callnationcmp(nation1, nation2):
    return model.nationcmp(nation1,nation2)
def callgreatestlist(headers,dictionary,greatest,generalcatalog):
    return model.greatestlist(headers,dictionary,greatest,generalcatalog)
#sortingalgorithms
def sortlistinsertion(catalog,cmpfunction):
    return insrt.sort(catalog,cmpfunction)
def sortlistshell(catalog,cmpfunction):
    return shllsrt.sort(catalog,cmpfunction)
def sortlistquick(catalog,cmpfunction):
    return qck.sort(catalog,cmpfunction)
def sortlistmerge(catalog,cmpfunction):
    model.mergesort(catalog,cmpfunction)

def transferartworks(artworks, department):
    return model.transferartworks(artworks, department)

def clasificarobrasartista(artists, artworks, nombre):
    return model.clasificar_obras_artista_por_tecnica(artists, artworks, nombre)
# Funciones de ordenamiento

# Funciones de consulta sobre el catálogo
