import dl
print('nor',dl.get(36.84,-76.32,36.90,-76.27,'nor-osm.json','motorway|trunk|primary|secondary|tertiary|unclassified|residential|service'),flush=True)
print('all',dl.get(40.57,-75.56,40.63,-75.44,'all-osm.json','motorway|trunk|primary|secondary|tertiary|unclassified|residential'),flush=True)
