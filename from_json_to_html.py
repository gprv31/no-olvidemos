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

with open('hdps.json', 'r', encoding='utf-8') as infile:
    hdps = json.load(infile)
    for hdp in hdps:
        print(f"""<div class="media" data-nombre="{hdp['nombre']}" data-partido="{hdp['partido']}" data-votacion="VOTACION">
                <a href="{hdp['img']}"><img src="{hdp['img']}" alt="" title="{hdp['nombre']}. Partido: {hdp['partido']}" /></a>
				</div>""")
