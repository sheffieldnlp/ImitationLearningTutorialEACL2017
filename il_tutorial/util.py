import uuid


def generic_to_html(element, top_level=True):
    if getattr(element, "_repr_html_", None) is not None:
        value = element._repr_html_()
    else:
        if isinstance(element, list) or isinstance(element, tuple):
            if top_level:
                value = "<ul>" + "\n".join(["<li>{}</li>".format(generic_to_html(e, False)) for e in element]) + "</ul>"
            else:
                # value = """<ul>""" + "\n".join(
                #     ["""<li style="display:inline;">{}</li>""".format(generic_to_html(e, False)) for e in element]) + "</ul>"
                value = " ".join([generic_to_html(e, False) for e in element])


        else:
            value = str(element)
            # print(value)
    return value


class Carousel:
    def __init__(self, elements):
        self.elements = elements

    def _repr_html_(self):
        def create_item(index, active=False):
            element = self.elements[index]
            value = generic_to_html(element)
            css_class = "item active" if active else "item"
            return """<div class="{}">{}</div>""".format(css_class, value)

        items = [create_item(i, i == 0) for i in range(0, len(self.elements))]
        items_html = "\n".join(items)
        div_id = str(uuid.uuid1())

        result = """
        <div id="{0}" class="carousel" data-ride="carousel" data-interval="false">
          <div class="carousel-inner" role="listbox">
          {1}
          </div>
          <!-- Controls -->
          <a href="#{0}" role="button2" data-slide="prev">Previous</a>
          &nbsp
          <a  href="#{0}" role="button2" data-slide="next">Next</a>
        </div>
        """.format(div_id, items_html)
        return result
