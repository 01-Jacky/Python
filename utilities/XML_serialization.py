"""
<div>
    <h1> Foobar </h1>
    <p>
        Bah bah bah <b> yo </b>
    </p>
</div>
"""

class Node:
    def __init__(self, tag, text=""):
        # e.g. <div class="greeting">What a <b>lovely</b> day!</div>
        self.tag = tag          # div
        self.attribute = {}     # {'class': 'greeting', 'attr2': ''}
        self.text = []          # How to handle text with a node inside? Maybe [W,h,a,t, , a , Node, , d, a, y,!]
        self.children = []      # [Node, Node, Node...]


def serialize(root):
    # Replace print statements with writes to text file
    for child in root.children:
        print('<{}>'.format(root.tag))

        print()




