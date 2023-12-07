<!DOCTYPE qgis PUBLIC 'http://mrcc.com/qgis.dtd' 'SYSTEM'>
<qgis version="3.32.0-Lima" styleCategories="Symbology|Labeling" labelsEnabled="1">
  <renderer-v2 type="singleSymbol" forceraster="0" enableorderby="0" referencescale="-1" symbollevels="0">
    <symbols>
      <symbol clip_to_extent="1" type="fill" is_animated="0" force_rhr="0" frame_rate="10" alpha="1" name="0">
        <data_defined_properties>
          <Option type="Map">
            <Option type="QString" value="" name="name"/>
            <Option name="properties"/>
            <Option type="QString" value="collection" name="type"/>
          </Option>
        </data_defined_properties>
        <layer pass="0" class="SimpleFill" id="{56937d7f-b189-481d-bf21-13a54564d0f8}" enabled="1" locked="0">
          <Option type="Map">
            <Option type="QString" value="3x:0,0,0,0,0,0" name="border_width_map_unit_scale"/>
            <Option type="QString" value="144,201,0,255" name="color"/>
            <Option type="QString" value="bevel" name="joinstyle"/>
            <Option type="QString" value="0,0" name="offset"/>
            <Option type="QString" value="3x:0,0,0,0,0,0" name="offset_map_unit_scale"/>
            <Option type="QString" value="RenderMetersInMapUnits" name="offset_unit"/>
            <Option type="QString" value="70,70,70,255" name="outline_color"/>
            <Option type="QString" value="solid" name="outline_style"/>
            <Option type="QString" value="0.26" name="outline_width"/>
            <Option type="QString" value="RenderMetersInMapUnits" name="outline_width_unit"/>
            <Option type="QString" value="solid" name="style"/>
          </Option>
          <data_defined_properties>
            <Option type="Map">
              <Option type="QString" value="" name="name"/>
              <Option name="properties"/>
              <Option type="QString" value="collection" name="type"/>
            </Option>
          </data_defined_properties>
        </layer>
        <layer pass="0" class="GeometryGenerator" id="{960d46dd-ad7b-4399-9855-128596365c8e}" enabled="1" locked="0">
          <Option type="Map">
            <Option type="QString" value="Line" name="SymbolType"/>
            <Option type="QString" value=" segments_to_lines( $geometry)" name="geometryModifier"/>
            <Option type="QString" value="MapUnit" name="units"/>
          </Option>
          <data_defined_properties>
            <Option type="Map">
              <Option type="QString" value="" name="name"/>
              <Option name="properties"/>
              <Option type="QString" value="collection" name="type"/>
            </Option>
          </data_defined_properties>
          <symbol clip_to_extent="1" type="line" is_animated="0" force_rhr="0" frame_rate="10" alpha="1" name="@0@1">
            <data_defined_properties>
              <Option type="Map">
                <Option type="QString" value="" name="name"/>
                <Option name="properties"/>
                <Option type="QString" value="collection" name="type"/>
              </Option>
            </data_defined_properties>
            <layer pass="0" class="ArrowLine" id="{1a82671a-2ac7-4f69-9d26-d662ffd6337d}" enabled="1" locked="0">
              <Option type="Map">
                <Option type="QString" value="1" name="arrow_start_width"/>
                <Option type="QString" value="MM" name="arrow_start_width_unit"/>
                <Option type="QString" value="3x:0,0,0,0,0,0" name="arrow_start_width_unit_scale"/>
                <Option type="QString" value="0" name="arrow_type"/>
                <Option type="QString" value="2" name="arrow_width"/>
                <Option type="QString" value="MapUnit" name="arrow_width_unit"/>
                <Option type="QString" value="3x:0,0,0,0,0,0" name="arrow_width_unit_scale"/>
                <Option type="QString" value="15" name="head_length"/>
                <Option type="QString" value="MapUnit" name="head_length_unit"/>
                <Option type="QString" value="3x:0,0,0,0,0,0" name="head_length_unit_scale"/>
                <Option type="QString" value="15" name="head_thickness"/>
                <Option type="QString" value="MapUnit" name="head_thickness_unit"/>
                <Option type="QString" value="3x:0,0,0,0,0,0" name="head_thickness_unit_scale"/>
                <Option type="QString" value="2" name="head_type"/>
                <Option type="QString" value="1" name="is_curved"/>
                <Option type="QString" value="1" name="is_repeated"/>
                <Option type="QString" value="-100" name="offset"/>
                <Option type="QString" value="MapUnit" name="offset_unit"/>
                <Option type="QString" value="3x:0,0,0,0,0,0" name="offset_unit_scale"/>
                <Option type="QString" value="0" name="ring_filter"/>
              </Option>
              <data_defined_properties>
                <Option type="Map">
                  <Option type="QString" value="" name="name"/>
                  <Option name="properties"/>
                  <Option type="QString" value="collection" name="type"/>
                </Option>
              </data_defined_properties>
              <symbol clip_to_extent="1" type="fill" is_animated="0" force_rhr="0" frame_rate="10" alpha="1" name="@@0@1@0">
                <data_defined_properties>
                  <Option type="Map">
                    <Option type="QString" value="" name="name"/>
                    <Option name="properties"/>
                    <Option type="QString" value="collection" name="type"/>
                  </Option>
                </data_defined_properties>
                <layer pass="0" class="SimpleFill" id="{50784f58-f098-4053-824b-dbf17a88108b}" enabled="1" locked="0">
                  <Option type="Map">
                    <Option type="QString" value="3x:0,0,0,0,0,0" name="border_width_map_unit_scale"/>
                    <Option type="QString" value="60,60,60,255" name="color"/>
                    <Option type="QString" value="bevel" name="joinstyle"/>
                    <Option type="QString" value="0,0" name="offset"/>
                    <Option type="QString" value="3x:0,0,0,0,0,0" name="offset_map_unit_scale"/>
                    <Option type="QString" value="MM" name="offset_unit"/>
                    <Option type="QString" value="70,70,70,255" name="outline_color"/>
                    <Option type="QString" value="solid" name="outline_style"/>
                    <Option type="QString" value="0.26" name="outline_width"/>
                    <Option type="QString" value="MM" name="outline_width_unit"/>
                    <Option type="QString" value="solid" name="style"/>
                  </Option>
                  <data_defined_properties>
                    <Option type="Map">
                      <Option type="QString" value="" name="name"/>
                      <Option name="properties"/>
                      <Option type="QString" value="collection" name="type"/>
                    </Option>
                  </data_defined_properties>
                </layer>
              </symbol>
            </layer>
            <layer pass="0" class="MarkerLine" id="{ecd40cc3-0318-4176-a5f6-322604a6f0ed}" enabled="1" locked="0">
              <Option type="Map">
                <Option type="QString" value="4" name="average_angle_length"/>
                <Option type="QString" value="3x:0,0,0,0,0,0" name="average_angle_map_unit_scale"/>
                <Option type="QString" value="MM" name="average_angle_unit"/>
                <Option type="QString" value="3" name="interval"/>
                <Option type="QString" value="3x:0,0,0,0,0,0" name="interval_map_unit_scale"/>
                <Option type="QString" value="RenderMetersInMapUnits" name="interval_unit"/>
                <Option type="QString" value="0" name="offset"/>
                <Option type="QString" value="0" name="offset_along_line"/>
                <Option type="QString" value="3x:0,0,0,0,0,0" name="offset_along_line_map_unit_scale"/>
                <Option type="QString" value="RenderMetersInMapUnits" name="offset_along_line_unit"/>
                <Option type="QString" value="3x:0,0,0,0,0,0" name="offset_map_unit_scale"/>
                <Option type="QString" value="RenderMetersInMapUnits" name="offset_unit"/>
                <Option type="bool" value="true" name="place_on_every_part"/>
                <Option type="QString" value="LastVertex|FirstVertex|InnerVertices" name="placements"/>
                <Option type="QString" value="0" name="ring_filter"/>
                <Option type="QString" value="1" name="rotate"/>
              </Option>
              <data_defined_properties>
                <Option type="Map">
                  <Option type="QString" value="" name="name"/>
                  <Option name="properties"/>
                  <Option type="QString" value="collection" name="type"/>
                </Option>
              </data_defined_properties>
              <symbol clip_to_extent="1" type="marker" is_animated="0" force_rhr="0" frame_rate="10" alpha="1" name="@@0@1@1">
                <data_defined_properties>
                  <Option type="Map">
                    <Option type="QString" value="" name="name"/>
                    <Option name="properties"/>
                    <Option type="QString" value="collection" name="type"/>
                  </Option>
                </data_defined_properties>
                <layer pass="0" class="SimpleMarker" id="{b24fe3c0-fe22-4e5d-b026-5547f042e4c6}" enabled="1" locked="0">
                  <Option type="Map">
                    <Option type="QString" value="0" name="angle"/>
                    <Option type="QString" value="square" name="cap_style"/>
                    <Option type="QString" value="255,0,0,255" name="color"/>
                    <Option type="QString" value="1" name="horizontal_anchor_point"/>
                    <Option type="QString" value="bevel" name="joinstyle"/>
                    <Option type="QString" value="line" name="name"/>
                    <Option type="QString" value="0,0" name="offset"/>
                    <Option type="QString" value="3x:0,0,0,0,0,0" name="offset_map_unit_scale"/>
                    <Option type="QString" value="RenderMetersInMapUnits" name="offset_unit"/>
                    <Option type="QString" value="70,70,70,255" name="outline_color"/>
                    <Option type="QString" value="solid" name="outline_style"/>
                    <Option type="QString" value="0" name="outline_width"/>
                    <Option type="QString" value="3x:0,0,0,0,0,0" name="outline_width_map_unit_scale"/>
                    <Option type="QString" value="RenderMetersInMapUnits" name="outline_width_unit"/>
                    <Option type="QString" value="diameter" name="scale_method"/>
                    <Option type="QString" value="150" name="size"/>
                    <Option type="QString" value="3x:0,0,0,0,0,0" name="size_map_unit_scale"/>
                    <Option type="QString" value="RenderMetersInMapUnits" name="size_unit"/>
                    <Option type="QString" value="2" name="vertical_anchor_point"/>
                  </Option>
                  <data_defined_properties>
                    <Option type="Map">
                      <Option type="QString" value="" name="name"/>
                      <Option type="Map" name="properties">
                        <Option type="Map" name="angle">
                          <Option type="bool" value="false" name="active"/>
                          <Option type="QString" value="" name="expression"/>
                          <Option type="Map" name="transformer">
                            <Option type="Map" name="d">
                              <Option type="double" value="1" name="exponent"/>
                              <Option type="double" value="360" name="maxOutput"/>
                              <Option type="double" value="0" name="maxValue"/>
                              <Option type="double" value="0" name="minOutput"/>
                              <Option type="double" value="0" name="minValue"/>
                              <Option type="double" value="0" name="nullOutput"/>
                            </Option>
                            <Option type="int" value="0" name="t"/>
                          </Option>
                          <Option type="int" value="3" name="type"/>
                        </Option>
                      </Option>
                      <Option type="QString" value="collection" name="type"/>
                    </Option>
                  </data_defined_properties>
                </layer>
              </symbol>
            </layer>
          </symbol>
        </layer>
        <layer pass="0" class="GeometryGenerator" id="{38b0121d-f96a-45c8-8cb3-2a9cb74aae90}" enabled="1" locked="0">
          <Option type="Map">
            <Option type="QString" value="Line" name="SymbolType"/>
            <Option type="QString" value="segments_to_lines($geometry)" name="geometryModifier"/>
            <Option type="QString" value="MapUnit" name="units"/>
          </Option>
          <data_defined_properties>
            <Option type="Map">
              <Option type="QString" value="" name="name"/>
              <Option name="properties"/>
              <Option type="QString" value="collection" name="type"/>
            </Option>
          </data_defined_properties>
          <symbol clip_to_extent="1" type="line" is_animated="0" force_rhr="0" frame_rate="10" alpha="1" name="@0@2">
            <data_defined_properties>
              <Option type="Map">
                <Option type="QString" value="" name="name"/>
                <Option name="properties"/>
                <Option type="QString" value="collection" name="type"/>
              </Option>
            </data_defined_properties>
            <layer pass="0" class="MarkerLine" id="{ef0bdb3c-c6da-421b-a478-29941e34fb95}" enabled="1" locked="0">
              <Option type="Map">
                <Option type="QString" value="4" name="average_angle_length"/>
                <Option type="QString" value="3x:0,0,0,0,0,0" name="average_angle_map_unit_scale"/>
                <Option type="QString" value="MM" name="average_angle_unit"/>
                <Option type="QString" value="3" name="interval"/>
                <Option type="QString" value="3x:0,0,0,0,0,0" name="interval_map_unit_scale"/>
                <Option type="QString" value="MM" name="interval_unit"/>
                <Option type="QString" value="-160" name="offset"/>
                <Option type="QString" value="0" name="offset_along_line"/>
                <Option type="QString" value="3x:0,0,0,0,0,0" name="offset_along_line_map_unit_scale"/>
                <Option type="QString" value="MM" name="offset_along_line_unit"/>
                <Option type="QString" value="3x:0,0,0,0,0,0" name="offset_map_unit_scale"/>
                <Option type="QString" value="RenderMetersInMapUnits" name="offset_unit"/>
                <Option type="bool" value="true" name="place_on_every_part"/>
                <Option type="QString" value="CentralPoint" name="placements"/>
                <Option type="QString" value="0" name="ring_filter"/>
                <Option type="QString" value="0" name="rotate"/>
              </Option>
              <data_defined_properties>
                <Option type="Map">
                  <Option type="QString" value="" name="name"/>
                  <Option name="properties"/>
                  <Option type="QString" value="collection" name="type"/>
                </Option>
              </data_defined_properties>
              <symbol clip_to_extent="1" type="marker" is_animated="0" force_rhr="0" frame_rate="10" alpha="1" name="@@0@2@0">
                <data_defined_properties>
                  <Option type="Map">
                    <Option type="QString" value="" name="name"/>
                    <Option name="properties"/>
                    <Option type="QString" value="collection" name="type"/>
                  </Option>
                </data_defined_properties>
                <layer pass="0" class="FontMarker" id="{f753f227-be1a-49de-a2db-9433adb08237}" enabled="1" locked="0">
                  <Option type="Map">
                    <Option type="QString" value="0" name="angle"/>
                    <Option type="QString" value="A" name="chr"/>
                    <Option type="QString" value="69,69,69,255" name="color"/>
                    <Option type="QString" value="Arial" name="font"/>
                    <Option type="QString" value="Standaard" name="font_style"/>
                    <Option type="QString" value="1" name="horizontal_anchor_point"/>
                    <Option type="QString" value="bevel" name="joinstyle"/>
                    <Option type="QString" value="0,0" name="offset"/>
                    <Option type="QString" value="3x:0,0,0,0,0,0" name="offset_map_unit_scale"/>
                    <Option type="QString" value="MM" name="offset_unit"/>
                    <Option type="QString" value="35,35,35,255" name="outline_color"/>
                    <Option type="QString" value="0" name="outline_width"/>
                    <Option type="QString" value="3x:0,0,0,0,0,0" name="outline_width_map_unit_scale"/>
                    <Option type="QString" value="MM" name="outline_width_unit"/>
                    <Option type="QString" value="50" name="size"/>
                    <Option type="QString" value="3x:0,0,0,0,0,0" name="size_map_unit_scale"/>
                    <Option type="QString" value="RenderMetersInMapUnits" name="size_unit"/>
                    <Option type="QString" value="1" name="vertical_anchor_point"/>
                  </Option>
                  <data_defined_properties>
                    <Option type="Map">
                      <Option type="QString" value="" name="name"/>
                      <Option type="Map" name="properties">
                        <Option type="Map" name="angle">
                          <Option type="bool" value="true" name="active"/>
                          <Option type="QString" value="CASE WHEN azimuth(&#xd;&#xa;&#x9;&#x9;start_point( geometry_n( $geometry, @geometry_part_num)),&#xd;&#xa;&#x9;&#x9;end_point( geometry_n( $geometry, @geometry_part_num))&#xd;&#xa;&#x9;)> pi()  THEN degrees(azimuth(&#xd;&#xa;&#x9;&#x9;start_point( geometry_n( $geometry, @geometry_part_num)),&#xd;&#xa;&#x9;&#x9;end_point( geometry_n( $geometry, @geometry_part_num))&#xd;&#xa;&#x9;)) + 90 + @map_rotation&#xd;&#xa;&#x9;ELSE&#xd;&#xa;&#x9;degrees(azimuth(&#xd;&#xa;&#x9;&#x9;start_point( geometry_n( $geometry, @geometry_part_num)),&#xd;&#xa;&#x9;&#x9;end_point( geometry_n( $geometry, @geometry_part_num))&#xd;&#xa;&#x9;)) - 90 + @map_rotation&#xd;&#xa;&#x9;END" name="expression"/>
                          <Option type="int" value="3" name="type"/>
                        </Option>
                        <Option type="Map" name="char">
                          <Option type="bool" value="true" name="active"/>
                          <Option type="QString" value="concat(round(length(geometry_n( $geometry, @geometry_part_num)),3),'m')" name="expression"/>
                          <Option type="int" value="3" name="type"/>
                        </Option>
                        <Option type="Map" name="outlineWidth">
                          <Option type="bool" value="false" name="active"/>
                          <Option type="int" value="1" name="type"/>
                          <Option type="QString" value="" name="val"/>
                        </Option>
                      </Option>
                      <Option type="QString" value="collection" name="type"/>
                    </Option>
                  </data_defined_properties>
                </layer>
              </symbol>
            </layer>
          </symbol>
        </layer>
      </symbol>
    </symbols>
    <rotation/>
    <sizescale/>
  </renderer-v2>
  <labeling type="simple">
    <settings calloutType="simple">
      <text-style capitalization="0" fontSize="60" isExpression="1" fontItalic="0" fontSizeUnit="RenderMetersInMapUnits" previewBkgrdColor="255,255,255,255" allowHtml="0" fontFamily="MS Shell Dlg 2" fieldName="concat(round($area),' m²')" textColor="0,0,0,255" fontKerning="1" fontSizeMapUnitScale="3x:0,0,0,0,0,0" useSubstitutions="0" fontWordSpacing="0" fontStrikeout="0" forcedBold="0" textOrientation="horizontal" multilineHeight="1" fontUnderline="0" fontWeight="50" legendString="Aa" textOpacity="1" namedStyle="Standaard" forcedItalic="0" blendMode="0" multilineHeightUnit="Percentage" fontLetterSpacing="0">
        <families/>
        <text-buffer bufferSizeMapUnitScale="3x:0,0,0,0,0,0" bufferJoinStyle="128" bufferBlendMode="0" bufferDraw="0" bufferNoFill="1" bufferSize="1" bufferOpacity="1" bufferSizeUnits="MM" bufferColor="255,255,255,255"/>
        <text-mask maskSize="0" maskJoinStyle="128" maskEnabled="0" maskOpacity="1" maskedSymbolLayers="" maskSizeUnits="MM" maskSizeMapUnitScale="3x:0,0,0,0,0,0" maskType="0"/>
        <background shapeRadiiX="0" shapeBorderWidthMapUnitScale="3x:0,0,0,0,0,0" shapeRotation="0" shapeType="0" shapeSVGFile="" shapeSizeUnit="RenderMetersInMapUnits" shapeRadiiY="0" shapeBlendMode="0" shapeJoinStyle="64" shapeOffsetX="0" shapeOffsetY="0" shapeDraw="1" shapeOffsetMapUnitScale="3x:0,0,0,0,0,0" shapeSizeType="0" shapeRadiiUnit="MM" shapeOffsetUnit="MM" shapeSizeY="10" shapeRotationType="0" shapeRadiiMapUnitScale="3x:0,0,0,0,0,0" shapeOpacity="1" shapeFillColor="255,255,255,152" shapeSizeMapUnitScale="3x:0,0,0,0,0,0" shapeSizeX="20" shapeBorderColor="128,128,128,255" shapeBorderWidth="3" shapeBorderWidthUnit="RenderMetersInMapUnits">
          <symbol clip_to_extent="1" type="marker" is_animated="0" force_rhr="0" frame_rate="10" alpha="1" name="markerSymbol">
            <data_defined_properties>
              <Option type="Map">
                <Option type="QString" value="" name="name"/>
                <Option name="properties"/>
                <Option type="QString" value="collection" name="type"/>
              </Option>
            </data_defined_properties>
            <layer pass="0" class="SimpleMarker" id="" enabled="1" locked="0">
              <Option type="Map">
                <Option type="QString" value="0" name="angle"/>
                <Option type="QString" value="square" name="cap_style"/>
                <Option type="QString" value="255,158,23,255" name="color"/>
                <Option type="QString" value="1" name="horizontal_anchor_point"/>
                <Option type="QString" value="bevel" name="joinstyle"/>
                <Option type="QString" value="circle" name="name"/>
                <Option type="QString" value="0,0" name="offset"/>
                <Option type="QString" value="3x:0,0,0,0,0,0" name="offset_map_unit_scale"/>
                <Option type="QString" value="MM" name="offset_unit"/>
                <Option type="QString" value="35,35,35,255" name="outline_color"/>
                <Option type="QString" value="solid" name="outline_style"/>
                <Option type="QString" value="0" name="outline_width"/>
                <Option type="QString" value="3x:0,0,0,0,0,0" name="outline_width_map_unit_scale"/>
                <Option type="QString" value="MM" name="outline_width_unit"/>
                <Option type="QString" value="diameter" name="scale_method"/>
                <Option type="QString" value="2" name="size"/>
                <Option type="QString" value="3x:0,0,0,0,0,0" name="size_map_unit_scale"/>
                <Option type="QString" value="MM" name="size_unit"/>
                <Option type="QString" value="1" name="vertical_anchor_point"/>
              </Option>
              <data_defined_properties>
                <Option type="Map">
                  <Option type="QString" value="" name="name"/>
                  <Option name="properties"/>
                  <Option type="QString" value="collection" name="type"/>
                </Option>
              </data_defined_properties>
            </layer>
          </symbol>
          <symbol clip_to_extent="1" type="fill" is_animated="0" force_rhr="0" frame_rate="10" alpha="1" name="fillSymbol">
            <data_defined_properties>
              <Option type="Map">
                <Option type="QString" value="" name="name"/>
                <Option name="properties"/>
                <Option type="QString" value="collection" name="type"/>
              </Option>
            </data_defined_properties>
            <layer pass="0" class="SimpleFill" id="" enabled="1" locked="0">
              <Option type="Map">
                <Option type="QString" value="3x:0,0,0,0,0,0" name="border_width_map_unit_scale"/>
                <Option type="QString" value="255,255,255,152" name="color"/>
                <Option type="QString" value="bevel" name="joinstyle"/>
                <Option type="QString" value="0,0" name="offset"/>
                <Option type="QString" value="3x:0,0,0,0,0,0" name="offset_map_unit_scale"/>
                <Option type="QString" value="MM" name="offset_unit"/>
                <Option type="QString" value="128,128,128,255" name="outline_color"/>
                <Option type="QString" value="solid" name="outline_style"/>
                <Option type="QString" value="3" name="outline_width"/>
                <Option type="QString" value="RenderMetersInMapUnits" name="outline_width_unit"/>
                <Option type="QString" value="solid" name="style"/>
              </Option>
              <data_defined_properties>
                <Option type="Map">
                  <Option type="QString" value="" name="name"/>
                  <Option name="properties"/>
                  <Option type="QString" value="collection" name="type"/>
                </Option>
              </data_defined_properties>
            </layer>
          </symbol>
        </background>
        <shadow shadowRadiusMapUnitScale="3x:0,0,0,0,0,0" shadowOffsetMapUnitScale="3x:0,0,0,0,0,0" shadowRadius="1.5" shadowScale="100" shadowBlendMode="6" shadowUnder="0" shadowOffsetGlobal="1" shadowRadiusAlphaOnly="0" shadowOffsetUnit="MM" shadowColor="0,0,0,255" shadowOffsetDist="1" shadowRadiusUnit="MM" shadowDraw="0" shadowOffsetAngle="135" shadowOpacity="0.69999999999999996"/>
        <dd_properties>
          <Option type="Map">
            <Option type="QString" value="" name="name"/>
            <Option name="properties"/>
            <Option type="QString" value="collection" name="type"/>
          </Option>
        </dd_properties>
        <substitutions/>
      </text-style>
      <text-format multilineAlign="0" autoWrapLength="0" formatNumbers="0" plussign="0" useMaxLineLengthForAutoWrap="1" reverseDirectionSymbol="0" rightDirectionSymbol=">" wrapChar="" addDirectionSymbol="0" leftDirectionSymbol="&lt;" decimals="3" placeDirectionSymbol="0"/>
      <placement overrunDistanceMapUnitScale="3x:0,0,0,0,0,0" offsetUnits="MM" maxCurvedCharAngleIn="25" polygonPlacementFlags="2" maxCurvedCharAngleOut="-25" repeatDistance="0" fitInPolygonOnly="0" centroidInside="0" rotationUnit="AngleDegrees" labelOffsetMapUnitScale="3x:0,0,0,0,0,0" preserveRotation="1" lineAnchorClipping="0" geometryGeneratorEnabled="0" quadOffset="4" rotationAngle="0" distMapUnitScale="3x:0,0,0,0,0,0" yOffset="0" lineAnchorType="0" distUnits="MM" repeatDistanceMapUnitScale="3x:0,0,0,0,0,0" xOffset="0" placementFlags="10" predefinedPositionOrder="TR,TL,BR,BL,R,L,TSR,BSR" geometryGeneratorType="PointGeometry" geometryGenerator="" layerType="PolygonGeometry" overrunDistance="0" priority="5" lineAnchorTextPoint="CenterOfText" allowDegraded="0" overrunDistanceUnit="MM" lineAnchorPercent="0.5" placement="4" centroidWhole="0" repeatDistanceUnits="MM" offsetType="0" overlapHandling="PreventOverlap" dist="0"/>
      <rendering zIndex="0" obstacle="1" obstacleFactor="1" unplacedVisibility="0" limitNumLabels="0" scaleMax="0" fontMaxPixelSize="10000" upsidedownLabels="0" mergeLines="0" obstacleType="0" drawLabels="1" labelPerPart="0" scaleVisibility="0" fontLimitPixelSize="0" scaleMin="0" fontMinPixelSize="3" maxNumLabels="2000" minFeatureSize="0"/>
      <dd_properties>
        <Option type="Map">
          <Option type="QString" value="" name="name"/>
          <Option name="properties"/>
          <Option type="QString" value="collection" name="type"/>
        </Option>
      </dd_properties>
      <callout type="simple">
        <Option type="Map">
          <Option type="QString" value="pole_of_inaccessibility" name="anchorPoint"/>
          <Option type="int" value="0" name="blendMode"/>
          <Option type="Map" name="ddProperties">
            <Option type="QString" value="" name="name"/>
            <Option name="properties"/>
            <Option type="QString" value="collection" name="type"/>
          </Option>
          <Option type="bool" value="false" name="drawToAllParts"/>
          <Option type="QString" value="0" name="enabled"/>
          <Option type="QString" value="point_on_exterior" name="labelAnchorPoint"/>
          <Option type="QString" value="&lt;symbol clip_to_extent=&quot;1&quot; type=&quot;line&quot; is_animated=&quot;0&quot; force_rhr=&quot;0&quot; frame_rate=&quot;10&quot; alpha=&quot;1&quot; name=&quot;symbol&quot;>&lt;data_defined_properties>&lt;Option type=&quot;Map&quot;>&lt;Option type=&quot;QString&quot; value=&quot;&quot; name=&quot;name&quot;/>&lt;Option name=&quot;properties&quot;/>&lt;Option type=&quot;QString&quot; value=&quot;collection&quot; name=&quot;type&quot;/>&lt;/Option>&lt;/data_defined_properties>&lt;layer pass=&quot;0&quot; class=&quot;SimpleLine&quot; id=&quot;{0dd12e68-b29c-4f7f-b97c-813e4628e66e}&quot; enabled=&quot;1&quot; locked=&quot;0&quot;>&lt;Option type=&quot;Map&quot;>&lt;Option type=&quot;QString&quot; value=&quot;0&quot; name=&quot;align_dash_pattern&quot;/>&lt;Option type=&quot;QString&quot; value=&quot;square&quot; name=&quot;capstyle&quot;/>&lt;Option type=&quot;QString&quot; value=&quot;5;2&quot; name=&quot;customdash&quot;/>&lt;Option type=&quot;QString&quot; value=&quot;3x:0,0,0,0,0,0&quot; name=&quot;customdash_map_unit_scale&quot;/>&lt;Option type=&quot;QString&quot; value=&quot;MM&quot; name=&quot;customdash_unit&quot;/>&lt;Option type=&quot;QString&quot; value=&quot;0&quot; name=&quot;dash_pattern_offset&quot;/>&lt;Option type=&quot;QString&quot; value=&quot;3x:0,0,0,0,0,0&quot; name=&quot;dash_pattern_offset_map_unit_scale&quot;/>&lt;Option type=&quot;QString&quot; value=&quot;MM&quot; name=&quot;dash_pattern_offset_unit&quot;/>&lt;Option type=&quot;QString&quot; value=&quot;0&quot; name=&quot;draw_inside_polygon&quot;/>&lt;Option type=&quot;QString&quot; value=&quot;bevel&quot; name=&quot;joinstyle&quot;/>&lt;Option type=&quot;QString&quot; value=&quot;60,60,60,255&quot; name=&quot;line_color&quot;/>&lt;Option type=&quot;QString&quot; value=&quot;solid&quot; name=&quot;line_style&quot;/>&lt;Option type=&quot;QString&quot; value=&quot;0.3&quot; name=&quot;line_width&quot;/>&lt;Option type=&quot;QString&quot; value=&quot;MM&quot; name=&quot;line_width_unit&quot;/>&lt;Option type=&quot;QString&quot; value=&quot;0&quot; name=&quot;offset&quot;/>&lt;Option type=&quot;QString&quot; value=&quot;3x:0,0,0,0,0,0&quot; name=&quot;offset_map_unit_scale&quot;/>&lt;Option type=&quot;QString&quot; value=&quot;MM&quot; name=&quot;offset_unit&quot;/>&lt;Option type=&quot;QString&quot; value=&quot;0&quot; name=&quot;ring_filter&quot;/>&lt;Option type=&quot;QString&quot; value=&quot;0&quot; name=&quot;trim_distance_end&quot;/>&lt;Option type=&quot;QString&quot; value=&quot;3x:0,0,0,0,0,0&quot; name=&quot;trim_distance_end_map_unit_scale&quot;/>&lt;Option type=&quot;QString&quot; value=&quot;MM&quot; name=&quot;trim_distance_end_unit&quot;/>&lt;Option type=&quot;QString&quot; value=&quot;0&quot; name=&quot;trim_distance_start&quot;/>&lt;Option type=&quot;QString&quot; value=&quot;3x:0,0,0,0,0,0&quot; name=&quot;trim_distance_start_map_unit_scale&quot;/>&lt;Option type=&quot;QString&quot; value=&quot;MM&quot; name=&quot;trim_distance_start_unit&quot;/>&lt;Option type=&quot;QString&quot; value=&quot;0&quot; name=&quot;tweak_dash_pattern_on_corners&quot;/>&lt;Option type=&quot;QString&quot; value=&quot;0&quot; name=&quot;use_custom_dash&quot;/>&lt;Option type=&quot;QString&quot; value=&quot;3x:0,0,0,0,0,0&quot; name=&quot;width_map_unit_scale&quot;/>&lt;/Option>&lt;data_defined_properties>&lt;Option type=&quot;Map&quot;>&lt;Option type=&quot;QString&quot; value=&quot;&quot; name=&quot;name&quot;/>&lt;Option name=&quot;properties&quot;/>&lt;Option type=&quot;QString&quot; value=&quot;collection&quot; name=&quot;type&quot;/>&lt;/Option>&lt;/data_defined_properties>&lt;/layer>&lt;/symbol>" name="lineSymbol"/>
          <Option type="double" value="0" name="minLength"/>
          <Option type="QString" value="3x:0,0,0,0,0,0" name="minLengthMapUnitScale"/>
          <Option type="QString" value="MM" name="minLengthUnit"/>
          <Option type="double" value="0" name="offsetFromAnchor"/>
          <Option type="QString" value="3x:0,0,0,0,0,0" name="offsetFromAnchorMapUnitScale"/>
          <Option type="QString" value="MM" name="offsetFromAnchorUnit"/>
          <Option type="double" value="0" name="offsetFromLabel"/>
          <Option type="QString" value="3x:0,0,0,0,0,0" name="offsetFromLabelMapUnitScale"/>
          <Option type="QString" value="MM" name="offsetFromLabelUnit"/>
        </Option>
      </callout>
    </settings>
  </labeling>
  <blendMode>0</blendMode>
  <featureBlendMode>0</featureBlendMode>
  <layerGeometryType>2</layerGeometryType>
</qgis>
