def define_env(env):

    # Variable type display
    @env.macro
    def var_display(value, data_type, is_reference = None) -> None:
        
        icon = ""
        color = ""
        text = ""
        tooltip = ""
        space = " "
        reference_class = ""
        reference_info = ""

        if is_reference == "normal":
            reference_class = " var-reference"
            reference_info = "Variable reference: "
        if is_reference == "array":
            reference_class = " var-array-reference"
            reference_info = "Array variable reference: "

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
            if data_type == "vector":
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
        if value == "":
            space = "";
        return f'<span class="text info-mini {color}{reference_class}" title="{reference_info}{tooltip}" markdown><b> :{icon}:{{.trans}}{space}{text}</b></span>'

    # Gate availability
    @env.macro
    def gate_availability(value, is_advanced = False) -> None:

        availability_text = ""

        if value == "admin-only":
            availability_text = f'**Availability:** **:lucide-shield-alert: Admin Only**{{.info-mini .text .red}}<br> Only people with the "Place Admin Gates" permission are allowed to use this gate.'
        elif value == "everyone":
            availability_text = f'**Availability:** **:lucide-circle-check-big: Everyone**{{.info-mini}}<br> Everyone can use this gate.'

        if is_advanced == True:
            availability_text = (
                f'{availability_text}\n\n'
                f'**Visibility:** **:lucide-cog: Advanced gate**{{.info-mini}} <br>Hidden by default unless you choose to display advanced gates.'
            )
        elif is_advanced == False:
            availability_text = (
                f'{availability_text}\n\n'
                f'**Visibility:** **:lucide-check: Simple gate**{{.info-mini}} <br>This gate is always visible.'
            )

        return availability_text

    # Color square
    @env.macro
    def color_display(color) -> None:
        return f"<span title=\"{color}\" style=\"display: inline-block; vertical-align: middle; width: .8rem; height: .8rem; border: 1px solid var(--md-default-fg-color); background-color: {color};\"></span>"

    # Wire color display
    @env.macro
    def wire_display(length, data_type, variant = str, secondary_type = str, map_key_type = str) -> None:

        # Symbol variable with arrow, whitespace and wire string variable.

        symbols = "&#x25B6;&#xFE0E;"
        wire = ""

        # Start formatting the wire display.
        
        text = f'<span aria-hidden="true" class="wire {data_type}'

        # If data type has a variant, add the variant class.

        if variant != None:
            text += f' {variant}'

        # Add secondary type class when the wire is of a variable reference.

        if secondary_type == "var-ref":
            text += f' var-ref'
        elif secondary_type == "array-ref":
            text += f' array-ref'
        elif secondary_type == "map-ref":
            text += f' map-ref'

        # Map key data type.

        if map_key_type == 'integer':
            text = text + f' key-integer'
        elif map_key_type == 'string':
            text = text + f' key-string'
        elif map_key_type == 'object':
            text = text + f' key-object'

        # Make the wire string.

        for i in range(length):
            wire += symbols
        
        # Finish formatting the wire display.

        text += f'"><span class="wire-arrows">{wire}</span></span>'

        return text

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
