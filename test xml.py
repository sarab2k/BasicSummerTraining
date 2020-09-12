import xml.etree.ElementTree as ET

data='''
<comments>
        <comment>
                <name>Romina</name>
                <count>97</count>
        </comment>
        <comment>
                <name>Laurie</name>
                <count>97</count>
        </comment>
        <comment>
                <name>Bayli</name>
                <count>90</count>
        </comment>
        <comment>
                <name>Siyona</name>
                <count>90</count>
        </comment>'''


tree = ET.fromstring(data)
lst = tree.findall('comment/comment')
for item in lst:
    print('count', item.find('count').text)
