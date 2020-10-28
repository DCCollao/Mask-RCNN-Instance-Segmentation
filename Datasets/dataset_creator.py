import json
import os
from shutil import copyfile


"""

you need to create a root dir that contains the berkeley training images and 
it's labels in a .json file. For this you need to download both the images 
and the label separately and unzip the respective folders into a new one.

"""

# add the wanted labels in this list to filter
wanted_labels = ["drivable area", "traffic sign", "car", "bike"]

root_dir = "labels" # name of the root dir with pics+labels
wanted_dir = "train"  # will you make a "train" or "valid" set?

# Open the BDD labels, replace "dataset.json" for the file name below
with open(os.path.join(root_dir, "dataset.json"), "r") as file:
    dicts = (json.load(file))

# Create the new dict and fill it with the info
newdict = {}
# Will filter only the images that contain at least 1 object of interest
validimages = []

for i in dicts:
    # Basic data
    innerdict = {}
    innerdict["height"], innerdict["width"] = 720, 1280
    innerdict["filename"] = i["name"]

    # a for loop that will read the segmentation dict and create the correct
    # data
    regioncounter = 0
    regiondict = {}
    for x in i["labels"]:

        if x["category"] in wanted_labels:
            auxdict = {}
            x_coord = []
            y_coord = []
            # checks if it has the kind of labeled sections we need
            if "poly2d" in x:
                poly = x["poly2d"][0]["vertices"]
                for point in poly:
                    x_coord.append(point[0])
                    y_coord.append(point[1])

            if "box2d" in x:
                x_coord.append(x["box2d"]["x1"])
                y_coord.append(x["box2d"]["y1"])
                x_coord.append(x["box2d"]["x1"])
                y_coord.append(x["box2d"]["y2"])
                x_coord.append(x["box2d"]["x2"])
                y_coord.append(x["box2d"]["y2"])
                x_coord.append(x["box2d"]["x2"])
                y_coord.append(x["box2d"]["y1"])

            auxdict["shape_attributes"] = {"name": "polygon", "all_points_x":
                                           x_coord,
                                           "all_points_y": y_coord}
            auxdict["region_attributes"] = {"name": x["category"]}

            if x_coord and y_coord:
                regiondict[str(regioncounter)] = auxdict
                regioncounter += 1

    # adds to label file and valid images if there was at least 1 object of
    # interest on the pic

    if regiondict:
        innerdict["regions"] = regiondict
        newdict[i["name"]] = innerdict
        validimages.append(i["name"])

# creates the folder to dump the json and the relevant images
if not os.path.exists(wanted_dir):
    os.mkdir(wanted_dir)

# copies the valid images to the new folder
for image in validimages:
    copyfile(os.path.join(root_dir, image), os.path.join(wanted_dir, image))

# creates the new labels file and copies it to the new folder
with open(os.path.join(wanted_dir, "via_region_data.json"), "w") as file:
    json.dump(newdict, file)
