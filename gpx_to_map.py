import glob

from gpxplotter import add_segment_to_map, create_folium_map, read_gpx_file

files = glob.glob("input/*.gpx")

# Append converted .fit files
former_fit_files = glob.glob("input/fit_to_gpx/*.gpx")
files.extend(former_fit_files)

# Using a subset for tests.
# files = files[0:55]

the_map = create_folium_map()

for file in files:
    print(file)
    # TODO Add check to filter out empty .gpx files (<1kb).
    for track in read_gpx_file(file):
        for i, segment in enumerate(track["segments"]):  # TODO Use tqdm here.
            add_segment_to_map(the_map=the_map, segment=segment, add_start_end=False, line_options={"opacity": 0.30, "weight": 5, "color": "red"})

# To store the map as a HTML page:
the_map.save("output/map.html")


# To display the map in a Jupyter notebook:
# the_map
