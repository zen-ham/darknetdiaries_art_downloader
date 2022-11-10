import requests
base = 'https://darknetdiaries.com/'
save_directory = 'artwork'
count = 0
go = 1
images = []
while go == 1:
    count += 1
    url = f'{base}episode/{count}/'
    r = requests.get(url, allow_redirects=True)
    r = str(r.content)
    if 'url(/imgs/404.jpg)' in r:
        go = 0
    else:
        r = r.split('"')
        nr = []
        for i in r:
            nr.extend(i.split(', '))
        r = nr
        nr = []
        for i in r:
            nr.extend(i.split(' '))
        r = nr
        r = list(dict.fromkeys(r))
        for i in r:
            if i.startswith('http') and any(c in i for c in ["png", "jpg", "mp3", "mp4", "gif", "jpeg", "wav", "ogg"]):
                if 'imgs' in i and not '-sm' in i:
                    images.append(i)
                    print(f'got {i}')
count = 0
for image in images:
    count+=1
    name = image.replace(f'{base}imgs/','')
    name = name.replace('.jpg','')
    name = f"darknetdiaries_episode_{count}_artwork_'{name}'.png"
    r = requests.get(image)
    with open(f'{save_directory}/{name}', 'wb') as f:
        f.write(r.content)
    print(f'saved {image} as {name}')
