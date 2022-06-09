from importlib.resources import path
import ifcopenshell
import ifcopenshell.util
from ifcopenshell import geom
import rdflib

class Utils:
    def createGraph(self):
        g = rdflib.Graph()
        g_boot = rdflib.Graph().parse("https://w3id.org/bot#")
        g.namespace_manager.bind('boot', rdflib.URIRef('https://w3id.org/bot#'))
        g.namespace_manager.bind('inst', rdflib.URIRef('https://example.org/'))
        g.namespace_manager.bind('CBIM_Ontology', rdflib.URIRef('https://example.org/CBIM_Ontology'))
        return g

    def createBoundingBoxes(self, path, file):
        ifcFile = ifcopenshell.open(path/file.name)

        # IfcBuildingElement
        ifcBuildingElements = ifcFile.by_type("IFCBUILDINGELEMENT")

        # settings
        settings = geom.settings()
        settings.set(settings.USE_WORLD_COORDS, True)

        # Bounding box
        boundingBoxes = []
        for ifcBuildingElement in ifcBuildingElements:
            shape = geom.create_shape(settings, ifcBuildingElement)
            points = shape.geometry.verts
            points = tuple([
                tuple(points[i : i + 3])
                for i in range(0, len(points), 3)
                ])

            x_pos = [p[0] for p in points]
            y_pos = [p[1] for p in points]
            z_pos = [p[2] for p in points]

            x_min, x_max = min(x_pos), max(x_pos)
            y_min, y_max = min(y_pos), max(y_pos)
            z_min, z_max = min(z_pos), max(z_pos)

            box = (
                x_min, y_min, z_min,
                x_max, y_max, z_max
            )

            boundingBoxes.append({
                "GlobalId": ifcBuildingElement.GlobalId,
                "box": box,
                "name": ifcBuildingElement.Name
            })
        return boundingBoxes

    def collisionCheck(self, boundingBoxes, graph):
        count = 1
        countElementTotal = len(boundingBoxes)
        posElement = 0

        while(posElement < countElementTotal - 1):
            posElement2 = posElement + 1
            x1_min, y1_min, z1_min, x1_max, y1_max, z1_max = boundingBoxes[posElement]["box"]
            while(posElement2 <= countElementTotal - 1):      
                x2_min, y2_min, z2_min, x2_max, y2_max, z2_max = boundingBoxes[posElement2]["box"]
                
                pred1 = x1_min <= x2_max and x1_max >= x2_min
                pred2 = y1_min <= y2_max and y1_max >= y2_min
                pred3 = z1_min <= z2_max and z1_max >= z2_min

                if (pred1 and pred2 and pred3):
                    if (z1_max > z2_max):
                        Utils.createInfoRdf(self, graph, boundingBoxes, posElement, posElement2, count)
                    else:
                        Utils.createInfoRdf(self, graph, boundingBoxes, posElement2, posElement, count)
                    count +=1
                posElement2 +=1
            posElement+=1

    def createInfoRdf(self, graph, boundingBoxes, posElement, posElement2, count):        
        buildingElementUri = rdflib.URIRef('https://example.org/buildingElement' + boundingBoxes[posElement]["GlobalId"])
        buildingElementUri2 = rdflib.URIRef('https://example.org/buildingElement' + boundingBoxes[posElement2]["GlobalId"])          
        graph.add((buildingElementUri, rdflib.RDF.type, rdflib.URIRef('https://w3id.org/bot#Element')))
        graph.add((buildingElementUri, rdflib.URIRef('https://example.org/touches'),buildingElementUri2))
        relSpatial1 = rdflib.URIRef('https://example.org/CBIM_Ontology/' + 'relSpatial'+ str(count))
        graph.add((relSpatial1, rdflib.URIRef('https://example.org/hasSubject'),buildingElementUri))
        graph.add((relSpatial1, rdflib.URIRef('https://example.org/hasObject'),buildingElementUri2))              
        graph.add((relSpatial1, rdflib.URIRef('https://example.org/CBIM_Ontology/inContact'), rdflib.Literal(True)))