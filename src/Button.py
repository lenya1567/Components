from modules.TkinterDesign import PassParams

ButtonInitProps = {
    'text': 'Click me!',
    'font': ('black', 'Arial -15 bold'),
    'action': 'print("You clicked at button")',
    'help': 'Click at me!',
    'fill': "white",
    'tint': (2, "black"),
    'border': (1, "black"),
    'tabactive': (2, 3, "blue"),
    'delay': 0.1
}

class Button():
    def __init__(self, page, id, *s, **m):
        self.id = id
        current_paramms = ButtonInitProps.copy()
        for e in m:
            current_paramms[e] = m[e]
        self.params = current_paramms.copy()
        self.body = s
        page.add(self.current())
    def current(self):
        coords = self.body
        value = self.params['text']
        font = self.params['font']
        action = self.params['action']
        help = self.params['help']
        fill = self.params['fill']
        tint = self.params['tint']
        border = self.params['border']
        delay = self.params['delay']
        tabactive = self.params['tabactive']

        self_name = f"{self.id}_body"
        self_x = f"{self.id}_x"
        self_y = f"{self.id}_y"
        self_w = f"{self.id}_w"
        self_h = f"{self.id}_h"
        self_value = f"{self.id}_text"
        self_font = f"{self.id}_font"
        self_fill = f"{self.id}_fill"
        self_tint = f"{self.id}_tint"
        self_border = f"{self.id}_border"
        self_active = f"{self.id}_active"
        self_delay = f"{self.id}_delay"
        self_tabactive = f"{self.id}_tabactive"

        initVars = f"{self_name} = None\n"
        initVars += f"{self_x} = {coords[0]}\n"
        initVars += f"{self_y} = {coords[1]}\n"
        initVars += f"{self_w} = {coords[2]}\n"
        initVars += f"{self_h} = {coords[3]}\n"
        initVars += f"{self_value} = '{value}'\n"
        initVars += f"{self_font} = {font}\n"
        initVars += f"{self_fill} = '{fill}'\n"
        initVars += f"{self_tint} = {tint}\n"
        initVars += f"{self_delay} = {delay}\n"
        initVars += f"{self_border} = {border}\n"
        initVars += f"{self_active} = True\n\n"
        initVars += f"{self_tabactive} = {tabactive}\n\n"
       
        view = f"\tif {self_name} == None:\n"
        view += f"\t\t{self_name}_tint = canvas.create_rectangle({self_x}, {self_y}, {self_x} + {self_w}, {self_y} + {self_h}, fill={self_tint}[1])\n"
        view += f"\t\t{self_name}_body = canvas.create_rectangle({self_x} - {self_tint}[0], {self_y} - {self_tint}[0], {self_x} + {self_w} - {self_tint}[0], {self_y} + {self_h} - {self_tint}[0], width={self_border}[0], outline={self_border}[1], fill={self_fill})\n"
        view += f"\t\t{self_name}_title = canvas.create_text(({self_x} + {self_x} + {self_w}  - {self_tint}[0]) // 2, ({self_y} + {self_y} + {self_h} - {self_tint}[0]) // 2, text={self_value}, font={self_font}[1], fill={self_font}[0])\n"
        view += f"\t\t{self_name}_tabactive = canvas.create_rectangle({self_x} - {self_tabactive}[0], {self_y} - {self_tabactive}[0], {self_x} - {self_tabactive}[0] + {self_w} - {self_tabactive}[0], {self_y} + {self_h} - {self_tabactive}[0], outline='white', width={self_tabactive}[1])\n"
        view += f"\t\t{self_name} = ({self_name}_tint, {self_name}_body, {self_name}_title, {self_name}_tabactive)\n"
        view += f"\telse:\n"
        view += f"\t\tcanvas.coords({self_name}[0], {self_x}, {self_y}, {self_x} + {self_w}, {self_y} + {self_h})\n"
        view += f"\t\tcanvas.itemconfig({self_name}[0], fill={self_tint}[1])\n"
        view += f"\t\tcanvas.coords({self_name}[1], {self_x} - {self_tint}[0], {self_y} - {self_tint}[0], {self_x} + {self_w} - {self_tint}[0], {self_y} + {self_h} - {self_tint}[0])\n"
        view += f"\t\tcanvas.itemconfig({self_name}[1], width={self_border}[0], outline={self_border}[1], fill={self_fill})\n"
        view += f"\t\tcanvas.coords({self_name}[2], ({self_x} + {self_x} + {self_w} - {self_tint}[0]) // 2, ({self_y} + {self_y} + {self_h} - {self_tint}[0]) // 2)\n"
        view += f"\t\tcanvas.itemconfig({self_name}[2], text={self_value}, font={self_font}[1], fill={self_font}[0])\n"
        view += f"\t\tif screen_buttons_activated == '{self.id}':\n"
        view += f"\t\t\tcanvas.coords({self_name}[3], {self_x} - {self_tabactive}[0], {self_y} - {self_tabactive}[0], {self_x} - {self_tabactive}[0] + {self_w} - {self_tabactive}[0], {self_y} + {self_h} - {self_tabactive}[0], fill={self_tint}[1], outline={self_tabactive}[2], width={self_tabactive}[1])\n"
        view += f"\t\t\tcanvas.itemconfig({self_name}[3], outline={self_tabactive}[2], width={self_tabactive}[1])\n"

        globalVars = f"global {self_name}, {self_x}, {self_y}, {self_w}, {self_h}, {self_value}, {self_font}, {self_fill}, {self_tint}, {self_border}, {self_active}, {self_delay}"

        btn1 = f"\tif ({self_x} - {self_tint}[0]) <= click_x and click_x <= ({self_x} - {self_tint}[0] + {self_w}) and ({self_y} - {self_tint}[0]) <= click_y and click_y <= ({self_y} - {self_tint}[0] + {self_h}) and {self_active} == True:\n"
        btn1 += f"\t\t{self_active} = False\n"
        btn1 += f"\t\t{self_tint} = (-{self_tint}[0], {self_tint}[1])\n"
        btn1 += f"\t\tscreen_action = 'MOVE'\n"
        btn1 += f"\t\tpresent()\n\n"
        btn1 += f"\t\t{action}\n\n"
        btn1 += f"\t\ttime.sleep({self_delay})\n"
        btn1 += f"\t\t{self_tint} = (-{self_tint}[0], {self_tint}[1])\n"
        btn1 += f"\t\tscreen_action = 'MOVE'\n"
        btn1 += f"\t\tpresent()\n\n"
        btn1 += f"\t\t{self_active} = True\n"

        return PassParams(initVars, view, btn1, "", "", "", globalVars)
