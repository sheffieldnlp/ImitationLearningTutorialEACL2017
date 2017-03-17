import svgwrite
from IPython.core.display import HTML


def draw_cost_breakdown(rows, columns, path, cost, cost_cell, roll_in_cell, roll_out_cell,
                        row_height=40, column_width=80):
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
        dwg.add(dwg.text(row, insert=(0, row_height + i * row_height)))

    for i, col in enumerate(columns):
        dwg.add(dwg.text(col, insert=((i + 1) * column_width, table_height + row_height)))

    for i in range(1, len(path)):
        prev = path[i - 1]
        current = path[i]
        line = dwg.add(dwg.line(coord(*prev), coord(*current), stroke=svgwrite.rgb(10, 10, 16, '%')))
        line['marker-end'] = marker.get_funciri()

    def label_cost():
        x, y = coord(*cost_cell)
        dwg.add(dwg.text("cost = " + str(cost), insert=(x + 10, y)))

    def label_cell(cell, label):
        x, y = coord(*cell)
        dwg.add(dwg.text(label, insert=(x, y - 5)))

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

    label_cost()
    label_cell(roll_in_cell, "rollin")
    label_cell(roll_out_cell, "rollout")
    plot_grid()

    # dwg.add(dwg.text('Blah', insert=(0, 10)))
    return HTML(dwg.tostring())
