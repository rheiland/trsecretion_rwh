 
# This file is auto-generated from a Python script that parses a PhysiCell configuration (.xml) file.
#
# Edit at your own risk.
#
import os
from ipywidgets import Label,Text,Checkbox,Button,HBox,VBox,FloatText,IntText,BoundedIntText,BoundedFloatText,Layout,Box
    
class UserTab(object):

    def __init__(self):
        
        micron_units = Label('micron')   # use "option m" (Mac, for micro symbol)

        constWidth = '180px'
        tab_height = '500px'
        stepsize = 10

        #style = {'description_width': '250px'}
        style = {'description_width': '25%'}
        layout = {'width': '400px'}

        name_button_layout={'width':'25%'}
        widget_layout = {'width': '15%'}
        widget2_layout = {'width': '10%'}
        units_button_layout ={'width':'15%'}
        desc_button_layout={'width':'45%'}
        divider_button_layout={'width':'40%'}

        div_row1 = Button(description='---Chemical A (uptaken chemical)---', disabled=True, layout=divider_button_layout)

        param_name1 = Button(description='chemical_A_uptake_rate_coefficient', disabled=True, layout=name_button_layout)
        param_name1.style.button_color = 'tan'

        self.chemical_A_uptake_rate_coefficient = FloatText(
          value=0.0000075,
          step=1e-06,
          style=style, layout=widget_layout)

        param_name2 = Button(description='internal_chemical_A', disabled=True, layout=name_button_layout)
        param_name2.style.button_color = 'lightgreen'

        self.internal_chemical_A = FloatText(
          value=10.0,
          step=1,
          style=style, layout=widget_layout)

        div_row2 = Button(description='---Chemical B (secreted chemical)---', disabled=True, layout=divider_button_layout)

        param_name3 = Button(description='chemical_B_secretion_rate', disabled=True, layout=name_button_layout)
        param_name3.style.button_color = 'tan'

        self.chemical_B_secretion_rate = FloatText(
          value=0.0000075,
          step=1e-06,
          style=style, layout=widget_layout)

        param_name4 = Button(description='chemical_B_saturation_density', disabled=True, layout=name_button_layout)
        param_name4.style.button_color = 'lightgreen'

        self.chemical_B_saturation_density = FloatText(
          value=10.0,
          step=1,
          style=style, layout=widget_layout)

        param_name5 = Button(description='internal_chemical_B', disabled=True, layout=name_button_layout)
        param_name5.style.button_color = 'tan'

        self.internal_chemical_B = FloatText(
          value=10.0,
          step=1,
          style=style, layout=widget_layout)

        div_row3 = Button(description='---Chemical C (exported chemical)---', disabled=True, layout=divider_button_layout)

        param_name6 = Button(description='chemical_C_secretion_rate', disabled=True, layout=name_button_layout)
        param_name6.style.button_color = 'lightgreen'

        self.chemical_C_secretion_rate = FloatText(
          value=0.0000075,
          step=1e-06,
          style=style, layout=widget_layout)

        param_name7 = Button(description='chemical_C_saturation_density', disabled=True, layout=name_button_layout)
        param_name7.style.button_color = 'tan'

        self.chemical_C_saturation_density = FloatText(
          value=10.0,
          step=1,
          style=style, layout=widget_layout)

        param_name8 = Button(description='internal_chemical_C', disabled=True, layout=name_button_layout)
        param_name8.style.button_color = 'lightgreen'

        self.internal_chemical_C = FloatText(
          value=10.0,
          step=1,
          style=style, layout=widget_layout)

        div_row4 = Button(description='---colorization---', disabled=True, layout=divider_button_layout)

        param_name9 = Button(description='internalization_color', disabled=True, layout=name_button_layout)
        param_name9.style.button_color = 'tan'

        self.internalization_color = Checkbox(
          value=False,
          style=style, layout=widget_layout)

        div_row5 = Button(description='---internal creation or consumption---', disabled=True, layout=divider_button_layout)

        param_name10 = Button(description='internal_reactions', disabled=True, layout=name_button_layout)
        param_name10.style.button_color = 'lightgreen'

        self.internal_reactions = Checkbox(
          value=True,
          style=style, layout=widget_layout)

        param_name11 = Button(description='Chemical_A_consumption_rate', disabled=True, layout=name_button_layout)
        param_name11.style.button_color = 'tan'

        self.Chemical_A_consumption_rate = FloatText(
          value=0.001,
          step=0.0001,
          style=style, layout=widget_layout)

        param_name12 = Button(description='Chemical_B_creation_rate', disabled=True, layout=name_button_layout)
        param_name12.style.button_color = 'lightgreen'

        self.Chemical_B_creation_rate = FloatText(
          value=0.001,
          step=0.0001,
          style=style, layout=widget_layout)

        param_name13 = Button(description='Chemical_C_consumption_rate', disabled=True, layout=name_button_layout)
        param_name13.style.button_color = 'tan'

        self.Chemical_C_consumption_rate = FloatText(
          value=0.0,
          step=0.01,
          style=style, layout=widget_layout)

        param_name14 = Button(description='Chemical_C_creation_rate', disabled=True, layout=name_button_layout)
        param_name14.style.button_color = 'lightgreen'

        self.Chemical_C_creation_rate = FloatText(
          value=0.0,
          step=0.01,
          style=style, layout=widget_layout)

        units_button1 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button1.style.button_color = 'lightgreen'
        units_button2 = Button(description='1/min', disabled=True, layout=units_button_layout) 
        units_button2.style.button_color = 'tan'
        units_button3 = Button(description='substance', disabled=True, layout=units_button_layout) 
        units_button3.style.button_color = 'lightgreen'
        units_button4 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button4.style.button_color = 'lightgreen'
        units_button5 = Button(description='1/min', disabled=True, layout=units_button_layout) 
        units_button5.style.button_color = 'tan'
        units_button6 = Button(description='1/min', disabled=True, layout=units_button_layout) 
        units_button6.style.button_color = 'lightgreen'
        units_button7 = Button(description='1/min', disabled=True, layout=units_button_layout) 
        units_button7.style.button_color = 'tan'
        units_button8 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button8.style.button_color = 'tan'
        units_button9 = Button(description='substance/min', disabled=True, layout=units_button_layout) 
        units_button9.style.button_color = 'lightgreen'
        units_button10 = Button(description='1/min', disabled=True, layout=units_button_layout) 
        units_button10.style.button_color = 'tan'
        units_button11 = Button(description='1/min', disabled=True, layout=units_button_layout) 
        units_button11.style.button_color = 'lightgreen'
        units_button12 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button12.style.button_color = 'lightgreen'
        units_button13 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button13.style.button_color = 'tan'
        units_button14 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button14.style.button_color = 'tan'
        units_button15 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button15.style.button_color = 'lightgreen'
        units_button16 = Button(description='1/min', disabled=True, layout=units_button_layout) 
        units_button16.style.button_color = 'tan'
        units_button17 = Button(description='1/min', disabled=True, layout=units_button_layout) 
        units_button17.style.button_color = 'lightgreen'
        units_button18 = Button(description='1/min', disabled=True, layout=units_button_layout) 
        units_button18.style.button_color = 'tan'
        units_button19 = Button(description='1/min', disabled=True, layout=units_button_layout) 
        units_button19.style.button_color = 'lightgreen'

        desc_button2 = Button(description='uptake rate for chemical A (Default = 0.0000075)' , tooltip='uptake rate for chemical A (Default = 0.0000075)', disabled=True, layout=desc_button_layout) 
        desc_button2.style.button_color = 'tan'
        desc_button3 = Button(description='initial internalized secreted chemical (Default = 0.0)' , tooltip='initial internalized secreted chemical (Default = 0.0)', disabled=True, layout=desc_button_layout) 
        desc_button3.style.button_color = 'lightgreen'
        desc_button4 = Button(description='secreteion rate for secreted chemical (Default = 0.0000075)' , tooltip='secreteion rate for secreted chemical (Default = 0.0000075)', disabled=True, layout=desc_button_layout) 
        desc_button4.style.button_color = 'tan'
        desc_button5 = Button(description='saturation density for secreted chemical (Default = 10.0)' , tooltip='saturation density for secreted chemical (Default = 10.0)', disabled=True, layout=desc_button_layout) 
        desc_button5.style.button_color = 'lightgreen'
        desc_button6 = Button(description='initial internalized secreted chemical (Default = 10.0)' , tooltip='initial internalized secreted chemical (Default = 10.0)', disabled=True, layout=desc_button_layout) 
        desc_button6.style.button_color = 'tan'
        desc_button7 = Button(description='net export rate for chemical C (Default = 0.0000075)' , tooltip='net export rate for chemical C (Default = 0.0000075)', disabled=True, layout=desc_button_layout) 
        desc_button7.style.button_color = 'lightgreen'
        desc_button8 = Button(description='saturation density for secreted chemical (Default = 10.0)' , tooltip='saturation density for secreted chemical (Default = 10.0)', disabled=True, layout=desc_button_layout) 
        desc_button8.style.button_color = 'tan'
        desc_button9 = Button(description='initial internalized secreted chemical (Default = 10.0)' , tooltip='initial internalized secreted chemical (Default = 10.0)', disabled=True, layout=desc_button_layout) 
        desc_button9.style.button_color = 'lightgreen'
        desc_button10 = Button(description='Colorization (false->Default (Red), true->Colorize cells according to internal concentrations' , tooltip='Colorization (false->Default (Red), true->Colorize cells according to internal concentrations', disabled=True, layout=desc_button_layout) 
        desc_button10.style.button_color = 'tan'
        desc_button11 = Button(description='Cells will have intracellular reactions if it is true' , tooltip='Cells will have intracellular reactions if it is true', disabled=True, layout=desc_button_layout) 
        desc_button11.style.button_color = 'lightgreen'
        desc_button12 = Button(description='Chemical A consumption rate for First Cell' , tooltip='Chemical A consumption rate for First Cell', disabled=True, layout=desc_button_layout) 
        desc_button12.style.button_color = 'tan'
        desc_button13 = Button(description='Chemical B creation rate for Second Cell' , tooltip='Chemical B creation rate for Second Cell', disabled=True, layout=desc_button_layout) 
        desc_button13.style.button_color = 'lightgreen'
        desc_button14 = Button(description='Chemical C consumption rate for Third Cell' , tooltip='Chemical C consumption rate for Third Cell', disabled=True, layout=desc_button_layout) 
        desc_button14.style.button_color = 'tan'
        desc_button15 = Button(description='Chemical C creation rate for Third Cell' , tooltip='Chemical C creation rate for Third Cell', disabled=True, layout=desc_button_layout) 
        desc_button15.style.button_color = 'lightgreen'

        row2 = [param_name1, self.chemical_A_uptake_rate_coefficient, units_button2, desc_button2] 
        row3 = [param_name2, self.internal_chemical_A, units_button3, desc_button3] 
        row4 = [param_name3, self.chemical_B_secretion_rate, units_button5, desc_button4] 
        row5 = [param_name4, self.chemical_B_saturation_density, units_button6, desc_button5] 
        row6 = [param_name5, self.internal_chemical_B, units_button7, desc_button6] 
        row7 = [param_name6, self.chemical_C_secretion_rate, units_button9, desc_button7] 
        row8 = [param_name7, self.chemical_C_saturation_density, units_button10, desc_button8] 
        row9 = [param_name8, self.internal_chemical_C, units_button11, desc_button9] 
        row10 = [param_name9, self.internalization_color, units_button13, desc_button10] 
        row11 = [param_name10, self.internal_reactions, units_button15, desc_button11] 
        row12 = [param_name11, self.Chemical_A_consumption_rate, units_button16, desc_button12] 
        row13 = [param_name12, self.Chemical_B_creation_rate, units_button17, desc_button13] 
        row14 = [param_name13, self.Chemical_C_consumption_rate, units_button18, desc_button14] 
        row15 = [param_name14, self.Chemical_C_creation_rate, units_button19, desc_button15] 

        box_layout = Layout(display='flex', flex_flow='row', align_items='stretch', width='100%')
        box2 = Box(children=row2, layout=box_layout)
        box3 = Box(children=row3, layout=box_layout)
        box4 = Box(children=row4, layout=box_layout)
        box5 = Box(children=row5, layout=box_layout)
        box6 = Box(children=row6, layout=box_layout)
        box7 = Box(children=row7, layout=box_layout)
        box8 = Box(children=row8, layout=box_layout)
        box9 = Box(children=row9, layout=box_layout)
        box10 = Box(children=row10, layout=box_layout)
        box11 = Box(children=row11, layout=box_layout)
        box12 = Box(children=row12, layout=box_layout)
        box13 = Box(children=row13, layout=box_layout)
        box14 = Box(children=row14, layout=box_layout)
        box15 = Box(children=row15, layout=box_layout)

        self.tab = VBox([
          div_row1,
          box2,
          box3,
          div_row2,
          box4,
          box5,
          box6,
          div_row3,
          box7,
          box8,
          box9,
          div_row4,
          box10,
          div_row5,
          box11,
          box12,
          box13,
          box14,
          box15,
        ])

    # Populate the GUI widgets with values from the XML
    def fill_gui(self, xml_root):
        uep = xml_root.find('.//microenvironment_setup')  # find unique entry point
        vp = []   # pointers to <variable> nodes
        if uep:
            for var in uep.findall('variable'):
                vp.append(var)

        uep = xml_root.find('.//user_parameters')  # find unique entry point
        self.chemical_A_uptake_rate_coefficient.value = float(uep.find('.//chemical_A_uptake_rate_coefficient').text)
        self.internal_chemical_A.value = float(uep.find('.//internal_chemical_A').text)
        self.chemical_B_secretion_rate.value = float(uep.find('.//chemical_B_secretion_rate').text)
        self.chemical_B_saturation_density.value = float(uep.find('.//chemical_B_saturation_density').text)
        self.internal_chemical_B.value = float(uep.find('.//internal_chemical_B').text)
        self.chemical_C_secretion_rate.value = float(uep.find('.//chemical_C_secretion_rate').text)
        self.chemical_C_saturation_density.value = float(uep.find('.//chemical_C_saturation_density').text)
        self.internal_chemical_C.value = float(uep.find('.//internal_chemical_C').text)
        self.internalization_color.value = ('true' == (uep.find('.//internalization_color').text.lower()) )
        self.internal_reactions.value = ('true' == (uep.find('.//internal_reactions').text.lower()) )
        self.Chemical_A_consumption_rate.value = float(uep.find('.//Chemical_A_consumption_rate').text)
        self.Chemical_B_creation_rate.value = float(uep.find('.//Chemical_B_creation_rate').text)
        self.Chemical_C_consumption_rate.value = float(uep.find('.//Chemical_C_consumption_rate').text)
        self.Chemical_C_creation_rate.value = float(uep.find('.//Chemical_C_creation_rate').text)


    # Read values from the GUI widgets to enable editing XML
    def fill_xml(self, xml_root):
        uep = xml_root.find('.//microenvironment_setup')  # find unique entry point
        vp = []   # pointers to <variable> nodes
        if uep:
            for var in uep.findall('variable'):
                vp.append(var)

        uep = xml_root.find('.//user_parameters')  # find unique entry point
        uep.find('.//chemical_A_uptake_rate_coefficient').text = str(self.chemical_A_uptake_rate_coefficient.value)
        uep.find('.//internal_chemical_A').text = str(self.internal_chemical_A.value)
        uep.find('.//chemical_B_secretion_rate').text = str(self.chemical_B_secretion_rate.value)
        uep.find('.//chemical_B_saturation_density').text = str(self.chemical_B_saturation_density.value)
        uep.find('.//internal_chemical_B').text = str(self.internal_chemical_B.value)
        uep.find('.//chemical_C_secretion_rate').text = str(self.chemical_C_secretion_rate.value)
        uep.find('.//chemical_C_saturation_density').text = str(self.chemical_C_saturation_density.value)
        uep.find('.//internal_chemical_C').text = str(self.internal_chemical_C.value)
        uep.find('.//internalization_color').text = str(self.internalization_color.value)
        uep.find('.//internal_reactions').text = str(self.internal_reactions.value)
        uep.find('.//Chemical_A_consumption_rate').text = str(self.Chemical_A_consumption_rate.value)
        uep.find('.//Chemical_B_creation_rate').text = str(self.Chemical_B_creation_rate.value)
        uep.find('.//Chemical_C_consumption_rate').text = str(self.Chemical_C_consumption_rate.value)
        uep.find('.//Chemical_C_creation_rate').text = str(self.Chemical_C_creation_rate.value)
