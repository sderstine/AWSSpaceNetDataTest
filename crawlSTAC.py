import json

from pystac import Catalog, get_stac_version, read_file, read_dict
from pystac.extensions.eo import EOExtension
from pystac.extensions.label import LabelExtension
from pystac import Collection
from testAPI import *
from s3_upload import *
import os
import sys

os.environ['GDAL_HTTP_UNSAFESSL'] = 'YES'

response_dict = get_response_dict()
print(response_dict)

if response_dict is None:
    print("Error: Failed to retrieve response data from API.")
else:
    # Read the example catalog
    root_catalog = Catalog.from_dict(response_dict)

    # Print some basic metadata from the Catalog
    print(f"ID: {root_catalog.id}")
    print(f"Title: {root_catalog.title or 'N/A'}")
    print(f"Description: {root_catalog.description or 'N/A'}")
    #print(f"Links: {root_catalog.links or 'N/A'}")
    print(get_stac_version())
    # root_catalog.normalize_hrefs('https://maxar-opendata.s3.amazonaws.com/events/catalog.json')
    # list(root_catalog.get_children()) eweaeadwawdaswd

    links = list(root_catalog.get_child_links())
    for link in links:
        link = link.href

        link = link[1:len(link)]
        extended_link = 'https://maxar-opendata.s3.amazonaws.com/events' + link #end goal
        AOI = get_linkresponse_dict(extended_link)
        root_collection = Collection.from_dict(AOI)
        localLinks = list(root_collection.get_child_links())
        print(localLinks)

        for localLink in localLinks:
            localLink = localLink.href

                #localLink =localLink[1:len(localLink)]
                #extended = extended_link[0:len(extended_link)-16] + localLink
            if localLink == "./ard/acquisition_collections/1040010096551700_collection.json":
                extended = "https://maxar-opendata.s3.amazonaws.com/events/Brazil-Flooding-May24/ard/acquisition_collections/1040010096551700_collection.json" #changeable area

                Areas= get_linkresponse_dict(extended)
                root_locations = Collection.from_dict(Areas)
                locations = list(root_locations.get_item_links())
                print(f"Locations")
                print(locations)
                
                for location in locations:
                    location = location.href
                    print(f"Location")
                    print(location)

                    if location == "../22/213131133031/2024-05-08/1040010096551700.json":
                        address = "https://maxar-opendata.s3.amazonaws.com/events/Brazil-Flooding-May24/ard/22/213131133031/2024-05-08/1040010096551700.json"

                        images = get_linkresponse_dict(address)
                        print(images)
                        print(f"DONEHERE!!!!!")
                        #multispectral
                        print (images['assets']['ms_analytic']['href'])
                        #upload(images)
                        ms_analytic_path = "https://maxar-opendata.s3.amazonaws.com/events/Brazil-Flooding-May24/ard/22/213131133031/2024-05-08/1040010096551700-ms.tif"
                        pan_analytic_path = "https://maxar-opendata.s3.amazonaws.com/events/Brazil-Flooding-May24/ard/22/213131133031/2024-05-08/1040010096551700-pan.tif"
                        visual_path = "https://maxar-opendata.s3.amazonaws.com/events/Brazil-Flooding-May24/ard/22/213131133031/2024-05-08/1040010096551700-visual.tif"
                        
                        ms_analytic_image, ms_analytic_metadata = open_image(ms_analytic_path)
                        pan_analytic_image, pan_analytic_metadata = open_image(pan_analytic_path)
                        visual_image, visual_metadata = open_image(visual_path)

                        print("Multispectral image shape:", ms_analytic_image.shape)
                        print("Panchromatic image shape:", pan_analytic_image.shape)
                        print("Visual image shape:", visual_image.shape)    
                print("HERE")
                sys.exit()
            

