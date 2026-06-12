def define_env(env):

    # Variable type display
    @env.macro
    def var_display(text, data_type) -> None:
        
        icon = ""
        color = ""
        displayed_text = ""
        tooltip = ""

        if data_type == "boolean":
            icon = "lucide-power"
            displayed_text = "Boolean"
            tooltip = displayed_text
            color = "red"
        elif data_type == "integer":
            icon = "lucide-arrow-up-1-0"
            displayed_text = "Integer"
            tooltip = displayed_text
            color = "teal"
        elif data_type == "float":
            icon = "lucide-decimals-arrow-right"
            displayed_text = "Float"
            tooltip = displayed_text
            color = "green"
        elif data_type == "exec":
            icon = "lucide-split"
            displayed_text = "Exec"
            tooltip = displayed_text

        if text != None:
            displayed_text = text
    
        return f"**:{icon}:{{.trans}} {displayed_text}**{{.text .info-mini .{color} title={tooltip}}}"

    # Color square
    @env.macro
    def color_display(color) -> None:
        return f"<span title=\"{color}\" style=\"display: inline-block; vertical-align: middle; width: .8rem; height: .8rem; border: 1px solid var(--md-default-fg-color); background-color: {color};\"></span>"

    # Wire color display
    @env.macro
    def wire_display(length, data_type, variant) -> None:

        symbol = ":material-play:"
        wire = ""

        for i in range(length):
            wire += symbol

        return f"**{wire}**{{.wire .{data_type} .{variant}}}"

    # Video
    @env.macro
    def video(path, title):

        video = f"{path}"
        thumbnail = f"{path}"

        html = (
            f'<video playsinline controls preload="none" src="{path}.mp4" poster="{path}.jpg" title="{title}">'
            f'  <source src="{path}.mp4" type="video/mp4" size="1080">'
            f'  <source src="{path}-540p.mp4" type="video/mp4" size="540">'
            f'</video>'
        )
        return html
