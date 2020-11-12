"""
import re
import json


img = re.compile('href="([^"]+)"')
nombre = re.compile('title="(.+)Partido')
partido = re.compile('Partido:([^"]+)')

hdps = []

partidos = set()


with open("congresistas.txt") as f:
    for line in f.readlines():
        line = line.strip()
        if line:
            hdp_img = img.findall(line)[0]
            hdp_nombre = nombre.findall(line)[0].strip(' ').strip('.')
            hdp_partido = partido.findall(line)[0].strip(' ')
            hdps.append({
                'img': hdp_img,
                'nombre': hdp_nombre,
                'partido': hdp_partido
            })
            partidos.add(hdp_partido)
    print(partidos)


with open('hdps.json', 'w', encoding='utf-8') as outfile:
    json.dump(hdps, outfile, ensure_ascii=False)    
"""
import json

EQUIV = {
    "Acción Popular": {'siglas': '(AP)', 'icon': 'icon-partido icon-ap'},
    "Alianza para el Progreso": {'siglas': '(APP)', 'icon': 'icon-partido icon-app'},
    "Frente Amplio": {'siglas': '(FA)', 'icon': 'icon-partido icon-fa'},
    "FREPAP": {'siglas': '(FREPAP)', 'icon': 'icon-partido icon-frepap'},
    "Fuerza Popular": {'siglas': '(FP)', 'icon': 'icon-partido icon-fp'},
    "No Agrupados": {'siglas': '(NA)', 'icon': 'icon-partido icon-na'},
    "Podemos Perú": {'siglas': '(PP)', 'icon': 'icon-partido icon-pp'},
    "Somos Perú": {'siglas': '(SP)', 'icon': 'icon-partido icon-sp'},
    "Unión por el Perú": {'siglas': '(UPP)', 'icon': 'icon-partido icon-upp'}
}
with open('hdps.json', 'r', encoding='utf-8') as infile:
    hdps = json.load(infile)
    for hdp in hdps:
        print(f"""
        <div class="media" data-nombre="{hdp['nombre']}" data-partido="{hdp['partido']}" data-votacion="{"ABSTENCIÓN" if hdp['voto'] == 'A' else 'A FAVOR'}">
            <a href="{hdp['img']}"><img src="{hdp['img']}" alt="" title="{hdp['nombre']}. Partido: {hdp['partido']} {EQUIV[hdp['partido']]['siglas']}" /></a>
            <div class="caption caption-{'abstencion'  if hdp['voto'] == 'A' else 'favor' }">{hdp['nombre']} - <span class="{EQUIV[hdp['partido']]['icon']}"></span></div>
		</div>""")
