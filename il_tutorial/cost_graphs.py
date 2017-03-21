import svgwrite
from IPython.core.display import HTML


def draw_cost_breakdown(rows, columns, path, cost=None, cost_cell=None, roll_in_cell=None, roll_out_cell=None,
                        row_height=60, column_width=100):
    height = row_height * (len(rows) + 2)
    width = column_width * (len(columns) + 1)
    dwg = svgwrite.Drawing('test.svg', size=(width, height))

    marker = dwg.marker(insert=(5, 5), size=(10, 10), orient='auto')
    marker.add(dwg.path('M 0 0 L 10 5 L 0 10 z', fill='blue'))

    dwg.defs.add(marker)

    table_height = len(rows) * row_height
    table_width = len(columns) * column_width

    def coord(col, row):
        return (col + 1) * column_width, (row + 1) * row_height

    for i, row in enumerate(rows):
        dwg.add(dwg.text(row, insert=(0, row_height + i * row_height), style="font-size:20px; font-weight:bold; font-family:Lato"))

    for i, col in enumerate(columns):
        dwg.add(dwg.text(col, insert=((i + 1) * column_width, table_height + row_height), style="font-size:20px; font-family:Lato"))

    for i in range(1, len(path)):
        prev = path[i - 1]
        current = path[i]
        line = dwg.add(dwg.line(coord(*prev), coord(*current), stroke=svgwrite.rgb(10, 10, 16, '%'),  stroke_width="2.5"))
        line['marker-end'] = marker.get_funciri()

    def label_cost():
        x, y = coord(*cost_cell)
        dwg.add(dwg.text("cost = " + str(cost), insert=(x + 10, y), style="font-size:20px; font-weight:bold; font-family:Lato"))

    def label_cell(cell, label):
        x, y = coord(*cell)
        dwg.add(dwg.text(label, insert=(x-15, y - 15), style="font-size:20px; font-weight:bold; font-family:Lato"))

    def plot_grid():
        # horizontal lines
        for col in range(1, len(columns)):
            for row in range(0, len(rows)):
                x1, y1 = coord(col - 1, row)
                x2, y2 = coord(col, row)
                dwg.add(dwg.line((x1 + 5, y1), (x2 - 5, y2), stroke=svgwrite.rgb(10, 10, 16, '%'))).dasharray([5, 5])

        for col in range(0, len(columns)):
            for row in range(1, len(rows)):
                x1, y1 = coord(col, row - 1)
                x2, y2 = coord(col, row)
                dwg.add(dwg.line((x1, y1 + 5), (x2, y2 - 5), stroke=svgwrite.rgb(10, 10, 16, '%'))).dasharray([5, 5])

    if not cost==None:
        label_cost()
    if roll_in_cell:
        label_cell(roll_in_cell, "rollin")
    if roll_out_cell:
        label_cell(roll_out_cell, "rollout")
    plot_grid()

    # dwg.add(dwg.text('Blah', insert=(0, 10)))
    return HTML(dwg.tostring())
