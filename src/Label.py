from modules.design import include

PassParams = include("TkinterDesign").PassParams

LabelInitProps = {
    'text': 'Hello world!',
    'font': 'Arial -15 bold',
    'anchor': 'c',
    'fill': 'black'
}

class Label():
    def __init__(self, page, id, *s, **m):
        self.id = id
        current_paramms = LabelInitProps.copy()
        for e in m:
            current_paramms[e] = m[e]
        self.params = current_paramms.copy()
        self.body = s
        page.add(self.current())
    def current(self):
        coords = self.body
        value = self.params['text']
        font = self.params['font']
        anchor = self.params['anchor']
        fill = self.params['fill']

        self_name = f"{self.id}_body"
        self_x = f"{self.id}_x"
        self_y = f"{self.id}_y"
        self_value = f"{self.id}_value"
        self_font = f"{self.id}_font"
        self_anchor = f"{self.id}_anchor"
        self_fill = f"{self.id}_fill"

        initVars = f"{self_name} = None\n"
        initVars += f"{self_x} = {coords[0]}\n"
        initVars += f"{self_y} = {coords[1]}\n"
        initVars += f"{self_value} = '{value}'\n"
        initVars += f"{self_font} = '{font}'\n"
        initVars += f"{self_anchor} = '{anchor}'\n"
        initVars += f"{self_fill} = '{fill}'\n\n"

        view = f"\tif {self_name} == None:\n"
        view += f"\t\t{self_name} = canvas.create_text({self_x}, {self_y}, text={self_value}, font={self_font}, anchor={self_anchor}, fill={self_fill})\n"
        view += f"\telse:\n"
        view += f"\t\tcanvas.setcoords({self_name}, {self_x}, {self_y})\n"
        view += f"\t\tcanvas.itemconfig({self_name}, text={self_value}, font={self_font}, anchor={self_anchor}, fill={self_fill})\n"

        globalVars = f"global {self_name}, {self_x}, {self_y}, {self_value}, {self_font}, {self_anchor}, {self_fill}"

        return PassParams(initVars, view, "", "", "", "", globalVars)
