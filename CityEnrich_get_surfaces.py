from surfacegml import SurfaceGML



def sort_outer_surfaces(gml_surfaces):
    OuterWalls = []
    Roofs = []
    GroundPlate = []
    Surface_lists = []
    i = 0
    e = 0
    for surface in gml_surfaces:
        print(surface.surface_tilt)
        print(surface.surface_orientation)
        if surface.surface_tilt is not None and surface.name is None:

            if surface.surface_tilt == 90:
                i += 1
                surface.name = f"OuterWall_{i}"
                OuterWalls.append(surface)
            elif surface.surface_tilt == 0 and \
                    surface.surface_orientation == \
                    -2:
                surface.name = f"GroundSlab"
                GroundPlate.append(surface)
            else:
                e += 1
                surface.name = f"Roof_{e}"
                Roofs.append(surface)
    Surface_lists.append(OuterWalls)
    Surface_lists.append(Roofs)
    Surface_lists.append(GroundPlate)
    return Surface_lists


def get_gml_surfaces(city_object, namespace):
    """
    This Function extracts the position coordinates of CityGML Building surfaces and passes them to the SurfaceGML
    class for processing and finally populates the TEASER building gml_surfaces list for further calculation.

    :param namespace: lxml.msmap()
            Original namespaces from CityGML file (root)
    :param bldg: TEASER building()
            TEASER Building Object
    :param city_object: lxml object
            CityGML City Object(Building)
    """
    gml_surfaces = []

    lod = get_lod(city_object=city_object)
    if lod == 0:
        if city_object.find(".//bldg:measuredHeight", namespace) is not None:
            from itertools import chain
            height = float(city_object.find(".//bldg:measuredHeight", namespace).text)
            a_list = city_object.find("bldg:lod0FootPrint/gml:MultiSurface/gml:surfaceMember/gml:Polygon/"
                                      "gml:exterior/gml:LinearRing/gml:posList", namespace).text.split()
            map_object = map(float, a_list)
            coord_list = list(map_object)
            base = coord_list
            roof = [base[0], base[1], base[2] + height, base[9], base[10], base[11] + height, base[6], base[7],
                    base[8] + height, base[3], base[4], base[5] + height, base[12], base[13], base[14] + height]

            help_list_base = list(zip(*[iter(base)] * 3))
            help_list_roof = list(zip(*[iter(roof)] * 3))

            wall_help_1 = [help_list_base[0], help_list_base[1], help_list_roof[3], help_list_roof[0],
                           help_list_base[0]]
            wall_list_1 = list(chain(*wall_help_1))

            wall_help_2 = [help_list_base[0], help_list_base[3], help_list_roof[1], help_list_roof[0],
                           help_list_base[0]]
            wall_list_2 = list(chain(*wall_help_2))

            wall_help_3 = [help_list_base[2], help_list_base[1], help_list_roof[3], help_list_roof[2],
                           help_list_base[2]]
            wall_list_3 = list(chain(*wall_help_3))

            wall_help_4 = [help_list_base[2], help_list_base[3], help_list_roof[1], help_list_roof[2],
                           help_list_base[2]]
            wall_list_4 = list(chain(*wall_help_4))

            gml_surfaces.append(SurfaceGML(base))
            gml_surfaces.append(SurfaceGML(roof))
            gml_surfaces.append(SurfaceGML(wall_list_1))
            gml_surfaces.append(SurfaceGML(wall_list_2))
            gml_surfaces.append(SurfaceGML(wall_list_3))
            gml_surfaces.append(SurfaceGML(wall_list_4))

        else:
            print("The LoD0 Model, no building-height is defined, set a height or no calculations are possible")

    elif lod == 1:
        boundary_surfaces = city_object.findall('./bldg:lod1Solid', namespace)

    elif lod == 2 or lod == 3:
        boundary_surfaces = city_object.findall('./bldg:boundedBy', namespace)

    if not lod == 0:
        for bound_surf in boundary_surfaces:
            for surf_member in bound_surf.iter():

                # if surf_member.tag == "{http://www.opengis.net/gml}name":
                #     print("Surface Name:", surf_member.text)

                # modelling option 1
                if surf_member.tag == "{http://www.opengis.net/gml}exterior":
                    for surf_pos in surf_member.iter():
                        if "{http://www.opengis.net/gml}posList" in surf_member:
                            if surf_pos.tag == "{http://www.opengis.net/gml}posList":
                                a_list = surf_pos.text.split()
                                map_object = map(float, a_list)
                                coord_list = list(map_object)
                                help = SurfaceGML(coord_list)
                                if help.surface_area > 1:
                                    gml_surfaces.append(help)

                        # modelling option 2
                        else:
                            try:
                                if surf_pos.tag == "{http://www.opengis.net/gml}LinearRing":
                                    position_list_help = []
                                    # for pos in surf_pos.iter():
                                    for pos in surf_pos:
                                        a_list = pos.text.split()
                                        map_object = map(float, a_list)
                                        coord_list = list(map_object)
                                        position_list_help.extend(coord_list)
                                    help = SurfaceGML(position_list_help)
                                    if help.surface_area > 1:
                                        gml_surfaces.append(help)
                            except:
                                pass
    if lod == 3 or lod == 4:
        openings_name = "Window"
        for bound_surf in boundary_surfaces:
            for surf_member in bound_surf.iter():
                if surf_member.tag == "{http://www.opengis.net/citygml/building/2.0}opening":
                    # if surf_member.tag == "{http://www.opengis.net/gml}name":
                    #     openings_name = surf_member.text
                    #     print("Opening Name:", surf_member.text)
                    for openings in surf_member.iter():
                        if openings.tag == "{http://www.opengis.net/gml}exterior":
                            for openings_pos in openings.iter():
                                if "{http://www.opengis.net/gml}posList" in surf_member:
                                    # modelling option 1
                                    if openings_pos.tag == "{http://www.opengis.net/gml}posList":
                                        a_list = openings_pos.text.split()
                                        map_object = map(float, a_list)
                                        coord_list = list(map_object)
                                        opening = SurfaceGML(coord_list)
                                        opening.name = openings_name
                                        # print(opening.surface_area)
                                        gml_surfaces.append(opening)
                                else:
                                    # modelling option 2
                                    if openings_pos.tag == "{http://www.opengis.net/gml}LinearRing":
                                        position_list_help = []
                                        for pos in openings_pos.iter():
                                            a_list = pos.text.split()
                                            map_object = map(float, a_list)
                                            coord_list = list(map_object)
                                            position_list_help.extend(coord_list)
                                        help = SurfaceGML(position_list_help)
                                        help.name = openings_name
                                        # print(help.surface_area)
                                        gml_surfaces.append(help)

    return sort_outer_surfaces(gml_surfaces)


def get_lod(city_object):
    """
    Help Function, gets and returns the Level of Detail of a CityGML Building.
    By Simon Raming CityATB

    :param city_object: lxml CityGML City Object(Building)
    :return: CityGML City Object Level of Detail
    """
    lods = []
    for elem in city_object.iter():
        # print(elem)
        try:
            if elem.tag.split("}")[1].startswith('lod'):
                lods.append(elem.tag.split('}')[1][3])
        except:
            pass

    if lods != []:
        lods = list(set(lods))
        if len(lods) > 1:
            print("Check file for LoDs!!!")
        lods.sort()
        lod = int(lods[0])
    return lod