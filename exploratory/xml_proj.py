#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 26 00:11:19 2022

@author: sarahrandall
"""

import os
import xml.etree.ElementTree as ET #parsing the file

#pass a list of lists -> create xml file with same tiers as han files

os.chdir('/Users/sarahrandall/Downloads')


    
global file 
file =  '4E00.han'

def xml_parser(file):

    xmlTree = ET.parse(file)
    root = xmlTree.getroot()
    
    """Root Tag: {http://biologicinstitute.org/schemas/stylus/1.0}hanDefinition
       Attributes: {'uuid': '791D0736-B512-47C8-A103-40FEB6334F37', 'unicode': '4E00', 'creationDate': '2008-09-16T17:03:35.512367', 'creationTool': 'inscribe.py 1.0'}"""
    
    
    """As an Element, root has a tag and a dictionary of attributes:
        root.tag,  root.attr"""
        
    for child in root:
        print('child_tag: ', child.tag, '\n', 'child_attr: ' , child.attrib, '\n')
       
    """child_tag:  {http://biologicinstitute.org/schemas/stylus/1.0}bounds 
     child_attr:  {'top': '270.0', 'left': '70.0', 'bottom': '270.0', 'right': '470.0', 'width': '400.0', 'height': '0.0', 'x-midpoint': '270.0', 'y-midpoint': '270.0'} 
    
    child_tag:  {http://biologicinstitute.org/schemas/stylus/1.0}length 
     child_attr:  {} 
    
    child_tag:  {http://biologicinstitute.org/schemas/stylus/1.0}minimumStrokeLength 
     child_attr:  {} 
    
    child_tag:  {http://biologicinstitute.org/schemas/stylus/1.0}groups 
     child_attr:  {} 
    
    child_tag:  {http://biologicinstitute.org/schemas/stylus/1.0}strokes 
     child_attr:  {} 
     
     Child elements (Subelements) from root element. Subelements can also have their own child elements"""
        
    print([elem.tag for elem in root.iter()]) #Prints out all elements (including root, child elements of root, and child subelements) in file from root
    
    """T{http://biologicinstitute.org/schemas/stylus/1.0}hanDefinition',
     '{http://biologicinstitute.org/schemas/stylus/1.0}bounds',
     '{http://biologicinstitute.org/schemas/stylus/1.0}length',
     '{http://biologicinstitute.org/schemas/stylus/1.0}minimumStrokeLength',
     
     '{http://biologicinstitute.org/schemas/stylus/1.0}groups', [3]
     '{http://biologicinstitute.org/schemas/stylus/1.0}group', #child of groups [3][0]
     '{http://biologicinstitute.org/schemas/stylus/1.0}bounds', #child of group [3][0][0]
     '{http://biologicinstitute.org/schemas/stylus/1.0}length',#child of group [3][0][1]
     '{http://biologicinstitute.org/schemas/stylus/1.0}weightedCenter', #child of group [3][0][2]
     '{http://biologicinstitute.org/schemas/stylus/1.0}containedStrokes', #child of group [3][0][3]
     
     '{http://biologicinstitute.org/schemas/stylus/1.0}strokes', [4]
     '{http://biologicinstitute.org/schemas/stylus/1.0}stroke', #child of strokes [4]0]
     '{http://biologicinstitute.org/schemas/stylus/1.0}bounds', #child of stroke  [4][0][0]
     '{http://biologicinstitute.org/schemas/stylus/1.0}length', #child of stroke  [4][0][1]
     '{http://biologicinstitute.org/schemas/stylus/1.0}points', #child of stroke  [4][0][2]
     
     '{http://biologicinstitute.org/schemas/stylus/1.0}forward', #child of points [4][0][2][0]
     '{http://biologicinstitute.org/schemas/stylus/1.0}pointDistance',
     '{http://biologicinstitute.org/schemas/stylus/1.0}pointDistance',
     
     '{http://biologicinstitute.org/schemas/stylus/1.0}reverse', [4][0][2][1]
     '{http://biologicinstitute.org/schemas/stylus/1.0}pointDistance',
     '{http://biologicinstitute.org/schemas/stylus/1.0}pointDistance'"""
     
     #>> list(root[index]) - finds children of elements
     
    
    for elem in root.iter():
        print(elem.tag,': ', elem.attrib, '\n') #Prints out element tag with their respective attributes
        
    """ Tags and Attributes:
    {http://biologicinstitute.org/schemas/stylus/1.0}hanDefinition : {'uuid': '791D0736-B512-47C8-A103-40FEB6334F37', 'unicode': '4E00', 'creationDate': '2008-09-16T17:03:35.512367', 'creationTool': 'inscribe.py 1.0'}
    
    {http://biologicinstitute.org/schemas/stylus/1.0}length :  {} 
    
    {http://biologicinstitute.org/schemas/stylus/1.0}minimumStrokeLength :  {} 
    
    {http://biologicinstitute.org/schemas/stylus/1.0}groups :  {} 
    
    {http://biologicinstitute.org/schemas/stylus/1.0}group :  {} 
    
    {http://biologicinstitute.org/schemas/stylus/1.0}bounds :  {'top': '270.0', 'left': '70.0', 'bottom': '270.0', 'right': '470.0', 'width': '400.0', 'height': '0.0', 'x-midpoint': '270.0', 'y-midpoint': '270.0'} 
    
    {http://biologicinstitute.org/schemas/stylus/1.0}length :  {} 
    
    {http://biologicinstitute.org/schemas/stylus/1.0}weightedCenter :  {'x': '270.0', 'y': '270.0'} 
    
    {http://biologicinstitute.org/schemas/stylus/1.0}containedStrokes :  {} 
    
    {http://biologicinstitute.org/schemas/stylus/1.0}strokes :  {} 
    
    {http://biologicinstitute.org/schemas/stylus/1.0}stroke :  {} 
    
    {http://biologicinstitute.org/schemas/stylus/1.0}bounds :  {'top': '270.0', 'left': '70.0', 'bottom': '270.0', 'right': '470.0', 'width': '400.0', 'height': '0.0', 'x-midpoint': '270.0', 'y-midpoint': '270.0'} 
    
    {http://biologicinstitute.org/schemas/stylus/1.0}length :  {} 
    
    {http://biologicinstitute.org/schemas/stylus/1.0}points :  {} 
    
    {http://biologicinstitute.org/schemas/stylus/1.0}forward :  {} 
    
    {http://biologicinstitute.org/schemas/stylus/1.0}pointDistance :  {'x': '70.0', 'y': '270.0', 'fractionalDistance': '0.0'} 
    
    {http://biologicinstitute.org/schemas/stylus/1.0}pointDistance :  {'x': '470.0', 'y': '270.0', 'fractionalDistance': '1.0'} 
    
    {http://biologicinstitute.org/schemas/stylus/1.0}reverse :  {} 
    
    {http://biologicinstitute.org/schemas/stylus/1.0}pointDistance :  {'x': '470.0', 'y': '270.0', 'fractionalDistance': '0.0'} 
    
    {http://biologicinstitute.org/schemas/stylus/1.0}pointDistance :  {'x': '70.0', 'y': '270.0', 'fractionalDistance': '1.0'} 
    """
    
    #Example: 1 tag: several attributes
    # for pointDistance in root.iter('{http://biologicinstitute.org/schemas/stylus/1.0}pointDistance'):
    #     print(pointDistance.tag, pointDistance.attrib) 
    
    # <a><b - signifies b is a subelement of element a
    
    """MUY IMPORTANTE:
        
    If the element is created from an XML file, the text attribute holds either the text between the element’s
    start tag and its first child or end tag, or None, and the tail attribute holds either the text between 
    the element’s end tag and the next tag, or None. For the XML data:
    
    <a><b>1<c>2<d/>3</c></b>4</a>
    
    The a element has None for both text and tail attributes, 
    the b element has text "1" and tail "4", 
    the c element has text "2" and tail None, 
    the d element has text None and tail "3"."""
    
            
    # The xml file:
    
   
    """
    <?xml version='1.0' encoding='utf8'?>
    <hanDefinition xmlns:ns0="http://biologicinstitute.org/schemas/stylus/1.0" uuid="791D0736-B512-47C8-A103-40FEB6334F37" unicode="4E00" creationDate="2008-09-16T17:03:35.512367" creationTool="inscribe.py 1.0">
    <bounds top="270.0" left="70.0" bottom="270.0" right="470.0" width="400.0" height="0.0" x-midpoint="270.0" y-midpoint="270.0" />
    <length>400.0</length>
    <minimumStrokeLength>400.0</minimumStrokeLength>
    <groups>
    <group>
    <bounds top="270.0" left="70.0" bottom="270.0" right="470.0" width="400.0" height="0.0" x-midpoint="270.0" y-midpoint="270.0" />
    <length>400.0</length>
    <weightedCenter x="270.0" y="270.0" />
    <containedStrokes>1</containedStrokes>
    </group>
    </groups>
    <strokes>
    <stroke>
    <bounds top="270.0" left="70.0" bottom="270.0" right="470.0" width="400.0" height="0.0" x-midpoint="270.0" y-midpoint="270.0" />
    <length>400.0</length>
    <points>
    <forward><pointDistance x="70.0" y="270.0" fractionalDistance="0.0" />
    <pointDistance x="470.0" y="270.0" fractionalDistance="1.0" /></forward>
    <reverse><pointDistance x="470.0" y="270.0" fractionalDistance="0.0" />
    <pointDistance x="70.0" y="270.0" fractionalDistance="1.0" /></reverse>
    </points>
    </stroke>
    </strokes>
    
    </hanDefinition>"""
    


# innermost brackets - points - pointDistance
# Next -  segments
# Outer - strokes
# Most outer - character


def xml_file_maker(info):    #create xml file based on passed info
    """Publish this code as jupyter file"""
    import xml.dom.minidom as dom #xml file builder
    
    root = dom.Document() # instantiation of root
    
    hanDef = root.createElementNS('http://biologicinstitute.org/schemas/stylus/1.0', 'hanDefinition')
    hanDef.setAttribute("xmlns:ns0", "http://biologicinstitute.org/schemas/stylus/1.0")  #set attributes
    hanDef.setAttribute("uuid", "N/A")
    hanDef.setAttribute("unicode", "4E00")
    hanDef.setAttribute("creationDate", "2022-11-28")
    hanDef.setAttribute("creationTool", "inscribe.py 1.0")
    
    root.appendChild(hanDef) #hanDef is now the root
    
    #bounds - root[0]
    bounds = root.createElementNS('http://biologicinstitute.org/schemas/stylus/1.0','bounds')  #root[0]
    
    attrib = {'top': '270.0',
      'left': '70.0',
      'bottom': '270.0',
      'right': '470.0',
      'width': '400.0',
      'height': '0.0',
      'x-midpoint': '270.0',
      'y-midpoint': '270.0'}
    
    for k, v in attrib.items():
        bounds.setAttribute(k, v)
        
    hanDef.appendChild(bounds)
    
    #Root child elements
    #length - root[1]
    length = root.createElementNS('http://biologicinstitute.org/schemas/stylus/1.0','length' )
    text = root.createTextNode("400")  #<--- get length value from app
    length.appendChild(text) #appending text; no attrb
    
    hanDef.appendChild(length)
    
    #minimumStrokeLength - root[2]
    minimumStrokeLength = root.createElementNS('http://biologicinstitute.org/schemas/stylus/1.0','minimumStrokeLength' )
    text = root.createTextNode("400")  #<--- get minimumStrokeLength val from app
    minimumStrokeLength.appendChild(text) #appending text; no attrb
    
    hanDef.appendChild(minimumStrokeLength)
    
    #groups - root[3]
    groups = root.createElementNS('http://biologicinstitute.org/schemas/stylus/1.0','groups')
    hanDef.appendChild(groups)
    
    strokes = root.createElementNS('http://biologicinstitute.org/schemas/stylus/1.0','strokes')
    hanDef.appendChild(groups)
    
    #Child elements' child nodes - group
    group = root.createElementNS('http://biologicinstitute.org/schemas/stylus/1.0','group') #groups child
    groups.appendChild(group)
    
    #bounds - # group child
    bounds = root.createElementNS('http://biologicinstitute.org/schemas/stylus/1.0','bounds') 
    attrib =  {'top': '270.0', 'left': '70.0', 'bottom': '270.0', 'right': '470.0', 'width': '400.0', 'height': '0.0', 'x-midpoint': '270.0', 'y-midpoint': '270.0'} 
    for k, v in attrib.items():
        bounds.setAttribute(k, v)
    group.appendChild(bounds)
    
    #length - group child
    length = root.createElementNS('http://biologicinstitute.org/schemas/stylus/1.0','bounds') 
    group.appendChild(length)
    
    #"""{http://biologicinstitute.org/schemas/stylus/1.0}weightedCenter', #child of group [3][0][2]"""
    weightedCenter = root.createElementNS('http://biologicinstitute.org/schemas/stylus/1.0','weightedCenter') 
    attrib =  {'x': '270.0', 'y': '270.0'} 
    for k, v in attrib.items():
        weightedCenter.setAttribute(k, v)
    group.appendChild(weightedCenter)
    
    #"""'{http://biologicinstitute.org/schemas/stylus/1.0}containedStrokes', #child of group [3][0][3]"""
    containedStrokes = root.createElementNS('http://biologicinstitute.org/schemas/stylus/1.0','containedStrokes')
    
    num_strokes = 0
    for i in info:
        num_strokes+=1 # counts number of strokes within set
    
    converted_num = "{}".format(num_strokes)
          
    text = root.createTextNode(converted_num)
    containedStrokes.appendChild(text)
    group.appendChild(containedStrokes)
    
    #"#""{http://biologicinstitute.org/schemas/stylus/1.0}strokes, [4]"""
    
    strokes =  root.createElementNS('http://biologicinstitute.org/schemas/stylus/1.0','strokes')
    hanDef.appendChild(strokes)
    
    #""""'{http://biologicinstitute.org/schemas/stylus/1.0}stroke', #child of strokes [4][0]"""
    stroke =  root.createElementNS('http://biologicinstitute.org/schemas/stylus/1.0','stroke')
    strokes.appendChild(stroke)
    
    
    #"""'{http://biologicinstitute.org/schemas/stylus/1.0}bounds', #child of stroke  [4][0][0]"""
    bounds = root.createElementNS('http://biologicinstitute.org/schemas/stylus/1.0','bounds')
    attrib = {'top': '270.0', 'left': '70.0', 'bottom': '270.0', 'right': '470.0', 'width': '400.0', 'height': '0.0', 'x-midpoint': '270.0', 'y-midpoint': '270.0'} 
    for k, v in attrib.items():
        bounds.setAttribute(k, v)
    stroke.appendChild(bounds)
        
    #'{http://biologicinstitute.org/schemas/stylus/1.0}length', #child of stroke  [4][0][1]"""
    length = root.createElementNS('http://biologicinstitute.org/schemas/stylus/1.0','length')
    stroke.appendChild(length)
    
    
    #'{http://biologicinstitute.org/schemas/stylus/1.0}points', #child of stroke  [4][0][2]"""
    points = root.createElementNS('http://biologicinstitute.org/schemas/stylus/1.0','points')
    stroke.appendChild(points)
    
    #'{http://biologicinstitute.org/schemas/stylus/1.0}forward', #child of points [4][0][2][0]"""
    forward =  root.createElementNS('http://biologicinstitute.org/schemas/stylus/1.0','forward')
    stroke.appendChild(forward)
    
    #'{http://biologicinstitute.org/schemas/stylus/1.0}pointDistance', #children of forward
    pointD1 = root.createElementNS('http://biologicinstitute.org/schemas/stylus/1.0','pointDistance')
    # info = [[[20,20], [80,20]]]
    y1 = info[0][0][0]  #Position of first y-value
    y2 = info[0][0][1]  #Position of second y-value
    y1 = float(y1)  #Turn into float values
    y2 = float(y2)
    
    c1 = "{}".format(y1)  #Converts integer values to string
    c2 = "{}".format(y2)
    
    attrib = {'x': c1, 'y': c2, 'fractionalDistance': '0.0'}
    for k, v in attrib.items():
        pointD1.setAttribute(k, v)
    forward.appendChild(pointD1)
    
    
    #'{http://biologicinstitute.org/schemas/stylus/1.0}pointDistance',
    pointD2 = root.createElementNS('http://biologicinstitute.org/schemas/stylus/1.0','pointDistance')
    # info = [[[20,20], [80,20]]]
    y1 = info[0][1][0]
    y2 = info[0][1][1]
    y1 = float(y1) #Turn into float values
    y2 = float(y2)
    c1 = "{}".format(y1) #Converts integer values to string
    c2 = "{}".format(y2)
    
    attrib = {'x': c1, 'y': c2, 'fractionalDistance': '0.0'}
    for k, v in attrib.items():
        pointD2.setAttribute(k, v)
    forward.appendChild(pointD2)
    
    
    #""""'{http://biologicinstitute.org/schemas/stylus/1.0}reverse', [4][0][2][1]"""
    reverse =  root.createElementNS('http://biologicinstitute.org/schemas/stylus/1.0','forward')
    stroke.appendChild(reverse)
    
    #""""'{http://biologicinstitute.org/schemas/stylus/1.0}pointDistance',""" #children of reverse
    pD1 = root.createElementNS('http://biologicinstitute.org/schemas/stylus/1.0','pointDistance')
    
    y1 = info[0][1][0]
    y2 = info[0][1][1]
    y1 = float(y1)  #Turn into float values
    y2 = float(y2)
    c1 = "{}".format(y1) #Converts integer values to string
    c2 = "{}".format(y2)
    
    attrib = {'x': c1, 'y': c2, 'fractionalDistance': '0.0'}
    for k, v in attrib.items():
        pD1.setAttribute(k, v)
    reverse.appendChild(pD1)
        
    #""""'{http://biologicinstitute.org/schemas/stylus/1.0}pointDistance'"""
    pD2 = root.createElementNS('http://biologicinstitute.org/schemas/stylus/1.0','pointDistance')
    
    y1 = info[0][0][0]
    y2 = info[0][0][1]
    y1 = float(y1)  #Turn into float values
    y2 = float(y2)
    c1 = "{}".format(y1)  #Converts integer values to string
    c2 = "{}".format(y2)
    attrib = {'x': c1, 'y': c2, 'fractionalDistance': '0.0'}
    
    for k, v in attrib.items():
        pD2.setAttribute(k, v)
    reverse.appendChild(pD2)
    print(root.toprettyxml())
    
   
xml_file_maker(info = [[[20,20], [80,20]]])

# <?xml version="1.0" ?>
# <hanDefinition xmlns:ns0="http://biologicinstitute.org/schemas/stylus/1.0" uuid="N/A" unicode="4E00" creationDate="2022-11-28" creationTool="inscribe.py 1.0">
#  	<bounds top="270.0" left="70.0" bottom="270.0" right="470.0" width="400.0" height="0.0" x-midpoint="270.0" y-midpoint="270.0"/>
#  	<length>400</length>
#  	<minimumStrokeLength>400</minimumStrokeLength>
#  	<groups>
# 		<group>
#  			<bounds top="270.0" left="70.0" bottom="270.0" right="470.0" width="400.0" height="0.0" x-midpoint="270.0" y-midpoint="270.0"/>
#  			<bounds/>
#  			<weightedCenter x="270.0" y="270.0"/>
#  			<containedStrokes>1</containedStrokes> # of strokes within a group
# 		</group>
#  	</groups>
#  	<strokes>
# 		<stroke>
#  			<bounds top="270.0" left="70.0" bottom="270.0" right="470.0" width="400.0" height="0.0" x-midpoint="270.0" y-midpoint="270.0"/>
#  			<length/>
#  			<points/>
#  			<forward>
# 				<pointDistance x="20.0" y="20.0" fractionalDistance="0.0"/>
# 				<pointDistance x="80.0" y="20.0" fractionalDistance="0.0"/>
#  			</forward>
#  			<forward>
# 				<pointDistance x="80.0" y="20.0" fractionalDistance="0.0"/>
# 				<pointDistance x="20.0" y="20.0" fractionalDistance="0.0"/>
#  			</forward>
# 		</stroke>
#  	</strokes>
# </hanDefinition>



   
    