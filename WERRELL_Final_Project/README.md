Song Clouds

Turn your playlist into a sky of clouds!

## Data Source
This program takes a CSV of a Spotify playlist created by [Exportify](https://exportify.net), and animates it as a data-visualization.

## Data Mapping
The animation is based on 4 different data points:
- Year released - Earlier songs appear at the bottom of the animation and more recent songs at the top.
- Popularity - The size of the cloud is based on the popularity of the song, with more popular songs appearing larger.
- Energy - The color of each cloud is based on the energy of the song, with more energetic songs appearing lighter.
- Tempo - The speed of the cloud moving left to right across the screen. The faster the tempo, the faster they move.

## Try it with your own playlist!
1. Go to https://exportify.net and export your Spotify playlist as a CSV.
2. Put the downloaded CSV file in the same folder as `clouds.py` and `Visual_Objects.py`.
3. Open **Visual_Objects.py**.
4. At the very bottom (around line 60) change this line
   `with open('spotify.csv', newline='', encoding='utf-8') as csvfile:`  
   to your file’s name, for example  
   `with open('my_favorite_playlist.csv', newline='', encoding='utf-8') as csvfile:`  
5. Save the file.
6. Run **clouds.py**.
7. Enjoy!

![Clouds](Clouds.gif)
