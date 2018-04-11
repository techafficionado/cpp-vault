from xml.etree import ElementTree
import keytree
from shapely.geometry import Point, shape, asShape

###################################################################################################
# populate service boundaries
###################################################################################################
def populateServiceBoundary():
    kmlFile = None
    try:
        if conf:
            kmlFile = g_grpmDir + conf['kmlFile'] 
    except Exception as e:
        dbLogger.error("Failed to load KML file. Exception: " + str(e))
        return

    serv_bounds = {}
    doc = open(kmlFile, "rb").read()
    tree = ElementTree.fromstring(str(doc))
    kmlns = tree.tag.split('}')[0][1:]
    pmarks = tree.findall("*/{%s}Placemark" % kmlns)
    for pmark in pmarks:
        tag = re.findall("}(\w+)", str(pmark[0]))[0]
        if tag == "name":
            kmlNetwork = str(pmark[0].text)
            f = keytree.feature(pmark)
            shape = asShape(f.geometry)
            serv_bounds[str(kmlNetwork)] = shape
    # if multigeometry
    mgs = tree.findall("*/{%s}MultiGeometry" % kmlns)
    for mg in mgs:
        for pm in mg:
            tag = re.findall("}(\w+)", str(pm[0]))[0]
            if tag == "name":
                kmlNetwork = str(pm[0].text)
                #dbLogger.info("kmlNetwork:"+str(kmlNetwork))
                f = keytree.feature(pm)
                shape = asShape(f.geometry)
                if str(kmlNetwork) in serv_bounds.keys():
                    serv_bounds[str(kmlNetwork)].append(shape)
                else:
                    serv_bounds[str(kmlNetwork)] = [shape]
    dbLogger.info("serv_bounds:"+str(serv_bounds))
    return serv_bounds


###################################################################################################
# check if given lat and lon in network
###################################################################################################
def checkServiceBoundary(lon, lat, network):
    in_poly = None
    try:
        try:
            sh = servBounds[str(network)]
        except KeyError:
            sh = None

        # if multigeometry with multiple contours
        if isinstance(sh, list):
            for shape in sh:
                if shape is not None:
                    inpoly = shape.contains(Point(lon, lat))
                    if inpoly is True:
                        in_poly = 1
                        return in_poly
                    else:
                        in_poly = 0
        # if not multigeometry
        else:
            if sh is not None:
                inpoly = sh.contains(Point(lon, lat))
                if inpoly is True:
                    in_poly = 1
                else:
                    in_poly = 0
    except Exception as e:
        dbLogger.error("Exception: " + str(e))
    return in_poly
