def define_env(env):

    # Variable type display

    @env.macro
    def var_display(value, data_type, secondary_type = None, map_key_type = None) -> None:

        # CSS classes
        main_classes = " "
        key_classes = "."

        # Text/caption
        main_text = " "
        key_text = ""

        # Icon
        main_icon = ""

        # Tooltip / HTML title of variable display span element
        tooltip = ""

        # Overwrite the string variables above based on data type given by the
        # user. New types can be added as they come in subsequent updates.

        if data_type == "boolean":

            main_classes += "red"
            main_text += "Boolean"
            main_icon = "lucide-check-square"
            tooltip = "Boolean"

            if value == False:
                main_icon = "lucide-square"
                main_text = " False"

            elif value == True:
                main_text = " True"

            elif value == None:
                pass

            else:
                main_text = " " + str(value)
        
        if data_type == "integer":

            main_classes += "teal"
            main_text += "Integer"
            main_icon = "lucide-hash"
            tooltip = "Integer"

            if value == None:
                pass

            else:
                main_text = " " + str(value)

        if data_type == "float":
            
            main_classes += "green"
            main_text += "Number/Float"
            main_icon = "lucide-spline"
            tooltip = "Number/Float"

            if value == None:
                pass

            else:
                main_text = " " + str(value)

        if data_type == "string":

            main_classes += "orange"
            main_text += "String"
            main_icon = "lucide-type"
            tooltip = "String"

            if value == None:
                pass

            else:
                main_text = " " + str(value)

        if data_type == "vector":

            main_classes += "yellow"
            main_text += "Vector"
            main_icon = "lucide-axis-3d"
            tooltip = "Vector"

            if value != None:
                if len(value) == 2:
                    main_text = f' **X: {value[0]}**{{.array}} **Y: {value[1]}**{{.array}}'
                elif len(value) == 3:
                    main_text = f' **X: {value[0]}**{{.array}} **Y: {value[1]}**{{.array}} **Z: {value[2]}**{{.array}}'
                else:
                    main_text = " " + str(value)
            elif value == None:
                pass

        if data_type == "rotation":

            main_classes += "lime"
            main_text += "Rotation"
            main_icon = "lucide-rotate-cw"
            tooltip = "Rotation"

            if value != None:
                if len(value) == 3:
                    main_text = f' **R: {value[0]}**{{.array}} **P: {value[1]}**{{.array}} **Y: {value[2]}**{{.array}}'
                else:
                    main_text = " " + str(value)
            elif value == None:
                pass

        if data_type == "quaternion":

            main_classes += "sky-blue"
            main_text += "Quaternion"
            main_icon = "lucide-rotate-3d"
            tooltip = "Quaternion"

            if value != None:
                if len(value) == 4:
                    main_text = f' **X: {value[0]}**{{.array}} **Y: {value[1]}**{{.array}} **Z: {value[2]}**{{.array}} **W: {value[3]}**{{.array}}'
                else:
                    main_text = " " + str(value)
            elif value == None:
                pass

        if data_type == "object":
            
            main_classes += "cyan"
            main_text += "Object/Reference"
            main_icon = "lucide-link"
            tooltip = "Object/Reference"

            if value == None:
                pass

            else:
                main_text = " " + str(value)

        if data_type == "color":

            main_classes += "pink"
            main_text += "Color"
            main_icon = "lucide-palette"
            tooltip = "Color"

            if value != None:
                if len(value) == 3:
                    main_text = f' :material-square:{{style="color:rgb({value[0]},{value[1]},{value[2]});"}} **R: {value[0]}**{{.array}} **G: {value[1]}**{{.array}} **B: {value[2]}**{{.array}}'
                elif len(value) == 4:
                    main_text = f' :material-square:{{style="color:rgb({value[0]},{value[1]},{value[2]});"}} **R: {value[0]}**{{.array}} **G: {value[1]}**{{.array}} **B: {value[2]}**{{.array}} **A: {value[3]}**{{.array}}'
                else:
                    main_text = " " + str(value)
            elif value == None:
                pass

        if data_type == "enum":

            main_classes += "lilac"
            main_text += "Enum"
            main_icon = "lucide-list-ordered"
            tooltip = "Enum"

            if value != None:
                if len(value) == 2:
                    main_text = f' **{value[0]}**{{.array}} = **{value[1]}**'
                else:
                    main_text = " " + str(value)
            elif value == None:
                pass

        if data_type == "exec":

            main_text += "Exec"
            main_icon = "lucide-split"
            tooltip = "Exec"

            if value == None:
                pass

            else:
                main_text = " " + str(value)

        if data_type == "special":
            
            main_classes += "blue"
            main_text += str(value)
            main_icon = "lucide-boxes"
            tooltip = str(value)

        # Clear the space if a color is not specified.
        if main_classes == " ":
            main_classes = ""

        # Build text for secondary class
        if secondary_type == "var-ref":
            main_classes += " var-ref"
            tooltip = "Variable reference: " + tooltip
        elif secondary_type == "array-ref":
            main_classes += " array-ref"
            tooltip = "Array variable reference: " + tooltip
        elif secondary_type == "map-ref":
            main_classes += " map-ref"
            tooltip = "Map variable reference: " + tooltip

            # Only execute this if the secondary type is specified as
            # map-ref (map array variable reference).
            if map_key_type == "integer":
                main_classes += " key-integer"
                key_text = "Int."
                tooltip += " (Integer keys)"
            elif map_key_type == "string":
                main_classes += " key-string"
                key_text = "Str."
                tooltip += " (String keys)"
            elif map_key_type == "object":
                main_classes += " key-object"
                key_text = "Obj."
                tooltip += " (Object keys)"

        # Clear the space if the user gives an empty string.
        if value == "":
            main_text = ""

        # Build output: Main classes, tooltip, icon and text.
        output = f'<span class="text info-mini {main_classes}" title="{tooltip}" markdown><b>:{main_icon}:{{.trans}}{main_text}'

        # Build additional output as needed.
        if secondary_type == "var-ref":
            output += f' **[V]**{{.text .blue}}'
        elif secondary_type == "array-ref":
            output += f' **[Av]**{{.text .blue}}'
        if secondary_type == "map-ref":
            output += f' **[Mv: {key_text}]**{{.text .blue}}'

        output += f'</b></span>'

        return output
    
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
