import glob

from gpxplotter import add_segment_to_map, create_folium_map, read_gpx_file

files = glob.glob("input/*.gpx")

former_fit_files = glob.glob("input/fit_to_gpx/*.gpx")

files.append(former_fit_files)

# Using a subset for tests.
# files = files[0:15]

the_map = create_folium_map()

for file in files:
    print(file)
    for track in read_gpx_file(file):
        for i, segment in enumerate(track["segments"]):
            add_segment_to_map(the_map=the_map, segment=segment, add_start_end=False, line_options={"opacity": 0.5, "weight": 5})


# To store the map as a HTML page:
the_map.save("map_005.html")


# To display the map in a Jupyter notebook:
# the_map
