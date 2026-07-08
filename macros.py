def define_env(env):

    # Variable type display
    @env.macro
    def var_display(value, data_type) -> None:
        
        icon = ""
        color = ""
        text = ""
        tooltip = ""

        if data_type == "boolean":
            icon = "lucide-check-square"
            text = "Boolean"
            tooltip = text
            color = "red"
        elif data_type == "integer":
            icon = "lucide-hash"
            text = "Integer"
            tooltip = text
            color = "teal"
        elif data_type == "float":
            icon = "lucide-spline"
            text = "Float"
            tooltip = text
            color = "green"
        elif data_type == "string":
            icon = "lucide-type"
            text = "String"
            tooltip = text
            color = "orange"
        elif data_type == "vector":
            icon = "lucide-axis-3d"
            text = "Vector"
            tooltip = text
            color = "yellow"
        elif data_type == "rotation":
            icon = "lucide-rotate-cw"
            text = "Rotation"
            tooltip = text
            color = "lime"
        elif data_type == "quaternion":
            icon = "lucide-rotate-3d"
            text = "Quaternion"
            tooltip = text
            color = "sky-blue"
        elif data_type == "reference":
            icon = "lucide-link"
            text = "Reference"
            tooltip = text
            color = "cyan"
        elif data_type == "color":
            icon = "lucide-palette"
            text = "Color"
            tooltip = text
            color = "pink"
        elif data_type == "enum":
            icon = "lucide-list-ordered"
            text = "Enum"
            tooltip = text
            color = "lilac"
        elif data_type == "exec":
            icon = "lucide-split"
            text = "Exec"
            tooltip = text
        elif data_type == "special":
            icon = "lucide-boxes"
            text = value
            tooltip = text
            color = "blue"

        if value != None:
            text = value
            if data_type == "string":
                value = value.replace(" ", "·")
                text = f'"{value}"'
            elif data_type == "vector":
                text = f'**X: {value[0]}**{{.array}} **Y: {value[1]}**{{.array}} **Z: {value[2]}**{{.array}}'
            elif data_type == "rotation":
                text = f'**Roll: {value[0]}&#176;**{{.array}} **Pitch: {value[1]}&#176;**{{.array}} **Yaw: {value[2]}&#176;**{{.array}}'
            elif data_type == "quaternion":
                text = f'**X: {value[0]}**{{.array}} **Y: {value[1]}**{{.array}} **Z: {value[2]}**{{.array}} **W: {value[3]}**{{.array}}'
            elif data_type == "color":
                text = f':material-square:{{style="color:rgb({value[0]},{value[1]},{value[2]});"}} **R: {value[0]}**{{.array}} **G: {value[1]}**{{.array}} **B: {value[2]}**{{.array}}'
                if len(value) == 4:
                    text += f' **A: {value[3]}**{{.array}}'
            elif data_type == "enum":
                text = f'**{value[0]}**{{.array}} = **{value[1]}**'
            elif value == "False":
                icon = "lucide-square"
    
        return f'<span class="text info-mini {color}" title="{tooltip}" markdown><b> :{icon}:{{.trans}} {text}</b></span>'

    # Color square
    @env.macro
    def color_display(color) -> None:
        return f"<span title=\"{color}\" style=\"display: inline-block; vertical-align: middle; width: .8rem; height: .8rem; border: 1px solid var(--md-default-fg-color); background-color: {color};\"></span>"

    # Wire color display
    @env.macro
    def wire_display(length, data_type, variant, reference) -> None:

        symbols = "&#x25B6;&#xFE0E;"
        wire = ""
        stripe_class = ""
        
        if reference == True:
            stripe_class = ' wire-var-ref'

        for i in range(length):
            wire += symbols

        return f'<span aria-hidden="true" class="wire {data_type} {variant}{stripe_class}"><span class="wire-arrows">{wire}</span></span>'

    # Video
    @env.macro
    def video(path, title):

        video = f"{path}"
        thumbnail = f"{path}"

        html = (
            f'<video playsinline controls preload="none" src="{path}.mp4" poster="{path}-poster.jpg" title="{title}">'
            f'  <source src="{path}-1080p.mp4" type="video/mp4" size="1080">'
            f'  <source src="{path}-540p.mp4" type="video/mp4" size="540">'
            f'</video>'
        )
        return html
