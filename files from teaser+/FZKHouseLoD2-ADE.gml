<?xml version="1.0" encoding="utf-8" standalone="yes"?>
<!--Erzeugt mit KIT (www.kit.edu) GML-Toolbox, Erstellungsdatum: 06/18/18-->
<core:CityModel xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
 xsi:schemaLocation="http://www.opengis.net/citygml/2.0 http://www.citygmlwiki.org/images/a/ac/EnergyADE.xsd"
 xmlns:water="http://www.opengis.net/citygml/waterbody/2.0"
 xmlns:xAL="urn:oasis:names:tc:ciq:xsdschema:xAL:2.0"
 xmlns:app="http://www.opengis.net/citygml/appearance/2.0"
 xmlns:genobj="http://www.opengis.net/citygml/generics/2.0"
 xmlns:xs="http://www.w3.org/2001/XMLSchema"
 xmlns:veget="http://www.opengis.net/citygml/vegetation/2.0"
 xmlns:trpt="http://www.opengis.net/citygml/transportation/2.0"
 xmlns:noise="http://www.citygml.org/ade/noise_de/2.0"
 xmlns:relief="http://www.opengis.net/citygml/relief/2.0"
 xmlns:utility="http://www.citygml.org/ade/utility/0.9.2"
 xmlns:tun="http://www.citygml.org/tunnel/2.0" xmlns:wfs="http://www.opengis.net/wfs"
 xmlns:xlink="http://www.w3.org/1999/xlink"
 xmlns:texsurf="http://www.opengis.net/citygml/texturedsurface/2.0"
 xmlns:brid="http://www.citygml.org/bridge/2.0" xmlns:core="http://www.opengis.net/citygml/2.0"
 xmlns:gml="http://www.opengis.net/gml" xmlns:landuse="http://www.opengis.net/citygml/landuse/2.0"
 xmlns:group="http://www.opengis.net/citygml/cityobjectgroup/2.0"
 xmlns:furnit="http://www.opengis.net/citygml/cityfurniture/2.0"
 xmlns:bldg="http://www.opengis.net/citygml/building/2.0"
 xmlns:energy="http://www.sig3d.org/citygml/2.0/energy/1.0"
 xmlns:rep="http://www.citygml.org/ade/georep/2.0" gml:id="GML_81edc4b5-b061-4565-b3ac-8223f6a8695d">
  <gml:boundedBy>
    <gml:Envelope srsName="urn:adv:crs:ETRS89_UTM32">
      <gml:lowerCorner>458877 5438353 -0.2</gml:lowerCorner>
      <gml:upperCorner>458889 5438363 6.31769</gml:upperCorner>
    </gml:Envelope>
  </gml:boundedBy>
  <core:cityObjectMember>
    <bldg:Building gml:id="UUID_d281adfc-4901-0f52-540b-4cc1a9325f82">
      <gml:description>FZK-Haus (Forschungszentrum Karlsruhe, now KIT), created by Karl-Heinz
                Haefele </gml:description>
      <gml:name>AC14-FZK-Haus</gml:name>
      <gml:boundedBy>
        <gml:Envelope srsName="urn:adv:crs:ETRS89_UTM32">
          <gml:lowerCorner>458877 5438353 -0.2</gml:lowerCorner>
          <gml:upperCorner>458889 5438363 6.31769</gml:upperCorner>
        </gml:Envelope>
      </gml:boundedBy>
      <core:creationDate>2010-12-01</core:creationDate>    
      <bldg:class>1000</bldg:class>
      <bldg:function>1000</bldg:function>
      <bldg:usage>1000</bldg:usage>
      <bldg:yearOfConstruction>1980</bldg:yearOfConstruction>
      <bldg:roofType>1030</bldg:roofType>
      <!--<bldg:measuredHeight uom="m">6.52</bldg:measuredHeight>-->
      <bldg:storeysAboveGround>2</bldg:storeysAboveGround>
      <bldg:storeyHeightsAboveGround uom="m">3.26</bldg:storeyHeightsAboveGround>
      <!--<bldg:storeysBelowGround>0</bldg:storeysBelowGround>-->
      <bldg:lod2Solid>
        <gml:Solid gml:id="GML_6dc0fc4e-b45c-4c71-9880-e39f23521776">
          <gml:exterior>
            <gml:CompositeSurface srsName="urn:adv:crs:ETRS89_UTM32" gml:id="GML_ff8a7e7b-76a6-43dc-bf68-5a0d132b6a2f">
              <gml:surfaceMember xlink:href="#PolyID7350_878_759628_120742" />
              <gml:surfaceMember xlink:href="#PolyID7351_1722_416019_316876" />
              <gml:surfaceMember xlink:href="#PolyID7352_230_209861_355851" />
              <gml:surfaceMember xlink:href="#PolyID7353_166_774155_320806" />
              <gml:surfaceMember xlink:href="#PolyID7354_1362_450904_410226" />
              <gml:surfaceMember xlink:href="#PolyID7355_537_416207_260034" />
              <gml:surfaceMember xlink:href="#PolyID7356_612_880782_415367" />
            </gml:CompositeSurface>
          </gml:exterior>
        </gml:Solid>
      </bldg:lod2Solid>
      <bldg:boundedBy>
        <bldg:WallSurface gml:id="GML_5856d7ad-5e34-498a-817b-9544bfbb1475">
          <gml:name>Outer Wall 1 (West)</gml:name>
          <gml:boundedBy>
            <gml:Envelope srsName="urn:adv:crs:ETRS89_UTM32">
              <gml:lowerCorner>458877 5438353 -0.2</gml:lowerCorner>
              <gml:upperCorner>458877 5438363 6.31769</gml:upperCorner>
            </gml:Envelope>
          </gml:boundedBy>
          <bldg:lod2MultiSurface>
            <gml:MultiSurface srsName="urn:adv:crs:ETRS89_UTM32" gml:id="GML_da2a0d15-ae6e-4e93-a6ae-81d1ce8cce9a">
              <gml:surfaceMember>
                <gml:Polygon srsName="urn:adv:crs:ETRS89_UTM32" gml:id="PolyID7350_878_759628_120742">
                  <gml:exterior>
                    <gml:LinearRing gml:id="PolyID7350_878_759628_120742_0">
                      <gml:posList srsDimension="3" count="6">458877 5438358 6.31769 458877 5438363 3.43094 458877 5438363 -0.2 458877 5438353 -0.2 458877 5438353 3.43094 458877 5438358 6.31769 </gml:posList>
                    </gml:LinearRing>
                  </gml:exterior>
                </gml:Polygon>
              </gml:surfaceMember>
            </gml:MultiSurface>
          </bldg:lod2MultiSurface>
        </bldg:WallSurface>
      </bldg:boundedBy>
      <bldg:boundedBy>
        <bldg:WallSurface gml:id="GML_d38cf762-c29d-4491-88c9-bdc89e141978">
          <gml:name>Outer Wall 2 (South)</gml:name>
          <gml:boundedBy>
            <gml:Envelope srsName="urn:adv:crs:ETRS89_UTM32">
              <gml:lowerCorner>458877 5438353 -0.2</gml:lowerCorner>
              <gml:upperCorner>458889 5438353 3.43094</gml:upperCorner>
            </gml:Envelope>
          </gml:boundedBy>
          <bldg:lod2MultiSurface>
            <gml:MultiSurface srsName="urn:adv:crs:ETRS89_UTM32" gml:id="GML_08917888-17fb-420d-9d49-a85621bf70b9">
              <gml:surfaceMember>
                <gml:Polygon srsName="urn:adv:crs:ETRS89_UTM32" gml:id="PolyID7351_1722_416019_316876">
                  <gml:exterior>
                    <gml:LinearRing gml:id="PolyID7351_1722_416019_316876_0">
                      <gml:posList srsDimension="3" count="5">458889 5438353 3.43094 458877 5438353 3.43094 458877 5438353 -0.2 458889 5438353 -0.2 458889 5438353 3.43094 </gml:posList>
                    </gml:LinearRing>
                  </gml:exterior>
                </gml:Polygon>
              </gml:surfaceMember>
            </gml:MultiSurface>
          </bldg:lod2MultiSurface>
        </bldg:WallSurface>
      </bldg:boundedBy>
      <bldg:boundedBy>
        <bldg:WallSurface gml:id="GML_8e5db638-e46a-4739-a98a-2fc2d39c9069">
          <gml:name>Outer Wall 3 (East)</gml:name>
          <gml:boundedBy>
            <gml:Envelope srsName="urn:adv:crs:ETRS89_UTM32">
              <gml:lowerCorner>458889 5438353 -0.2</gml:lowerCorner>
              <gml:upperCorner>458889 5438363 6.31769</gml:upperCorner>
            </gml:Envelope>
          </gml:boundedBy>
          <bldg:lod2MultiSurface>
            <gml:MultiSurface srsName="urn:adv:crs:ETRS89_UTM32" gml:id="GML_8ee038a3-1247-4cb9-b3a0-f9b2a9151993">
              <gml:surfaceMember>
                <gml:Polygon srsName="urn:adv:crs:ETRS89_UTM32" gml:id="PolyID7352_230_209861_355851">
                  <gml:exterior>
                    <gml:LinearRing gml:id="PolyID7352_230_209861_355851_0">
                      <gml:posList srsDimension="3" count="6">458889 5438358 6.31769 458889 5438353 3.43094 458889 5438353 -0.2 458889 5438363 -0.2 458889 5438363 3.43094 458889 5438358 6.31769 </gml:posList>
                    </gml:LinearRing>
                  </gml:exterior>
                </gml:Polygon>
              </gml:surfaceMember>
            </gml:MultiSurface>
          </bldg:lod2MultiSurface>
        </bldg:WallSurface>
      </bldg:boundedBy>
      <bldg:boundedBy>
        <bldg:RoofSurface gml:id="GML_875d470b-32b4-4985-a4c8-0f02caa342a2">
          <gml:name>Roof 1 (North)</gml:name>
          <gml:boundedBy>
            <gml:Envelope srsName="urn:adv:crs:ETRS89_UTM32">
              <gml:lowerCorner>458877 5438358 3.43094</gml:lowerCorner>
              <gml:upperCorner>458889 5438363 6.31769</gml:upperCorner>
            </gml:Envelope>
          </gml:boundedBy>
          <bldg:lod2MultiSurface>
            <gml:MultiSurface srsName="urn:adv:crs:ETRS89_UTM32" gml:id="GML_5ab9d859-729e-422a-807f-f1db90f64743">
              <gml:surfaceMember>
                <gml:Polygon srsName="urn:adv:crs:ETRS89_UTM32" gml:id="PolyID7353_166_774155_320806">
                  <gml:exterior>
                    <gml:LinearRing gml:id="PolyID7353_166_774155_320806_0">
                      <gml:posList srsDimension="3" count="5">458877 5438358 6.31769 458889 5438358 6.31769 458889 5438363 3.43094 458877 5438363 3.43094 458877 5438358 6.31769 </gml:posList>
                    </gml:LinearRing>
                  </gml:exterior>
                </gml:Polygon>
              </gml:surfaceMember>
            </gml:MultiSurface>
          </bldg:lod2MultiSurface>
        </bldg:RoofSurface>
      </bldg:boundedBy>
      <bldg:boundedBy>
        <bldg:WallSurface gml:id="GML_0f30f604-e70d-4dfe-ba35-853bc69609cc">
          <gml:name>Outer Wall 4 (North)</gml:name>
          <gml:boundedBy>
            <gml:Envelope srsName="urn:adv:crs:ETRS89_UTM32">
              <gml:lowerCorner>458877 5438363 -0.2</gml:lowerCorner>
              <gml:upperCorner>458889 5438363 3.43094</gml:upperCorner>
            </gml:Envelope>
          </gml:boundedBy>
          <bldg:lod2MultiSurface>
            <gml:MultiSurface srsName="urn:adv:crs:ETRS89_UTM32" gml:id="GML_bb6cf275-7859-4692-9faa-cb9bec574cf4">
              <gml:surfaceMember>
                <gml:Polygon srsName="urn:adv:crs:ETRS89_UTM32" gml:id="PolyID7354_1362_450904_410226">
                  <gml:exterior>
                    <gml:LinearRing gml:id="PolyID7354_1362_450904_410226_0">
                      <gml:posList srsDimension="3" count="5">458877 5438363 3.43094 458889 5438363 3.43094 458889 5438363 -0.2 458877 5438363 -0.2 458877 5438363 3.43094 </gml:posList>
                    </gml:LinearRing>
                  </gml:exterior>
                </gml:Polygon>
              </gml:surfaceMember>
            </gml:MultiSurface>
          </bldg:lod2MultiSurface>
        </bldg:WallSurface>
      </bldg:boundedBy>
      <bldg:boundedBy>
        <bldg:RoofSurface gml:id="GML_eeb6796a-e261-4d3b-a6f2-475940cca80a">
          <gml:name>Roof 2 (South)</gml:name>
          <gml:boundedBy>
            <gml:Envelope srsName="urn:adv:crs:ETRS89_UTM32">
              <gml:lowerCorner>458877 5438353 3.43094</gml:lowerCorner>
              <gml:upperCorner>458889 5438358 6.31769</gml:upperCorner>
            </gml:Envelope>
          </gml:boundedBy>
          <bldg:lod2MultiSurface>
            <gml:MultiSurface srsName="urn:adv:crs:ETRS89_UTM32" gml:id="GML_944a2a58-7e85-4e85-af47-34143941be40">
              <gml:surfaceMember>
                <gml:Polygon srsName="urn:adv:crs:ETRS89_UTM32" gml:id="PolyID7355_537_416207_260034">
                  <gml:exterior>
                    <gml:LinearRing gml:id="PolyID7355_537_416207_260034_0">
                      <gml:posList srsDimension="3" count="5">458889 5438353 3.43094 458889 5438358 6.31769 458877 5438358 6.31769 458877 5438353 3.43094 458889 5438353 3.43094 </gml:posList>
                    </gml:LinearRing>
                  </gml:exterior>
                </gml:Polygon>
              </gml:surfaceMember>
            </gml:MultiSurface>
          </bldg:lod2MultiSurface>
        </bldg:RoofSurface>
      </bldg:boundedBy>
      <bldg:boundedBy>
        <bldg:GroundSurface gml:id="GML_257a8dde-8194-4ca3-b581-abd591dcd6a3">
          <gml:description>Bodenplatte</gml:description>
          <gml:name>Base Surface</gml:name>
          <gml:boundedBy>
            <gml:Envelope srsName="urn:adv:crs:ETRS89_UTM32">
              <gml:lowerCorner>458877 5438353 -0.2</gml:lowerCorner>
              <gml:upperCorner>458889 5438363 -0.2</gml:upperCorner>
            </gml:Envelope>
          </gml:boundedBy>
          <bldg:lod2MultiSurface>
            <gml:MultiSurface srsName="urn:adv:crs:ETRS89_UTM32" gml:id="GML_1682543a-abf0-4976-a506-0bc704ff67d8">
              <gml:surfaceMember>
                <gml:Polygon srsName="urn:adv:crs:ETRS89_UTM32" gml:id="PolyID7356_612_880782_415367">
                  <gml:exterior>
                    <gml:LinearRing gml:id="PolyID7356_612_880782_415367_0">
                      <gml:posList srsDimension="3" count="5">458889 5438353 -0.2 458877 5438353 -0.2 458877 5438363 -0.2 458889 5438363 -0.2 458889 5438353 -0.2 </gml:posList>
                    </gml:LinearRing>
                  </gml:exterior>
                </gml:Polygon>
              </gml:surfaceMember>
            </gml:MultiSurface>
          </bldg:lod2MultiSurface>
        </bldg:GroundSurface>
      </bldg:boundedBy>
      <energy:constructionWeight>medium</energy:constructionWeight>
      <energy:volume>
        <energy:VolumeType>
          <energy:type>grossVolume</energy:type>
          <energy:value uom="m3">608.91789367799</energy:value>
        </energy:VolumeType>
      </energy:volume>
      <energy:referencePoint>
        <gml:Point srsName="urn:adv:crs:ETRS89_UTM32" gml:id="GML_42027936-d254-4fa5-98c6-0a0386fce9a5">
          <gml:pos>458883 5438358 3.05884</gml:pos>
        </gml:Point>
      </energy:referencePoint>
      <energy:thermalZone>
        <energy:ThermalZone gml:id="GML_615f6fa3-b3c6-432c-aa93-41fb7aaa64c9">
          <gml:boundedBy>
            <gml:Envelope srsName="urn:adv:crs:ETRS89_UTM32">
              <gml:lowerCorner>458877 5438353 -0.2</gml:lowerCorner>
              <gml:upperCorner>458889 5438363 6.31769</gml:upperCorner>
            </gml:Envelope>
          </gml:boundedBy>
          <energy:contains xlink:href="#GML_296e5877-8f24-4437-adc0-cbdb61f2d583" />
          <energy:floorArea>
            <energy:FloorArea>
              <energy:type>grossFloorArea</energy:type>
              <energy:value uom="m2">240</energy:value>
            </energy:FloorArea>
          </energy:floorArea>
          <energy:volume>
            <energy:VolumeType>
              <energy:type>grossVolume</energy:type>
              <energy:value uom="m3">608.91789367799</energy:value>
            </energy:VolumeType>
          </energy:volume>
          <energy:isCooled>false</energy:isCooled>
          <energy:isHeated>true</energy:isHeated>
          <energy:volumeGeometry>
            <gml:Solid gml:id="GML_29571d2d-200a-47b1-9ceb-8d67956183d3">
              <gml:exterior>
                <gml:CompositeSurface srsName="urn:adv:crs:ETRS89_UTM32" gml:id="GML_cb246983-458c-4273-9876-1087663471af">
                  <gml:surfaceMember xlink:href="#PolyID7350_878_759628_120742" />
                  <gml:surfaceMember xlink:href="#PolyID7351_1722_416019_316876" />
                  <gml:surfaceMember xlink:href="#PolyID7352_230_209861_355851" />
                  <gml:surfaceMember xlink:href="#PolyID7353_166_774155_320806" />
                  <gml:surfaceMember xlink:href="#PolyID7354_1362_450904_410226" />
                  <gml:surfaceMember xlink:href="#PolyID7355_537_416207_260034" />
                  <gml:surfaceMember xlink:href="#PolyID7356_612_880782_415367" />
                </gml:CompositeSurface>
              </gml:exterior>
            </gml:Solid>
          </energy:volumeGeometry>
          <energy:boundedBy>
            <energy:ThermalBoundary gml:id="GML_06482fd9-1fe9-4de0-be15-ded2c8bffe68">
              <gml:boundedBy>
                <gml:Envelope srsName="urn:adv:crs:ETRS89_UTM32">
                  <gml:lowerCorner>458877 5438363 -0.2</gml:lowerCorner>
                  <gml:upperCorner>458889 5438363 3.43094</gml:upperCorner>
                </gml:Envelope>
              </gml:boundedBy>
              <energy:thermalBoundaryType>outerWall</energy:thermalBoundaryType>
              <energy:azimuth uom="deg">0</energy:azimuth>
              <energy:inclination uom="deg">90</energy:inclination>
              <energy:area uom="m2">43.5712812921102</energy:area>
              <energy:surfaceGeometry>
                <gml:MultiSurface gml:id="GML_eb2d16ad-21e0-4f86-962d-32afbb067d6f">
                  <gml:surfaceMember>
                    <gml:Polygon srsName="urn:adv:crs:ETRS89_UTM32" gml:id="GML_f26ef662-ccb0-4dfd-9fec-f8c5d7ab0093">
                      <gml:exterior>
                        <gml:LinearRing gml:id="GML_3a0d4e2b-3470-42fc-8c83-b9325414d8cc">
                          <gml:posList srsDimension="3" count="5">458877 5438363 3.43094 458889 5438363 3.43094 458889 5438363 -0.2 458877 5438363 -0.2 458877 5438363 3.43094 </gml:posList>
                        </gml:LinearRing>
                      </gml:exterior>
                    </gml:Polygon>
                  </gml:surfaceMember>
                </gml:MultiSurface>
              </energy:surfaceGeometry>
              <energy:construction xlink:href="#GML_14ffe1b2-1753-427f-8e59-8b17ce397f5c" />
              <energy:contains>
                <energy:ThermalOpening gml:id="GML_b7c07a84-c325-4776-81a7-3c1648aab7ef">
                  <energy:area uom="m2">17.42851251684408</energy:area>
                  <energy:construction xlink:href="#GML_d8622004-ac1b-4c96-901d-86c53318207d" />
                </energy:ThermalOpening>
              </energy:contains>
              <energy:delimits xlink:href="#GML_615f6fa3-b3c6-432c-aa93-41fb7aaa64c9" />
            </energy:ThermalBoundary>
          </energy:boundedBy>
          <energy:boundedBy>
            <energy:ThermalBoundary gml:id="GML_caf17518-ced6-4ff9-96db-c2ee0e5aed97">
              <gml:boundedBy>
                <gml:Envelope srsName="urn:adv:crs:ETRS89_UTM32">
                  <gml:lowerCorner>458877 5438353 -0.2</gml:lowerCorner>
                  <gml:upperCorner>458877 5438363 6.31769</gml:upperCorner>
                </gml:Envelope>
              </gml:boundedBy>
              <energy:thermalBoundaryType>outerWall</energy:thermalBoundaryType>
              <energy:azimuth uom="deg">270</energy:azimuth>
              <energy:inclination uom="deg">90</energy:inclination>
              <energy:area uom="m2">50.743157806499156</energy:area>
              <energy:surfaceGeometry>
                <gml:MultiSurface gml:id="GML_6d8f8d05-f26c-48ba-b6cb-7d2806c7d6cf">
                  <gml:surfaceMember>
                    <gml:Polygon srsName="urn:adv:crs:ETRS89_UTM32" gml:id="GML_4196b804-38e6-425d-bb97-42f0c80d75ec">
                      <gml:exterior>
                        <gml:LinearRing gml:id="GML_b339c025-a181-4f88-9451-e3a733867093">
                          <gml:posList srsDimension="3" count="6">458877 5438358 6.31769 458877 5438363 3.43094 458877 5438363 -0.2 458877 5438353 -0.2 458877 5438353 3.43094 458877 5438358 6.31769 </gml:posList>
                        </gml:LinearRing>
                      </gml:exterior>
                    </gml:Polygon>
                  </gml:surfaceMember>
                </gml:MultiSurface>
              </energy:surfaceGeometry>
              <energy:construction xlink:href="#GML_14ffe1b2-1753-427f-8e59-8b17ce397f5c" />
              <energy:contains>
                <energy:ThermalOpening gml:id="GML_1760c10f-48a6-4dd6-973b-43470a80353c">
                  <energy:area uom="m2">20.297263122599663</energy:area>
                  <energy:construction xlink:href="#GML_d8622004-ac1b-4c96-901d-86c53318207d" />
                </energy:ThermalOpening>
              </energy:contains>
              <energy:delimits xlink:href="#GML_615f6fa3-b3c6-432c-aa93-41fb7aaa64c9" />
            </energy:ThermalBoundary>
          </energy:boundedBy>
          <energy:boundedBy>
            <energy:ThermalBoundary gml:id="GML_30d58eaa-e2fc-426f-b74d-bffe9212649b">
              <gml:boundedBy>
                <gml:Envelope srsName="urn:adv:crs:ETRS89_UTM32">
                  <gml:lowerCorner>458889 5438353 -0.2</gml:lowerCorner>
                  <gml:upperCorner>458889 5438363 6.31769</gml:upperCorner>
                </gml:Envelope>
              </gml:boundedBy>
              <energy:thermalBoundaryType>outerWall</energy:thermalBoundaryType>
              <energy:azimuth uom="deg">90</energy:azimuth>
              <energy:inclination uom="deg">90</energy:inclination>
              <energy:area uom="m2">50.743157806499156</energy:area>
              <energy:surfaceGeometry>
                <gml:MultiSurface gml:id="GML_db7076af-725d-4014-830c-ed4920743d56">
                  <gml:surfaceMember>
                    <gml:Polygon srsName="urn:adv:crs:ETRS89_UTM32" gml:id="GML_99c41fee-8737-499b-a019-3b175dae21cb">
                      <gml:exterior>
                        <gml:LinearRing gml:id="GML_5b7ec854-d459-42ec-ab99-fb76dffaddb7">
                          <gml:posList srsDimension="3" count="6">458889 5438358 6.31769 458889 5438353 3.43094 458889 5438353 -0.2 458889 5438363 -0.2 458889 5438363 3.43094 458889 5438358 6.31769 </gml:posList>
                        </gml:LinearRing>
                      </gml:exterior>
                    </gml:Polygon>
                  </gml:surfaceMember>
                </gml:MultiSurface>
              </energy:surfaceGeometry>
              <energy:construction xlink:href="#GML_14ffe1b2-1753-427f-8e59-8b17ce397f5c" />
              <energy:contains>
                <energy:ThermalOpening gml:id="GML_755d358a-f749-4fec-a43a-f9bb1d9bbcf9">
                  <energy:area uom="m2">20.297263122599663</energy:area>
                  <energy:construction xlink:href="#GML_d8622004-ac1b-4c96-901d-86c53318207d" />
                </energy:ThermalOpening>
              </energy:contains>
              <energy:delimits xlink:href="#GML_615f6fa3-b3c6-432c-aa93-41fb7aaa64c9" />
            </energy:ThermalBoundary>
          </energy:boundedBy>
          <energy:boundedBy>
            <energy:ThermalBoundary gml:id="GML_5333431e-6e80-41c4-b18f-cb57e6e8d130">
              <gml:boundedBy>
                <gml:Envelope srsName="urn:adv:crs:ETRS89_UTM32">
                  <gml:lowerCorner>458877 5438353 -0.2</gml:lowerCorner>
                  <gml:upperCorner>458889 5438353 3.43094</gml:upperCorner>
                </gml:Envelope>
              </gml:boundedBy>
              <energy:thermalBoundaryType>outerWall</energy:thermalBoundaryType>
              <energy:azimuth uom="deg">180</energy:azimuth>
              <energy:inclination uom="deg">90</energy:inclination>
              <energy:area uom="m2">43.5712812921102</energy:area>
              <energy:surfaceGeometry>
                <gml:MultiSurface gml:id="GML_0f39ee45-2718-4083-a10c-dea2333e7664">
                  <gml:surfaceMember>
                    <gml:Polygon srsName="urn:adv:crs:ETRS89_UTM32" gml:id="GML_d5fecbfd-75e9-4171-8791-b21b5dd84b86">
                      <gml:exterior>
                        <gml:LinearRing gml:id="GML_0015b49a-c965-4ee0-b6fd-1db79d452eb5">
                          <gml:posList srsDimension="3" count="5">458889 5438353 3.43094 458877 5438353 3.43094 458877 5438353 -0.2 458889 5438353 -0.2 458889 5438353 3.43094 </gml:posList>
                        </gml:LinearRing>
                      </gml:exterior>
                    </gml:Polygon>
                  </gml:surfaceMember>
                </gml:MultiSurface>
              </energy:surfaceGeometry>
              <energy:construction xlink:href="#GML_14ffe1b2-1753-427f-8e59-8b17ce397f5c" />
              <energy:contains>
                <energy:ThermalOpening gml:id="GML_8e9b3f6c-19af-4eab-bf55-a360d5277823">
                  <energy:area uom="m2">17.42851251684408</energy:area>
                  <energy:construction xlink:href="#GML_d8622004-ac1b-4c96-901d-86c53318207d" />
                </energy:ThermalOpening>
              </energy:contains>
              <energy:delimits xlink:href="#GML_615f6fa3-b3c6-432c-aa93-41fb7aaa64c9" />
            </energy:ThermalBoundary>
          </energy:boundedBy>
          <energy:boundedBy>
            <energy:ThermalBoundary gml:id="GML_877a8cde-9f32-4052-b0db-059f47aa1ef4">
              <gml:boundedBy>
                <gml:Envelope srsName="urn:adv:crs:ETRS89_UTM32">
                  <gml:lowerCorner>458877 5438358 3.43094</gml:lowerCorner>
                  <gml:upperCorner>458889 5438363 6.31769</gml:upperCorner>
                </gml:Envelope>
              </gml:boundedBy>
              <energy:thermalBoundaryType>roof</energy:thermalBoundaryType>
              <energy:azimuth uom="deg">0</energy:azimuth>
              <energy:inclination uom="deg">30.000000000000014</energy:inclination>
              <energy:area uom="m2">69.282032288610935</energy:area>
              <energy:surfaceGeometry>
                <gml:MultiSurface gml:id="GML_1aa40144-4f08-44c2-89ea-a4e2ba9617e4">
                  <gml:surfaceMember>
                    <gml:Polygon srsName="urn:adv:crs:ETRS89_UTM32" gml:id="GML_78c5bccf-be3e-45b2-b970-79c2600050bc">
                      <gml:exterior>
                        <gml:LinearRing gml:id="GML_4e1d0d30-b547-4686-8bbc-766740d4f744">
                          <gml:posList srsDimension="3" count="5">458877 5438358 6.31769 458889 5438358 6.31769 458889 5438363 3.43094 458877 5438363 3.43094 458877 5438358 6.31769 </gml:posList>
                        </gml:LinearRing>
                      </gml:exterior>
                    </gml:Polygon>
                  </gml:surfaceMember>
                </gml:MultiSurface>
              </energy:surfaceGeometry>
              <energy:construction xlink:href="#GML_26c28117-7c13-4522-82fc-6c2564df9f68" />
              <energy:delimits xlink:href="#GML_615f6fa3-b3c6-432c-aa93-41fb7aaa64c9" />
            </energy:ThermalBoundary>
          </energy:boundedBy>
          <energy:boundedBy>
            <energy:ThermalBoundary gml:id="GML_84003000-5c0d-4ecb-8785-04783da1d641">
              <gml:boundedBy>
                <gml:Envelope srsName="urn:adv:crs:ETRS89_UTM32">
                  <gml:lowerCorner>458877 5438353 3.43094</gml:lowerCorner>
                  <gml:upperCorner>458889 5438358 6.31769</gml:upperCorner>
                </gml:Envelope>
              </gml:boundedBy>
              <energy:thermalBoundaryType>roof</energy:thermalBoundaryType>
              <energy:azimuth uom="deg">180</energy:azimuth>
              <energy:inclination uom="deg">30.000000000000014</energy:inclination>
              <energy:area uom="m2">69.2820322997868</energy:area>
              <energy:surfaceGeometry>
                <gml:MultiSurface gml:id="GML_5e5b1199-cc7f-4ccb-bc5a-48db155055ed">
                  <gml:surfaceMember>
                    <gml:Polygon srsName="urn:adv:crs:ETRS89_UTM32" gml:id="GML_f29f546e-e3e9-43cd-a974-617a00eb97a2">
                      <gml:exterior>
                        <gml:LinearRing gml:id="GML_f5696830-7a3f-4874-ba13-5dee9d10a241">
                          <gml:posList srsDimension="3" count="5">458889 5438353 3.43094 458889 5438358 6.31769 458877 5438358 6.31769 458877 5438353 3.43094 458889 5438353 3.43094 </gml:posList>
                        </gml:LinearRing>
                      </gml:exterior>
                    </gml:Polygon>
                  </gml:surfaceMember>
                </gml:MultiSurface>
              </energy:surfaceGeometry>
              <energy:construction xlink:href="#GML_26c28117-7c13-4522-82fc-6c2564df9f68" />
              <energy:delimits xlink:href="#GML_615f6fa3-b3c6-432c-aa93-41fb7aaa64c9" />
            </energy:ThermalBoundary>
          </energy:boundedBy>
          <energy:boundedBy>
            <energy:ThermalBoundary gml:id="GML_e4e78e97-4026-4cd0-b45e-ec4cfc14cf09">
              <gml:boundedBy>
                <gml:Envelope srsName="urn:adv:crs:ETRS89_UTM32">
                  <gml:lowerCorner>458877 5438353 -0.2</gml:lowerCorner>
                  <gml:upperCorner>458889 5438363 -0.2</gml:upperCorner>
                </gml:Envelope>
              </gml:boundedBy>
              <energy:thermalBoundaryType>groundSlab</energy:thermalBoundaryType>
              <energy:azimuth uom="deg">0</energy:azimuth>
              <energy:inclination uom="deg">180</energy:inclination>
              <energy:area uom="m2">120</energy:area>
              <energy:surfaceGeometry>
                <gml:MultiSurface gml:id="GML_be07d87f-a6a1-4831-a6fd-0b8812f71b47">
                  <gml:surfaceMember>
                    <gml:Polygon srsName="urn:adv:crs:ETRS89_UTM32" gml:id="GML_bfe5368f-077c-497c-9caf-ed0b9ef8b129">
                      <gml:exterior>
                        <gml:LinearRing gml:id="GML_c66cbe93-04fe-4fbc-a0fc-4efefa068810">
                          <gml:posList srsDimension="3" count="5">458889 5438353 -0.2 458877 5438353 -0.2 458877 5438363 -0.2 458889 5438363 -0.2 458889 5438353 -0.2 </gml:posList>
                        </gml:LinearRing>
                      </gml:exterior>
                    </gml:Polygon>
                  </gml:surfaceMember>
                </gml:MultiSurface>
              </energy:surfaceGeometry>
              <energy:construction xlink:href="#GML_a9107dd3-d8b2-406f-a69a-3a181cf83a10" />
              <energy:delimits xlink:href="#GML_615f6fa3-b3c6-432c-aa93-41fb7aaa64c9" />
            </energy:ThermalBoundary>
          </energy:boundedBy>
        </energy:ThermalZone>
      </energy:thermalZone>
      <energy:usageZone>
        <energy:UsageZone gml:id="GML_296e5877-8f24-4437-adc0-cbdb61f2d583">
          <energy:heatingSchedule>
            <energy:DailyPatternSchedule gml:id="GML_5b97597f-cb88-4469-813d-0bebc8e292e8">
              <gml:name>KIT-FZK-Haus-Heizung</gml:name>
              <energy:periodOfYear>
                <energy:PeriodOfYear>
                  <energy:period>
                    <gml:TimePeriod>
                      <gml:beginPosition>2022-01-01T00:00:00</gml:beginPosition>
                      <gml:endPosition>2022-12-31T00:00:00</gml:endPosition>
                    </gml:TimePeriod>
                  </energy:period>
                  <energy:dailySchedule>
                    <energy:DailySchedule>
                      <energy:dayType>weekDay</energy:dayType>
                      <energy:schedule>
                        <energy:RegularTimeSeries>
                          <energy:variableProperties>
                            <energy:TimeValuesProperties>
                              <energy:acquisitionMethod>estimation</energy:acquisitionMethod>
                              <energy:interpolationType>averageInSucceedingInterval</energy:interpolationType>
                              <energy:thematicDescription>Nominal temperature heating</energy:thematicDescription>
                            </energy:TimeValuesProperties>
                          </energy:variableProperties>
                          <energy:temporalExtent>
                            <gml:TimePeriod>
                              <gml:beginPosition>00:00:00</gml:beginPosition>
                              <gml:endPosition>00:00:23</gml:endPosition>
                            </gml:TimePeriod>
                          </energy:temporalExtent>
                          <energy:timeInterval unit="hour">1</energy:timeInterval>
                          <energy:values uom="C">20 20 20 20 20 20 20 20 20 20 20 20 20 20 20 20 20 20 20 20 20 
20 20 20 </energy:values>
                        </energy:RegularTimeSeries>
                      </energy:schedule>
                    </energy:DailySchedule>
                  </energy:dailySchedule>
                  <energy:dailySchedule>
                    <energy:DailySchedule>
                      <energy:dayType>weekEnd</energy:dayType>
                      <energy:schedule>
                        <energy:RegularTimeSeries>
                          <energy:variableProperties>
                            <energy:TimeValuesProperties>
                              <energy:acquisitionMethod>estimation</energy:acquisitionMethod>
                              <energy:interpolationType>averageInSucceedingInterval</energy:interpolationType>
                              <energy:thematicDescription>Nominal temperature heating</energy:thematicDescription>
                            </energy:TimeValuesProperties>
                          </energy:variableProperties>
                          <energy:temporalExtent>
                            <gml:TimePeriod>
                              <gml:beginPosition>00:00:00</gml:beginPosition>
                              <gml:endPosition>00:00:23</gml:endPosition>
                            </gml:TimePeriod>
                          </energy:temporalExtent>
                          <energy:timeInterval unit="hour">1</energy:timeInterval>
                          <energy:values uom="C">20 20 20 20 20 20 20 20 20 20 20 20 20 20 20 20 20 20 20 20 20 
20 20 20 </energy:values>
                        </energy:RegularTimeSeries>
                      </energy:schedule>
                    </energy:DailySchedule>
                  </energy:dailySchedule>
                </energy:PeriodOfYear>
              </energy:periodOfYear>
            </energy:DailyPatternSchedule>
          </energy:heatingSchedule>
          <energy:usageZoneType codeSpace="http://hub.geosmartcity.eu/registry/codelist/CurrentUseValue/">residential</energy:usageZoneType>
          <energy:ventilationSchedule>
            <energy:DailyPatternSchedule gml:id="GML_4743f81c-ad7f-40ad-b3bb-1bd9b3bc3310">
              <gml:name>KIT-FZK-Haus-Lueftung</gml:name>
              <energy:periodOfYear>
                <energy:PeriodOfYear>
                  <energy:period>
                    <gml:TimePeriod>
                      <gml:beginPosition>2022-01-01T00:00:00</gml:beginPosition>
                      <gml:endPosition>2022-12-31T00:00:00</gml:endPosition>
                    </gml:TimePeriod>
                  </energy:period>
                  <energy:dailySchedule>
                    <energy:DailySchedule>
                      <energy:dayType>weekDay</energy:dayType>
                      <energy:schedule>
                        <energy:RegularTimeSeries>
                          <energy:variableProperties>
                            <energy:TimeValuesProperties>
                              <energy:acquisitionMethod>estimation</energy:acquisitionMethod>
                              <energy:interpolationType>averageInSucceedingInterval</energy:interpolationType>
                              <energy:thematicDescription>Nominal ventilation flow rate</energy:thematicDescription>
                            </energy:TimeValuesProperties>
                          </energy:variableProperties>
                          <energy:temporalExtent>
                            <gml:TimePeriod>
                              <gml:beginPosition>00:00:00</gml:beginPosition>
                              <gml:endPosition>00:00:23</gml:endPosition>
                            </gml:TimePeriod>
                          </energy:temporalExtent>
                          <energy:timeInterval unit="hour">1</energy:timeInterval>
                          <energy:values uom="1/h">0.8 0.8 0.8 0.8 0.8 0.8 0.8 0.8 0.8 0.8 0.8 0.8 0.8 0.8 0.8 0.8 0.8 0.8 0.8 0.8 0.8 
0.8 0.8 0.8 </energy:values>
                        </energy:RegularTimeSeries>
                      </energy:schedule>
                    </energy:DailySchedule>
                  </energy:dailySchedule>
                  <energy:dailySchedule>
                    <energy:DailySchedule>
                      <energy:dayType>weekEnd</energy:dayType>
                      <energy:schedule>
                        <energy:RegularTimeSeries>
                          <energy:variableProperties>
                            <energy:TimeValuesProperties>
                              <energy:acquisitionMethod>estimation</energy:acquisitionMethod>
                              <energy:interpolationType>averageInSucceedingInterval</energy:interpolationType>
                              <energy:thematicDescription>Nominal ventilation flow rate</energy:thematicDescription>
                            </energy:TimeValuesProperties>
                          </energy:variableProperties>
                          <energy:temporalExtent>
                            <gml:TimePeriod>
                              <gml:beginPosition>00:00:00</gml:beginPosition>
                              <gml:endPosition>00:00:23</gml:endPosition>
                            </gml:TimePeriod>
                          </energy:temporalExtent>
                          <energy:timeInterval unit="hour">1</energy:timeInterval>
                          <energy:values uom="1/h">0.8 0.8 0.8 0.8 0.8 0.8 0.8 0.8 0.8 0.8 0.8 0.8 0.8 0.8 0.8 0.8 0.8 0.8 0.8 0.8 0.8 
0.8 0.8 0.8 </energy:values>
                        </energy:RegularTimeSeries>
                      </energy:schedule>
                    </energy:DailySchedule>
                  </energy:dailySchedule>
                </energy:PeriodOfYear>
              </energy:periodOfYear>
            </energy:DailyPatternSchedule>
          </energy:ventilationSchedule>
          <energy:occupiedBy>
            <energy:Occupants gml:id="GML_b4b6a20b-3b89-4153-a050-3876846af354">
              <energy:heatDissipation>
                <energy:HeatExchangeType>
                  <energy:convectiveFraction uom="scale">0.5</energy:convectiveFraction>
                  <energy:radiantFraction uom="scale">0.5</energy:radiantFraction>
                  <energy:totalValue uom="W">82</energy:totalValue>
                </energy:HeatExchangeType>
              </energy:heatDissipation>
              <energy:numberOfOccupants>2</energy:numberOfOccupants>
              <energy:occupancyRate>
                <energy:DailyPatternSchedule gml:id="GML_1a3c6b67-75a6-4d48-899c-2b124fbdc911">
                  <gml:name>KIT-FZK-Haus-Personen</gml:name>
                  <energy:periodOfYear>
                    <energy:PeriodOfYear>
                      <energy:period>
                        <gml:TimePeriod>
                          <gml:beginPosition>2022-01-01T00:00:00</gml:beginPosition>
                          <gml:endPosition>2022-12-31T00:00:00</gml:endPosition>
                        </gml:TimePeriod>
                      </energy:period>
                      <energy:dailySchedule>
                        <energy:DailySchedule>
                          <energy:dayType>weekDay</energy:dayType>
                          <energy:schedule>
                            <energy:RegularTimeSeries>
                              <energy:variableProperties>
                                <energy:TimeValuesProperties>
                                  <energy:acquisitionMethod>estimation</energy:acquisitionMethod>
                                  <energy:interpolationType>averageInSucceedingInterval</energy:interpolationType>
                                  <energy:thematicDescription>Presence of occupants</energy:thematicDescription>
                                </energy:TimeValuesProperties>
                              </energy:variableProperties>
                              <energy:temporalExtent>
                                <gml:TimePeriod>
                                  <gml:beginPosition>00:00:00</gml:beginPosition>
                                  <gml:endPosition>00:00:23</gml:endPosition>
                                </gml:TimePeriod>
                              </energy:temporalExtent>
                              <energy:timeInterval unit="hour">1</energy:timeInterval>
                              <energy:values uom="scale">0.8 0.8 0.8 0.8 0.8 0.8 0.8 0.8 0.8 0.8 0.8 0.8 0.8 0.8 0.8 0.8 0.8 0.8 0.8 0.8 0.8 
0.8 0.8 0.8 </energy:values>
                            </energy:RegularTimeSeries>
                          </energy:schedule>
                        </energy:DailySchedule>
                      </energy:dailySchedule>
                      <energy:dailySchedule>
                        <energy:DailySchedule>
                          <energy:dayType>weekEnd</energy:dayType>
                          <energy:schedule>
                            <energy:RegularTimeSeries>
                              <energy:variableProperties>
                                <energy:TimeValuesProperties>
                                  <energy:acquisitionMethod>estimation</energy:acquisitionMethod>
                                  <energy:interpolationType>averageInSucceedingInterval</energy:interpolationType>
                                  <energy:thematicDescription>Presence of occupants</energy:thematicDescription>
                                </energy:TimeValuesProperties>
                              </energy:variableProperties>
                              <energy:temporalExtent>
                                <gml:TimePeriod>
                                  <gml:beginPosition>00:00:00</gml:beginPosition>
                                  <gml:endPosition>00:00:23</gml:endPosition>
                                </gml:TimePeriod>
                              </energy:temporalExtent>
                              <energy:timeInterval unit="hour">1</energy:timeInterval>
                              <energy:values uom="scale">0.8 0.8 0.8 0.8 0.8 0.8 0.8 0.8 0.8 0.8 0.8 0.8 0.8 0.8 0.8 0.8 0.8 0.8 0.8 0.8 0.8 
0.8 0.8 0.8 </energy:values>
                            </energy:RegularTimeSeries>
                          </energy:schedule>
                        </energy:DailySchedule>
                      </energy:dailySchedule>
                    </energy:PeriodOfYear>
                  </energy:periodOfYear>
                </energy:DailyPatternSchedule>
              </energy:occupancyRate>
            </energy:Occupants>
          </energy:occupiedBy>
          <energy:equippedWith>
            <energy:ElectricalAppliances gml:id="GML_e94dc3e6-a1f0-4080-aa76-5900e6fd9ee6">
              <energy:operationSchedule>
                <energy:DailyPatternSchedule gml:id="GML_99179a72-7ad3-4fbd-b1cb-6cf2baa03b61">
                  <gml:name>KIT-FZK-Haus-Geraete</gml:name>
                  <energy:periodOfYear>
                    <energy:PeriodOfYear>
                      <energy:period>
                        <gml:TimePeriod>
                          <gml:beginPosition>2022-01-01T00:00:00</gml:beginPosition>
                          <gml:endPosition>2022-12-31T00:00:00</gml:endPosition>
                        </gml:TimePeriod>
                      </energy:period>
                      <energy:dailySchedule>
                        <energy:DailySchedule>
                          <energy:dayType>weekDay</energy:dayType>
                          <energy:schedule>
                            <energy:RegularTimeSeries>
                              <energy:variableProperties>
                                <energy:TimeValuesProperties>
                                  <energy:acquisitionMethod>estimation</energy:acquisitionMethod>
                                  <energy:interpolationType>averageInSucceedingInterval</energy:interpolationType>
                                  <energy:thematicDescription>Facility usage</energy:thematicDescription>
                                </energy:TimeValuesProperties>
                              </energy:variableProperties>
                              <energy:temporalExtent>
                                <gml:TimePeriod>
                                  <gml:beginPosition>00:00:00</gml:beginPosition>
                                  <gml:endPosition>00:00:23</gml:endPosition>
                                </gml:TimePeriod>
                              </energy:temporalExtent>
                              <energy:timeInterval unit="hour">1</energy:timeInterval>
                              <energy:values uom="scale">0.5 0.5 0.5 0.5 0.5 0.5 0.5 0.5 0.5 0.5 0.5 0.5 0.5 0.5 0.5 0.5 0.5 0.5 0.5 0.5 0.5 
0.5 0.5 0.5 </energy:values>
                            </energy:RegularTimeSeries>
                          </energy:schedule>
                        </energy:DailySchedule>
                      </energy:dailySchedule>
                      <energy:dailySchedule>
                        <energy:DailySchedule>
                          <energy:dayType>weekEnd</energy:dayType>
                          <energy:schedule>
                            <energy:RegularTimeSeries>
                              <energy:variableProperties>
                                <energy:TimeValuesProperties>
                                  <energy:acquisitionMethod>estimation</energy:acquisitionMethod>
                                  <energy:interpolationType>averageInSucceedingInterval</energy:interpolationType>
                                  <energy:thematicDescription>Facility usage</energy:thematicDescription>
                                </energy:TimeValuesProperties>
                              </energy:variableProperties>
                              <energy:temporalExtent>
                                <gml:TimePeriod>
                                  <gml:beginPosition>00:00:00</gml:beginPosition>
                                  <gml:endPosition>00:00:23</gml:endPosition>
                                </gml:TimePeriod>
                              </energy:temporalExtent>
                              <energy:timeInterval unit="hour">1</energy:timeInterval>
                              <energy:values uom="scale">0.5 0.5 0.5 0.5 0.5 0.5 0.5 0.5 0.5 0.5 0.5 0.5 0.5 0.5 0.5 0.5 0.5 0.5 0.5 0.5 0.5 
0.5 0.5 0.5 </energy:values>
                            </energy:RegularTimeSeries>
                          </energy:schedule>
                        </energy:DailySchedule>
                      </energy:dailySchedule>
                    </energy:PeriodOfYear>
                  </energy:periodOfYear>
                </energy:DailyPatternSchedule>
              </energy:operationSchedule>
              <energy:heatDissipation>
                <energy:HeatExchangeType>
                  <energy:convectiveFraction uom="scale">0.5</energy:convectiveFraction>
                  <energy:radiantFraction uom="scale">0.5</energy:radiantFraction>
                  <energy:totalValue uom="W/m2">5</energy:totalValue>
                </energy:HeatExchangeType>
              </energy:heatDissipation>
            </energy:ElectricalAppliances>
          </energy:equippedWith>
          <energy:equippedWith>
            <energy:LightingFacilities gml:id="GML_4a20bc06-f389-4cf2-80b1-218ec902e26b">
              <energy:operationSchedule>
                <energy:DailyPatternSchedule gml:id="GML_746ec421-59c5-4db0-81fb-3f9336c7c8c3">
                  <gml:name>KIT-FZK-Haus-Beleuchtung</gml:name>
                  <energy:periodOfYear>
                    <energy:PeriodOfYear>
                      <energy:period>
                        <gml:TimePeriod>
                          <gml:beginPosition>2022-01-01T00:00:00</gml:beginPosition>
                          <gml:endPosition>2022-12-31T00:00:00</gml:endPosition>
                        </gml:TimePeriod>
                      </energy:period>
                      <energy:dailySchedule>
                        <energy:DailySchedule>
                          <energy:dayType>weekDay</energy:dayType>
                          <energy:schedule>
                            <energy:RegularTimeSeries>
                              <energy:variableProperties>
                                <energy:TimeValuesProperties>
                                  <energy:acquisitionMethod>estimation</energy:acquisitionMethod>
                                  <energy:interpolationType>averageInSucceedingInterval</energy:interpolationType>
                                  <energy:thematicDescription>Lighting usage</energy:thematicDescription>
                                </energy:TimeValuesProperties>
                              </energy:variableProperties>
                              <energy:temporalExtent>
                                <gml:TimePeriod>
                                  <gml:beginPosition>00:00:00</gml:beginPosition>
                                  <gml:endPosition>00:00:23</gml:endPosition>
                                </gml:TimePeriod>
                              </energy:temporalExtent>
                              <energy:timeInterval unit="hour">1</energy:timeInterval>
                              <energy:values uom="scale">0.5 0.5 0.5 0.5 0.5 0.5 0.5 0.5 0.5 0.5 0.5 0.5 0.5 0.5 0.5 0.5 0.5 0.5 0.5 0.5 0.5 
0.5 0.5 0.5 </energy:values>
                            </energy:RegularTimeSeries>
                          </energy:schedule>
                        </energy:DailySchedule>
                      </energy:dailySchedule>
                      <energy:dailySchedule>
                        <energy:DailySchedule>
                          <energy:dayType>weekEnd</energy:dayType>
                          <energy:schedule>
                            <energy:RegularTimeSeries>
                              <energy:variableProperties>
                                <energy:TimeValuesProperties>
                                  <energy:acquisitionMethod>estimation</energy:acquisitionMethod>
                                  <energy:interpolationType>averageInSucceedingInterval</energy:interpolationType>
                                  <energy:thematicDescription>Lighting usage</energy:thematicDescription>
                                </energy:TimeValuesProperties>
                              </energy:variableProperties>
                              <energy:temporalExtent>
                                <gml:TimePeriod>
                                  <gml:beginPosition>00:00:00</gml:beginPosition>
                                  <gml:endPosition>00:00:23</gml:endPosition>
                                </gml:TimePeriod>
                              </energy:temporalExtent>
                              <energy:timeInterval unit="hour">1</energy:timeInterval>
                              <energy:values uom="scale">0.5 0.5 0.5 0.5 0.5 0.5 0.5 0.5 0.5 0.5 0.5 0.5 0.5 0.5 0.5 0.5 0.5 0.5 0.5 0.5 0.5 
0.5 0.5 0.5 </energy:values>
                            </energy:RegularTimeSeries>
                          </energy:schedule>
                        </energy:DailySchedule>
                      </energy:dailySchedule>
                    </energy:PeriodOfYear>
                  </energy:periodOfYear>
                </energy:DailyPatternSchedule>
              </energy:operationSchedule>
              <energy:heatDissipation>
                <energy:HeatExchangeType>
                  <energy:convectiveFraction uom="scale">0.5</energy:convectiveFraction>
                  <energy:radiantFraction uom="scale">0.5</energy:radiantFraction>
                  <energy:totalValue uom="W/m2">4</energy:totalValue>
                </energy:HeatExchangeType>
              </energy:heatDissipation>
            </energy:LightingFacilities>
          </energy:equippedWith>
        </energy:UsageZone>
      </energy:usageZone>
      <energy:floorArea>
        <energy:FloorArea>
          <energy:type>grossFloorArea</energy:type>
          <energy:value uom="m2">240</energy:value>
        </energy:FloorArea>
      </energy:floorArea>
    </bldg:Building>
  </core:cityObjectMember>
  <gml:featureMember>
    <energy:Construction gml:id="GML_14ffe1b2-1753-427f-8e59-8b17ce397f5c">
      <gml:description>KIT-FZK-Haus-Aussenwand</gml:description>
      <gml:name>KIT-FZK-Haus-Aussenwand</gml:name>
      <energy:uValue uom="W/K*m2">0.4</energy:uValue>
      <energy:layer>
        <energy:Layer gml:id="GML_a632a07d-2e24-49c4-a359-2c03095bf0e0">
          <energy:layerComponent>
            <energy:LayerComponent gml:id="GML_5dce6401-2316-44f7-a404-411378568025">
              <energy:areaFraction uom="scale">1</energy:areaFraction>
              <energy:thickness uom="m">0.02</energy:thickness>
              <energy:material xlink:href="#GML_8e71f5f0-da77-45bf-a367-1f713fa29e7f" />
            </energy:LayerComponent>
          </energy:layerComponent>
        </energy:Layer>
      </energy:layer>
      <energy:layer>
        <energy:Layer gml:id="GML_c50d7b26-8124-46c0-be7c-e322eb4aa67a">
          <energy:layerComponent>
            <energy:LayerComponent gml:id="GML_8bf5a4f9-36b2-40ce-b854-eac04dce209d">
              <energy:areaFraction uom="scale">1</energy:areaFraction>
              <energy:thickness uom="m">0.2</energy:thickness>
              <energy:material xlink:href="#GML_61742d8e-50ec-4d64-b16f-c6c2cba3cd7a" />
            </energy:LayerComponent>
          </energy:layerComponent>
        </energy:Layer>
      </energy:layer>
      <energy:layer>
        <energy:Layer gml:id="GML_29970bfd-0937-436a-948e-4ec00c2198b3">
          <energy:layerComponent>
            <energy:LayerComponent gml:id="GML_e2ca97ae-3ca5-41c1-bc8d-d7b2ef664d01">
              <energy:areaFraction uom="scale">1</energy:areaFraction>
              <energy:thickness uom="m">0.015</energy:thickness>
              <energy:material xlink:href="#GML_3a5b5258-f4b4-4301-980a-df3823e15dae" />
            </energy:LayerComponent>
          </energy:layerComponent>
        </energy:Layer>
      </energy:layer>
    </energy:Construction>
  </gml:featureMember>
  <gml:featureMember>
    <energy:Construction gml:id="GML_26c28117-7c13-4522-82fc-6c2564df9f68">
      <gml:description>KIT-FZK-Haus-Dach</gml:description>
      <gml:name>KIT-FZK-Haus-Dach</gml:name>
      <energy:uValue uom="W/K*m2">0.4</energy:uValue>
      <energy:layer>
        <energy:Layer gml:id="GML_0291112f-68ee-47dc-b763-6bc4ff5d07dd">
          <energy:layerComponent>
            <energy:LayerComponent gml:id="GML_7cc9441d-dc69-40c1-999b-e014b7216aea">
              <energy:areaFraction uom="scale">1</energy:areaFraction>
              <energy:thickness uom="m">0.02</energy:thickness>
              <energy:material xlink:href="#GML_b5e20032-b106-4e8c-b0cc-ad3ebae32e9b" />
            </energy:LayerComponent>
          </energy:layerComponent>
        </energy:Layer>
      </energy:layer>
      <energy:layer>
        <energy:Layer gml:id="GML_7b16b47a-9cd9-4c92-8fec-abd4500a4ba1">
          <energy:layerComponent>
            <energy:LayerComponent gml:id="GML_fdf4191e-acdd-454c-a5b8-0fd15f2f18f4">
              <energy:areaFraction uom="scale">1</energy:areaFraction>
              <energy:thickness uom="m">0.04</energy:thickness>
              <energy:material xlink:href="#GML_32b0de14-eb01-4a30-9ce2-b27853f551c8" />
            </energy:LayerComponent>
          </energy:layerComponent>
        </energy:Layer>
      </energy:layer>
      <energy:layer>
        <energy:Layer gml:id="GML_a9217b68-8cf2-4d40-af77-c0d503e5aed6">
          <energy:layerComponent>
            <energy:LayerComponent gml:id="GML_f6fb486f-383f-41e0-bee5-68f1ff2cfac5">
              <energy:areaFraction uom="scale">1</energy:areaFraction>
              <energy:thickness uom="m">0.04</energy:thickness>
              <energy:material xlink:href="#GML_a6ff8d9c-a1c9-4926-86ab-af5a88919d0d" />
            </energy:LayerComponent>
          </energy:layerComponent>
        </energy:Layer>
      </energy:layer>
      <energy:layer>
        <energy:Layer gml:id="GML_1d9858f7-14ae-4858-b069-bb3a3e1684c9">
          <energy:layerComponent>
            <energy:LayerComponent gml:id="GML_8b15e6a1-f5b8-49ce-8bbc-abb37887169d">
              <energy:areaFraction uom="scale">0.125</energy:areaFraction>
              <energy:thickness uom="m">0.08</energy:thickness>
              <energy:material xlink:href="#GML_32b0de14-eb01-4a30-9ce2-b27853f551c8" />
            </energy:LayerComponent>
          </energy:layerComponent>
          <energy:layerComponent>
            <energy:LayerComponent gml:id="GML_b525da20-f740-4c29-b148-edc3610c8ca4">
              <energy:areaFraction uom="scale">0.875</energy:areaFraction>
              <energy:thickness uom="m">0.08</energy:thickness>
              <energy:material xlink:href="#GML_e8ade8a9-5aa1-4deb-b4ee-d4b11c2d3191" />
            </energy:LayerComponent>
          </energy:layerComponent>
        </energy:Layer>
      </energy:layer>
      <energy:layer>
        <energy:Layer gml:id="GML_6189a505-55c4-4331-a6d5-bcf57f1b1353">
          <energy:layerComponent>
            <energy:LayerComponent gml:id="GML_00902380-acef-413c-a58e-6bdb70b8e7dd">
              <energy:areaFraction uom="scale">1</energy:areaFraction>
              <energy:thickness uom="m">0.0005</energy:thickness>
              <energy:material xlink:href="#GML_7c214fe2-2085-4588-af7a-338cfea31361" />
            </energy:LayerComponent>
          </energy:layerComponent>
        </energy:Layer>
      </energy:layer>
      <energy:layer>
        <energy:Layer gml:id="GML_f91a9664-d245-4309-a9b6-601f5cfd2df7">
          <energy:layerComponent>
            <energy:LayerComponent gml:id="GML_6e489cc0-0bb4-43b9-aeed-206cd9d4003c">
              <energy:areaFraction uom="scale">1</energy:areaFraction>
              <energy:thickness uom="m">0.06</energy:thickness>
              <energy:material xlink:href="#GML_e8ade8a9-5aa1-4deb-b4ee-d4b11c2d3191" />
            </energy:LayerComponent>
          </energy:layerComponent>
        </energy:Layer>
      </energy:layer>
      <energy:layer>
        <energy:Layer gml:id="GML_bb04c4e4-3383-48b0-9671-4b70cea71ef5">
          <energy:layerComponent>
            <energy:LayerComponent gml:id="GML_03976c12-1962-4bfb-924b-d595446e47ea">
              <energy:areaFraction uom="scale">1</energy:areaFraction>
              <energy:thickness uom="m">0.025</energy:thickness>
              <energy:material xlink:href="#GML_1d0b6b38-fa4b-4696-98de-2f9747cabbbf" />
            </energy:LayerComponent>
          </energy:layerComponent>
        </energy:Layer>
      </energy:layer>
    </energy:Construction>
  </gml:featureMember>
  <gml:featureMember>
    <energy:Construction gml:id="GML_a9107dd3-d8b2-406f-a69a-3a181cf83a10">
      <gml:description>KIT-FZK-Haus-Bodenplatte</gml:description>
      <gml:name>KIT-FZK-Haus-Bodenplatte</gml:name>
      <energy:uValue uom="W/K*m2">0.26</energy:uValue>
      <energy:layer>
        <energy:Layer gml:id="GML_ad88266a-db1c-45a7-b05a-da0fdd198dcb">
          <energy:layerComponent>
            <energy:LayerComponent gml:id="GML_1e4713e6-8d04-48cb-a521-32af6a55051e">
              <energy:areaFraction uom="scale">1</energy:areaFraction>
              <energy:thickness uom="m">0.12</energy:thickness>
              <energy:material xlink:href="#GML_2a0076e2-26cf-4328-a304-a60ce83db3b3" />
            </energy:LayerComponent>
          </energy:layerComponent>
        </energy:Layer>
      </energy:layer>
      <energy:layer>
        <energy:Layer gml:id="GML_af803312-e749-45f6-8048-ecf791eb60a7">
          <energy:layerComponent>
            <energy:LayerComponent gml:id="GML_a8f6f271-474a-4340-9d0c-d5f39eb315b0">
              <energy:areaFraction uom="scale">1</energy:areaFraction>
              <energy:thickness uom="m">0.0005</energy:thickness>
              <energy:material xlink:href="#GML_90d29894-8732-43ae-a990-cce0d4d77bd8" />
            </energy:LayerComponent>
          </energy:layerComponent>
        </energy:Layer>
      </energy:layer>
      <energy:layer>
        <energy:Layer gml:id="GML_540c7475-b099-4680-b615-192c55791245">
          <energy:layerComponent>
            <energy:LayerComponent gml:id="GML_4a3e96c4-d24a-408b-975b-a73ade0af0cd">
              <energy:areaFraction uom="scale">1</energy:areaFraction>
              <energy:thickness uom="m">0.1</energy:thickness>
              <energy:material xlink:href="#GML_6dc2035b-4eed-45d6-923b-e1c87e732d1b" />
            </energy:LayerComponent>
          </energy:layerComponent>
        </energy:Layer>
      </energy:layer>
      <energy:layer>
        <energy:Layer gml:id="GML_6bcf6da7-9a36-4f5e-8438-331e80249dce">
          <energy:layerComponent>
            <energy:LayerComponent gml:id="GML_b0ee648c-ab37-4459-b02f-8fb36f3c3f60">
              <energy:areaFraction uom="scale">1</energy:areaFraction>
              <energy:thickness uom="m">0.01</energy:thickness>
              <energy:material xlink:href="#GML_e8ade8a9-5aa1-4deb-b4ee-d4b11c2d3191" />
            </energy:LayerComponent>
          </energy:layerComponent>
        </energy:Layer>
      </energy:layer>
      <energy:layer>
        <energy:Layer gml:id="GML_331114fb-2ead-432c-9e54-113779e8437a">
          <energy:layerComponent>
            <energy:LayerComponent gml:id="GML_d12d701c-5fb0-4549-96b1-025dd67be0cc">
              <energy:areaFraction uom="scale">1</energy:areaFraction>
              <energy:thickness uom="m">0.0002</energy:thickness>
              <energy:material xlink:href="#GML_7c214fe2-2085-4588-af7a-338cfea31361" />
            </energy:LayerComponent>
          </energy:layerComponent>
        </energy:Layer>
      </energy:layer>
      <energy:layer>
        <energy:Layer gml:id="GML_26dd32af-fa59-4944-9737-9703502ee068">
          <energy:layerComponent>
            <energy:LayerComponent gml:id="GML_d8f3688b-8a35-4634-aed8-d7a27b1f2bff">
              <energy:areaFraction uom="scale">1</energy:areaFraction>
              <energy:thickness uom="m">0.02</energy:thickness>
              <energy:material xlink:href="#GML_11761b4b-996d-4c3d-b86c-82117e95de29" />
            </energy:LayerComponent>
          </energy:layerComponent>
        </energy:Layer>
      </energy:layer>
    </energy:Construction>
  </gml:featureMember>
  <gml:featureMember>
    <energy:Construction gml:id="GML_d8622004-ac1b-4c96-901d-86c53318207d">
      <gml:description>KIT-FZK-Haus-Fenster</gml:description>
      <gml:name>KIT-FZK-Haus-Fenster</gml:name>
      <energy:uValue uom="W/K*m2">1.2</energy:uValue>
      <energy:opticalProperties>
        <energy:OpticalProperties>
          <energy:transmittance>
            <energy:Transmittance>
              <energy:fraction uom="scale">0.6</energy:fraction>
              <energy:wavelengthRange>solar</energy:wavelengthRange>
            </energy:Transmittance>
          </energy:transmittance>
          <energy:glazingRatio uom="scale">0.7</energy:glazingRatio>
        </energy:OpticalProperties>
      </energy:opticalProperties>
    </energy:Construction>
  </gml:featureMember>
  <gml:featureMember>
    <energy:SolidMaterial gml:id="GML_11761b4b-996d-4c3d-b86c-82117e95de29">
      <gml:description>Zement-Estrich</gml:description>
      <gml:name>KIT-FZK-Haus-ZementEstrich</gml:name>
      <energy:conductivity uom="W/K*m">1.4</energy:conductivity>
      <energy:density uom="kg/m3">2000</energy:density>
      <energy:specificHeat uom="kJ/K*kg">1</energy:specificHeat>
    </energy:SolidMaterial>
  </gml:featureMember>
  <gml:featureMember>
    <energy:SolidMaterial gml:id="GML_1d0b6b38-fa4b-4696-98de-2f9747cabbbf">
      <gml:description>Gipskartonplatte</gml:description>
      <gml:name>KIT-FZK-Haus-Gipskarton</gml:name>
      <energy:conductivity uom="W/K*m">0.25</energy:conductivity>
      <energy:density uom="kg/m3">900</energy:density>
      <energy:specificHeat uom="kJ/K*kg">1</energy:specificHeat>
    </energy:SolidMaterial>
  </gml:featureMember>
  <gml:featureMember>
    <energy:SolidMaterial gml:id="GML_2a0076e2-26cf-4328-a304-a60ce83db3b3">
      <gml:description>Polystyrol-Extruderschaum</gml:description>
      <gml:name>KIT-FZK-Haus-Polystyrol-Extruderschaum</gml:name>
      <energy:conductivity uom="W/K*m">0.035</energy:conductivity>
      <energy:density uom="kg/m3">25</energy:density>
      <energy:specificHeat uom="kJ/K*kg">1.5</energy:specificHeat>
    </energy:SolidMaterial>
  </gml:featureMember>
  <gml:featureMember>
    <energy:SolidMaterial gml:id="GML_32b0de14-eb01-4a30-9ce2-b27853f551c8">
      <gml:description>Konstruktionsholz Dach</gml:description>
      <gml:name>KIT-FZK-Haus-Holz-Dach</gml:name>
      <energy:conductivity uom="W/K*m">0.13</energy:conductivity>
      <energy:density uom="kg/m3">500</energy:density>
      <energy:specificHeat uom="kJ/K*kg">1.6</energy:specificHeat>
    </energy:SolidMaterial>
  </gml:featureMember>
  <gml:featureMember>
    <energy:SolidMaterial gml:id="GML_3a5b5258-f4b4-4301-980a-df3823e15dae">
      <gml:description>Putzmörtel (Kalkgips)</gml:description>
      <gml:name>KIT-FZK-Haus-Putz-Innen</gml:name>
      <energy:conductivity uom="W/K*m">0.7</energy:conductivity>
      <energy:density uom="kg/m3">1400</energy:density>
      <energy:specificHeat uom="kJ/K*kg">1</energy:specificHeat>
    </energy:SolidMaterial>
  </gml:featureMember>
  <gml:featureMember>
    <energy:SolidMaterial gml:id="GML_61742d8e-50ec-4d64-b16f-c6c2cba3cd7a">
      <gml:description>Porenbeton</gml:description>
      <gml:name>KIT-FZK-Haus-Porenbeton</gml:name>
      <energy:conductivity uom="W/K*m">0.13</energy:conductivity>
      <energy:density uom="kg/m3">400</energy:density>
      <energy:specificHeat uom="kJ/K*kg">1</energy:specificHeat>
    </energy:SolidMaterial>
  </gml:featureMember>
  <gml:featureMember>
    <energy:SolidMaterial gml:id="GML_6dc2035b-4eed-45d6-923b-e1c87e732d1b">
      <gml:description>Beton Bodenplatte</gml:description>
      <gml:name>KIT-FZK-Haus-Beton-Bodenplatte</gml:name>
      <energy:conductivity uom="W/K*m">2</energy:conductivity>
      <energy:density uom="kg/m3">2400</energy:density>
      <energy:specificHeat uom="kJ/K*kg">1</energy:specificHeat>
    </energy:SolidMaterial>
  </gml:featureMember>
  <gml:featureMember>
    <energy:SolidMaterial gml:id="GML_7c214fe2-2085-4588-af7a-338cfea31361">
      <gml:description>Polyethylenfolie</gml:description>
      <gml:name>KIT-FZK-Haus-Polyethylenfolie</gml:name>
      <energy:conductivity uom="W/K*m">0.33</energy:conductivity>
      <energy:density uom="kg/m3">960</energy:density>
      <energy:specificHeat uom="kJ/K*kg">1.5</energy:specificHeat>
    </energy:SolidMaterial>
  </gml:featureMember>
  <gml:featureMember>
    <energy:SolidMaterial gml:id="GML_8e71f5f0-da77-45bf-a367-1f713fa29e7f">
      <gml:description>Normalmörtel</gml:description>
      <gml:name>KIT-FZK-Haus-Putz-Aussen</gml:name>
      <energy:conductivity uom="W/K*m">1.2</energy:conductivity>
      <energy:density uom="kg/m3">1800</energy:density>
      <energy:specificHeat uom="kJ/K*kg">1</energy:specificHeat>
    </energy:SolidMaterial>
  </gml:featureMember>
  <gml:featureMember>
    <energy:SolidMaterial gml:id="GML_90d29894-8732-43ae-a990-cce0d4d77bd8">
      <gml:description>Bitumendachbahn</gml:description>
      <gml:name>KIT-FZK-Haus-Bitumendachbahn</gml:name>
      <energy:conductivity uom="W/K*m">0.17</energy:conductivity>
      <energy:density uom="kg/m3">1200</energy:density>
      <energy:specificHeat uom="kJ/K*kg">1.5</energy:specificHeat>
    </energy:SolidMaterial>
  </gml:featureMember>
  <gml:featureMember>
    <energy:Gas gml:id="GML_a6ff8d9c-a1c9-4926-86ab-af5a88919d0d">
      <gml:description>Luftschicht</gml:description>
      <gml:name>KIT-FZK-Haus-Luftschicht</gml:name>
      <energy:isVentilated>false</energy:isVentilated>
      <energy:rValue uom="K*m2/W">0.04</energy:rValue>
    </energy:Gas>
  </gml:featureMember>
  <gml:featureMember>
    <energy:SolidMaterial gml:id="GML_b5e20032-b106-4e8c-b0cc-ad3ebae32e9b">
      <gml:description>Dachziegel</gml:description>
      <gml:name>KIT-FZK-Haus-Ziegel</gml:name>
      <energy:conductivity uom="W/K*m">1</energy:conductivity>
      <energy:density uom="kg/m3">2000</energy:density>
      <energy:specificHeat uom="kJ/K*kg">0.8</energy:specificHeat>
    </energy:SolidMaterial>
  </gml:featureMember>
  <gml:featureMember>
    <energy:SolidMaterial gml:id="GML_e8ade8a9-5aa1-4deb-b4ee-d4b11c2d3191">
      <gml:description>Polystyrol-Partikelschaum</gml:description>
      <gml:name>KIT-FZK-Haus-Polystyrol-Partikelschaum</gml:name>
      <energy:conductivity uom="W/K*m">0.04</energy:conductivity>
      <energy:density uom="kg/m3">30</energy:density>
      <energy:specificHeat uom="kJ/K*kg">1.5</energy:specificHeat>
    </energy:SolidMaterial>
  </gml:featureMember>
</core:CityModel>