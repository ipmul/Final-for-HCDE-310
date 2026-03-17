import requests

def search_artworks(artist, time_available, minutes_per_artwork=5):
    minutes = time_available * 60
    max_artworks = int(minutes / minutes_per_artwork)
    
    url = "https://api.artic.edu/api/v1/artworks/search"
    params = {
        "q": artist,
        "limit": max_artworks,
        "fields":"id,title,artist_title,gallery_title,place_of_origin,image_id"
    }
    
    response = requests.get(url, params=params)
    data = response.json()
    
    if "data" not in data or len(data["data"]) == 0:
        return []
    artworks = []
    for artwork in data["data"]:
        if artwork.get("_score", 0) > 1:
            artworks.append(artwork)
    if len(artworks) == 0:
        return []
    
    def get_gallery(artwork):
        gallery = artwork.get("gallery_title")
        if gallery is None:
            return ""
        return gallery
    
    artworks = sorted(artworks, key=get_gallery)
    
    return artworks
