def is_extremum(dy1, dy2):
    if dy1 == 0 and dy2 == 0:
        return True
    elif dy1 != 0 and dy2 != 0:
        return True
    else:
        return False


class Edge(object):
    x1, y1 = 0, 0
    x2, y2 = 0, 0

    def __init__(self, p1, p2):
        if p1[1] < p2[1]:
            p1, p2 = p2, p1
        elif p1[1] == p2[1]:
            if p1[0] > p2[0]:
                p1, p2 = p2, p1

        self.x1, self.y1 = p1[0], p1[1]
        self.x2, self.y2 = p2[0], p2[1]

    def __repr__(self):
        return "Edge: ({:}, {:})===({:}, {:})".format(self.x1, self.y1, self.x2, self.y2)


class ActiveEdge(object):
    x = 0
    dx, dy = 0.0, 0
    next = None

    # horizontal = False

    def __repr__(self):
        return "[{:}, {:}] -> {:}".format(self.x, self.dy, self.next)


def is_horisontal(edge):
    return edge.dy == -2
    # return edge.horizontal


def is_match(ae1, ae2):
    x1 = round(ae1.x)
    x2 = round(ae2.x)
    return x1 == x2


# Функции y-группы
def create_y_group(edge_arr):
    y_group = {}
    for edge in edge_arr:
        active_edge = ActiveEdge()
        active_edge.x = edge.x1
        active_edge.dy = edge.y1 - edge.y2
        if active_edge.dy != 0:
            active_edge.dx = (edge.x2 - edge.x1) / active_edge.dy
        else:
            active_edge.dy = -2
            active_edge.dx = 0

        if edge.y1 in y_group.keys():
            y_group[edge.y1].append(active_edge)
        else:
            y_group[edge.y1] = [active_edge]
    return y_group


def find_min_y(edge_arr):
    y_min = edge_arr[0].y2
    for edge in edge_arr:
        y_min = min(edge.y2, y_min)
    return y_min


def lae_add(lae, edge):
    if lae is None or edge.x < lae.x or \
            (edge.x == lae.x and edge.dx < lae.dx):
        edge.next = lae
        return edge

    temp = lae
    while temp.next is not None:
        if edge.x < temp.next.x\
                or (edge.x == temp.next.x and edge.dx < temp.next.dx):
            switch = temp.next
            temp.next = edge
            edge.next = switch
            return lae
        else:
            temp = temp.next
    temp.next = edge
    return lae


def sort_lae(lae):
    last = None
    temp = lae
    switch = None
    while lae is not last:
        if lae.x > lae.next.x:
            switch = lae.next
            lae.next = switch.next
            switch.next = lae
            lae = switch

        temp = lae
        while temp.next is not last:
            if temp.next.next is not None and \
                    temp.next.x > temp.next.next.x:
                switch = temp.next
                temp.next = switch.next
                switch.next = temp.next.next
                temp.next.next = switch
            temp = temp.next
        last = temp
    return lae
    # for i in range(len(lae)):
    #    for j in range(len(lae) - 1 - i):
    #        if lae[j].x > lae[j+1].x:
    #            lae[j], lae[j+1] = lae[j+1], lae[j]


def lae_step(lae):
    temp = lae
    while temp is not None:
        temp.dy -= 1
        temp.x += temp.dx
        temp = temp.next

    while lae.dy < 0:
        lae = lae.next
    temp = lae
    while temp.next is not None:
        if temp.next.dy < 0:
            temp.next = temp.next.next
        else:
            temp = temp.next

    return lae
